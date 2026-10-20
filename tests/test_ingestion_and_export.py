"""
Verification suite for Boeing CLM OOXML .docx ingestion, diff engine, and .docx/.xlsx exporters.
Validates 100% conformance against specs/04_golden_fixtures/* and specs/02_domain_models.py.
"""
from __future__ import annotations

import json
from pathlib import Path
import zipfile

from docx import Document
from lxml import etree
from openpyxl import load_workbook
import pytest

from boeing_clm.export import (
    generate_counter_proposal_docx,
    generate_deviation_matrix_xlsx,
)
from boeing_clm.ingestion import (
    compute_untracked_diff,
    parse_redlined_docx,
)
from boeing_clm.models import (
    AuditEventItem,
    ClauseWorkbenchItem,
    CrossClauseConflict,
    DealWorkbenchState,
    ExtractedClauseDiff,
    OutcomeDistribution,
    PlaybookOption,
    PrecedentMatchItem,
    PrecedentSearchResult,
)

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

REPO_ROOT = Path(__file__).resolve().parents[1]
GOLDEN_DIR = REPO_ROOT / "specs" / "04_golden_fixtures"
BASELINE_DOCX = GOLDEN_DIR / "Boeing_GP1_Standard.docx"
VENDOR_REDLINED_DOCX = GOLDEN_DIR / "Vendor_Redlined_GP1.docx"
EXPECTED_DIFFS_JSON = GOLDEN_DIR / "expected_extracted_diffs.json"


