"""
Verification suite for Cymbal Aerospace CLM OOXML .docx ingestion, diff engine, and .docx/.xlsx exporters.
Validates 100% conformance against specs/04_golden_fixtures/*, specs/02_domain_models.py,
and the docx / xlsx / tabular-review / explanations-for-redlines / playbook-sanitization skills.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import re
import zipfile

from docx import Document
from lxml import etree
from openpyxl import load_workbook

from boeing_clm.export import (
    COUNTER_PROPOSAL_AUTHOR,
    generate_counter_proposal_docx,
    generate_deviation_matrix_xlsx,
    sanitize_counterparty_comment,
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
VANGUARD_TR5510_DOCX = GOLDEN_DIR / "Vanguard_Working_Review_TR5510.docx"
MERIDIAN_LG7740_DOCX = GOLDEN_DIR / "Meridian_Working_Review_LG7740.docx"
EXPECTED_DIFFS_JSON = GOLDEN_DIR / "expected_extracted_diffs.json"


def _load_skill_script(rel_path: str):
    script_path = REPO_ROOT / rel_path
    spec = importlib.util.spec_from_file_location(script_path.stem, script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
                    sme_reviewer="Miriam Graham (Corporate Legal)",
                    sme_rationale=(
                        "Miriam Graham (VP Legal & IP): Applied 80% Tier-1 Avionics precedent "
                        "(11 of 16 deals) and 1.5x ($67.5M) walk-away floor on CONFLICT-GP1-19: "
                        "2x PO $90M cap on general damages with uncapped recall & IP indemnity "
                        "(https://36zrbd.sharepoint.com/sites/CymbalAerospace / boeing_clm)."
                    ),
                    precedent_analysis=sample_precedent,
                )
            )
        else:
            clauses.append(
                ClauseWorkbenchItem(
                    clause_id=item.clause_id,
                    proforma_doc=item.proforma_doc,
                    clause_ref=item.clause_ref,
                    clause_title=f"✅ {item.clause_title}",
                    has_redline=True,
                    sme_team=item.sme_team,
                    sme_owner_label=f"{item.sme_owner_label} (Pradeep Gupta)",
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
                    sme_reviewer="Megan Bowen",
                    sme_rationale=(
                        f"Megan Bowen: Mandatory regulatory and commercial hold-firm on {item.clause_ref} "
                        f"per LOCKOUT-{item.clause_id} and 88% precedent (14 of 16 deals)."
                    ),
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


def test_parse_all_three_golden_fixtures_zero_fcc900_contamination() -> None:
    """
    Verify parse_redlined_docx parses all 3 golden fixtures:
    - Vendor_Redlined_GP1.docx (Deal 1: BA-2026-AV-8921)
    - Vanguard_Working_Review_TR5510.docx (Deal 2: BA-2026-TR-5510, TRA-500 Thrust Reversers)
    - Meridian_Working_Review_LG7740.docx (Deal 3: BA-2026-LG-7740, TLG-800 Landing Gear)
    with 12 clauses each and zero 'FCC-900' contamination in TR5510 or LG7740.
    """
    parsed_av = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    parsed_tr = parse_redlined_docx(VANGUARD_TR5510_DOCX)
    parsed_lg = parse_redlined_docx(MERIDIAN_LG7740_DOCX)

    assert len(parsed_av) == 12
    assert len(parsed_tr) == 12
    assert len(parsed_lg) == 12

    # Deal 2 (TR5510) has 5 redlined clauses (GP1-03 Finance discount + GP1-12, GP1-19, SP3-04, SP5-03)
    tr_redlined = [d.clause_id for d in parsed_tr if d.has_redline]
    assert tr_redlined == ["GP1-03", "GP1-12", "GP1-19", "SP3-04", "SP5-03"]
    tr_blob = json.dumps([d.model_dump() for d in parsed_tr])
    assert "TRA-500" in tr_blob
    assert "FCC-900" not in tr_blob

    # Deal 3 (LG7740) has 4 redlined clauses (GP1-12, GP1-19, SP3-04, SP5-03)
    lg_redlined = [d.clause_id for d in parsed_lg if d.has_redline]
    assert lg_redlined == ["GP1-12", "GP1-19", "SP3-04", "SP5-03"]
    lg_blob = json.dumps([d.model_dump() for d in parsed_lg])
    assert "TLG-800" in lg_blob
    assert "FCC-900" not in lg_blob


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


def test_generate_counter_proposal_docx_surgical_diffs_sanitization_and_ooxml_validation(
    tmp_path: Path,
) -> None:
    """
    Verify generate_counter_proposal_docx:
    - Passes .agents/skills/docx/scripts/validate.py with zero errors
    - Produces word-level surgical <w:del>/<w:ins> alongside regular <w:r> runs
    - Attributes all <w:del>, <w:ins>, and <w:comment> elements to 'Cymbal Aerospace Legal & Procurement'
    - Includes <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr> inside <w:r> wrapping <w:commentReference>
    - Strips emojis (✅, ⚠️, ⏳) from Heading 2 text
    - Contains zero internal SME names, precedent percentages, walk-away floors, internal URLs,
      or CONFLICT-/LOCKOUT- strings in word/comments.xml (and <75 words per comment)
    """
    extracted = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    state = _build_sample_workbench_state(extracted)

    out_docx = tmp_path / "Cymbal_Counter_Proposal.docx"
    res_path = generate_counter_proposal_docx(state, out_docx)
    assert res_path == out_docx
    assert out_docx.exists()

    # 1. Validate via .agents/skills/docx/scripts/validate.py
    docx_validator = _load_skill_script(".agents/skills/docx/scripts/validate.py")
    validation_errors = docx_validator.validate(out_docx)
    assert validation_errors == [], f"DOCX validation failed: {validation_errors}"

    with zipfile.ZipFile(out_docx, "r") as zf:
        assert "word/document.xml" in zf.namelist()
        assert "word/comments.xml" in zf.namelist()
        doc_xml = etree.fromstring(zf.read("word/document.xml"))
        comments_xml = etree.fromstring(zf.read("word/comments.xml"))

    # 2. Verify executive summary table in document.xml & emoji-free Heading 2s
    all_text = "".join(t.text or "" for t in doc_xml.findall(f".//{{{W_NS}}}t"))
    assert "BA-2026-AV-8921" in all_text
    assert "Apex AeroSystems" in all_text
    assert "$45,000,000.00" in all_text
    assert "READY_FOR_DISPATCH" in all_text
    for emoji_ch in ("✅", "⚠️", "⏳"):
        assert emoji_ch not in all_text

    # 3. Verify surgical word-level <w:ins> and <w:del> alongside regular <w:r> runs
    ins_nodes = doc_xml.findall(f".//{{{W_NS}}}ins")
    del_nodes = doc_xml.findall(f".//{{{W_NS}}}del")
    assert len(ins_nodes) >= 4
    assert len(del_nodes) >= 4
    for node in ins_nodes + del_nodes:
        assert node.get(f"{{{W_NS}}}author") == COUNTER_PROPOSAL_AUTHOR

    # Every redlined paragraph with <w:del>/<w:ins> also preserves unchanged words in standard <w:r> runs
    redlined_paragraphs = [
        p for p in doc_xml.findall(f".//{{{W_NS}}}p") if p.findall(f"./{{{W_NS}}}ins")
    ]
    assert len(redlined_paragraphs) == 4
    for p_el in redlined_paragraphs:
        direct_r_texts = [
            "".join(t.text or "" for t in r.findall(f"./{{{W_NS}}}t"))
            for r in p_el.findall(f"./{{{W_NS}}}r")
        ]
        assert any(txt.strip() for txt in direct_r_texts), "Expected unchanged <w:r> tokens alongside surgical <w:del>/<w:ins>"

    # 4. Verify <w:rPr><w:rStyle w:val="CommentReference"/></w:rPr> inside every <w:commentReference> parent <w:r>
    cref_nodes = doc_xml.findall(f".//{{{W_NS}}}commentReference")
    assert len(cref_nodes) == 4
    for cref in cref_nodes:
        r_parent = cref.getparent()
        assert r_parent is not None and r_parent.tag == f"{{{W_NS}}}r"
        r_style = r_parent.find(f"./{{{W_NS}}}rPr/{{{W_NS}}}rStyle")
        assert r_style is not None
        assert r_style.get(f"{{{W_NS}}}val") == "CommentReference"

    # 5. Verify comments.xml sanitization & <75 words constraint
    comment_els = comments_xml.findall(f".//{{{W_NS}}}comment")
    assert len(comment_els) == 4
    for c_el in comment_els:
        assert c_el.get(f"{{{W_NS}}}author") == COUNTER_PROPOSAL_AUTHOR
        c_text = "".join(t.text or "" for t in c_el.findall(f".//{{{W_NS}}}t"))
        assert len(c_text.split()) < 75, f"Comment exceeds 75 words: {c_text}"

    comments_text = " ".join(
        "".join(t.text or "" for t in c_el.findall(f".//{{{W_NS}}}t"))
        for c_el in comment_els
    )
    assert "2x PO $90M cap on general damages" in comments_text
    assert "FAA 14 CFR Part 21" in comments_text

    for forbidden_name in (
        "Pradeep Gupta",
        "Megan Bowen",
        "Alex Wilber",
        "Miriam Graham",
        "Diego Siciliani",
    ):
        assert forbidden_name not in comments_text
        assert forbidden_name not in all_text

    assert not re.search(
        r"\b\d+(?:\.\d+)?%\s*(?:precedent|held firm|compromise|tier-1|deals)\b",
        comments_text,
        flags=re.IGNORECASE,
    )
    assert not re.search(r"\(\d+\s*(?:of|/)\s*\d+\s*deals?\)", comments_text, flags=re.IGNORECASE)
    for forbidden_token in ("CONFLICT-", "LOCKOUT-", "walk-away", "floor", "boeing_clm", "sharepoint.com", "127.0.0.1"):
        assert forbidden_token not in comments_text.lower() if forbidden_token in ("walk-away", "floor") else forbidden_token not in comments_text

    # 6. Round-trip parse with parse_redlined_docx
    reparsed = parse_redlined_docx(out_docx)
    assert len(reparsed) == 12
    reparsed_redlined = [d for d in reparsed if d.has_redline]
    assert len(reparsed_redlined) == 4
    gp19 = next(d for d in reparsed_redlined if d.clause_id == "GP1-19")
    assert "two hundred percent (200%)" in gp19.vendor_redline_text
    assert "one hundred percent (100%)" in gp19.boeing_baseline_text
    assert len(gp19.vendor_comments) == 1
    assert COUNTER_PROPOSAL_AUTHOR in gp19.vendor_comments[0]


def test_generate_deviation_matrix_xlsx_formulas_tabular_review_and_validation(
    tmp_path: Path,
) -> None:
    """
    Verify generate_deviation_matrix_xlsx:
    - Builds 5 worksheets including 5_Portfolio_Tabular_Review
    - Emits real Excel formulas (=COUNTA, =COUNTIF, =COUNTIFS, =SUM, =IF) on 1_Executive_Summary,
      4_BigQuery_Precedent_Benchmarks, and 5_Portfolio_Tabular_Review
    - Applies institutional number formats ($#,##0, 0.0%, 0.0"x") and banker font colors
      (0000FF blue inputs, 000000 black same-sheet formulas, 008000 green cross-sheet links)
    - Passes .agents/skills/xlsx/scripts/recalc_pure_python.py, .agents/skills/xlsx/scripts/scan_errors.py,
      and .agents/skills/xlsx/scripts/validate.py
    """
    extracted = parse_redlined_docx(VENDOR_REDLINED_DOCX)
    state = _build_sample_workbench_state(extracted)

    out_xlsx = tmp_path / "Deviation_Matrix.xlsx"
    res_path = generate_deviation_matrix_xlsx(state, out_xlsx)
    assert res_path == out_xlsx
    assert out_xlsx.exists()

    wb = load_workbook(str(out_xlsx), data_only=False)
    assert wb.sheetnames == [
        "1_Executive_Summary",
        "2_Clause_Deviation_Matrix",
        "3_Cross_Clause_Conflict_Log",
        "4_BigQuery_Precedent_Benchmarks",
        "5_Portfolio_Tabular_Review",
    ]

    # 1. Verify Sheet 1: 1_Executive_Summary formulas & banker styling
    ws_exec = wb["1_Executive_Summary"]
    exec_formulas = {
        ws_exec.cell(row=r, column=1).value: ws_exec.cell(row=r, column=2).value
        for r in range(3, ws_exec.max_row + 1)
    }
    assert exec_formulas["Total Clauses Parsed"] == "=COUNTA('2_Clause_Deviation_Matrix'!A2:A13)"
    assert exec_formulas["Untouched Clauses Count"] == '=COUNTIF(\'2_Clause_Deviation_Matrix\'!F2:F13,"NO")'
    assert exec_formulas["Redlined Clauses Count"] == '=COUNTIF(\'2_Clause_Deviation_Matrix\'!F2:F13,"YES")'
    assert (
        exec_formulas["Approved Redlined Clauses Count"]
        == '=COUNTIFS(\'2_Clause_Deviation_Matrix\'!F2:F13,"YES",\'2_Clause_Deviation_Matrix\'!G2:G13,"APPROVED")'
    )
    assert exec_formulas["Active Cross-Clause Conflicts"] == "=COUNTA('3_Cross_Clause_Conflict_Log'!A2:A20)"

    # Verify banker colors and number formats on 1_Executive_Summary
    assert ws_exec["B8"].value == 45_000_000.0
    assert ws_exec["B8"].number_format == "$#,##0"
    assert ws_exec["B8"].font.color.rgb.endswith("0000FF")
    assert ws_exec["B9"].number_format == '0.0"x"'
    assert ws_exec["B10"].value == "=B8*B9"
    assert ws_exec["B10"].font.color.rgb.endswith("000000")
    assert ws_exec["B15"].font.color.rgb.endswith("008000")

    # 2. Verify Sheet 2: 2_Clause_Deviation_Matrix
    ws_matrix = wb["2_Clause_Deviation_Matrix"]
    assert ws_matrix.max_row == 13
    assert [ws_matrix.cell(row=r, column=1).value for r in range(2, 14)] == [c.clause_id for c in state.clauses]

    # 3. Verify Sheet 3: 3_Cross_Clause_Conflict_Log
    ws_conflict = wb["3_Cross_Clause_Conflict_Log"]
    assert ws_conflict["A2"].value == "CONFLICT-SP3-04-GP1-03"

    # 4. Verify Sheet 4: 4_BigQuery_Precedent_Benchmarks has Total Matched Precedents (=SUM(E2:G2)) & 0.0%
    ws_prec = wb["4_BigQuery_Precedent_Benchmarks"]
    assert ws_prec["H1"].value == "Total Matched Precedents"
    assert ws_prec["H2"].value == "=SUM(E2:G2)"
    assert ws_prec["H2"].font.color.rgb.endswith("000000")
    assert ws_prec["I2"].value == "=IF(H2>0,E2/H2,0)"
    assert ws_prec["I2"].number_format == "0.0%"

    # 5. Verify Sheet 5: 5_Portfolio_Tabular_Review
    ws_tab = wb["5_Portfolio_Tabular_Review"]
    deal_ids = [ws_tab.cell(row=r, column=1).value for r in range(2, 5)]
    assert deal_ids == ["BA-2026-AV-8921", "BA-2026-TR-5510", "BA-2026-LG-7740"]
    assert ws_tab["D5"].value == "=SUM(D2:D4)"
    assert str(ws_tab["E5"].value).startswith("=COUNTIF(")
    assert str(ws_tab["J5"].value).startswith("=COUNTIF(")

    # 6. Run recalc_pure_python.py, scan_errors.py, and validate.py
    recalc_mod = _load_skill_script(".agents/skills/xlsx/scripts/recalc_pure_python.py")
    scan_mod = _load_skill_script(".agents/skills/xlsx/scripts/scan_errors.py")
    validate_mod = _load_skill_script(".agents/skills/xlsx/scripts/validate.py")

    recalced_xlsx = tmp_path / "Deviation_Matrix_Recalced.xlsx"
    recalc_mod.recalc(out_xlsx, recalced_xlsx)
    assert recalced_xlsx.exists()

    hits_orig = scan_mod.scan(out_xlsx)
    hits_recalced = scan_mod.scan(recalced_xlsx)
    status = "clean" if (len(hits_orig) == 0 and len(hits_recalced) == 0) else "errors"
    assert status == "clean", f"Excel formula errors detected: {hits_orig} / {hits_recalced}"

    assert validate_mod.validate(out_xlsx) == []
    assert validate_mod.validate(recalced_xlsx) == []

    # Verify recalculated values materialized accurately
    wb_recalc = load_workbook(str(recalced_xlsx), data_only=True)
    ws_exec_eval = wb_recalc["1_Executive_Summary"]
    eval_map = {
        ws_exec_eval.cell(row=r, column=1).value: ws_exec_eval.cell(row=r, column=2).value
        for r in range(3, ws_exec_eval.max_row + 1)
    }
    assert eval_map["Total Clauses Parsed"] == 12
    assert eval_map["Untouched Clauses Count"] == 8
    assert eval_map["Redlined Clauses Count"] == 4
    assert eval_map["Approved Redlined Clauses Count"] == 4
    assert eval_map["Active Cross-Clause Conflicts"] == 1
    assert wb_recalc["5_Portfolio_Tabular_Review"]["D5"].value == 135_000_000.0
