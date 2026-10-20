"""
tests/test_end_to_end_adversarial.py — Adversarial & End-to-End Verification Suite (challenger_m1).

Executes strictly against live BigQuery (`vertex-ai-demos-468803.boeing_clm`) with zero mocks:
1. All FastAPI REST & UI routes (`GET /health`, `GET /`, `GET /api/deals/{deal_id}`,
   `POST /api/deals/{deal_id}/ingest`, `GET /api/deals/{deal_id}/clauses/{clause_id}/precedents`,
   `POST /api/deals/{deal_id}/clauses/{clause_id}/position`,
   `POST /api/deals/{deal_id}/conflicts/{rule_id}/harmonize`,
   `GET /api/deals/{deal_id}/export/docx`, `GET /api/deals/{deal_id}/export/xlsx`,
   `GET /api/deals/{deal_id}/export/package`, `POST /api/deals/{deal_id}/reset`) via `TestClient`.
2. All 6 FastMCP tools (`ingest_vendor_redline`, `analyze_clause_precedents`,
   `record_sme_position`, `harmonize_clause_conflict`, `export_counter_proposal_package`,
   `reset_deal_workbench`).
3. Adversarial governance & contract checks:
   - `ConfigDict(extra="forbid")` rejects unknown/extra fields in `SMEReviewSubmission`
     both at the Pydantic model layer (`ValidationError`) and HTTP layer (`422 Unprocessable Entity`).
   - Selecting `accept_vendor` on `GP1-12` triggers `LOCKOUT-GP1-12-FAA` (`REGULATORY_LOCKOUT`)
     and sets `sme_status="CONFLICT"`.
   - Selecting `accept_vendor` on `SP5-03` triggers `LOCKOUT-SP5-03-DFARS` (`REGULATORY_LOCKOUT`)
     and sets `sme_status="CONFLICT"`.
   - Selecting `accept_vendor` on `SP3-04` triggers `CONFLICT-SP3-04-GP1-03` (`CROSS_CLAUSE_CONFLICT`),
     and `harmonize_clause_conflict` resolves it cleanly to `READY_FOR_DISPATCH`.
   - Always finishes by calling `reset_deal_workbench("BA-2026-AV-8921")` so live BigQuery
     is left in its canonical initial state.
"""
from __future__ import annotations

import asyncio
import io
from pathlib import Path
import zipfile

from fastapi.testclient import TestClient
from lxml import etree
from openpyxl import load_workbook
from pydantic import ValidationError
import pytest

from boeing_clm.config import DEFAULT_DEAL_ID, GOLDEN_VENDOR_REDLINE_DOCX
from boeing_clm.models import (
    DealWorkbenchState,
    PrecedentSearchResult,
    SMEReviewSubmission,
)
from boeing_clm.server.api_server import app
from boeing_clm.server.mcp_server import (
    analyze_clause_precedents,
    export_counter_proposal_package,
    harmonize_clause_conflict,
    ingest_vendor_redline,
    mcp,
    record_sme_position,
    reset_deal_workbench,
)

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


@pytest.fixture(scope="module")
def client() -> TestClient:
    """Create a FastAPI TestClient and ensure canonical workbench state before and after the module."""
    reset_deal_workbench(DEFAULT_DEAL_ID)
    with TestClient(app) as test_client:
        yield test_client
    reset_deal_workbench(DEFAULT_DEAL_ID)


def test_fastmcp_registered_tool_inventory() -> None:
    """Verify all 6 frozen FastMCP tools are registered on the `Boeing-CLM-Engine` MCP server."""
    tools = asyncio.run(mcp.list_tools())
    tool_names = [t.name for t in tools]
    assert tool_names == [
        "ingest_vendor_redline",
        "analyze_clause_precedents",
        "record_sme_position",
        "harmonize_clause_conflict",
        "export_counter_proposal_package",
        "reset_deal_workbench",
    ]


def test_fastapi_health_and_experience_layer_ui_routes(client: TestClient) -> None:
    """Verify `GET /health` and `GET /` serve live metadata and the 3-stage Experience Layer HTML."""
    health_resp = client.get("/health")
    assert health_resp.status_code == 200
    health_data = health_resp.json()
    assert health_data["status"] == "ok"
    assert health_data["service"] == "boeing-clm-engine"
    assert health_data["bigquery_dataset"] == "vertex-ai-demos-468803.boeing_clm"
    assert health_data["embedding_model"] == "vertex-ai-demos-468803.boeing_clm.text_embedding_005"

    ui_resp = client.get("/")
    assert ui_resp.status_code == 200
    assert "text/html" in ui_resp.headers["content-type"]
    html = ui_resp.text
    assert "BA-2026-AV-8921" in html
    assert "Apex AeroSystems" in html
    assert "/api/deals/" in html


