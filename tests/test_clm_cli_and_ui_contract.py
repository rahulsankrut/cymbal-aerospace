"""
Verification suite for the 4 Focused Cymbal Aerospace CLM Skills (`clm-contract-intake`,
`clm-comms`, `clm-tax-tariff-review`, `clm-contract-consolidation`), the Document-Style
Interactive Counter-Position Reviewer UI, and Working Review `.docx` generation with
human-user-attributed Word comments (`w:author=<User>`).
"""
from __future__ import annotations

import json
from pathlib import Path
import zipfile

from boeing_clm.models import (
    DealWorkbenchState,
    PrecedentSearchResult,
    SMEReviewSubmission,
)
from skills.clm_cli import (
    RECOMMENDED_COUNTER_DEFAULTS,
    apply_local_harmonize,
    apply_local_position,
    build_fresh_docx_and_xlsx,
    build_sme_draft_specs,
    generate_canvas_workbench_html,
    generate_tax_reviewer_workbench_html,
    load_seed,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_four_focused_clm_skills_exist() -> None:
    expected_skills = [
        "clm-contract-intake",
        "clm-comms",
        "clm-tax-tariff-review",
        "clm-contract-consolidation",
    ]
    for skill_name in expected_skills:
        skill_md = REPO_ROOT / "skills" / skill_name / "SKILL.md"
        assert skill_md.exists(), f"Missing SKILL.md for {skill_name}"
        content = skill_md.read_text(encoding="utf-8")
        assert f"name: {skill_name}" in content


def test_seed_conforms_to_frozen_domain_models() -> None:
    seed = load_seed()
    state = DealWorkbenchState.model_validate(seed["initial_state"])
    assert state.deal_id == "BA-2026-AV-8921"
    assert state.total_clauses_parsed == 12
    assert state.untouched_clauses_count == 8
    assert state.redlined_clauses_count == 4

    for cid in ("GP1-12", "GP1-19", "SP3-04", "SP5-03"):
        prec = PrecedentSearchResult.model_validate(seed["precedents"][cid])
        assert prec.clause_id == cid
        assert prec.distribution.total_matches == 16
        assert len(prec.precedents) == 5


def test_working_review_docx_applies_accepted_changes_and_user_comments(tmp_path: Path) -> None:
    seed = load_seed()
    state = json.loads(json.dumps(seed["initial_state"]))

    # Validate submission via SMEReviewSubmission from specs/02_domain_models.py
    sub = SMEReviewSubmission(
        deal_id="BA-2026-AV-8921",
        clause_id="GP1-19",
        sme_team="LEGAL",
        selected_option_key="compromise_tier_1",
        selected_counter_text="19.1 Tier-1 Avionics Super-Cap (2x PO / $90,000,000) with uncapped AD recall & IP.",
        sme_reviewer="Rahul Kasanagottu",
        sme_rationale="Approved 2x PO ($90M) Super-Cap per 69% Tier-1 Avionics precedent.",
        source_surface="DOCUMENT_REVIEWER_UI",
    )

    state = apply_local_position(
        state=state,
        clause_id=sub.clause_id,
        sme_team=sub.sme_team,
        option=sub.selected_option_key,
        counter_text=sub.selected_counter_text,
        reviewer=sub.sme_reviewer,
        rationale=sub.sme_rationale,
    )

    counter_docx, matrix_xlsx = build_fresh_docx_and_xlsx(state, tmp_path)
    working_docx = tmp_path / "BA-2026-AV-8921_Working_Review.docx"
    assert counter_docx.exists()
    assert working_docx.exists()
    assert matrix_xlsx.exists()

    with zipfile.ZipFile(working_docx, "r") as z:
        doc_xml = z.read("word/document.xml").decode("utf-8")
        comments_xml = z.read("word/comments.xml").decode("utf-8")

    # Accepted change is cleanly applied in word/document.xml with human user attribution
    assert "[✓ ACCEPTED BY Rahul Kasanagottu]" in doc_xml
    assert "19.1 Tier-1 Avionics Super-Cap (2x PO / $90,000,000)" in doc_xml

    # Comments in word/comments.xml are attributed to human users (not system)
    assert 'w:author="Rahul Kasanagottu"' in comments_xml
    assert "Approved 2x PO ($90M) Super-Cap per 69% Tier-1 Avionics precedent." in comments_xml
    assert "Cymbal CLM" not in comments_xml


def test_document_reviewer_ui_generation(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    seed = load_seed()
    state = json.loads(json.dumps(seed["initial_state"]))
    main_html = generate_canvas_workbench_html(state, active_clause_id="GP1-19")
    tax_html = generate_tax_reviewer_workbench_html(state, seed["precedents"]["SP3-04"])

    assert main_html.exists()
    assert tax_html.exists()

    main_text = main_html.read_text(encoding="utf-8")
    assert "Rewrite with Input" in main_text
    assert "Accept changes" in main_text
    assert "Reject changes" in main_text
    assert "Comment" in main_text
    assert "/api/review" in main_text
    assert "/api/download/working-docx" in main_text
    # Verify Pastel Design System & Synthesized User Feedback Features
    assert "--pastel-canvas: #faf8f5" in main_text
    assert "Why This Counter-Position Is Recommended" in main_text
    assert "Revert to Recommended Counter" in main_text
    assert "Revert to Original Proforma Baseline" in main_text
    assert "Use Language" in main_text
    assert "SPLIT_3COL" in main_text
    assert "DEPENDENCY_GRAPH" in main_text
    assert "PRE_CONSOLIDATION" in main_text
    # Verify Contract Playbook Comparison Features
    assert "Compared Against: Cymbal Tier-1 Avionics Playbook" in main_text
    assert "PLAYBOOK_COUNTER" in main_text
    assert "PLAYBOOK_STANDARD" in main_text
    assert "APPLY PRE-APPROVED 2.0x PLAYBOOK FALLBACK" in main_text
    assert "VIOLATES PLAYBOOK LOCKOUT (LOCKOUT-GP1-12-FAA)" in main_text
    assert "Cymbal Playbook Preferred Standard" in main_text

    # Fix 1: applyPreset(optionKey) looks up matchedOpt in playbook_options & renders o.badge + recommended_option_key
    assert "const matchedOpt = opts.find(o => o.option_key === optionKey);" in main_text
    assert "const isRec = o.recommended || o.option_key === clause.recommended_option_key;" in main_text
    assert "o.badge" in main_text

    # Fix 2: Sticky Word Margin Balloons + scrollIntoView in openDrawer
    assert 'style="position:sticky;top:12px;"' in main_text
    assert "el.scrollIntoView({ behavior: 'smooth', block: 'center' });" in main_text

    # Fix 3 & 4: Off-by-one GP1-12 index removed & SP3-04 tariff cap standardized to 2.0% ($900,000) everywhere
    cli_source = (REPO_ROOT / "skills" / "clm_cli.py").read_text(encoding="utf-8")
    assert 'state["clauses"][4]["boeing_baseline_text"]' not in cli_source
    assert "2.5%" not in cli_source
    assert "$1,125,000" not in cli_source
    assert RECOMMENDED_COUNTER_DEFAULTS["GP1-12"]["counter_text"].startswith("12.2")
    assert "2.0% ($900,000)" in RECOMMENDED_COUNTER_DEFAULTS["SP3-04"]["counter_text"]

    specs = build_sme_draft_specs(state)
    tax_spec = next(s for s in specs if s["clause_id"] == "SP3-04")
    assert "2.0% ($900,000)" in tax_spec["precedent_stat"]
    assert "+2.0% ($900,000)" in tax_spec["recommended_action"]

    harmonized_state = apply_local_harmonize(json.loads(json.dumps(state)), "CONFLICT-SP3-04-GP1-03", "Pradeep Gupta")
    sp3_clause = next(c for c in harmonized_state["clauses"] if c["clause_id"] == "SP3-04")
    assert "2.0% ($900,000)" in sp3_clause["selected_counter_text"]
    assert "+2.0% ($900,000)" in sp3_clause["sme_rationale"]