def _build_sample_workbench_state(
    extracted: list[ExtractedClauseDiff],
) -> DealWorkbenchState:
    """Construct a complete, realistic 12-clause DealWorkbenchState validated by Pydantic v2."""
    clauses: list[ClauseWorkbenchItem] = []

    sample_precedent = PrecedentSearchResult(
        clause_id="GP1-19",
        clause_ref="GP1 §19 & §24",
        clause_title="Limitation of Liability & IP Indemnity",
        sme_team="LEGAL",
        guardrail_summary="Never accept 1x PO cap on flight-critical avionics; Tier-1 compromise is 2x PO value ($90M) with uncapped airworthiness/IP indemnity.",
        regulatory_lockout=False,
        regulatory_citation="Corporate Legal Playbook Tier-1",
        distribution=OutcomeDistribution(
            total_matches=5,
            held_firm_count=1,
            held_firm_pct=20,
            compromise_tier_1_count=4,
            compromise_tier_1_pct=80,
            accepted_vendor_count=0,
            accepted_vendor_pct=0,
        ),
        precedents=[
            PrecedentMatchItem(
                exception_id="EXC-2025-787-019",
                clause_id="GP1-19",
                contract_id="BCA-787-AV-2025-114",
                supplier_name="Honeywell Aerospace",
                supplier_tier="Tier-1 Avionics",
                boeing_program="787-10 Flight Controls",
                vendor_requested_redline="100% PO liability cap ($40M) and combination IP carveout.",
                final_agreed_language="19.1 Direct damages capped at two hundred percent (200%) of total Purchase Order value ($90M), provided that airworthiness recall and 24.1 IP indemnity remain uncapped.",
                outcome_category="COMPROMISE_TIER_1",
                approval_authority="VP Legal & Associate General Counsel",
                negotiation_notes="Approved 2x PO cap while preserving uncapped airworthiness recall & system IP indemnity.",
                signed_date="2025-11-18",
                similarity_score=0.9642,
            )
        ],
        playbook_options=[
            PlaybookOption(
                option_key="hold_firm",
                label="Hold Firm (Boeing Baseline)",
                badge="20% Historical",
                badge_class="badge-navy",
                counter_text="19.1 Seller's liability for direct damages, line-stoppage, and airworthiness recall costs shall be uncapped. 24.1 Seller shall indemnify Boeing against all third-party intellectual property infringement claims including system-level avionics bus integration.",
            ),
            PlaybookOption(
                option_key="compromise_tier_1",
                label="Tier-1 Compromise (2x PO Cap / Uncapped Recall & IP)",
                badge="80% Precedent Match",
                badge_class="badge-green",
                counter_text="19.1 Seller's liability for general direct damages shall not exceed two hundred percent (200%) of total Purchase Order value ($90M), provided that airworthiness recall costs and 24.1 IP indemnity including system-level avionics bus integration remain uncapped.",
            ),
        ],
    )

    for item in extracted:
        if not item.has_redline:
            clauses.append(
                ClauseWorkbenchItem(
                    clause_id=item.clause_id,
                    proforma_doc=item.proforma_doc,
                    clause_ref=item.clause_ref,
                    clause_title=item.clause_title,
                    has_redline=False,
                    sme_team=item.sme_team,
                    sme_owner_label=item.sme_owner_label,
                    risk_level=item.risk_level,
                    regulatory_flag=item.regulatory_flag,
                    boeing_baseline_text=item.boeing_baseline_text,
                    vendor_redline_text=item.vendor_redline_text,
                    diff_html=item.diff_html,
                    vendor_comment="",
                    recommended_option_key="hold_firm",
                    recommended_counter_text=item.boeing_baseline_text,
                    selected_option_key="hold_firm",
                    selected_counter_text=item.boeing_baseline_text,
                    sme_status="UNTOUCHED",
                    sme_reviewer="Auto-Verified Baseline",
                    sme_rationale="Clause untouched by vendor; matches Boeing GP1/SP standard.",
                    precedent_analysis=None,
                )
            )
        elif item.clause_id == "GP1-19":
            counter_19 = (
                "19.1 Seller's liability for general direct damages shall not exceed two hundred percent (200%) "
                "of total Purchase Order value ($90M), provided that airworthiness recall costs and 24.1 IP "
                "indemnity including system-level avionics bus integration remain uncapped."
            )
            clauses.append(
                ClauseWorkbenchItem(
                    clause_id=item.clause_id,
                    proforma_doc=item.proforma_doc,
                    clause_ref=item.clause_ref,
                    clause_title=item.clause_title,
                    has_redline=True,
                    sme_team=item.sme_team,
                    sme_owner_label=item.sme_owner_label,
                    risk_level=item.risk_level,
                    regulatory_flag=item.regulatory_flag,
                    boeing_baseline_text=item.boeing_baseline_text,
                    vendor_redline_text=item.vendor_redline_text,
                    diff_html=item.diff_html,
                    vendor_comment=item.vendor_comments[0] if item.vendor_comments else "",
                    recommended_option_key="compromise_tier_1",
                    recommended_counter_text=counter_19,
                    selected_option_key="compromise_tier_1",
                    selected_counter_text=counter_19,
                    sme_status="APPROVED",
                    sme_reviewer="R. Vance (Corporate Legal)",
                    sme_rationale="Applied 80% Tier-1 Avionics precedent (2x PO $90M cap on general damages; uncapped recall & IP).",
                    precedent_analysis=sample_precedent,
                )
            )
        else:
            clauses.append(
                ClauseWorkbenchItem(
                    clause_id=item.clause_id,
                    proforma_doc=item.proforma_doc,
                    clause_ref=item.clause_ref,
                    clause_title=item.clause_title,
                    has_redline=True,
                    sme_team=item.sme_team,
                    sme_owner_label=item.sme_owner_label,
                    risk_level=item.risk_level,
                    regulatory_flag=item.regulatory_flag,
                    boeing_baseline_text=item.boeing_baseline_text,
                    vendor_redline_text=item.vendor_redline_text,
                    diff_html=item.diff_html,
                    vendor_comment=item.vendor_comments[0] if item.vendor_comments else "",
                    recommended_option_key="hold_firm",
                    recommended_counter_text=item.boeing_baseline_text,
                    selected_option_key="hold_firm",
                    selected_counter_text=item.boeing_baseline_text,
                    sme_status="APPROVED",
                    sme_reviewer=f"{item.sme_team.title()} Lead Reviewer",
                    sme_rationale=f"Mandatory regulatory and commercial hold-firm on {item.clause_ref} ({item.regulatory_flag}).",
                    precedent_analysis=None,
                )
            )

    return DealWorkbenchState(
        deal_id="BA-2026-AV-8921",
        vendor_name="Apex AeroSystems",
        supplier_tier="Tier-1 Avionics",
        boeing_program="Cymbal C900 / C700-MAX Flight Control Display Units",
        contract_value_usd=45_000_000.0,
        proforma_stack="GP1 + SP3 (International) + SP5 (Cyber/DFARS)",
        pricing_model="Firm-Fixed-Price (FFP)",
        sow_cap_clause_ref="GP1 §3.1",
        sharepoint_folder_url="https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-AV-8921",
        deviation_matrix_xlsx="BA-2026-AV-8921_Deviation_Matrix.xlsx",
        total_clauses_parsed=12,
        untouched_clauses_count=8,
        redlined_clauses_count=4,
        status="READY_FOR_DISPATCH",
        bigquery_dataset="vertex-ai-demos-468803.boeing_clm",
        clauses=clauses,
        active_conflicts=[
            CrossClauseConflict(
                rule_id="CONFLICT-SP3-04-GP1-03",
                rule_type="CROSS_CLAUSE_CONFLICT",
                source_clause_id="SP3-04",
                target_clause_id="GP1-03",
                source_sme_team="TAX",
                target_sme_team="PROCUREMENT",
                severity="CRITICAL_CONFLICT",
                conflict_title="SP3 §4.1 Tariff Pass-Through Violates GP1 §3.1 Firm-Fixed-Price SOW Cap",
                conflict_description="Granting 100% tariff pass-through above 5% in SP3 §4.1 directly contradicts the FFP SOW lock in GP1 §3.1.",
                harmonized_option_key="custom_harmonized",
                harmonized_resolution_text="4.1 All unit prices are DDP Cymbal Everett/Renton facility. Any verified Section 232/301 tariff increase exceeding 10% shall be shared 50/50 up to a strict maximum adjustment cap of 1.5% of unit price pursuant to a bilateral GP1 §3.1 Change Order.",
            )
        ],
        recent_events=[
            AuditEventItem(
                event_id="EVT-2026-001",
                deal_id="BA-2026-AV-8921",
                clause_id="ALL",
                sme_team="PROCUREMENT",
                actor="M. Vance (Procurement Lead)",
                action="INGESTED_REDLINE",
                selected_option_key="hold_firm",
                rationale="Parsed 12 clauses from Vendor_Redlined_GP1.docx (8 untouched, 4 redlined).",
                source_surface="GEMINI_AGENT_MCP",
                created_at="2026-10-16T18:00:00Z",
            ),
            AuditEventItem(
                event_id="EVT-2026-002",
                deal_id="BA-2026-AV-8921",
                clause_id="GP1-12",
                sme_team="ENGINEERING",
                actor="Dr. K. Chen (FAA DER)",
                action="SME_POSITION_RECORDED",
                selected_option_key="hold_firm",
                rationale="FAA 14 CFR Part 21 requires unannounced source inspection access and 36-month airworthiness warranty.",
                source_surface="EXPERIENCE_LAYER_UI",
                created_at="2026-10-16T18:05:00Z",
            ),
        ],
        updated_at="2026-10-16T18:10:00Z",
    )


