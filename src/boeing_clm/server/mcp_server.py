"""
src/boeing_clm/server/mcp_server.py — FastMCP Server for Boeing CLM Engine.
Exposes all 6 deterministic CLM tools defined in specs/03_mcp_and_rest_contract.md
for Gemini Agent (Spark) and broadcasts state mutations to the Experience Layer UI via SSE.
"""
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastmcp import FastMCP

from boeing_clm.config import (
    BQ_DATASET,
    EXPORTS_DIR,
    GCP_PROJECT_ID,
    PROJECT_ROOT,
)
from boeing_clm.export.docx_generator import generate_counter_proposal_docx
from boeing_clm.export.xlsx_generator import generate_deviation_matrix_xlsx
from boeing_clm.ingestion.docx_track_changes import parse_redlined_docx
from boeing_clm.models import (
    DealWorkbenchState,
    ExtractedClauseDiff,
    PrecedentSearchResult,
    SMEReviewSubmission,
)

try:
    from boeing_clm.storage.repository import BigQueryCLMRepository
except ImportError:
    BigQueryCLMRepository = None  # type: ignore[assignment,misc]

mcp = FastMCP("Boeing-CLM-Engine")

_repository: Any = None
_sse_subscribers: list[tuple[asyncio.AbstractEventLoop, asyncio.Queue[dict[str, Any]]]] = []


def get_repository() -> Any:
    """Return the singleton BigQueryCLMRepository connected to live BigQuery."""
    global _repository, BigQueryCLMRepository
    if BigQueryCLMRepository is None:
        from boeing_clm.storage.repository import BigQueryCLMRepository as _Repo

        BigQueryCLMRepository = _Repo
    if _repository is None:
        _repository = BigQueryCLMRepository(project_id=GCP_PROJECT_ID, dataset=BQ_DATASET)
    return _repository


def register_sse_subscriber(loop: asyncio.AbstractEventLoop, queue: asyncio.Queue[dict[str, Any]]) -> None:
    """Register an SSE subscriber queue bound to an event loop."""
    _sse_subscribers.append((loop, queue))


def unregister_sse_subscriber(queue: asyncio.Queue[dict[str, Any]]) -> None:
    """Remove a disconnected SSE subscriber queue."""
    global _sse_subscribers
    _sse_subscribers = [(lp, q) for lp, q in _sse_subscribers if q is not queue]


