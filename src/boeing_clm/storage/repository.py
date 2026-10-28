"""
src/boeing_clm/storage/repository.py — Live BigQuery Repository for Boeing CLM.

All reads and writes execute strictly against `vertex-ai-demos-468803.boeing_clm`
with zero in-memory mock fallbacks and zero backend LLM calls.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
from typing import Any, Dict, List, Optional
import uuid

from google.cloud import bigquery

from boeing_clm.config import (
    BQ_DATASET,
    BQ_LOCATION,
    DEFAULT_DEAL_ID,
    GCP_PROJECT_ID,
    GOLDEN_EXPECTED_DIFFS_JSON,
    GOLDEN_FIXTURES_DIR,
)
from boeing_clm.ingestion.docx_track_changes import parse_redlined_docx
from boeing_clm.intelligence.conflict_detector import (
    BigQueryConflictDetector,
    is_rule_triggered,
    row_to_conflict_model,
)
from boeing_clm.intelligence.precedent_engine import BigQueryPrecedentEngine
from boeing_clm.models import (
    AuditEventItem,
    ClauseWorkbenchItem,
    CrossClauseConflict,
    DealWorkbenchState,
    ExtractedClauseDiff,
    PrecedentSearchResult,
    SMEReviewSubmission,
)

JOB_LABELS = {"datacloud": "antigravity"}


# Canonical metadata for all 3 active portfolio deals
CANONICAL_DEAL_PROFILES: Dict[str, Dict[str, Any]] = {
    "BA-2026-AV-8921": {
        "deal_id": "BA-2026-AV-8921",
        "vendor_name": "Apex AeroSystems Inc.",
        "supplier_tier": "Tier-1 Avionics",
        "boeing_program": "787 / 737-MAX Flight Control Display Units (FCC-900)",
        "contract_value_usd": 45000000.0,
        "proforma_stack": "Cymbal GP1 (General Provisions) + SP3 (International/Tax) + SP5 (Cyber/DFARS)",
        "pricing_model": "Firm-Fixed-Price (FFP) — $45,000,000 Ceiling",
        "sow_cap_clause_ref": "GP1 §3.1",
        "sharepoint_folder_url": "https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-AV-8921",
        "deviation_matrix_xlsx": "BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx",
        "total_clauses_parsed": 12,
        "untouched_clauses_count": 8,
        "redlined_clauses_count": 4,
        "initial_table_status": "INGESTED",
        "fixture_docx": "Vendor_Redlined_GP1.docx",
    },
    "BA-2026-TR-5510": {
        "deal_id": "BA-2026-TR-5510",
        "vendor_name": "Vanguard Thrust Systems Corp.",
        "supplier_tier": "Tier-1 Propulsion & Actuation",
        "boeing_program": "777X / 787 Thrust Reverser Actuators (TRA-500)",
        "contract_value_usd": 38000000.0,
        "proforma_stack": "Cymbal GP1 (General Provisions) + SP3 (International/Tax) + SP5 (Cyber/DFARS)",
        "pricing_model": "Firm-Fixed-Price (FFP) — $38,000,000 Ceiling",
        "sow_cap_clause_ref": "GP1 §3.1",
        "sharepoint_folder_url": "https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-TR-5510",
        "deviation_matrix_xlsx": "BA-2026-TR-5510_SharePoint_Deviation_Matrix.xlsx",
        "total_clauses_parsed": 12,
        "untouched_clauses_count": 7,
        "redlined_clauses_count": 5,
        "initial_table_status": "CONFLICT_DETECTED",
        "fixture_docx": "Vanguard_Working_Review_TR5510.docx",
    },
    "BA-2026-LG-7740": {
        "deal_id": "BA-2026-LG-7740",
        "vendor_name": "Meridian Landing Gear Corp.",
        "supplier_tier": "Tier-1 Structural & Landing Gear",
        "boeing_program": "787-10 Titanium Main Landing Gear Assemblies (TLG-800)",
        "contract_value_usd": 52000000.0,
        "proforma_stack": "Cymbal GP1 (General Provisions) + SP3 (International/Tax) + SP5 (Cyber/DFARS)",
        "pricing_model": "Firm-Fixed-Price (FFP) — $52,000,000 Ceiling",
        "sow_cap_clause_ref": "GP1 §3.1",
        "sharepoint_folder_url": "https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-LG-7740",
        "deviation_matrix_xlsx": "BA-2026-LG-7740_SharePoint_Deviation_Matrix.xlsx",
        "total_clauses_parsed": 12,
        "untouched_clauses_count": 8,
        "redlined_clauses_count": 4,
        "initial_table_status": "IN_SME_REVIEW",
        "fixture_docx": "Meridian_Working_Review_LG7740.docx",
    },
}

# Canonical initial SME state for the 4 redlined clauses in BA-2026-AV-8921
CANONICAL_INITIAL_POSITIONS: Dict[str, Dict[str, str]] = {
    "GP1-12": {
        "recommended_option_key": "hold_firm",
        "selected_option_key": "hold_firm",
        "sme_status": "APPROVED",
        "sme_reviewer": "Dr. Aris Thorne (Principal FAA DER, Flight Controls QA)",
        "sme_rationale": (
            "Rejected vendor 12-month warranty and 30-day inspection notice. "
            "FAA 14 CFR Part 21.140 and AS9100 Rev D mandate unannounced source inspection access at all times. "
            "Precedent shows 88% (14/16) held firm."
        ),
    },
    "GP1-19": {
        "recommended_option_key": "compromise_tier_1",
        "selected_option_key": "compromise_tier_1",
        "sme_status": "APPROVED",
        "sme_reviewer": "Elena Rostova, J.D. (Senior Counsel, Commercial & IP)",
        "sme_rationale": (
            "Applied Playbook Tier-1 Compromise (69% historical precedent across 11/16 Tier-1 avionics deals): "
            "2x PO ($90M) super-cap on general direct damages while holding uncapped liability for airworthiness "
            "recall and IP indemnity, narrowing the IP carveout strictly to Cymbal Aerospace proprietary bus specifications."
        ),
    },
    "SP3-04": {
        "recommended_option_key": "compromise_tier_1",
        "selected_option_key": "accept_vendor",
        "sme_status": "CONFLICT",
        "sme_reviewer": "Marcus Chen, CPA (Director, Global Tax & Trade)",
        "sme_rationale": (
            "Accepted vendor >5% Section 232/301 titanium and wafer tariff pass-through to avoid Q3 avionics "
            "delivery delay, pending Procurement verification against SOW cap."
        ),
    },
    "SP5-03": {
        "recommended_option_key": "hold_firm",
        "selected_option_key": "hold_firm",
        "sme_status": "APPROVED",
        "sme_reviewer": "Capt. Devon Brooks (Lead, Supplier Cyber Defense)",
        "sme_rationale": (
            "Held firm on 72-hour incident notification. DFARS 252.204-7012 and NIST SP 800-171 impose a "
            "non-negotiable 72-hour DoD reporting window (94% held firm across 15/16 historical contracts)."
        ),
    },
}

CANONICAL_INITIAL_POSITIONS_BY_DEAL: Dict[str, Dict[str, Dict[str, str]]] = {
    "BA-2026-AV-8921": CANONICAL_INITIAL_POSITIONS,
    "BA-2026-TR-5510": {
        "GP1-03": {
            "recommended_option_key": "hold_firm",
            "selected_option_key": "accept_vendor",
            "sme_status": "CONFLICT",
            "sme_reviewer": "Sloane Mercer, MBA (VP Finance & Cost Management)",
            "sme_rationale": (
                "Accepted 2.5% ($950,000) FFP unit-price discount under GP1 §3.1 conditioned on 1.0x ($38M) "
                "general liability cap in GP1 §19.1 — conflicts with Corporate Legal 2.0x ($76M) Super-Cap floor."
            ),
        },
        "GP1-12": {
            "recommended_option_key": "hold_firm",
            "selected_option_key": "hold_firm",
            "sme_status": "APPROVED",
            "sme_reviewer": "Dr. Aris Thorne (Principal FAA DER, Flight Controls QA)",
            "sme_rationale": (
                "Held firm on 36-month airworthiness warranty and mandatory unannounced FAA 14 CFR Part 21.140 / "
                "AS9100 Rev D source inspections."
            ),
        },
        "GP1-19": {
            "recommended_option_key": "compromise_tier_1",
            "selected_option_key": "accept_vendor",
            "sme_status": "CONFLICT",
            "sme_reviewer": "Elena Rostova, J.D. (Senior Counsel, Commercial & IP)",
            "sme_rationale": (
                "CRITICAL CROSS-CLAUSE CONFLICT: Finance accepted 2.5% ($950K) commercial discount in GP1 §3.1 "
                "tied to 1.0x ($38M) liability cap in GP1 §19.1, violating Corporate Legal 2.0x ($76M) Super-Cap floor."
            ),
        },
        "SP3-04": {
            "recommended_option_key": "compromise_tier_1",
            "selected_option_key": "compromise_tier_1",
            "sme_status": "APPROVED",
            "sme_reviewer": "Marcus Chen, CPA (Director, Global Tax & Trade)",
            "sme_rationale": (
                "Approved Playbook Tier-1 Compromise: 50/50 shared Section 232/301 tariff adjustment above 5% "
                "threshold strictly capped at 2.0% of FFP SOW unit price."
            ),
        },
        "SP5-03": {
            "recommended_option_key": "hold_firm",
            "selected_option_key": "hold_firm",
            "sme_status": "APPROVED",
            "sme_reviewer": "Capt. Devon Brooks (Lead, Supplier Cyber Defense)",
            "sme_rationale": (
                "Held firm on mandatory 72-hour DoD DFARS 252.204-7012 cyber incident reporting and "
                "NIST SP 800-171 Rev 2 controls."
            ),
        },
    },
    "BA-2026-LG-7740": {
        "GP1-12": {
            "recommended_option_key": "hold_firm",
            "selected_option_key": "hold_firm",
            "sme_status": "APPROVED",
            "sme_reviewer": "Dr. Aris Thorne (Principal FAA DER, Structural & Landing Gear QA)",
            "sme_rationale": (
                "Approved Hold Firm: Enforced 36-month airworthiness warranty on titanium landing gear forgings "
                "and mandatory unannounced FAA 14 CFR Part 21.140 ultrasonic NDT source inspections."
            ),
        },
        "SP3-04": {
            "recommended_option_key": "compromise_tier_1",
            "selected_option_key": "compromise_tier_1",
            "sme_status": "APPROVED",
            "sme_reviewer": "Marcus Chen, CPA (Director, Global Tax & Trade)",
            "sme_rationale": (
                "Approved Playbook Tier-1 Compromise: 50/50 Section 232 titanium forging tariff sharing above 5% "
                "threshold strictly capped at 2.0% aggregate FFP SOW adjustment."
            ),
        },
        "GP1-19": {
            "recommended_option_key": "compromise_tier_1",
            "selected_option_key": "compromise_tier_1",
            "sme_status": "PENDING",
            "sme_reviewer": "Pending SME Review (Elena Rostova, J.D. — Corporate Legal & IP)",
            "sme_rationale": (
                "Awaiting Corporate Legal & IP review of Meridian 1.0x ($52M) liability cap and structural "
                "trunnion pin integration IP carveout."
            ),
        },
        "SP5-03": {
            "recommended_option_key": "hold_firm",
            "selected_option_key": "hold_firm",
            "sme_status": "PENDING",
            "sme_reviewer": "Pending SME Review (Capt. Devon Brooks — Supplier Cyber Defense)",
            "sme_rationale": (
                "Awaiting Supplier Cyber Defense review of Meridian 7-business-day cyber notification redline "
                "against DFARS 252.204-7012 72-hour mandate."
            ),
        },
    },
}


def _format_ts(val: Any) -> str:
    if val is None:
        return datetime.now(timezone.utc).isoformat()
    if isinstance(val, datetime):
        return val.astimezone(timezone.utc).isoformat()
    return str(val)


class BigQueryCLMRepository:
    """Production BigQuery repository for Boeing CLM deal state, precedents, and conflict governance."""

    def __init__(self, project_id: str = GCP_PROJECT_ID, dataset: str = BQ_DATASET) -> None:
        self.project_id = project_id
        self.dataset = dataset
        self.client = bigquery.Client(project=project_id, location=BQ_LOCATION)
        self.precedent_engine = BigQueryPrecedentEngine(
            client=self.client, project_id=project_id, dataset=dataset
        )
        self.conflict_detector = BigQueryConflictDetector(
            client=self.client, project_id=project_id, dataset=dataset
        )

    @property
    def dataset_fqn(self) -> str:
        return f"{self.project_id}.{self.dataset}"

    def search_clause_precedents(
        self,
        clause_id: str,
        vendor_redline_text: str = "",
        supplier_tier: str = "Tier-1 Avionics",
        top_k: int = 5,
    ) -> PrecedentSearchResult:
        """Delegate live BigQuery `VECTOR_SEARCH` and `COUNTIF` distribution to `BigQueryPrecedentEngine`."""
        return self.precedent_engine.search_clause_precedents(
            clause_id=clause_id,
            vendor_redline_text=vendor_redline_text,
            supplier_tier=supplier_tier,
            top_k=top_k,
        )

    def get_deal_workbench_state(
        self,
        deal_id: str = DEFAULT_DEAL_ID,
        include_precedents: bool = True,
    ) -> DealWorkbenchState:
        """
        Retrieve complete `DealWorkbenchState` from live BigQuery (`active_deals`,
        `deal_clause_deviations`, `clause_conflict_rules`, `sme_review_events`, and
        optional `VECTOR_SEARCH` precedent analysis for redlined clauses).
        """
        sql = f"""
        WITH deal AS (
          SELECT *
          FROM `{self.dataset_fqn}.active_deals`
          WHERE deal_id = @deal_id
          LIMIT 1
        )
        SELECT
          d.deal_id,
          d.vendor_name,
          d.supplier_tier,
          d.boeing_program,
          d.contract_value_usd,
          d.proforma_stack,
          d.pricing_model,
          d.sow_cap_clause_ref,
          d.sharepoint_folder_url,
          d.deviation_matrix_xlsx,
          d.total_clauses_parsed,
          d.untouched_clauses_count,
          d.redlined_clauses_count,
          d.status,
          d.updated_at,
          ARRAY(
            SELECT AS STRUCT
              c.clause_id,
              c.proforma_doc,
              c.clause_ref,
              c.clause_title,
              c.has_redline,
              c.sme_team,
              c.sme_owner_label,
              c.risk_level,
              c.regulatory_flag,
              c.boeing_baseline_text,
              c.vendor_redline_text,
              c.diff_html,
              c.vendor_comment,
              c.recommended_option_key,
              c.recommended_counter_text,
              c.selected_option_key,
              c.selected_counter_text,
              c.sme_status,
              c.sme_reviewer,
              c.sme_rationale
            FROM `{self.dataset_fqn}.deal_clause_deviations` c
            WHERE c.deal_id = @deal_id
            ORDER BY c.clause_id ASC
          ) AS clauses,
          ARRAY(
            SELECT AS STRUCT
              e.event_id,
              e.deal_id,
              e.clause_id,
              e.sme_team,
              e.actor,
              e.action,
              e.selected_option_key,
              e.rationale,
              e.source_surface,
              e.created_at
            FROM `{self.dataset_fqn}.sme_review_events` e
            WHERE e.deal_id = @deal_id
            ORDER BY e.created_at DESC, e.event_id DESC
            LIMIT 25
          ) AS recent_events,
          ARRAY(
            SELECT AS STRUCT
              r.rule_id,
              r.rule_type,
              r.source_clause_id,
              r.target_clause_id,
              r.source_sme_team,
              r.target_sme_team,
              r.trigger_option_keys,
              r.forbidden_patterns,
              r.required_patterns,
              r.severity,
              r.conflict_title,
              r.conflict_description,
              r.harmonized_option_key,
              r.harmonized_resolution_text
            FROM `{self.dataset_fqn}.clause_conflict_rules` r
            ORDER BY r.rule_id ASC
          ) AS conflict_rules
        FROM deal d
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id)],
            labels=JOB_LABELS,
        )
        rows = list(self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result())
        if not rows:
            raise ValueError(f"Deal '{deal_id}' not found in `{self.dataset_fqn}.active_deals`.")

        row = rows[0]
        raw_clauses = [dict(c.items()) for c in (row["clauses"] or [])]
        raw_rules = [dict(r.items()) for r in (row["conflict_rules"] or [])]
        raw_events = [dict(e.items()) for e in (row["recent_events"] or [])]

        clauses_by_id = {c["clause_id"]: c for c in raw_clauses}

        # Evaluate declarative conflict & lockout rules against current clause positions
        active_conflicts: List[CrossClauseConflict] = []
        conflicted_clause_ids: set[str] = set()
        for rule in raw_rules:
            src_clause = clauses_by_id.get(rule["source_clause_id"])
            if not src_clause or not src_clause.get("has_redline"):
                continue
            if is_rule_triggered(
                rule,
                selected_option_key=src_clause.get("selected_option_key", ""),
                selected_counter_text=src_clause.get("selected_counter_text", ""),
            ):
                active_conflicts.append(row_to_conflict_model(rule))
                conflicted_clause_ids.add(rule["source_clause_id"])
                tgt_clause = clauses_by_id.get(rule["target_clause_id"])
                if tgt_clause and tgt_clause.get("has_redline") and tgt_clause.get("sme_status") == "CONFLICT":
                    conflicted_clause_ids.add(rule["target_clause_id"])

        # Optionally fetch live VECTOR_SEARCH precedent analysis for all redlined clauses in parallel
        precedent_map: Dict[str, PrecedentSearchResult] = {}
        if include_precedents:
            redlined_inputs = [
                {
                    "clause_id": c["clause_id"],
                    "vendor_redline_text": c["vendor_redline_text"],
                }
                for c in raw_clauses
                if c.get("has_redline")
            ]
            precedent_map = self.precedent_engine.search_redlined_clauses_parallel(
                redlined_clauses=redlined_inputs,
                supplier_tier=row["supplier_tier"],
                top_k=5,
                deal_id=deal_id,
            )

        clause_items: List[ClauseWorkbenchItem] = []
        for c in raw_clauses:
            cid = c["clause_id"]
            has_redline = bool(c["has_redline"])
            if not has_redline:
                effective_status = "UNTOUCHED"
            elif cid in conflicted_clause_ids:
                effective_status = "CONFLICT"
            elif c["sme_status"] == "CONFLICT" and cid not in conflicted_clause_ids:
                effective_status = "APPROVED"
            else:
                effective_status = c["sme_status"]

            clause_items.append(
                ClauseWorkbenchItem(
                    clause_id=cid,
                    proforma_doc=c["proforma_doc"],
                    clause_ref=c["clause_ref"],
                    clause_title=c["clause_title"],
                    has_redline=has_redline,
                    sme_team=c["sme_team"],
                    sme_owner_label=c["sme_owner_label"],
                    risk_level=c["risk_level"],
                    regulatory_flag=c["regulatory_flag"],
                    boeing_baseline_text=c["boeing_baseline_text"],
                    vendor_redline_text=c["vendor_redline_text"],
                    diff_html=c["diff_html"],
                    vendor_comment=c["vendor_comment"] or "",
                    recommended_option_key=c["recommended_option_key"],
                    recommended_counter_text=c["recommended_counter_text"],
                    selected_option_key=c["selected_option_key"],
                    selected_counter_text=c["selected_counter_text"],
                    sme_status=effective_status,
                    sme_reviewer=c["sme_reviewer"],
                    sme_rationale=c["sme_rationale"],
                    precedent_analysis=precedent_map.get(cid),
                )
            )

        # Compute deterministic deal status
        if active_conflicts or any(c.sme_status == "CONFLICT" for c in clause_items):
            deal_status = "CONFLICT_DETECTED"
        elif any(c.has_redline and c.sme_status == "PENDING" for c in clause_items):
            deal_status = "IN_SME_REVIEW"
        else:
            deal_status = "READY_FOR_DISPATCH"

        audit_items = [
            AuditEventItem(
                event_id=e["event_id"],
                deal_id=e["deal_id"],
                clause_id=e["clause_id"],
                sme_team=e["sme_team"],
                actor=e["actor"],
                action=e["action"],
                selected_option_key=e["selected_option_key"],
                rationale=e["rationale"],
                source_surface=e["source_surface"],
                created_at=_format_ts(e["created_at"]),
            )
            for e in raw_events
        ]

        untouched_count = sum(1 for c in clause_items if not c.has_redline)
        redlined_count = sum(1 for c in clause_items if c.has_redline)

        return DealWorkbenchState(
            deal_id=row["deal_id"],
            vendor_name=row["vendor_name"],
            supplier_tier=row["supplier_tier"],
            boeing_program=row["boeing_program"],
            contract_value_usd=float(row["contract_value_usd"]),
            proforma_stack=row["proforma_stack"],
            pricing_model=row["pricing_model"],
            sow_cap_clause_ref=row["sow_cap_clause_ref"],
            sharepoint_folder_url=row["sharepoint_folder_url"],
            deviation_matrix_xlsx=row["deviation_matrix_xlsx"],
            total_clauses_parsed=len(clause_items),
            untouched_clauses_count=untouched_count,
            redlined_clauses_count=redlined_count,
            status=deal_status,
            bigquery_dataset=self.dataset_fqn,
            clauses=clause_items,
            active_conflicts=active_conflicts,
            recent_events=audit_items,
            updated_at=_format_ts(row["updated_at"]),
        )

    def record_sme_submission(self, submission: SMEReviewSubmission) -> DealWorkbenchState:
        """
        Persist an SME review decision to `deal_clause_deviations`, evaluate declarative
        conflict/lockout rules against `clause_conflict_rules`, append an immutable event
        to `sme_review_events`, update `active_deals.status`, and return `DealWorkbenchState`.
        """
        validated = SMEReviewSubmission.model_validate(submission)
        triggered_conflicts = self.conflict_detector.evaluate_clause_submission(
            clause_id=validated.clause_id,
            selected_option_key=validated.selected_option_key,
            selected_counter_text=validated.selected_counter_text,
        )

        new_sme_status = "CONFLICT" if triggered_conflicts else "APPROVED"
        action_name = "CONFLICT_TRIGGERED" if triggered_conflicts else "SME_APPROVED"
        event_id = f"EVT-{uuid.uuid4().hex[:8].upper()}"

        dml_sql = f"""
        UPDATE `{self.dataset_fqn}.deal_clause_deviations`
        SET
          selected_option_key = @selected_option_key,
          selected_counter_text = @selected_counter_text,
          sme_status = @sme_status,
          sme_reviewer = @sme_reviewer,
          sme_rationale = @sme_rationale,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id
          AND clause_id = @clause_id;

        INSERT INTO `{self.dataset_fqn}.sme_review_events` (
          event_id, deal_id, clause_id, sme_team, actor, action,
          selected_option_key, selected_counter_text, rationale, source_surface, created_at
        )
        VALUES (
          @event_id, @deal_id, @clause_id, @sme_team, @sme_reviewer, @action_name,
          @selected_option_key, @selected_counter_text, @sme_rationale, @source_surface, CURRENT_TIMESTAMP()
        );

        UPDATE `{self.dataset_fqn}.active_deals`
        SET
          status = CASE
            WHEN EXISTS (
              SELECT 1 FROM `{self.dataset_fqn}.deal_clause_deviations` c
              WHERE c.deal_id = @deal_id AND c.sme_status = 'CONFLICT'
            ) THEN 'CONFLICT_DETECTED'
            WHEN EXISTS (
              SELECT 1 FROM `{self.dataset_fqn}.deal_clause_deviations` c
              WHERE c.deal_id = @deal_id AND c.has_redline = TRUE AND c.sme_status = 'PENDING'
            ) THEN 'IN_SME_REVIEW'
            ELSE 'READY_FOR_DISPATCH'
          END,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id;
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("deal_id", "STRING", validated.deal_id),
                bigquery.ScalarQueryParameter("clause_id", "STRING", validated.clause_id),
                bigquery.ScalarQueryParameter("sme_team", "STRING", validated.sme_team),
                bigquery.ScalarQueryParameter("selected_option_key", "STRING", validated.selected_option_key),
                bigquery.ScalarQueryParameter("selected_counter_text", "STRING", validated.selected_counter_text),
                bigquery.ScalarQueryParameter("sme_status", "STRING", new_sme_status),
                bigquery.ScalarQueryParameter("sme_reviewer", "STRING", validated.sme_reviewer),
                bigquery.ScalarQueryParameter("sme_rationale", "STRING", validated.sme_rationale),
                bigquery.ScalarQueryParameter("source_surface", "STRING", validated.source_surface),
                bigquery.ScalarQueryParameter("event_id", "STRING", event_id),
                bigquery.ScalarQueryParameter("action_name", "STRING", action_name),
            ],
            labels=JOB_LABELS,
        )
        self.client.query(dml_sql, job_config=job_config, location=BQ_LOCATION).result()
        return self.get_deal_workbench_state(deal_id=validated.deal_id, include_precedents=True)

    def list_active_deals(self) -> List[Dict[str, Any]]:
        """List all active portfolio deals from `boeing_clm.active_deals`."""
        sql = f"""
        SELECT
          deal_id,
          vendor_name,
          supplier_tier,
          boeing_program,
          contract_value_usd,
          proforma_stack,
          pricing_model,
          sow_cap_clause_ref,
          sharepoint_folder_url,
          deviation_matrix_xlsx,
          total_clauses_parsed,
          untouched_clauses_count,
          redlined_clauses_count,
          status,
          updated_at
        FROM `{self.dataset_fqn}.active_deals`
        ORDER BY deal_id ASC
        """
        job_config = bigquery.QueryJobConfig(labels=JOB_LABELS)
        rows = self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result()
        return [dict(r.items()) for r in rows]

    def harmonize_conflict(
        self,
        deal_id: str = DEFAULT_DEAL_ID,
        rule_id: str = "CONFLICT-SP3-04-GP1-03",
        actor: str = "Lead Contract Owner (M. Vance)",
        source_surface: str = "EXPERIENCE_LAYER_UI",
    ) -> DealWorkbenchState:
        """
        Resolve an active cross-clause conflict or regulatory lockout by applying
        `harmonized_resolution_text` from `boeing_clm.clause_conflict_rules` in BigQuery.
        """
        rule = self.conflict_detector.get_rule(rule_id)
        source_clause_id = rule["source_clause_id"]
        target_clause_id = rule["target_clause_id"]
        source_sme_team = rule["source_sme_team"]
        target_sme_team = rule["target_sme_team"]
        harmonized_option_key = rule["harmonized_option_key"]
        harmonized_text = rule["harmonized_resolution_text"]

        rationale = (
            f"Harmonized {rule_id} across {source_sme_team} ({source_clause_id}) and "
            f"{target_sme_team} ({target_clause_id}): applied Playbook harmonized resolution "
            f"({harmonized_option_key}) preserving {target_clause_id} guardrails."
        )
        event_id = f"EVT-{uuid.uuid4().hex[:8].upper()}"

        dml_sql = f"""
        UPDATE `{self.dataset_fqn}.deal_clause_deviations`
        SET
          selected_option_key = @harmonized_option_key,
          selected_counter_text = @harmonized_text,
          sme_status = 'APPROVED',
          sme_reviewer = @actor,
          sme_rationale = @rationale,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id
          AND clause_id = @source_clause_id;

        UPDATE `{self.dataset_fqn}.deal_clause_deviations`
        SET
          selected_option_key = 'hold_firm',
          selected_counter_text = boeing_baseline_text,
          sme_status = 'APPROVED',
          sme_reviewer = @actor,
          sme_rationale = @rationale,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id
          AND clause_id = @target_clause_id
          AND @target_clause_id != @source_clause_id
          AND sme_status = 'CONFLICT';

        INSERT INTO `{self.dataset_fqn}.sme_review_events` (
          event_id, deal_id, clause_id, sme_team, actor, action,
          selected_option_key, selected_counter_text, rationale, source_surface, created_at
        )
        VALUES (
          @event_id, @deal_id, @source_clause_id, @source_sme_team, @actor, 'CONFLICT_HARMONIZED',
          @harmonized_option_key, @harmonized_text, @rationale, @source_surface, CURRENT_TIMESTAMP()
        );

        UPDATE `{self.dataset_fqn}.active_deals`
        SET
          status = CASE
            WHEN EXISTS (
              SELECT 1 FROM `{self.dataset_fqn}.deal_clause_deviations` c
              WHERE c.deal_id = @deal_id AND c.sme_status = 'CONFLICT'
            ) THEN 'CONFLICT_DETECTED'
            WHEN EXISTS (
              SELECT 1 FROM `{self.dataset_fqn}.deal_clause_deviations` c
              WHERE c.deal_id = @deal_id AND c.has_redline = TRUE AND c.sme_status = 'PENDING'
            ) THEN 'IN_SME_REVIEW'
            ELSE 'READY_FOR_DISPATCH'
          END,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id;
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id),
                bigquery.ScalarQueryParameter("source_clause_id", "STRING", source_clause_id),
                bigquery.ScalarQueryParameter("target_clause_id", "STRING", target_clause_id),
                bigquery.ScalarQueryParameter("source_sme_team", "STRING", source_sme_team),
                bigquery.ScalarQueryParameter("harmonized_option_key", "STRING", harmonized_option_key),
                bigquery.ScalarQueryParameter("harmonized_text", "STRING", harmonized_text),
                bigquery.ScalarQueryParameter("actor", "STRING", actor),
                bigquery.ScalarQueryParameter("rationale", "STRING", rationale),
                bigquery.ScalarQueryParameter("source_surface", "STRING", source_surface),
                bigquery.ScalarQueryParameter("event_id", "STRING", event_id),
            ],
            labels=JOB_LABELS,
        )
        self.client.query(dml_sql, job_config=job_config, location=BQ_LOCATION).result()
        return self.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)

    def harmonize_clause_conflict(
        self,
        deal_id: str = DEFAULT_DEAL_ID,
        rule_id: str = "CONFLICT-SP3-04-GP1-03",
        actor: str = "Lead Contract Owner (M. Vance)",
        source_surface: str = "EXPERIENCE_LAYER_UI",
    ) -> DealWorkbenchState:
        """Alias for `harmonize_conflict` matching the FastMCP tool signature."""
        return self.harmonize_conflict(
            deal_id=deal_id,
            rule_id=rule_id,
            actor=actor,
            source_surface=source_surface,
        )

    def save_extracted_clauses(
        self,
        deal_id: str,
        diffs: List[ExtractedClauseDiff],
        source_surface: str = "GEMINI_AGENT_MCP",
    ) -> DealWorkbenchState:
        """
        Save extracted `.docx` Track Changes diffs into `boeing_clm.deal_clause_deviations`,
        log `INGESTED_REDLINE` in `boeing_clm.sme_review_events`, and return `DealWorkbenchState`.
        """
        validated_diffs = [ExtractedClauseDiff.model_validate(d) for d in diffs]
        deal_canonical_map = CANONICAL_INITIAL_POSITIONS_BY_DEAL.get(deal_id, CANONICAL_INITIAL_POSITIONS)

        # Fetch proforma fallbacks & current clause state in one query
        meta_sql = f"""
        SELECT
          p.clause_id,
          p.standard_text,
          p.fallback_tier_1_text,
          p.regulatory_lockout,
          d.selected_option_key AS existing_selected_option_key,
          d.selected_counter_text AS existing_selected_counter_text,
          d.sme_status AS existing_sme_status,
          d.sme_reviewer AS existing_sme_reviewer,
          d.sme_rationale AS existing_sme_rationale
        FROM `{self.dataset_fqn}.proforma_clauses` p
        LEFT JOIN `{self.dataset_fqn}.deal_clause_deviations` d
          ON d.deal_id = @deal_id
         AND d.clause_id = p.clause_id
        """
        meta_job = self.client.query(
            meta_sql,
            job_config=bigquery.QueryJobConfig(
                query_parameters=[bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id)],
                labels=JOB_LABELS,
            ),
            location=BQ_LOCATION,
        ).result()
        meta_by_id = {r["clause_id"]: dict(r.items()) for r in meta_job}

        # Build parameterized JSON payload for bulk MERGE/INSERT in BigQuery
        records_payload: List[Dict[str, Any]] = []
        for diff in validated_diffs:
            meta = meta_by_id.get(diff.clause_id, {})
            standard_text = meta.get("standard_text") or diff.boeing_baseline_text
            fallback_tier_1 = meta.get("fallback_tier_1_text") or diff.boeing_baseline_text
            reg_lockout = bool(meta.get("regulatory_lockout", False))

            if not diff.has_redline:
                rec_key = "hold_firm"
                rec_text = diff.boeing_baseline_text
                sel_key = "hold_firm"
                sel_text = diff.boeing_baseline_text
                sme_status = "UNTOUCHED"
                sme_reviewer = "Auto-Verified (No Redline)"
                sme_rationale = "Clause matches Boeing Proforma GP1/SP baseline with zero Track Changes."
            else:
                rec_key = "hold_firm" if reg_lockout else "compromise_tier_1"
                rec_text = standard_text if reg_lockout else fallback_tier_1

                canonical = deal_canonical_map.get(diff.clause_id, {})
                sel_key = meta.get("existing_selected_option_key") or canonical.get("selected_option_key", rec_key)
                if sel_key == "hold_firm":
                    default_sel_text = standard_text
                elif sel_key == "compromise_tier_1":
                    default_sel_text = fallback_tier_1
                else:
                    default_sel_text = diff.vendor_redline_text

                sel_text = meta.get("existing_selected_counter_text") or default_sel_text
                sme_status = meta.get("existing_sme_status") or canonical.get("sme_status", "PENDING")
                sme_reviewer = meta.get("existing_sme_reviewer") or canonical.get("sme_reviewer", "Pending SME Review")
                sme_rationale = meta.get("existing_sme_rationale") or canonical.get(
                    "sme_rationale", "Extracted from vendor redline .docx."
                )

            records_payload.append(
                {
                    "deal_id": deal_id,
                    "clause_id": diff.clause_id,
                    "proforma_doc": diff.proforma_doc,
                    "clause_ref": diff.clause_ref,
                    "clause_title": diff.clause_title,
                    "has_redline": diff.has_redline,
                    "sme_team": diff.sme_team,
                    "sme_owner_label": diff.sme_owner_label,
                    "risk_level": diff.risk_level,
                    "regulatory_flag": diff.regulatory_flag,
                    "boeing_baseline_text": diff.boeing_baseline_text,
                    "vendor_redline_text": diff.vendor_redline_text,
                    "diff_html": diff.diff_html,
                    "vendor_comment": " | ".join(diff.vendor_comments) if diff.vendor_comments else "",
                    "insertions_json": json.dumps(diff.insertions),
                    "deletions_json": json.dumps(diff.deletions),
                    "recommended_option_key": rec_key,
                    "recommended_counter_text": rec_text,
                    "selected_option_key": sel_key,
                    "selected_counter_text": sel_text,
                    "sme_status": sme_status,
                    "sme_reviewer": sme_reviewer,
                    "sme_rationale": sme_rationale,
                }
            )

        total_parsed = len(validated_diffs)
        untouched_cnt = sum(1 for d in validated_diffs if not d.has_redline)
        redlined_cnt = sum(1 for d in validated_diffs if d.has_redline)
        event_id = f"EVT-{uuid.uuid4().hex[:8].upper()}"

        dml_sql = f"""
        DELETE FROM `{self.dataset_fqn}.deal_clause_deviations`
        WHERE deal_id = @deal_id;

        INSERT INTO `{self.dataset_fqn}.deal_clause_deviations` (
          deal_id, clause_id, proforma_doc, clause_ref, clause_title, has_redline,
          sme_team, sme_owner_label, risk_level, regulatory_flag, boeing_baseline_text,
          vendor_redline_text, diff_html, vendor_comment, insertions_json, deletions_json,
          recommended_option_key, recommended_counter_text, selected_option_key,
          selected_counter_text, sme_status, sme_reviewer, sme_rationale, updated_at
        )
        SELECT
          JSON_VALUE(item, '$.deal_id'),
          JSON_VALUE(item, '$.clause_id'),
          JSON_VALUE(item, '$.proforma_doc'),
          JSON_VALUE(item, '$.clause_ref'),
          JSON_VALUE(item, '$.clause_title'),
          CAST(JSON_VALUE(item, '$.has_redline') AS BOOL),
          JSON_VALUE(item, '$.sme_team'),
          JSON_VALUE(item, '$.sme_owner_label'),
          JSON_VALUE(item, '$.risk_level'),
          JSON_VALUE(item, '$.regulatory_flag'),
          JSON_VALUE(item, '$.boeing_baseline_text'),
          JSON_VALUE(item, '$.vendor_redline_text'),
          JSON_VALUE(item, '$.diff_html'),
          JSON_VALUE(item, '$.vendor_comment'),
          JSON_VALUE(item, '$.insertions_json'),
          JSON_VALUE(item, '$.deletions_json'),
          JSON_VALUE(item, '$.recommended_option_key'),
          JSON_VALUE(item, '$.recommended_counter_text'),
          JSON_VALUE(item, '$.selected_option_key'),
          JSON_VALUE(item, '$.selected_counter_text'),
          JSON_VALUE(item, '$.sme_status'),
          JSON_VALUE(item, '$.sme_reviewer'),
          JSON_VALUE(item, '$.sme_rationale'),
          CURRENT_TIMESTAMP()
        FROM UNNEST(JSON_QUERY_ARRAY(@records_json)) AS item;

        UPDATE `{self.dataset_fqn}.active_deals`
        SET
          total_clauses_parsed = @total_parsed,
          untouched_clauses_count = @untouched_cnt,
          redlined_clauses_count = @redlined_cnt,
          updated_at = CURRENT_TIMESTAMP()
        WHERE deal_id = @deal_id;

        INSERT INTO `{self.dataset_fqn}.sme_review_events` (
          event_id, deal_id, clause_id, sme_team, actor, action,
          selected_option_key, selected_counter_text, rationale, source_surface, created_at
        )
        VALUES (
          @event_id, @deal_id, 'ALL', 'PROCUREMENT',
          'Lead Contract Owner (M. Vance)', 'INGESTED_REDLINE', 'hold_firm',
          CONCAT('Parsed ', CAST(@total_parsed AS STRING), ' clauses (', CAST(@untouched_cnt AS STRING), ' untouched, ', CAST(@redlined_cnt AS STRING), ' redlined).'),
          'Deterministic OOXML Track Changes extraction persisted to BigQuery deal_clause_deviations.',
          @source_surface, CURRENT_TIMESTAMP()
        );
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id),
                bigquery.ScalarQueryParameter("records_json", "STRING", json.dumps(records_payload)),
                bigquery.ScalarQueryParameter("total_parsed", "INT64", total_parsed),
                bigquery.ScalarQueryParameter("untouched_cnt", "INT64", untouched_cnt),
                bigquery.ScalarQueryParameter("redlined_cnt", "INT64", redlined_cnt),
                bigquery.ScalarQueryParameter("event_id", "STRING", event_id),
                bigquery.ScalarQueryParameter("source_surface", "STRING", source_surface),
            ],
            labels=JOB_LABELS,
        )
        self.client.query(dml_sql, job_config=job_config, location=BQ_LOCATION).result()
        return self.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)

    def reset_deal_workbench(
        self,
        deal_id: str = DEFAULT_DEAL_ID,
        source_surface: str = "EXPERIENCE_LAYER_UI",
        include_precedents: bool = True,
    ) -> DealWorkbenchState:
        """
        Reset `boeing_clm.deal_clause_deviations`, `active_deals`, and `sme_review_events`
        for `deal_id` (`BA-2026-AV-8921`, `BA-2026-TR-5510`, or `BA-2026-LG-7740`) to its
        canonical initial workbench state.
        """
        profile = CANONICAL_DEAL_PROFILES.get(deal_id)
        if profile is None:
            raise ValueError(f"Unknown deal_id '{deal_id}'. Expected one of {list(CANONICAL_DEAL_PROFILES.keys())}.")

        if deal_id == "BA-2026-AV-8921" and GOLDEN_EXPECTED_DIFFS_JSON.exists():
            raw_expected = json.loads(GOLDEN_EXPECTED_DIFFS_JSON.read_text(encoding="utf-8"))
            diffs = [ExtractedClauseDiff.model_validate(item) for item in raw_expected]
        else:
            fixture_path = GOLDEN_FIXTURES_DIR / profile["fixture_docx"]
            diffs = parse_redlined_docx(fixture_path)

        deal_canonical_map = CANONICAL_INITIAL_POSITIONS_BY_DEAL[deal_id]

        # Fetch proforma standard and fallback_tier_1 texts
        proforma_sql = f"""
        SELECT clause_id, standard_text, fallback_tier_1_text, regulatory_lockout
        FROM `{self.dataset_fqn}.proforma_clauses`
        """
        proforma_rows = self.client.query(
            proforma_sql,
            job_config=bigquery.QueryJobConfig(labels=JOB_LABELS),
            location=BQ_LOCATION,
        ).result()
        proforma_by_id = {r["clause_id"]: dict(r.items()) for r in proforma_rows}

        records_payload: List[Dict[str, Any]] = []
        for diff in diffs:
            p = proforma_by_id.get(diff.clause_id, {})
            standard_text = p.get("standard_text") or diff.boeing_baseline_text
            fallback_tier_1 = p.get("fallback_tier_1_text") or diff.boeing_baseline_text
            reg_lockout = bool(p.get("regulatory_lockout", False))

            if not diff.has_redline:
                rec_key = "hold_firm"
                rec_text = diff.boeing_baseline_text
                sel_key = "hold_firm"
                sel_text = diff.boeing_baseline_text
                sme_status = "UNTOUCHED"
                sme_reviewer = "Auto-Verified (No Redline)"
                sme_rationale = "Clause matches Cymbal Aerospace Proforma GP1/SP baseline with zero Track Changes."
            else:
                canonical = deal_canonical_map[diff.clause_id]
                rec_key = canonical["recommended_option_key"]
                rec_text = standard_text if reg_lockout else fallback_tier_1
                sel_key = canonical["selected_option_key"]
                if sel_key == "hold_firm":
                    sel_text = standard_text
                elif sel_key == "compromise_tier_1":
                    sel_text = fallback_tier_1
                else:
                    sel_text = diff.vendor_redline_text
                sme_status = canonical["sme_status"]
                sme_reviewer = canonical["sme_reviewer"]
                sme_rationale = canonical["sme_rationale"]

            records_payload.append(
                {
                    "deal_id": deal_id,
                    "clause_id": diff.clause_id,
                    "proforma_doc": diff.proforma_doc,
                    "clause_ref": diff.clause_ref,
                    "clause_title": diff.clause_title,
                    "has_redline": diff.has_redline,
                    "sme_team": diff.sme_team,
                    "sme_owner_label": diff.sme_owner_label,
                    "risk_level": diff.risk_level,
                    "regulatory_flag": diff.regulatory_flag,
                    "boeing_baseline_text": diff.boeing_baseline_text,
                    "vendor_redline_text": diff.vendor_redline_text,
                    "diff_html": diff.diff_html,
                    "vendor_comment": " | ".join(diff.vendor_comments) if diff.vendor_comments else "",
                    "insertions_json": json.dumps(diff.insertions),
                    "deletions_json": json.dumps(diff.deletions),
                    "recommended_option_key": rec_key,
                    "recommended_counter_text": rec_text,
                    "selected_option_key": sel_key,
                    "selected_counter_text": sel_text,
                    "sme_status": sme_status,
                    "sme_reviewer": sme_reviewer,
                    "sme_rationale": sme_rationale,
                }
            )

        rec_by_id = {r["clause_id"]: r for r in records_payload}
        deal_suffix = deal_id.split("-")[-1]
        events_payload: List[Dict[str, Any]] = [
            {
                "event_id": f"EVT-{deal_suffix}-001",
                "deal_id": deal_id,
                "clause_id": "ALL",
                "sme_team": "PROCUREMENT",
                "actor": "Lead Contract Owner (M. Vance)",
                "action": "INGESTED_REDLINE",
                "selected_option_key": "hold_firm",
                "selected_counter_text": (
                    f"Parsed {profile['total_clauses_parsed']} clauses from {profile['fixture_docx']}: "
                    f"{profile['untouched_clauses_count']} untouched auto-collapsed, "
                    f"{profile['redlined_clauses_count']} redlined routed to SMEs."
                ),
                "rationale": "Deterministic OOXML Track Changes extraction completed against Cymbal_GP1_Standard.docx.",
                "source_surface": "GEMINI_AGENT_MCP",
                "minutes_ago": "25",
            }
        ]
        evt_idx = 2
        for cid, r in rec_by_id.items():
            if not r["has_redline"] or r["sme_status"] == "PENDING":
                continue
            action_str = "CONFLICT_TRIGGERED" if r["sme_status"] == "CONFLICT" else "SME_APPROVED"
            events_payload.append(
                {
                    "event_id": f"EVT-{deal_suffix}-{evt_idx:03d}",
                    "deal_id": deal_id,
                    "clause_id": cid,
                    "sme_team": r["sme_team"],
                    "actor": r["sme_reviewer"],
                    "action": action_str,
                    "selected_option_key": r["selected_option_key"],
                    "selected_counter_text": r["selected_counter_text"],
                    "rationale": r["sme_rationale"],
                    "source_surface": source_surface if action_str == "CONFLICT_TRIGGERED" else "EXPERIENCE_LAYER_UI",
                    "minutes_ago": str(max(1, 22 - evt_idx * 4)),
                }
            )
            evt_idx += 1

        reset_sql = f"""
        DELETE FROM `{self.dataset_fqn}.deal_clause_deviations`
        WHERE deal_id = @deal_id;

        INSERT INTO `{self.dataset_fqn}.deal_clause_deviations` (
          deal_id, clause_id, proforma_doc, clause_ref, clause_title, has_redline,
          sme_team, sme_owner_label, risk_level, regulatory_flag, boeing_baseline_text,
          vendor_redline_text, diff_html, vendor_comment, insertions_json, deletions_json,
          recommended_option_key, recommended_counter_text, selected_option_key,
          selected_counter_text, sme_status, sme_reviewer, sme_rationale, updated_at
        )
        SELECT
          JSON_VALUE(item, '$.deal_id'),
          JSON_VALUE(item, '$.clause_id'),
          JSON_VALUE(item, '$.proforma_doc'),
          JSON_VALUE(item, '$.clause_ref'),
          JSON_VALUE(item, '$.clause_title'),
          CAST(JSON_VALUE(item, '$.has_redline') AS BOOL),
          JSON_VALUE(item, '$.sme_team'),
          JSON_VALUE(item, '$.sme_owner_label'),
          JSON_VALUE(item, '$.risk_level'),
          JSON_VALUE(item, '$.regulatory_flag'),
          JSON_VALUE(item, '$.boeing_baseline_text'),
          JSON_VALUE(item, '$.vendor_redline_text'),
          JSON_VALUE(item, '$.diff_html'),
          JSON_VALUE(item, '$.vendor_comment'),
          JSON_VALUE(item, '$.insertions_json'),
          JSON_VALUE(item, '$.deletions_json'),
          JSON_VALUE(item, '$.recommended_option_key'),
          JSON_VALUE(item, '$.recommended_counter_text'),
          JSON_VALUE(item, '$.selected_option_key'),
          JSON_VALUE(item, '$.selected_counter_text'),
          JSON_VALUE(item, '$.sme_status'),
          JSON_VALUE(item, '$.sme_reviewer'),
          JSON_VALUE(item, '$.sme_rationale'),
          CURRENT_TIMESTAMP()
        FROM UNNEST(JSON_QUERY_ARRAY(@records_json)) AS item;

        MERGE `{self.dataset_fqn}.active_deals` AS target
        USING (
          SELECT
            @deal_id AS deal_id,
            @vendor_name AS vendor_name,
            @supplier_tier AS supplier_tier,
            @boeing_program AS boeing_program,
            @contract_value_usd AS contract_value_usd,
            @proforma_stack AS proforma_stack,
            @pricing_model AS pricing_model,
            @sow_cap_clause_ref AS sow_cap_clause_ref,
            @sharepoint_folder_url AS sharepoint_folder_url,
            @deviation_matrix_xlsx AS deviation_matrix_xlsx,
            @total_clauses_parsed AS total_clauses_parsed,
            @untouched_clauses_count AS untouched_clauses_count,
            @redlined_clauses_count AS redlined_clauses_count,
            @initial_table_status AS status
        ) AS src
        ON target.deal_id = src.deal_id
        WHEN MATCHED THEN
          UPDATE SET
            vendor_name = src.vendor_name,
            supplier_tier = src.supplier_tier,
            boeing_program = src.boeing_program,
            contract_value_usd = src.contract_value_usd,
            proforma_stack = src.proforma_stack,
            pricing_model = src.pricing_model,
            sow_cap_clause_ref = src.sow_cap_clause_ref,
            sharepoint_folder_url = src.sharepoint_folder_url,
            deviation_matrix_xlsx = src.deviation_matrix_xlsx,
            total_clauses_parsed = src.total_clauses_parsed,
            untouched_clauses_count = src.untouched_clauses_count,
            redlined_clauses_count = src.redlined_clauses_count,
            status = src.status,
            updated_at = CURRENT_TIMESTAMP()
        WHEN NOT MATCHED THEN
          INSERT (
            deal_id, vendor_name, supplier_tier, boeing_program, contract_value_usd,
            proforma_stack, pricing_model, sow_cap_clause_ref, sharepoint_folder_url,
            deviation_matrix_xlsx, total_clauses_parsed, untouched_clauses_count,
            redlined_clauses_count, status, updated_at
          )
          VALUES (
            src.deal_id, src.vendor_name, src.supplier_tier, src.boeing_program, src.contract_value_usd,
            src.proforma_stack, src.pricing_model, src.sow_cap_clause_ref, src.sharepoint_folder_url,
            src.deviation_matrix_xlsx, src.total_clauses_parsed, src.untouched_clauses_count,
            src.redlined_clauses_count, src.status, CURRENT_TIMESTAMP()
          );

        DELETE FROM `{self.dataset_fqn}.sme_review_events`
        WHERE deal_id = @deal_id;

        INSERT INTO `{self.dataset_fqn}.sme_review_events` (
          event_id, deal_id, clause_id, sme_team, actor, action,
          selected_option_key, selected_counter_text, rationale, source_surface, created_at
        )
        SELECT
          JSON_VALUE(ev, '$.event_id'),
          JSON_VALUE(ev, '$.deal_id'),
          JSON_VALUE(ev, '$.clause_id'),
          JSON_VALUE(ev, '$.sme_team'),
          JSON_VALUE(ev, '$.actor'),
          JSON_VALUE(ev, '$.action'),
          JSON_VALUE(ev, '$.selected_option_key'),
          JSON_VALUE(ev, '$.selected_counter_text'),
          JSON_VALUE(ev, '$.rationale'),
          JSON_VALUE(ev, '$.source_surface'),
          TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL CAST(JSON_VALUE(ev, '$.minutes_ago') AS INT64) MINUTE)
        FROM UNNEST(JSON_QUERY_ARRAY(@events_json)) AS ev;
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id),
                bigquery.ScalarQueryParameter("records_json", "STRING", json.dumps(records_payload)),
                bigquery.ScalarQueryParameter("events_json", "STRING", json.dumps(events_payload)),
                bigquery.ScalarQueryParameter("vendor_name", "STRING", profile["vendor_name"]),
                bigquery.ScalarQueryParameter("supplier_tier", "STRING", profile["supplier_tier"]),
                bigquery.ScalarQueryParameter("boeing_program", "STRING", profile["boeing_program"]),
                bigquery.ScalarQueryParameter("contract_value_usd", "FLOAT64", float(profile["contract_value_usd"])),
                bigquery.ScalarQueryParameter("proforma_stack", "STRING", profile["proforma_stack"]),
                bigquery.ScalarQueryParameter("pricing_model", "STRING", profile["pricing_model"]),
                bigquery.ScalarQueryParameter("sow_cap_clause_ref", "STRING", profile["sow_cap_clause_ref"]),
                bigquery.ScalarQueryParameter("sharepoint_folder_url", "STRING", profile["sharepoint_folder_url"]),
                bigquery.ScalarQueryParameter("deviation_matrix_xlsx", "STRING", profile["deviation_matrix_xlsx"]),
                bigquery.ScalarQueryParameter("total_clauses_parsed", "INT64", int(profile["total_clauses_parsed"])),
                bigquery.ScalarQueryParameter("untouched_clauses_count", "INT64", int(profile["untouched_clauses_count"])),
                bigquery.ScalarQueryParameter("redlined_clauses_count", "INT64", int(profile["redlined_clauses_count"])),
                bigquery.ScalarQueryParameter("initial_table_status", "STRING", profile["initial_table_status"]),
            ],
            labels=JOB_LABELS,
        )
        self.client.query(reset_sql, job_config=job_config, location=BQ_LOCATION).result()
        return self.get_deal_workbench_state(deal_id=deal_id, include_precedents=include_precedents)
