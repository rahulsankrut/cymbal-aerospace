"""
src/boeing_clm/server/api_server.py — Unified FastAPI + FastMCP Server for Boeing CLM.
Serves:
- GET /                         -> Live 3-Stage Experience Layer UI (src/boeing_clm/ui/index.html)
- GET /health                   -> Cloud Run health probe
- /api/*                        -> All 10 REST + SSE routes from specs/03_mcp_and_rest_contract.md
- /mcp                          -> Mounted FastMCP streamable-HTTP server for Gemini Agent (Spark)
"""
from __future__ import annotations

import asyncio
import json
import tempfile
from pathlib import Path
from typing import Any, Optional

from fastapi import Body, FastAPI, File, HTTPException, Query, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from pydantic import BaseModel, ConfigDict

from boeing_clm.config import (
    BQ_DATASET,
    EXPORTS_DIR,
    GCP_PROJECT_ID,
    GOLDEN_VENDOR_REDLINE_DOCX,
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
from boeing_clm.server.mcp_server import (
    build_export_package_manifest,
    get_repository,
    mcp,
    notify_sse_subscribers,
    register_sse_subscriber,
    unregister_sse_subscriber,
)

UI_HTML_PATH = Path(__file__).resolve().parents[1] / "ui" / "index.html"

mcp_asgi_app = mcp.http_app(path="/", stateless_http=True)

app = FastAPI(
    title="Boeing CLM Engine — Gemini Agent (Spark) + BigQuery Vector Search",
    description=(
        "Deterministic OOXML .docx Track-Changes Parser, Live BigQuery VECTOR_SEARCH "
        "(text-embedding-005), Declarative Cross-Clause Conflict Detector, and Unified FastMCP + FastAPI Server."
    ),
    version="1.0.0",
    lifespan=mcp_asgi_app.lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HarmonizeRequestBody(BaseModel):
    model_config = ConfigDict(extra="forbid")
    actor: str = "Lead Contract Owner (M. Vance)"


@app.get("/", response_class=HTMLResponse)
async def serve_experience_layer_ui() -> HTMLResponse:
    """Serve the live 3-Stage Boeing CLM Experience Layer UI."""
    if not UI_HTML_PATH.exists():
        raise HTTPException(status_code=404, detail=f"UI file not found at {UI_HTML_PATH}")
    return HTMLResponse(content=UI_HTML_PATH.read_text(encoding="utf-8"))


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Cloud Run readiness and liveness probe."""
    return {
        "status": "ok",
        "service": "boeing-clm-engine",
        "bigquery_dataset": f"{GCP_PROJECT_ID}.{BQ_DATASET}",
        "embedding_model": f"{GCP_PROJECT_ID}.{BQ_DATASET}.text_embedding_005",
    }


@app.get("/api/deals/{deal_id}", response_model=DealWorkbenchState)
def get_deal_state(
    deal_id: str,
    include_precedents: bool = Query(default=True),
) -> DealWorkbenchState:
    """Fetch complete live DealWorkbenchState from BigQuery (including 12 clauses, conflicts, and events)."""
    repo = get_repository()
    state = repo.get_deal_workbench_state(deal_id=deal_id, include_precedents=include_precedents)
    return DealWorkbenchState.model_validate(state)


@app.post("/api/deals/{deal_id}/ingest", response_model=DealWorkbenchState)
async def ingest_deal_docx(
    deal_id: str,
    file: Optional[UploadFile] = File(default=None),
) -> DealWorkbenchState:
    """
    Parse an uploaded vendor-redlined .docx (or default to specs/04_golden_fixtures/Vendor_Redlined_GP1.docx),
    persist all 12 clauses to BigQuery, broadcast SSE event, and return DealWorkbenchState.
    """
    tmp_path: Optional[Path] = None
    try:
        if file is not None and file.filename:
            content = await file.read()
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
                tmp.write(content)
                tmp_path = Path(tmp.name)
            target_docx = tmp_path
        else:
            target_docx = GOLDEN_VENDOR_REDLINE_DOCX

        extracted = await asyncio.to_thread(parse_redlined_docx, target_docx)
        validated_diffs = [ExtractedClauseDiff.model_validate(d) for d in extracted]

        repo = get_repository()
        state = await asyncio.to_thread(
            repo.save_extracted_clauses,
            deal_id,
            validated_diffs,
            "EXPERIENCE_LAYER_UI",
        )
        validated_state = DealWorkbenchState.model_validate(state)

        notify_sse_subscribers(
            event_type="INGESTED_REDLINE",
            deal_id=deal_id,
            summary=(
                f"Parsed {validated_state.total_clauses_parsed} clauses from .docx "
                f"({validated_state.untouched_clauses_count} untouched, {validated_state.redlined_clauses_count} redlined)"
            ),
            source_surface="EXPERIENCE_LAYER_UI",
        )
        return validated_state
    finally:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink(missing_ok=True)


@app.get("/api/deals/{deal_id}/clauses/{clause_id}/precedents", response_model=PrecedentSearchResult)
def get_clause_precedents(
    deal_id: str,
    clause_id: str,
    vendor_redline_text: str = Query(default=""),
    supplier_tier: str = Query(default="Tier-1 Avionics"),
    top_k: int = Query(default=5, ge=1, le=20),
) -> PrecedentSearchResult:
    """Execute live BigQuery VECTOR_SEARCH + COUNTIF outcome aggregation for a specific clause."""
    _ = deal_id
    repo = get_repository()
    result = repo.search_clause_precedents(
        clause_id=clause_id,
        vendor_redline_text=vendor_redline_text,
        supplier_tier=supplier_tier,
        top_k=top_k,
    )
    return PrecedentSearchResult.model_validate(result)


@app.post("/api/deals/{deal_id}/clauses/{clause_id}/position", response_model=DealWorkbenchState)
def submit_clause_sme_position(
    deal_id: str,
    clause_id: str,
    submission: SMEReviewSubmission,
) -> DealWorkbenchState:
    """
    Validate and commit an SME position to BigQuery deal_clause_deviations & sme_review_events,
    re-evaluate cross-clause conflict rules, notify SSE subscribers, and return DealWorkbenchState.
    """
    normalized = SMEReviewSubmission(
        deal_id=deal_id,
        clause_id=clause_id,
        sme_team=submission.sme_team,
        selected_option_key=submission.selected_option_key,
        selected_counter_text=submission.selected_counter_text,
        sme_reviewer=submission.sme_reviewer,
        sme_rationale=submission.sme_rationale,
        source_surface=submission.source_surface,
    )
    repo = get_repository()
    state = repo.record_sme_submission(normalized)
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="SME_POSITION_RECORDED",
        deal_id=deal_id,
        summary=f"{normalized.sme_team} ({normalized.sme_reviewer}) committed '{normalized.selected_option_key}' on {clause_id}",
        source_surface=normalized.source_surface,
    )
    return validated_state


@app.post("/api/deals/{deal_id}/conflicts/{rule_id}/harmonize", response_model=DealWorkbenchState)
def harmonize_deal_conflict(
    deal_id: str,
    rule_id: str,
    body: Optional[HarmonizeRequestBody] = Body(default=None),
) -> DealWorkbenchState:
    """
    Apply the pre-approved harmonized resolution text from boeing_clm.clause_conflict_rules
    to resolve an inter-team conflict (e.g. SP3-04 vs GP1-03), log to BigQuery, and broadcast SSE.
    """
    actor = body.actor if body is not None else "Lead Contract Owner (M. Vance)"
    repo = get_repository()
    state = repo.harmonize_conflict(
        deal_id=deal_id,
        rule_id=rule_id,
        actor=actor,
        source_surface="EXPERIENCE_LAYER_UI",
    )
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="CONFLICT_HARMONIZED",
        deal_id=deal_id,
        summary=f"Conflict {rule_id} harmonized in BigQuery by {actor}",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    return validated_state


@app.post("/api/deals/{deal_id}/reset", response_model=DealWorkbenchState)
def reset_deal_state(deal_id: str) -> DealWorkbenchState:
    """Reset deal_clause_deviations to canonical initial state (3 approved, SP3-04 in conflict)."""
    repo = get_repository()
    state = repo.reset_deal_workbench(deal_id=deal_id, source_surface="EXPERIENCE_LAYER_UI")
    validated_state = DealWorkbenchState.model_validate(state)

    notify_sse_subscribers(
        event_type="DEAL_RESET",
        deal_id=deal_id,
        summary=f"Deal {deal_id} reset to canonical initial workbench state",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    return validated_state


@app.get("/api/deals/{deal_id}/export/docx")
def download_counter_proposal_docx(deal_id: str) -> FileResponse:
    """Generate and download the 12-clause Counter-Proposal .docx with native Word Track Changes & SME comments."""
    repo = get_repository()
    state = DealWorkbenchState.model_validate(
        repo.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)
    )
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = EXPORTS_DIR / f"{deal_id}_Boeing_Counter_Proposal.docx"
    generated_path = Path(generate_counter_proposal_docx(state, output_path))

    notify_sse_subscribers(
        event_type="DOCX_EXPORTED",
        deal_id=deal_id,
        summary=f"Generated native Track-Changes Counter-Proposal {generated_path.name}",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    return FileResponse(
        path=str(generated_path),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=generated_path.name,
    )


@app.get("/api/deals/{deal_id}/export/xlsx")
def download_deviation_matrix_xlsx(deal_id: str) -> FileResponse:
    """Generate and download the 4-tab SharePoint Deviation Matrix .xlsx."""
    repo = get_repository()
    state = DealWorkbenchState.model_validate(
        repo.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)
    )
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = EXPORTS_DIR / f"{deal_id}_SharePoint_Deviation_Matrix.xlsx"
    generated_path = Path(generate_deviation_matrix_xlsx(state, output_path))

    notify_sse_subscribers(
        event_type="XLSX_EXPORTED",
        deal_id=deal_id,
        summary=f"Generated 4-tab SharePoint Deviation Matrix {generated_path.name}",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    return FileResponse(
        path=str(generated_path),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=generated_path.name,
    )


@app.get("/api/deals/{deal_id}/export/package")
def get_export_package_manifest(deal_id: str) -> dict[str, Any]:
    """Generate both .docx and .xlsx artifacts and return JSON manifest with download URLs + M365 Outlook draft."""
    repo = get_repository()
    state = DealWorkbenchState.model_validate(
        repo.get_deal_workbench_state(deal_id=deal_id, include_precedents=True)
    )
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    docx_path = Path(
        generate_counter_proposal_docx(state, EXPORTS_DIR / f"{deal_id}_Boeing_Counter_Proposal.docx")
    )
    xlsx_path = Path(
        generate_deviation_matrix_xlsx(state, EXPORTS_DIR / f"{deal_id}_SharePoint_Deviation_Matrix.xlsx")
    )
    return build_export_package_manifest(state, docx_path, xlsx_path)


@app.get("/api/events")
async def stream_sse_events(request: Request) -> StreamingResponse:
    """Server-Sent Events stream notifying browser UI whenever Gemini Agent MCP or REST endpoints mutate state."""
    loop = asyncio.get_running_loop()
    queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
    register_sse_subscriber(loop, queue)

    async def event_generator():
        try:
            yield f"data: {json.dumps({'event_type': 'CONNECTED', 'summary': 'Connected to Boeing CLM Live Event Stream'})}\n\n"
            while True:
                if await request.is_disconnected():
                    break
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=15.0)
                    yield f"data: {json.dumps(event)}\n\n"
                except asyncio.TimeoutError:
                    yield ": keepalive\n\n"
        finally:
            unregister_sse_subscriber(queue)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# Mount FastMCP streamable-HTTP server at /mcp so Cloud Run serves both UI/REST and MCP from one container
app.mount("/mcp", mcp_asgi_app)