def notify_sse_subscribers(
    event_type: str,
    deal_id: str,
    summary: str,
    source_surface: str = "GEMINI_AGENT_MCP",
) -> None:
    """Thread-safe broadcast of state-mutating events to all connected browser SSE streams."""
    payload = {
        "event_type": event_type,
        "deal_id": deal_id,
        "summary": summary,
        "source_surface": source_surface,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    for loop, queue in list(_sse_subscribers):
        try:
            if loop.is_running():
                loop.call_soon_threadsafe(queue.put_nowait, payload)
            else:
                queue.put_nowait(payload)
        except Exception:
            pass


def _resolve_project_path(raw_path: str | Path) -> Path:
    """Resolve relative fixture/export paths against PROJECT_ROOT if not found in CWD."""
    p = Path(raw_path)
    if p.exists():
        return p.resolve()
    candidate = (PROJECT_ROOT / p).resolve()
    if candidate.exists():
        return candidate
    return p.resolve()


def build_export_package_manifest(
    state: DealWorkbenchState,
    docx_path: Path,
    xlsx_path: Path,
) -> dict[str, Any]:
    """Assemble the deterministic M365 Outlook draft, SharePoint/Teams manifest, and artifact metadata."""
    redlined = [c for c in state.clauses if c.has_redline]
    untouched = [c for c in state.clauses if not c.has_redline]

    clause_lines: list[str] = []
    for idx, c in enumerate(redlined, start=1):
        clause_lines.append(
            f"{idx}. {c.clause_ref} — {c.clause_title} [{c.sme_team} | {c.sme_status}]\n"
            f"   • Selected Option: {c.selected_option_key}\n"
            f"   • Boeing Counter-Language: {c.selected_counter_text}\n"
            f"   • SME Rationale & Regulatory Basis ({c.sme_reviewer}): {c.sme_rationale}"
        )

    conflict_note = (
        "All 4 SME domains (Engineering/FAA, Corporate Legal, Global Tax, Supplier Cyber) are aligned with zero cross-clause conflicts."
        if len(state.active_conflicts) == 0
        else f"WARNING: {len(state.active_conflicts)} active cross-clause conflict(s) remain pending harmonization ({', '.join(cf.rule_id for cf in state.active_conflicts)})."
    )

    outlook_subject = (
        f"[Cymbal Aerospace Counter-Proposal] {state.deal_id} — {state.vendor_name} "
        f"({state.proforma_stack} | ${state.contract_value_usd:,.0f})"
    )
    outlook_body = "\n".join(
        [
            f"TO: Contracts & Legal Counsel — {state.vendor_name}",
            "FROM: Cymbal Aerospace Corporation — Avionics Supplier Management & Procurement",
            f"SUBJECT: {outlook_subject}",
            "",
            f"Dear {state.vendor_name} Contracts Team,",
            "",
            f"Following cross-functional review by Cymbal Aerospace Engineering/Quality (FAA DER), Corporate Legal, Global Tax & Trade, and Supplier Cybersecurity against Cymbal Aerospace's CLM Precedent Repository ({state.bigquery_dataset}), please find attached Cymbal Aerospace's consolidated counter-proposal for Deal {state.deal_id} ({state.boeing_program}, {state.pricing_model}).",
            "",
            f"EXECUTIVE SUMMARY ({state.total_clauses_parsed} Total Clauses Parsed):",
            f"• {state.untouched_clauses_count} Baseline Clauses Accepted Without Deviation ({', '.join(c.clause_ref for c in untouched)})",
            f"• {state.redlined_clauses_count} Material Redline Clauses Countered with Native Word Track Changes & SME Margin Comments",
            f"• Cross-Functional Governance Status: {state.status} — {conflict_note}",
            "",
            "CONSOLIDATED CYMBAL AEROSPACE COUNTER-POSITIONS ON REDLINED CLAUSES:",
            "",
            "\n\n".join(clause_lines),
            "",
            "ATTACHMENTS (Generated Deterministically via Cymbal CLM Engine):",
            f"1. {docx_path.name} — Full 12-clause contract with native Word <w:del>/<w:ins> Track Changes and <w:comment> SME rationales",
            f"2. {xlsx_path.name} — 4-Tab SharePoint Deviation Matrix (Executive Summary, Clause Sign-Off Matrix, BigQuery Precedents, Immutable SME Audit Trail)",
            "",
            "Sincerely,",
            "Marcus Vance — Vice President, Avionics Procurement, Cymbal Aerospace Corporation",
        ]
    )

    return {
        "deal_id": state.deal_id,
        "vendor_name": state.vendor_name,
        "status": state.status,
        "ready_for_dispatch": state.status == "READY_FOR_DISPATCH" and len(state.active_conflicts) == 0,
        "active_conflicts_count": len(state.active_conflicts),
        "total_clauses_parsed": state.total_clauses_parsed,
        "untouched_clauses_count": state.untouched_clauses_count,
        "redlined_clauses_count": state.redlined_clauses_count,
        "docx_filename": docx_path.name,
        "docx_local_path": str(docx_path),
        "docx_size_bytes": docx_path.stat().st_size if docx_path.exists() else 0,
        "docx_download_url": f"/api/deals/{state.deal_id}/export/docx",
        "xlsx_filename": xlsx_path.name,
        "xlsx_local_path": str(xlsx_path),
        "xlsx_size_bytes": xlsx_path.stat().st_size if xlsx_path.exists() else 0,
        "xlsx_download_url": f"/api/deals/{state.deal_id}/export/xlsx",
        "outlook_draft": {
            "connector": "ms-outlook",
            "to": ["contracts@apexaerosystems.com", "general.counsel@apexaerosystems.com"],
            "cc": [
                "m365-admin@rahulsankrut.demo.altostrat.com",
                "JoniS@36zrbd.onmicrosoft.com",
                "LeeG@36zrbd.onmicrosoft.com",
                "JohannaL@36zrbd.onmicrosoft.com",
            ],
            "subject": outlook_subject,
            "body_text": outlook_body,
            "attachments": [docx_path.name, xlsx_path.name],
        },
        "m365_connector_actions": [
            {
                "connector": "ms-sharepoint",
                "action": "Upload Consolidated Counter-Proposal & 4-Tab Deviation Matrix",
                "target_url": state.sharepoint_folder_url,
                "artifacts": [docx_path.name, xlsx_path.name],
                "status": "READY",
            },
            {
                "connector": "ms-onedrive",
                "action": "Archive Working Redline & Track-Changes Diff Package",
                "target_url": f"https://36zrbd-my.sharepoint.com/personal/m365-admin_rahulsankrut_demo_altostrat_com/Documents/CymbalAerospace_CLM/{state.deal_id}",
                "artifacts": [docx_path.name],
                "status": "READY",
            },
            {
                "connector": "ms-teams",
                "action": "Post Multi-SME Sign-Off Completion Card to #deal-ba-2026-av-8921",
                "channel": "Cymbal Aerospace Avionics Procurement > Deal BA-2026-AV-8921",
                "summary": conflict_note,
                "status": "READY",
            },
            {
                "connector": "ms-outlook",
                "action": "Stage External Vendor Counter-Proposal Response Draft",
                "recipient": "contracts@apexaerosystems.com",
                "subject": outlook_subject,
                "status": "READY",
            },
        ],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


@mcp.tool
def ingest_vendor_redline(
    deal_id: str = "BA-2026-AV-8921",
    vendor_docx_path: str = "specs/04_golden_fixtures/Vendor_Redlined_GP1.docx",
    baseline_docx_path: str = "specs/04_golden_fixtures/Boeing_GP1_Standard.docx",
) -> dict:
    """
    Parse a vendor-redlined .docx contract (12 clauses: 8 untouched, 4 redlined)
    using lxml OOXML Track Changes (<w:ins>, <w:del>, <w:comment>), persist to
    live BigQuery (boeing_clm.deal_clause_deviations & sme_review_events), and
    return the full DealWorkbenchState.
    """
    resolved_vendor_path = _resolve_project_path(vendor_docx_path)
    _ = _resolve_project_path(baseline_docx_path)

    extracted = parse_redlined_docx(resolved_vendor_path)
    validated_diffs = [ExtractedClauseDiff.model_validate(item) for item in extracted]

    repo = get_repository()
    state = repo.save_extracted_clauses(
        deal_id=deal_id,
        diffs=validated_diffs,
        source_surface="GEMINI_AGENT_MCP",
    )
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="INGESTED_REDLINE",
        deal_id=deal_id,
        summary=(
            f"Ingested {validated_state.total_clauses_parsed} clauses "
            f"({validated_state.untouched_clauses_count} untouched, {validated_state.redlined_clauses_count} redlined)"
        ),
        source_surface="GEMINI_AGENT_MCP",
    )
    return validated_state.model_dump()


@mcp.tool
def analyze_clause_precedents(
    clause_id: str,
    vendor_redline_text: str = "",
    supplier_tier: str = "Tier-1 Avionics",
    top_k: int = 5,
) -> dict:
    """
    Execute live BigQuery VECTOR_SEARCH (COSINE distance with boeing_clm.text_embedding_005)
    against boeing_clm.historical_clause_exceptions and compute dynamic SQL COUNTIF
    outcome distribution percentages for a specific clause.
    """
    repo = get_repository()
    result = repo.search_clause_precedents(
        clause_id=clause_id,
        vendor_redline_text=vendor_redline_text,
        supplier_tier=supplier_tier,
        top_k=top_k,
    )
    validated = PrecedentSearchResult.model_validate(result)
    return validated.model_dump()


@mcp.tool
def record_sme_position(
    deal_id: str,
    clause_id: str,
    sme_team: str,
    selected_option_key: str,
    selected_counter_text: str,
    sme_reviewer: str,
    sme_rationale: str,
) -> dict:
    """
    Validate and record a domain SME's counter-position in BigQuery, append an immutable
    row to boeing_clm.sme_review_events, evaluate cross-clause conflict rules against
    boeing_clm.clause_conflict_rules, and broadcast an SSE update to the UI.
    """
    submission = SMEReviewSubmission(
        deal_id=deal_id,
        clause_id=clause_id,
        sme_team=sme_team,  # type: ignore[arg-type]
        selected_option_key=selected_option_key,  # type: ignore[arg-type]
        selected_counter_text=selected_counter_text,
        sme_reviewer=sme_reviewer,
        sme_rationale=sme_rationale,
        source_surface="GEMINI_AGENT_MCP",
    )
    repo = get_repository()
    state = repo.record_sme_submission(submission)
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="SME_POSITION_RECORDED",
        deal_id=deal_id,
        summary=f"{sme_team} ({sme_reviewer}) committed '{selected_option_key}' on {clause_id}",
        source_surface="GEMINI_AGENT_MCP",
    )
    return validated_state.model_dump()