def test_parse_vendor_redlined_docx_matches_golden_snapshot_100_percent() -> None:
    """Verify parse_redlined_docx on Vendor_Redlined_GP1.docx matches expected_extracted_diffs.json 100%."""
    parsed = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    assert len(parsed) == 12

    untouched = [d for d in parsed if not d.has_redline]
    redlined = [d for d in parsed if d.has_redline]
    assert len(untouched) == 8
    assert len(redlined) == 4
    assert [d.clause_id for d in redlined] == ["GP1-12", "GP1-19", "SP3-04", "SP5-03"]

    expected_raw = json.loads(EXPECTED_DIFFS_JSON.read_text(encoding="utf-8"))
    actual_raw = [d.model_dump() for d in parsed]
    assert actual_raw == expected_raw


def test_parse_boeing_baseline_docx_all_untouched() -> None:
    """Verify parse_redlined_docx on Boeing_GP1_Standard.docx produces 12 untouched clauses."""
    parsed = parse_redlined_docx(BASELINE_DOCX)
    assert len(parsed) == 12
    assert all(not d.has_redline for d in parsed)
    assert all(d.insertions == [] and d.deletions == [] and d.vendor_comments == [] for d in parsed)
    assert all(d.boeing_baseline_text == d.vendor_redline_text == d.diff_html for d in parsed)