def test_adversarial_extra_fields_rejected_by_strict_contract_model(client: TestClient) -> None:
    """
    Adversarial check: Unknown/extra fields in `SMEReviewSubmission` and `HarmonizeRequestBody`
    MUST be rejected with `ValidationError` and HTTP 422 due to `ConfigDict(extra='forbid')`.
    """
    with pytest.raises(ValidationError) as exc_info:
        SMEReviewSubmission(
            deal_id=DEFAULT_DEAL_ID,
            clause_id="GP1-19",
            sme_team="LEGAL",
            selected_option_key="compromise_tier_1",
            selected_counter_text="Valid text",
            sme_reviewer="Elena Rostova, J.D.",
            sme_rationale="Valid rationale",
            rogue_injected_field="should_fail",  # type: ignore[call-arg]
        )
    assert "extra_forbidden" in str(exc_info.value)

    # Verify FastAPI route also rejects extra fields with HTTP 422
    bad_payload = {
        "deal_id": DEFAULT_DEAL_ID,
        "clause_id": "GP1-19",
        "sme_team": "LEGAL",
        "selected_option_key": "compromise_tier_1",
        "selected_counter_text": "Valid text",
        "sme_reviewer": "Elena Rostova, J.D.",
        "sme_rationale": "Valid rationale",
        "unexpected_extra_property": "malicious_payload",
    }
    resp = client.post(
        f"/api/deals/{DEFAULT_DEAL_ID}/clauses/GP1-19/position",
        json=bad_payload,
    )
    assert resp.status_code == 422
    assert "extra_forbidden" in resp.text

    # Verify harmonize endpoint also forbids extra fields on HarmonizeRequestBody
    bad_harmonize_resp = client.post(
        f"/api/deals/{DEFAULT_DEAL_ID}/conflicts/CONFLICT-SP3-04-GP1-03/harmonize",
        json={"actor": "Lead Contract Owner", "rogue_field": 123},
    )
    assert bad_harmonize_resp.status_code == 422
    assert "extra_forbidden" in bad_harmonize_resp.text