@mcp.tool
def harmonize_clause_conflict(
    deal_id: str = "BA-2026-AV-8921",
    rule_id: str = "CONFLICT-SP3-04-GP1-03",
    actor: str = "Lead Contract Owner (M. Vance)",
) -> dict:
    """
    Resolve an active cross-clause conflict (e.g. SP3-04 Tariff Pass-Through vs. GP1-03
    Firm-Fixed-Price SOW Cap) using the pre-approved harmonized resolution text from
    boeing_clm.clause_conflict_rules, log CONFLICT_HARMONIZED to BigQuery, and notify SSE.
    """
    repo = get_repository()
    state = repo.harmonize_conflict(
        deal_id=deal_id,
        rule_id=rule_id,
        actor=actor,
        source_surface="GEMINI_AGENT_MCP",
    )
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="CONFLICT_HARMONIZED",
        deal_id=deal_id,
        summary=f"Cross-clause conflict {rule_id} harmonized by {actor}",
        source_surface="GEMINI_AGENT_MCP",
    )
    return validated_state.model_dump()


@mcp.tool
def export_counter_proposal_package(
    deal_id: str = "BA-2026-AV-8921",
) -> dict:
    """
    Generate the complete Boeing Counter-Proposal package:
    1. 12-clause .docx with native Word <w:del>/<w:ins> Track Changes & <w:comment> SME rationales
    2. 4-tab SharePoint Deviation Matrix .xlsx
    3. Structured Outlook email draft body & M365 SharePoint/OneDrive/Teams dispatch manifest.
    """
    repo = get_repository()
    state = repo.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)
    validated_state = DealWorkbenchState.model_validate(state)

    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    docx_path = generate_counter_proposal_docx(
        validated_state,
        EXPORTS_DIR / f"{deal_id}_Boeing_Counter_Proposal.docx",
    )
    xlsx_path = generate_deviation_matrix_xlsx(
        validated_state,
        EXPORTS_DIR / f"{deal_id}_SharePoint_Deviation_Matrix.xlsx",
    )

    manifest = build_export_package_manifest(validated_state, Path(docx_path), Path(xlsx_path))
    notify_sse_subscribers(
        event_type="PACKAGE_EXPORTED",
        deal_id=deal_id,
        summary=f"Exported {Path(docx_path).name} and {Path(xlsx_path).name}",
        source_surface="GEMINI_AGENT_MCP",
    )
    return manifest


@mcp.tool
def reset_deal_workbench(
    deal_id: str = "BA-2026-AV-8921",
) -> dict:
    """
    Reset boeing_clm.deal_clause_deviations for BA-2026-AV-8921 to the canonical initial
    workbench state (GP1-12 Approved Hold Firm, GP1-19 Approved Compromise Tier-1,
    SP5-03 Approved Hold Firm, and SP3-04 in CONFLICT with GP1-03).
    """
    repo = get_repository()
    state = repo.reset_deal_workbench(deal_id=deal_id, source_surface="GEMINI_AGENT_MCP")
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="DEAL_RESET",
        deal_id=deal_id,
        summary=f"Deal {deal_id} reset to canonical initial workbench state",
        source_surface="GEMINI_AGENT_MCP",
    )
    return validated_state.model_dump()
