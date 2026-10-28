"""
tests/test_bigquery_and_conflicts.py — Live BigQuery & Conflict Governance Verification Suite.

Executes strictly against `vertex-ai-demos-468803.boeing_clm` with zero mocks.
"""
from __future__ import annotations

import json
import pytest

from boeing_clm.config import DEFAULT_DEAL_ID, GOLDEN_EXPECTED_DIFFS_JSON
from boeing_clm.models import (
    DealWorkbenchState,
    ExtractedClauseDiff,
    PrecedentSearchResult,
    SMEReviewSubmission,
)
from boeing_clm.storage import BigQueryCLMRepository
from setup_bigquery import verify_seed


@pytest.fixture(scope="module")
def repo() -> BigQueryCLMRepository:
    repository = BigQueryCLMRepository()
    for deal_id in ("BA-2026-AV-8921", "BA-2026-TR-5510", "BA-2026-LG-7740"):
        repository.reset_deal_workbench(
            deal_id=deal_id,
            source_surface="EXPERIENCE_LAYER_UI",
            include_precedents=False,
        )
    yield repository
    # Ensure canonical initial workbench state is restored across all 3 portfolio deals after tests complete
    for deal_id in ("BA-2026-AV-8921", "BA-2026-TR-5510", "BA-2026-LG-7740"):
        repository.reset_deal_workbench(
            deal_id=deal_id,
            source_surface="EXPERIENCE_LAYER_UI",
            include_precedents=False,
        )


def test_bigquery_seeded_tables_and_768_dim_embeddings(repo: BigQueryCLMRepository) -> None:
    """Verify all 6 tables, 3 portfolio deals, 4 conflict rules, and 768-dimensional embeddings exist in live BigQuery."""
    summary = verify_seed(repo.client, repo.project_id, repo.dataset)
    assert summary["proforma_count"] == 12
    assert summary["proforma_embedded_count"] == 12
    assert summary["precedent_count"] == 64
    assert summary["precedent_embedded_count"] == 64
    assert summary["conflict_rules_count"] == 4
    assert summary["active_deals_count"] == 3
    assert summary["deviations_count"] == 36


@pytest.mark.parametrize(
    "clause_id,expected_lockout,expected_held_firm,expected_tier1,expected_accepted",
    [
        ("GP1-12", True, 14, 2, 0),
        ("GP1-19", False, 4, 11, 1),
        ("SP3-04", False, 5, 10, 1),
        ("SP5-03", True, 15, 1, 0),
    ],
)
def test_live_vector_search_and_outcome_distribution(
    repo: BigQueryCLMRepository,
    clause_id: str,
    expected_lockout: bool,
    expected_held_firm: int,
    expected_tier1: int,
    expected_accepted: int,
) -> None:
    """Verify live BigQuery VECTOR_SEARCH and COUNTIF outcome distributions across all 4 redlined clauses."""
    result = repo.search_clause_precedents(clause_id=clause_id, top_k=5)
    assert isinstance(result, PrecedentSearchResult)
    assert result.clause_id == clause_id
    assert result.regulatory_lockout is expected_lockout

    dist = result.distribution
    assert dist.total_matches == 16
    assert dist.held_firm_count == expected_held_firm
    assert dist.compromise_tier_1_count == expected_tier1
    assert dist.accepted_vendor_count == expected_accepted

    assert len(result.precedents) == 5
    for match in result.precedents:
        assert match.clause_id == clause_id
        assert 0.55 <= match.similarity_score <= 1.0

    assert [opt.option_key for opt in result.playbook_options] == [
        "hold_firm",
        "compromise_tier_1",
        "accept_vendor",
    ]


def test_initial_workbench_state_and_cross_clause_conflict(repo: BigQueryCLMRepository) -> None:
    """Verify initial deal workbench state has 8 untouched, 4 redlined, and active SP3-04 vs GP1-03 conflict."""
    state = repo.get_deal_workbench_state(deal_id=DEFAULT_DEAL_ID, include_precedents=True)
    assert isinstance(state, DealWorkbenchState)
    assert state.deal_id == DEFAULT_DEAL_ID
    assert state.total_clauses_parsed == 12
    assert state.untouched_clauses_count == 8
    assert state.redlined_clauses_count == 4
    assert state.status == "CONFLICT_DETECTED"

    assert len(state.active_conflicts) == 1
    conflict = state.active_conflicts[0]
    assert conflict.rule_id == "CONFLICT-SP3-04-GP1-03"
    assert conflict.rule_type == "CROSS_CLAUSE_CONFLICT"
    assert conflict.source_clause_id == "SP3-04"
    assert conflict.target_clause_id == "GP1-03"
    assert conflict.source_sme_team == "TAX"
    assert conflict.target_sme_team == "PROCUREMENT"
    assert conflict.severity == "CRITICAL_CONFLICT"

    clauses_by_id = {c.clause_id: c for c in state.clauses}
    assert clauses_by_id["GP1-12"].sme_status == "APPROVED"
    assert clauses_by_id["GP1-19"].sme_status == "APPROVED"
    assert clauses_by_id["SP5-03"].sme_status == "APPROVED"
    assert clauses_by_id["SP3-04"].sme_status == "CONFLICT"
    assert clauses_by_id["SP3-04"].precedent_analysis is not None