def test_fastapi_routes_end_to_end_lifecycle(client: TestClient) -> None:
    """
    End-to-end verification of all FastAPI REST routes against live BigQuery:
    - POST /api/deals/BA-2026-AV-8921/reset
    - GET  /api/deals/BA-2026-AV-8921
    - POST /api/deals/BA-2026-AV-8921/ingest (both default and multipart upload)
    - GET  /api/deals/BA-2026-AV-8921/clauses/GP1-19/precedents
    - POST /api/deals/BA-2026-AV-8921/clauses/GP1-19/position
    - POST /api/deals/BA-2026-AV-8921/conflicts/CONFLICT-SP3-04-GP1-03/harmonize
    - GET  /api/deals/BA-2026-AV-8921/export/docx
    - GET  /api/deals/BA-2026-AV-8921/export/xlsx
    - GET  /api/deals/BA-2026-AV-8921/export/package
    """
    # 1. Reset deal state via REST
    reset_resp = client.post(f"/api/deals/{DEFAULT_DEAL_ID}/reset")
    assert reset_resp.status_code == 200
    initial_state = DealWorkbenchState.model_validate(reset_resp.json())
    assert initial_state.deal_id == DEFAULT_DEAL_ID
    assert initial_state.status == "CONFLICT_DETECTED"
    assert len(initial_state.active_conflicts) == 1
    assert initial_state.active_conflicts[0].rule_id == "CONFLICT-SP3-04-GP1-03"

    # 2. GET /api/deals/BA-2026-AV-8921
    get_resp = client.get(f"/api/deals/{DEFAULT_DEAL_ID}")
    assert get_resp.status_code == 200
    fetched_state = DealWorkbenchState.model_validate(get_resp.json())
    assert fetched_state.total_clauses_parsed == 12
    assert fetched_state.untouched_clauses_count == 8
    assert fetched_state.redlined_clauses_count == 4

    # 3. POST /api/deals/BA-2026-AV-8921/ingest (with uploaded .docx file)
    docx_bytes = GOLDEN_VENDOR_REDLINE_DOCX.read_bytes()
    ingest_resp = client.post(
        f"/api/deals/{DEFAULT_DEAL_ID}/ingest",
        files={
            "file": (
                "Vendor_Redlined_GP1.docx",
                io.BytesIO(docx_bytes),
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        },
    )
    assert ingest_resp.status_code == 200
    ingested_state = DealWorkbenchState.model_validate(ingest_resp.json())
    assert ingested_state.total_clauses_parsed == 12
    assert ingested_state.untouched_clauses_count == 8
    assert ingested_state.redlined_clauses_count == 4
    assert any(e.action == "INGESTED_REDLINE" for e in ingested_state.recent_events)

    # 4. GET /api/deals/BA-2026-AV-8921/clauses/GP1-19/precedents
    prec_resp = client.get(f"/api/deals/{DEFAULT_DEAL_ID}/clauses/GP1-19/precedents")
    assert prec_resp.status_code == 200
    prec = PrecedentSearchResult.model_validate(prec_resp.json())
    assert prec.clause_id == "GP1-19"
    assert prec.regulatory_lockout is False
    assert prec.distribution.total_matches == 16
    assert prec.distribution.compromise_tier_1_count == 11
    assert len(prec.precedents) == 5

    # 5. POST /api/deals/BA-2026-AV-8921/clauses/GP1-19/position
    tier1_opt = next(o for o in prec.playbook_options if o.option_key == "compromise_tier_1")
    pos_resp = client.post(
        f"/api/deals/{DEFAULT_DEAL_ID}/clauses/GP1-19/position",
        json={
            "deal_id": DEFAULT_DEAL_ID,
            "clause_id": "GP1-19",
            "sme_team": "LEGAL",
            "selected_option_key": "compromise_tier_1",
            "selected_counter_text": tier1_opt.counter_text,
            "sme_reviewer": "Elena Rostova, J.D. (Senior Counsel, Commercial & IP)",
            "sme_rationale": "Verified 200% PO super-cap ($90M) with uncapped airworthiness recall & IP indemnity.",
            "source_surface": "EXPERIENCE_LAYER_UI",
        },
    )
    assert pos_resp.status_code == 200
    pos_state = DealWorkbenchState.model_validate(pos_resp.json())
    gp19_clause = next(c for c in pos_state.clauses if c.clause_id == "GP1-19")
    assert gp19_clause.sme_status == "APPROVED"
    assert gp19_clause.selected_option_key == "compromise_tier_1"

    # 6. POST /api/deals/BA-2026-AV-8921/conflicts/CONFLICT-SP3-04-GP1-03/harmonize
    harm_resp = client.post(
        f"/api/deals/{DEFAULT_DEAL_ID}/conflicts/CONFLICT-SP3-04-GP1-03/harmonize",
        json={"actor": "Lead Contract Owner (M. Vance)"},
    )
    assert harm_resp.status_code == 200
    harm_state = DealWorkbenchState.model_validate(harm_resp.json())
    assert harm_state.status == "READY_FOR_DISPATCH"
    assert len(harm_state.active_conflicts) == 0
    sp304_clause = next(c for c in harm_state.clauses if c.clause_id == "SP3-04")
    assert sp304_clause.sme_status == "APPROVED"
    assert sp304_clause.selected_option_key == "custom_harmonized"

    # 7. GET /api/deals/BA-2026-AV-8921/export/docx
    docx_resp = client.get(f"/api/deals/{DEFAULT_DEAL_ID}/export/docx")
    assert docx_resp.status_code == 200
    assert (
        docx_resp.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    with zipfile.ZipFile(io.BytesIO(docx_resp.content), "r") as zf:
        assert "word/document.xml" in zf.namelist()
        assert "word/comments.xml" in zf.namelist()
        doc_xml = etree.fromstring(zf.read("word/document.xml"))
        ins_nodes = doc_xml.findall(f".//{{{W_NS}}}ins")
        del_nodes = doc_xml.findall(f".//{{{W_NS}}}del")
        assert len(ins_nodes) == 4
        assert len(del_nodes) == 4

    # 8. GET /api/deals/BA-2026-AV-8921/export/xlsx
    xlsx_resp = client.get(f"/api/deals/{DEFAULT_DEAL_ID}/export/xlsx")
    assert xlsx_resp.status_code == 200
    assert (
        xlsx_resp.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    wb = load_workbook(io.BytesIO(xlsx_resp.content))
    assert wb.sheetnames == [
        "Executive Summary",
        "Clause Sign-Off Matrix",
        "BigQuery Precedents",
        "Immutable Audit Trail",
    ]

    # 9. GET /api/deals/BA-2026-AV-8921/export/package
    pkg_resp = client.get(f"/api/deals/{DEFAULT_DEAL_ID}/export/package")
    assert pkg_resp.status_code == 200
    pkg = pkg_resp.json()
    assert pkg["deal_id"] == DEFAULT_DEAL_ID
    assert pkg["ready_for_dispatch"] is True
    assert pkg["active_conflicts_count"] == 0
    assert pkg["docx_size_bytes"] > 0
    assert pkg["xlsx_size_bytes"] > 0
    assert pkg["outlook_draft"]["connector"] == "ms-outlook"
    assert len(pkg["m365_connector_actions"]) == 4


def test_fastmcp_tools_and_adversarial_lockout_and_conflict_flows() -> None:
    """
    Verify all 6 FastMCP tools and adversarial conflict/lockout triggers:
    - `reset_deal_workbench`
    - `ingest_vendor_redline`
    - `analyze_clause_precedents`
    - `record_sme_position` triggering `LOCKOUT-GP1-12-FAA` (`REGULATORY_LOCKOUT`) on `GP1-12`
    - `record_sme_position` triggering `LOCKOUT-SP5-03-DFARS` (`REGULATORY_LOCKOUT`) on `SP5-03`
    - `record_sme_position` triggering `CONFLICT-SP3-04-GP1-03` (`CROSS_CLAUSE_CONFLICT`) on `SP3-04`
    - `harmonize_clause_conflict` resolving all conflicts cleanly
    - `export_counter_proposal_package` generating valid artifacts
    - Final `reset_deal_workbench("BA-2026-AV-8921")` restoring canonical initial state
    """
    # 1. Reset via FastMCP tool 6
    reset_dict = reset_deal_workbench(DEFAULT_DEAL_ID)
    state_0 = DealWorkbenchState.model_validate(reset_dict)
    assert state_0.deal_id == DEFAULT_DEAL_ID
    assert state_0.status == "CONFLICT_DETECTED"

    # 2. Ingest via FastMCP tool 1
    ingest_dict = ingest_vendor_redline(
        deal_id=DEFAULT_DEAL_ID,
        vendor_docx_path="specs/04_golden_fixtures/Vendor_Redlined_GP1.docx",
        baseline_docx_path="specs/04_golden_fixtures/Boeing_GP1_Standard.docx",
    )
    state_1 = DealWorkbenchState.model_validate(ingest_dict)
    assert state_1.total_clauses_parsed == 12
    assert state_1.untouched_clauses_count == 8
    assert state_1.redlined_clauses_count == 4

    # 3. Analyze precedents via FastMCP tool 2
    prec_gp12_dict = analyze_clause_precedents(clause_id="GP1-12", top_k=5)
    prec_gp12 = PrecedentSearchResult.model_validate(prec_gp12_dict)
    assert prec_gp12.clause_id == "GP1-12"
    assert prec_gp12.regulatory_lockout is True
    assert prec_gp12.distribution.held_firm_count == 14

    # 4. Adversarial Check A: Selecting `accept_vendor` on `GP1-12` MUST trigger `LOCKOUT-GP1-12-FAA`
    gp12_vendor_text = next(c.vendor_redline_text for c in state_1.clauses if c.clause_id == "GP1-12")
    lockout_gp12_dict = record_sme_position(
        deal_id=DEFAULT_DEAL_ID,
        clause_id="GP1-12",
        sme_team="ENGINEERING",
        selected_option_key="accept_vendor",
        selected_counter_text=gp12_vendor_text,
        sme_reviewer="Adversarial Tester (Engineering)",
        sme_rationale="Attempting to accept 12-month warranty and 30-day scheduled inspection notice.",
    )
    state_lockout_gp12 = DealWorkbenchState.model_validate(lockout_gp12_dict)
    assert state_lockout_gp12.status == "CONFLICT_DETECTED"
    gp12_item = next(c for c in state_lockout_gp12.clauses if c.clause_id == "GP1-12")
    assert gp12_item.sme_status == "CONFLICT"
    faa_conflict = next(
        (cf for cf in state_lockout_gp12.active_conflicts if cf.rule_id == "LOCKOUT-GP1-12-FAA"),
        None,
    )
    assert faa_conflict is not None
    assert faa_conflict.rule_type == "REGULATORY_LOCKOUT"
    assert faa_conflict.severity == "REGULATORY_BLOCK"

    # 5. Adversarial Check B: Selecting `accept_vendor` on `SP5-03` MUST trigger `LOCKOUT-SP5-03-DFARS`
    sp503_vendor_text = next(c.vendor_redline_text for c in state_1.clauses if c.clause_id == "SP5-03")
    lockout_sp503_dict = record_sme_position(
        deal_id=DEFAULT_DEAL_ID,
        clause_id="SP5-03",
        sme_team="CYBER",
        selected_option_key="accept_vendor",
        selected_counter_text=sp503_vendor_text,
        sme_reviewer="Adversarial Tester (Cyber)",
        sme_rationale="Attempting to accept 10 business day cyber reporting window.",
    )
    state_lockout_sp503 = DealWorkbenchState.model_validate(lockout_sp503_dict)
    sp503_item = next(c for c in state_lockout_sp503.clauses if c.clause_id == "SP5-03")
    assert sp503_item.sme_status == "CONFLICT"
    dfars_conflict = next(
        (cf for cf in state_lockout_sp503.active_conflicts if cf.rule_id == "LOCKOUT-SP5-03-DFARS"),
        None,
    )
    assert dfars_conflict is not None
    assert dfars_conflict.rule_type == "REGULATORY_LOCKOUT"
    assert dfars_conflict.severity == "REGULATORY_BLOCK"

    # Resolve both regulatory lockouts via harmonize_clause_conflict
    harmonize_clause_conflict(deal_id=DEFAULT_DEAL_ID, rule_id="LOCKOUT-GP1-12-FAA")
    harmonize_clause_conflict(deal_id=DEFAULT_DEAL_ID, rule_id="LOCKOUT-SP5-03-DFARS")

    # 6. Adversarial Check C: Selecting `accept_vendor` on `SP3-04` triggers `CONFLICT-SP3-04-GP1-03`
    sp304_vendor_text = next(c.vendor_redline_text for c in state_1.clauses if c.clause_id == "SP3-04")
    conflict_sp304_dict = record_sme_position(
        deal_id=DEFAULT_DEAL_ID,
        clause_id="SP3-04",
        sme_team="TAX",
        selected_option_key="accept_vendor",
        selected_counter_text=sp304_vendor_text,
        sme_reviewer="Marcus Chen, CPA (Director, Global Tax & Trade)",
        sme_rationale="Accepting uncapped >5% tariff pass-through to expedite delivery.",
    )
    state_conflict_sp304 = DealWorkbenchState.model_validate(conflict_sp304_dict)
    assert state_conflict_sp304.status == "CONFLICT_DETECTED"
    sp304_item = next(c for c in state_conflict_sp304.clauses if c.clause_id == "SP3-04")
    assert sp304_item.sme_status == "CONFLICT"
    cross_conflict = next(
        (cf for cf in state_conflict_sp304.active_conflicts if cf.rule_id == "CONFLICT-SP3-04-GP1-03"),
        None,
    )
    assert cross_conflict is not None
    assert cross_conflict.rule_type == "CROSS_CLAUSE_CONFLICT"
    assert cross_conflict.source_clause_id == "SP3-04"
    assert cross_conflict.target_clause_id == "GP1-03"

    # Harmonize `CONFLICT-SP3-04-GP1-03` via FastMCP tool 4
    harmonized_dict = harmonize_clause_conflict(
        deal_id=DEFAULT_DEAL_ID,
        rule_id="CONFLICT-SP3-04-GP1-03",
        actor="Lead Contract Owner (M. Vance)",
    )
    state_harmonized = DealWorkbenchState.model_validate(harmonized_dict)
    assert state_harmonized.status == "READY_FOR_DISPATCH"
    assert len(state_harmonized.active_conflicts) == 0
    sp304_resolved = next(c for c in state_harmonized.clauses if c.clause_id == "SP3-04")
    assert sp304_resolved.sme_status == "APPROVED"
    assert sp304_resolved.selected_option_key == "custom_harmonized"

    # 7. Export Counter-Proposal Package via FastMCP tool 5
    export_manifest = export_counter_proposal_package(deal_id=DEFAULT_DEAL_ID)
    assert export_manifest["deal_id"] == DEFAULT_DEAL_ID
    assert export_manifest["ready_for_dispatch"] is True
    assert Path(export_manifest["docx_local_path"]).exists()
    assert Path(export_manifest["xlsx_local_path"]).exists()

    # 8. Always finish by calling `reset_deal_workbench("BA-2026-AV-8921")`
    final_reset_dict = reset_deal_workbench(DEFAULT_DEAL_ID)
    final_state = DealWorkbenchState.model_validate(final_reset_dict)
    assert final_state.deal_id == DEFAULT_DEAL_ID
    assert final_state.status == "CONFLICT_DETECTED"
    assert len(final_state.active_conflicts) == 1
    assert final_state.active_conflicts[0].rule_id == "CONFLICT-SP3-04-GP1-03"
