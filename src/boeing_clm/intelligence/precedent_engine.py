"""
src/boeing_clm/intelligence/precedent_engine.py — Live BigQuery Vector Search & Precedent Analytics.

Executes `VECTOR_SEARCH` with `ML.GENERATE_EMBEDDING` (`text_embedding_005`) and `COUNTIF`
statistical outcome aggregations strictly against live BigQuery (`vertex-ai-demos-468803.boeing_clm`).
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from google.cloud import bigquery

from boeing_clm.config import BQ_DATASET, BQ_LOCATION, DEFAULT_DEAL_ID, GCP_PROJECT_ID
from boeing_clm.models import (
    OutcomeDistribution,
    PlaybookOption,
    PrecedentMatchItem,
    PrecedentSearchResult,
)

JOB_LABELS = {"datacloud": "antigravity"}


def build_playbook_options(
    clause_id: str,
    standard_text: str,
    fallback_tier_1_text: str,
    vendor_redline_text: str,
    regulatory_lockout: bool,
) -> List[PlaybookOption]:
    """Construct the 3 canonical Boeing CLM Playbook Options for a clause."""
    if regulatory_lockout:
        hold_badge = "REGULATORY MANDATE • RECOMMENDED"
        hold_class = "badge-critical"
        tier1_badge = "TIER-1 FALLBACK (PERMITTED)"
        tier1_class = "badge-warning"
        vendor_badge = "REGULATORY LOCKOUT VIOLATION"
    elif clause_id == "SP3-04":
        hold_badge = "BOEING BASELINE (100% DDP)"
        hold_class = "badge-info"
        tier1_badge = "HARMONIZED 2.0% CAP • RECOMMENDED"
        tier1_class = "badge-success"
        vendor_badge = "TRIGGERS GP1 §3.1 SOW CAP CONFLICT"
    else:
        hold_badge = "BOEING BASELINE"
        hold_class = "badge-info"
        tier1_badge = "PLAYBOOK TIER-1 • RECOMMENDED"
        tier1_class = "badge-success"
        vendor_badge = "HIGH COMMERCIAL RISK"

    return [
        PlaybookOption(
            option_key="hold_firm",
            label="Option A — Hold Firm (Boeing Proforma Baseline)",
            badge=hold_badge,
            badge_class=hold_class,
            counter_text=standard_text,
        ),
        PlaybookOption(
            option_key="compromise_tier_1",
            label="Option B — Playbook Tier-1 Compromise",
            badge=tier1_badge,
            badge_class=tier1_class,
            counter_text=fallback_tier_1_text,
        ),
        PlaybookOption(
            option_key="accept_vendor",
            label="Option C — Accept Vendor Redline",
            badge=vendor_badge,
            badge_class="badge-danger",
            counter_text=vendor_redline_text or standard_text,
        ),
    ]


class BigQueryPrecedentEngine:
    """Live BigQuery Vector Search and statistical precedent distribution engine."""

    def __init__(
        self,
        client: Optional[bigquery.Client] = None,
        project_id: str = GCP_PROJECT_ID,
        dataset: str = BQ_DATASET,
    ) -> None:
        self.project_id = project_id
        self.dataset = dataset
        self.client = client or bigquery.Client(project=project_id, location=BQ_LOCATION)

    @property
    def dataset_fqn(self) -> str:
        return f"{self.project_id}.{self.dataset}"

    def search_clause_precedents(
        self,
        clause_id: str,
        vendor_redline_text: str = "",
        supplier_tier: str = "Tier-1 Avionics",
        top_k: int = 5,
        deal_id: str = DEFAULT_DEAL_ID,
    ) -> PrecedentSearchResult:
        """
        Execute live BigQuery `VECTOR_SEARCH` (`COSINE` distance with `text_embedding_005`)
        and `COUNTIF` statistical aggregation against `historical_clause_exceptions`.
        """
        sql = f"""
        WITH query_vec AS (
          SELECT ml_generate_embedding_result AS embedding
          FROM ML.GENERATE_EMBEDDING(
            MODEL `{self.dataset_fqn}.text_embedding_005`,
            (
              SELECT
                CONCAT(
                  @clause_id, ' | Supplier Tier: ', @supplier_tier, ' | Vendor Redline: ',
                  COALESCE(
                    NULLIF(@vendor_redline_text, ''),
                    (SELECT vendor_redline_text FROM `{self.dataset_fqn}.deal_clause_deviations` WHERE deal_id = @deal_id AND clause_id = @clause_id LIMIT 1),
                    (SELECT standard_text FROM `{self.dataset_fqn}.proforma_clauses` WHERE clause_id = @clause_id LIMIT 1),
                    @clause_id
                  )
                ) AS content
            ),
            STRUCT(TRUE AS flatten_json_output, 'RETRIEVAL_QUERY' AS task_type)
          )
        ),
        vector_matches AS (
          SELECT
            base.exception_id,
            base.clause_id,
            base.contract_id,
            base.supplier_name,
            base.supplier_tier,
            base.boeing_program,
            base.vendor_requested_redline,
            base.final_agreed_language,
            base.outcome_category,
            base.approval_authority,
            base.negotiation_notes,
            CAST(base.signed_date AS STRING) AS signed_date,
            GREATEST(0.0, LEAST(1.0, ROUND(1.0 - distance, 4))) AS similarity_score
          FROM VECTOR_SEARCH(
            (
              SELECT
                exception_id,
                clause_id,
                contract_id,
                supplier_name,
                supplier_tier,
                boeing_program,
                vendor_requested_redline,
                final_agreed_language,
                outcome_category,
                approval_authority,
                negotiation_notes,
                signed_date,
                embedding
              FROM `{self.dataset_fqn}.historical_clause_exceptions`
              WHERE (clause_id = @clause_id OR @clause_id NOT IN ('GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'))
            ),
            'embedding',
            TABLE query_vec,
            top_k => @top_k,
            distance_type => 'COSINE'
          )
        ),
        resolved_domain AS (
          SELECT
            COALESCE(
              (SELECT clause_id FROM `{self.dataset_fqn}.proforma_clauses` WHERE clause_id = @clause_id LIMIT 1),
              (SELECT clause_id FROM vector_matches ORDER BY similarity_score DESC LIMIT 1),
              'GP1-19'
            ) AS domain_clause_id
        ),
        clause_meta AS (
          SELECT
            @clause_id AS clause_id,
            p.clause_ref,
            p.clause_title,
            p.sme_team,
            p.standard_text,
            p.fallback_tier_1_text,
            p.fallback_tier_2_text,
            p.regulatory_lockout,
            p.regulatory_citation,
            p.guardrail_summary,
            COALESCE(
              NULLIF(@vendor_redline_text, ''),
              d.vendor_redline_text,
              p.standard_text
            ) AS effective_vendor_redline_text
          FROM `{self.dataset_fqn}.proforma_clauses` p
          CROSS JOIN resolved_domain rd
          LEFT JOIN `{self.dataset_fqn}.deal_clause_deviations` d
            ON d.deal_id = @deal_id
           AND d.clause_id = @clause_id
          WHERE p.clause_id = rd.domain_clause_id
          LIMIT 1
        ),
        clause_exceptions AS (
          SELECT
            e.*
          FROM `{self.dataset_fqn}.historical_clause_exceptions` e
          CROSS JOIN resolved_domain rd
          WHERE e.clause_id = rd.domain_clause_id
            AND ARRAY_LENGTH(e.embedding) = 768
        ),
        dist AS (
          SELECT
            COUNT(*) AS total_matches,
            COUNTIF(outcome_category = 'HELD_FIRM') AS held_firm_count,
            CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'HELD_FIRM') * 100.0, COUNT(*))) AS INT64) AS held_firm_pct,
            COUNTIF(outcome_category = 'COMPROMISE_TIER_1') AS compromise_tier_1_count,
            CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'COMPROMISE_TIER_1') * 100.0, COUNT(*))) AS INT64) AS compromise_tier_1_pct,
            COUNTIF(outcome_category = 'ACCEPTED_VENDOR') AS accepted_vendor_count,
            CAST(ROUND(SAFE_DIVIDE(COUNTIF(outcome_category = 'ACCEPTED_VENDOR') * 100.0, COUNT(*))) AS INT64) AS accepted_vendor_pct
          FROM clause_exceptions
        )
        SELECT
          m.clause_id,
          m.clause_ref,
          m.clause_title,
          m.sme_team,
          m.standard_text,
          m.fallback_tier_1_text,
          m.fallback_tier_2_text,
          m.regulatory_lockout,
          m.regulatory_citation,
          m.guardrail_summary,
          m.effective_vendor_redline_text,
          IFNULL(d.total_matches, 0) AS total_matches,
          IFNULL(d.held_firm_count, 0) AS held_firm_count,
          IFNULL(d.held_firm_pct, 0) AS held_firm_pct,
          IFNULL(d.compromise_tier_1_count, 0) AS compromise_tier_1_count,
          IFNULL(d.compromise_tier_1_pct, 0) AS compromise_tier_1_pct,
          IFNULL(d.accepted_vendor_count, 0) AS accepted_vendor_count,
          IFNULL(d.accepted_vendor_pct, 0) AS accepted_vendor_pct,
          ARRAY(
            SELECT AS STRUCT
              exception_id,
              clause_id,
              contract_id,
              supplier_name,
              supplier_tier,
              boeing_program,
              vendor_requested_redline,
              final_agreed_language,
              outcome_category,
              approval_authority,
              negotiation_notes,
              signed_date,
              similarity_score
            FROM vector_matches
            ORDER BY similarity_score DESC, signed_date DESC
          ) AS precedents
        FROM clause_meta m
        CROSS JOIN dist d
        """
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("clause_id", "STRING", clause_id),
                bigquery.ScalarQueryParameter("vendor_redline_text", "STRING", vendor_redline_text or ""),
                bigquery.ScalarQueryParameter("supplier_tier", "STRING", supplier_tier or "Tier-1 Avionics"),
                bigquery.ScalarQueryParameter("top_k", "INT64", int(top_k)),
                bigquery.ScalarQueryParameter("deal_id", "STRING", deal_id),
            ],
            labels=JOB_LABELS,
        )
        rows = list(self.client.query(sql, job_config=job_config, location=BQ_LOCATION).result())
        if not rows:
            raise ValueError(f"Clause '{clause_id}' not found in `{self.dataset_fqn}.proforma_clauses`.")

        row = rows[0]
        distribution = OutcomeDistribution(
            total_matches=int(row["total_matches"] or 0),
            held_firm_count=int(row["held_firm_count"] or 0),
            held_firm_pct=int(row["held_firm_pct"] or 0),
            compromise_tier_1_count=int(row["compromise_tier_1_count"] or 0),
            compromise_tier_1_pct=int(row["compromise_tier_1_pct"] or 0),
            accepted_vendor_count=int(row["accepted_vendor_count"] or 0),
            accepted_vendor_pct=int(row["accepted_vendor_pct"] or 0),
        )

        precedent_items = [
            PrecedentMatchItem(
                exception_id=p["exception_id"],
                clause_id=p["clause_id"],
                contract_id=p["contract_id"],
                supplier_name=p["supplier_name"],
                supplier_tier=p["supplier_tier"],
                boeing_program=p["boeing_program"],
                vendor_requested_redline=p["vendor_requested_redline"],
                final_agreed_language=p["final_agreed_language"],
                outcome_category=p["outcome_category"],
                approval_authority=p["approval_authority"],
                negotiation_notes=p["negotiation_notes"],
                signed_date=str(p["signed_date"]),
                similarity_score=float(p["similarity_score"]),
            )
            for p in (row["precedents"] or [])
        ]

        playbook_options = build_playbook_options(
            clause_id=row["clause_id"],
            standard_text=row["standard_text"],
            fallback_tier_1_text=row["fallback_tier_1_text"],
            vendor_redline_text=row["effective_vendor_redline_text"],
            regulatory_lockout=bool(row["regulatory_lockout"]),
        )

        return PrecedentSearchResult(
            clause_id=row["clause_id"],
            clause_ref=row["clause_ref"],
            clause_title=row["clause_title"],
            sme_team=row["sme_team"],
            guardrail_summary=row["guardrail_summary"],
            regulatory_lockout=bool(row["regulatory_lockout"]),
            regulatory_citation=row["regulatory_citation"],
            distribution=distribution,
            precedents=precedent_items,
            playbook_options=playbook_options,
        )

    def search_redlined_clauses_parallel(
        self,
        redlined_clauses: List[Dict[str, str]],
        supplier_tier: str = "Tier-1 Avionics",
        top_k: int = 5,
        deal_id: str = DEFAULT_DEAL_ID,
    ) -> Dict[str, PrecedentSearchResult]:
        """Run `search_clause_precedents` concurrently across multiple redlined clauses."""
        if not redlined_clauses:
            return {}

        def _fetch(item: Dict[str, str]) -> tuple[str, PrecedentSearchResult]:
            cid = item["clause_id"]
            res = self.search_clause_precedents(
                clause_id=cid,
                vendor_redline_text=item.get("vendor_redline_text", ""),
                supplier_tier=supplier_tier,
                top_k=top_k,
                deal_id=deal_id,
            )
            return cid, res

        results: Dict[str, PrecedentSearchResult] = {}
        with ThreadPoolExecutor(max_workers=min(4, len(redlined_clauses))) as pool:
            for cid, res in pool.map(_fetch, redlined_clauses):
                results[cid] = res
        return results