def test_regulatory_lockout_detection_and_conflict_harmonization_lifecycle(
    repo: BigQueryCLMRepository,
) -> None:
    """Verify regulatory lockout triggers on GP1-12 / SP5-03 and conflict harmonization transitions deal to READY_FOR_DISPATCH."""
    # 1. Trigger FAA 14 CFR Part 21 regulatory lockout on GP1-12 by selecting accept_vendor
    state_after_lockout = repo.record_sme_submission(
        SMEReviewSubmission(
            deal_id=DEFAULT_DEAL_ID,
            clause_id="GP1-12",
            sme_team="ENGINEERING",
            selected_option_key="accept_vendor",
            selected_counter_text=(
                "12.2 Seller warrants all Goods against defects in material, workmanship, and avionics firmware "
                "for twelve (12) months from factory shipment. Boeing and FAA representatives may conduct "
                "scheduled inspections upon thirty (30) days prior written notice."
            ),
            sme_reviewer="Test Engineering Reviewer",
            sme_rationale="Testing FAA Part 21 lockout detection.",
            source_surface="GEMINI_AGENT_MCP",
        )
    )
    active_rule_ids = {c.rule_id for c in state_after_lockout.active_conflicts}
    assert "LOCKOUT-GP1-12-FAA" in active_rule_ids
    assert "CONFLICT-SP3-04-GP1-03" in active_rule_ids

    # 2. Restore Hold Firm on GP1-12 via harmonize_conflict on LOCKOUT-GP1-12-FAA
    state_after_faa_fix = repo.harmonize_conflict(
        deal_id=DEFAULT_DEAL_ID,
        rule_id="LOCKOUT-GP1-12-FAA",
        actor="Dr. Aris Thorne (Principal FAA DER)",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    active_rule_ids_2 = {c.rule_id for c in state_after_faa_fix.active_conflicts}
    assert "LOCKOUT-GP1-12-FAA" not in active_rule_ids_2
    assert "CONFLICT-SP3-04-GP1-03" in active_rule_ids_2

    # 3. Harmonize the cross-clause conflict between SP3-04 (Tax) and GP1-03 (Procurement)
    harmonized_state = repo.harmonize_conflict(
        deal_id=DEFAULT_DEAL_ID,
        rule_id="CONFLICT-SP3-04-GP1-03",
        actor="Lead Contract Owner (M. Vance)",
        source_surface="EXPERIENCE_LAYER_UI",
    )
    assert len(harmonized_state.active_conflicts) == 0
    assert harmonized_state.status == "READY_FOR_DISPATCH"

    sp304 = next(c for c in harmonized_state.clauses if c.clause_id == "SP3-04")
    assert sp304.sme_status == "APPROVED"
    assert sp304.selected_option_key == "custom_harmonized"
    assert "capped at a maximum aggregate adjustment of 2.0%" in sp304.selected_counter_text
    assert any(e.action == "CONFLICT_HARMONIZED" for e in harmonized_state.recent_events)


def test_save_extracted_clauses_and_reset_workbench(repo: BigQueryCLMRepository) -> None:
    """Verify save_extracted_clauses and reset_deal_workbench persist and restore canonical state."""
    raw_diffs = json.loads(GOLDEN_EXPECTED_DIFFS_JSON.read_text(encoding="utf-8"))
    diffs = [ExtractedClauseDiff.model_validate(d) for d in raw_diffs]

    saved_state = repo.save_extracted_clauses(
        deal_id=DEFAULT_DEAL_ID,
        diffs=diffs,
        source_surface="GEMINI_AGENT_MCP",
    )
    assert saved_state.total_clauses_parsed == 12
    assert saved_state.untouched_clauses_count == 8
    assert saved_state.redlined_clauses_count == 4
    assert any(e.action == "INGESTED_REDLINE" for e in saved_state.recent_events)

    reset_state = repo.reset_deal_workbench(
        deal_id=DEFAULT_DEAL_ID,
        source_surface="EXPERIENCE_LAYER_UI",
    )
    assert reset_state.status == "CONFLICT_DETECTED"
    assert len(reset_state.active_conflicts) == 1
    assert reset_state.active_conflicts[0].rule_id == "CONFLICT-SP3-04-GP1-03"


def test_all_three_portfolio_deals_and_tr5510_finance_legal_harmonization(
    repo: BigQueryCLMRepository,
) -> None:
    """
    Verify:
    1. `get_deal_workbench_state` and `reset_deal_workbench` work for all 3 portfolio deals:
       - `BA-2026-AV-8921` (Apex AeroSystems Inc., $45M, 8 untouched / 4 redlined, SP3-04 vs GP1-03 conflict)
       - `BA-2026-TR-5510` (Vanguard Thrust Systems Corp., $38M, 7 untouched / 5 redlined, GP1-19 vs GP1-03 conflict)
       - `BA-2026-LG-7740` (Meridian Landing Gear Corp., $52M, 8 untouched / 4 redlined, IN_SME_REVIEW, 2 approved / 2 pending)
    2. `harmonize_clause_conflict` resolves `CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL` on `BA-2026-TR-5510`
       to `READY_FOR_DISPATCH`, and `reset_deal_workbench("BA-2026-TR-5510")` restores its initial conflict state.
    """
    # 1. Verify active_deals list in BigQuery
    deals = repo.list_active_deals()
    deals_by_id = {d["deal_id"]: d for d in deals}
    assert set(deals_by_id.keys()) == {"BA-2026-AV-8921", "BA-2026-TR-5510", "BA-2026-LG-7740"}
    assert deals_by_id["BA-2026-AV-8921"]["status"] == "INGESTED"
    assert deals_by_id["BA-2026-TR-5510"]["status"] == "CONFLICT_DETECTED"
    assert deals_by_id["BA-2026-LG-7740"]["status"] == "IN_SME_REVIEW"

    # 2. Verify Deal 2 (BA-2026-TR-5510) initial conflict state
    tr_state = repo.get_deal_workbench_state(deal_id="BA-2026-TR-5510", include_precedents=True)
    assert tr_state.deal_id == "BA-2026-TR-5510"
    assert tr_state.vendor_name == "Vanguard Thrust Systems Corp."
    assert tr_state.contract_value_usd == 38000000.0
    assert tr_state.total_clauses_parsed == 12
    assert tr_state.untouched_clauses_count == 7
    assert tr_state.redlined_clauses_count == 5
    assert tr_state.status == "CONFLICT_DETECTED"
    assert len(tr_state.active_conflicts) == 1

    tr_conflict = tr_state.active_conflicts[0]
    assert tr_conflict.rule_id == "CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL"
    assert tr_conflict.rule_type == "CROSS_CLAUSE_CONFLICT"
    assert tr_conflict.source_clause_id == "GP1-19"
    assert tr_conflict.target_clause_id == "GP1-03"
    assert tr_conflict.source_sme_team == "LEGAL"
    assert tr_conflict.target_sme_team == "PROCUREMENT"

    tr_clauses = {c.clause_id: c for c in tr_state.clauses}
    assert tr_clauses["GP1-19"].sme_status == "CONFLICT"
    assert tr_clauses["GP1-03"].sme_status == "CONFLICT"
    assert tr_clauses["GP1-12"].sme_status == "APPROVED"
    assert tr_clauses["SP3-04"].sme_status == "APPROVED"
    assert tr_clauses["SP5-03"].sme_status == "APPROVED"

    # 3. Harmonize CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL on BA-2026-TR-5510
    tr_harmonized = repo.harmonize_clause_conflict(
        deal_id="BA-2026-TR-5510",
        rule_id="CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL",
        actor="Elena Rostova, J.D. & Sloane Mercer, MBA",
    )
    assert tr_harmonized.status == "READY_FOR_DISPATCH"
    assert len(tr_harmonized.active_conflicts) == 0
    tr_h_clauses = {c.clause_id: c for c in tr_harmonized.clauses}
    assert tr_h_clauses["GP1-19"].sme_status == "APPROVED"
    assert tr_h_clauses["GP1-19"].selected_option_key == "custom_harmonized"
    assert "150% / 1.5x" in tr_h_clauses["GP1-19"].selected_counter_text
    assert tr_h_clauses["GP1-03"].sme_status == "APPROVED"

    # 4. Reset BA-2026-TR-5510 back to its initial conflict state
    tr_reset = repo.reset_deal_workbench(deal_id="BA-2026-TR-5510", source_surface="EXPERIENCE_LAYER_UI")
    assert tr_reset.status == "CONFLICT_DETECTED"
    assert len(tr_reset.active_conflicts) == 1
    assert tr_reset.active_conflicts[0].rule_id == "CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL"

    # 5. Verify Deal 3 (BA-2026-LG-7740) initial IN_SME_REVIEW state
    lg_state = repo.get_deal_workbench_state(deal_id="BA-2026-LG-7740", include_precedents=True)
    assert lg_state.deal_id == "BA-2026-LG-7740"
    assert lg_state.vendor_name == "Meridian Landing Gear Corp."
    assert lg_state.contract_value_usd == 52000000.0
    assert lg_state.total_clauses_parsed == 12
    assert lg_state.untouched_clauses_count == 8
    assert lg_state.redlined_clauses_count == 4
    assert lg_state.status == "IN_SME_REVIEW"
    assert len(lg_state.active_conflicts) == 0

    lg_clauses = {c.clause_id: c for c in lg_state.clauses}
    assert lg_clauses["GP1-12"].sme_status == "APPROVED"
    assert lg_clauses["SP3-04"].sme_status == "APPROVED"
    assert lg_clauses["GP1-19"].sme_status == "PENDING"
    assert lg_clauses["SP5-03"].sme_status == "PENDING"