def test_fallback_section_number_alignment_without_metadata_headers(tmp_path: Path) -> None:
    """Verify generic .docx files without Heading 2 metadata tags align cleanly by section numbers."""
    generic_docx = tmp_path / "generic_no_headers.docx"
    doc = Document()
    doc.add_heading("GENERIC SUPPLIER CONTRACT", level=1)
    doc.add_paragraph(
        "1.1 Buyer means Cymbal Aerospace Corporation or its wholly-owned subsidiary identified on the face of the Contract."
    )
    doc.add_paragraph(
        "12.2 Seller warrants all Goods against defects in material, workmanship, and avionics firmware for thirty-six (36) months."
    )
    doc.save(str(generic_docx))

    parsed = parse_redlined_docx(generic_docx)
    assert len(parsed) == 2
    assert parsed[0].clause_id == "GP1-01"
    assert parsed[0].sme_team == "PROCUREMENT"
    assert parsed[1].clause_id == "GP1-12"
    assert parsed[1].sme_team == "ENGINEERING"
    assert parsed[1].regulatory_flag == "FAA 14 CFR Part 21 Lockout"


def test_compute_untracked_diff_html() -> None:
    """Verify fallback word-level diff engine generates expected diff-del and diff-add spans."""
    ins, dels, html = compute_untracked_diff(
        "Warranty is 36 months from delivery.",
        "Warranty is 12 months fromdelivery.",
    )
    assert len(ins) >= 1
    assert len(dels) >= 1
    assert '<span class="diff-del">' in html
    assert '<span class="diff-add">' in html


def test_generate_counter_proposal_docx_track_changes_and_comments(tmp_path: Path) -> None:
    """
    Verify generate_counter_proposal_docx produces a complete 12-clause .docx with:
    - Executive Summary metadata table
    - Real <w:del> and <w:ins w:author='Cymbal CLM Counter-Proposal'> XML nodes on redlined clauses
    - word/comments.xml linked via <w:commentRangeStart>/<w:commentRangeEnd>/<w:commentReference>
    """
    extracted = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    state = _build_sample_workbench_state(extracted)

    out_docx = tmp_path / "Cymbal_Counter_Proposal.docx"
    res_path = generate_counter_proposal_docx(state, out_docx)
    assert res_path == out_docx
    assert out_docx.exists()

    with zipfile.ZipFile(out_docx, "r") as zf:
        assert "word/document.xml" in zf.namelist()
        assert "word/comments.xml" in zf.namelist()
        doc_xml = etree.fromstring(zf.read("word/document.xml"))
        comments_xml = etree.fromstring(zf.read("word/comments.xml"))

    # Verify executive summary table in document.xml
    all_text = "".join(t.text or "" for t in doc_xml.findall(f".//{{{W_NS}}}t"))
    assert "BA-2026-AV-8921" in all_text
    assert "Apex AeroSystems" in all_text
    assert "$45,000,000.00" in all_text
    assert "READY_FOR_DISPATCH" in all_text

    # Verify <w:ins> and <w:del> nodes exist for the 4 redlined clauses authored by Cymbal CLM Counter-Proposal
    ins_nodes = doc_xml.findall(f".//{{{W_NS}}}ins")
    del_nodes = doc_xml.findall(f".//{{{W_NS}}}del")
    assert len(ins_nodes) == 4
    assert len(del_nodes) == 4
    for ins_el in ins_nodes:
        assert ins_el.get(f"{{{W_NS}}}author") == "Cymbal CLM Counter-Proposal"

    # Verify comments.xml contains all 4 SME rationales
    comment_els = comments_xml.findall(f".//{{{W_NS}}}comment")
    assert len(comment_els) == 4
    comments_text = " ".join(
        "".join(t.text or "" for t in c_el.findall(f".//{{{W_NS}}}t"))
        for c_el in comment_els
    )
    assert "Applied 80% Tier-1 Avionics precedent" in comments_text
    assert "FAA 14 CFR Part 21 Lockout" in comments_text

    # Round-trip parse with parse_redlined_docx
    reparsed = parse_redlined_docx(out_docx)
    assert len(reparsed) == 12
    reparsed_redlined = [d for d in reparsed if d.has_redline]
    assert len(reparsed_redlined) == 4
    gp19 = next(d for d in reparsed_redlined if d.clause_id == "GP1-19")
    assert "two hundred percent (200%)" in gp19.vendor_redline_text
    assert "one hundred percent (100%)" in gp19.boeing_baseline_text
    assert len(gp19.vendor_comments) == 1
    assert "Applied 80% Tier-1 Avionics precedent" in gp19.vendor_comments[0]


def test_generate_deviation_matrix_xlsx_four_worksheets(tmp_path: Path) -> None:
    """
    Verify generate_deviation_matrix_xlsx builds a styled 4-worksheet workbook:
    1. Executive Summary
    2. Clause Sign-Off Matrix
    3. BigQuery Precedents
    4. Immutable Audit Trail
    """
    extracted = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    state = _build_sample_workbench_state(extracted)

    out_xlsx = tmp_path / "Deviation_Matrix.xlsx"
    res_path = generate_deviation_matrix_xlsx(state, out_xlsx)
    assert res_path == out_xlsx
    assert out_xlsx.exists()

    wb = load_workbook(str(out_xlsx))
    assert wb.sheetnames == [
        "Executive Summary",
        "Clause Sign-Off Matrix",
        "BigQuery Precedents",
        "Immutable Audit Trail",
    ]

    # Sheet 1: Executive Summary
    ws_exec = wb["Executive Summary"]
    exec_values = [
        str(cell)
        for row in ws_exec.iter_rows(values_only=True)
        for cell in row
        if cell is not None
    ]
    joined_exec = " | ".join(exec_values)
    assert "BA-2026-AV-8921" in joined_exec
    assert "Apex AeroSystems" in joined_exec
    assert "https://36zrbd.sharepoint.com/sites/CymbalAerospace" in joined_exec
    assert "CONFLICT-SP3-04-GP1-03" in joined_exec

    # Sheet 2: Clause Sign-Off Matrix (1 header row + 12 clause rows = 13 rows)
    ws_matrix = wb["Clause Sign-Off Matrix"]
    assert ws_matrix.max_row == 13
    clause_ids_in_sheet = [
        ws_matrix.cell(row=r, column=1).value for r in range(2, 14)
    ]
    assert clause_ids_in_sheet == [c.clause_id for c in state.clauses]

    # Sheet 3: BigQuery Precedents
    ws_prec = wb["BigQuery Precedents"]
    assert ws_prec.max_row >= 5  # 1 header + at least 4 redlined clause precedent rows
    prec_values = " | ".join(
        str(cell)
        for row in ws_prec.iter_rows(values_only=True)
        for cell in row
        if cell is not None
    )
    assert "EXC-2025-787-019" in prec_values
    assert "Honeywell Aerospace" in prec_values
    assert "80%" in prec_values

    # Sheet 4: Immutable Audit Trail
    ws_audit = wb["Immutable Audit Trail"]
    assert ws_audit.max_row == 1 + len(state.recent_events)
    assert ws_audit.cell(row=2, column=1).value == "EVT-2026-001"
    assert ws_audit.cell(row=3, column=1).value == "EVT-2026-002"
