# Challenger / Verifier Handoff (`challenger_m1`)

**Status:** `VERIFIED` (19 / 19 tests passed across the full test suite against live BigQuery `vertex-ai-demos-468803.boeing_clm`)

---

## 1. Deliverables Created

- `tests/test_end_to_end_adversarial.py` — Full end-to-end and adversarial verification suite covering:
  1. **FastAPI REST & UI Endpoints (`TestClient`)**:
     - `GET /health` — Verified Cloud Run probe returns `"ok"`, dataset `vertex-ai-demos-468803.boeing_clm`, and remote model `vertex-ai-demos-468803.boeing_clm.text_embedding_005`.
     - `GET /` — Verified live 3-Stage Experience Layer HTML UI renders with deal `BA-2026-AV-8921`, `Apex AeroSystems`, and `/api/deals/` hooks.
     - `POST /api/deals/BA-2026-AV-8921/reset` — Verified canonical workbench reset (`CONFLICT_DETECTED` with `CONFLICT-SP3-04-GP1-03`).
     - `GET /api/deals/BA-2026-AV-8921` — Verified full `DealWorkbenchState` with 12 clauses (`8` untouched, `4` redlined).
     - `POST /api/deals/BA-2026-AV-8921/ingest` — Verified multipart `.docx` upload (`Vendor_Redlined_GP1.docx`), `lxml` Track Changes extraction, BigQuery persistence, and `INGESTED_REDLINE` audit event logging.
     - `GET /api/deals/BA-2026-AV-8921/clauses/GP1-19/precedents` — Verified live BigQuery `VECTOR_SEARCH` (`COSINE`, `text_embedding_005`) and `COUNTIF` distribution (`16` matches: `4` held firm, `11` Tier-1 compromise, `1` accepted vendor).
     - `POST /api/deals/BA-2026-AV-8921/clauses/GP1-19/position` — Verified SME review submission (`compromise_tier_1`) updates BigQuery and returns `APPROVED` status on `GP1-19`.
     - `POST /api/deals/BA-2026-AV-8921/conflicts/CONFLICT-SP3-04-GP1-03/harmonize` — Verified conflict harmonization updates `SP3-04` to `custom_harmonized` (`APPROVED`), clears `active_conflicts`, and transitions deal to `READY_FOR_DISPATCH`.
     - `GET /api/deals/BA-2026-AV-8921/export/docx` — Verified binary `.docx` download contains `word/document.xml` (`4` `<w:ins>` and `4` `<w:del>` nodes) and `word/comments.xml`.
     - `GET /api/deals/BA-2026-AV-8921/export/xlsx` — Verified binary `.xlsx` download contains all 4 styled worksheets (`Executive Summary`, `Clause Sign-Off Matrix`, `BigQuery Precedents`, `Immutable Audit Trail`).
     - `GET /api/deals/BA-2026-AV-8921/export/package` — Verified JSON manifest with download URLs, byte sizes, Outlook draft (`ms-outlook`), and 4 M365 connector actions (`ms-sharepoint`, `ms-onedrive`, `ms-teams`, `ms-outlook`).
  2. **All 6 FastMCP Tools (`Boeing-CLM-Engine`)**:
     - Verified tool inventory via `mcp.list_tools()`: `ingest_vendor_redline`, `analyze_clause_precedents`, `record_sme_position`, `harmonize_clause_conflict`, `export_counter_proposal_package`, `reset_deal_workbench`.
     - Verified live execution of all 6 tools against `vertex-ai-demos-468803.boeing_clm`.
  3. **Adversarial Edge Cases & Governance Verification**:
     - **Strict Schema Validation (`ConfigDict(extra="forbid")`)**: Confirmed that passing unknown/extra fields to `SMEReviewSubmission` raises `pydantic.ValidationError` (`extra_forbidden`), and posting extra fields to `POST /api/deals/{deal_id}/clauses/{clause_id}/position` or `POST /api/deals/{deal_id}/conflicts/{rule_id}/harmonize` returns HTTP `422 Unprocessable Entity`.
     - **FAA 14 CFR Part 21 Regulatory Lockout (`GP1-12`)**: Confirmed that selecting `accept_vendor` on `GP1-12` triggers `LOCKOUT-GP1-12-FAA` (`rule_type="REGULATORY_LOCKOUT"`, `severity="REGULATORY_BLOCK"`), sets `GP1-12.sme_status="CONFLICT"`, and transitions deal status to `CONFLICT_DETECTED`.
     - **DFARS 252.204-7012 Regulatory Lockout (`SP5-03`)**: Confirmed that selecting `accept_vendor` on `SP5-03` triggers `LOCKOUT-SP5-03-DFARS` (`rule_type="REGULATORY_LOCKOUT"`, `severity="REGULATORY_BLOCK"`) and sets `SP5-03.sme_status="CONFLICT"`.
     - **Cross-Clause Conflict (`SP3-04` vs `GP1-03`)**: Confirmed that selecting `accept_vendor` on `SP3-04` triggers `CONFLICT-SP3-04-GP1-03` (`rule_type="CROSS_CLAUSE_CONFLICT"`, `source_clause_id="SP3-04"`, `target_clause_id="GP1-03"`), and calling `harmonize_clause_conflict` resolves it cleanly to `READY_FOR_DISPATCH`.
     - **Canonical State Restoration**: Finished by invoking `reset_deal_workbench("BA-2026-AV-8921")` so the live BigQuery dataset is left in its clean canonical starting state.

---

## 2. Complete Pytest Output (`/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/pytest -v`)

```text
============================= test session starts ==============================
platform darwin -- Python 3.13.12, pytest-9.1.1, pluggy-1.6.0 -- /Users/rahulsankrut/Desktop/code/boeing/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/rahulsankrut/Desktop/code/boeing
configfile: pyproject.toml
testpaths: tests
plugins: platformdirs-4.12.4, asyncio-1.4.0, anyio-4.15.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 19 items

tests/test_bigquery_and_conflicts.py::test_bigquery_seeded_tables_and_768_dim_embeddings PASSED [  5%]
tests/test_bigquery_and_conflicts.py::test_live_vector_search_and_outcome_distribution[GP1-12-True-14-2-0] PASSED [ 10%]
tests/test_bigquery_and_conflicts.py::test_live_vector_search_and_outcome_distribution[GP1-19-False-4-11-1] PASSED [ 15%]
tests/test_bigquery_and_conflicts.py::test_live_vector_search_and_outcome_distribution[SP3-04-False-5-10-1] PASSED [ 21%]
tests/test_bigquery_and_conflicts.py::test_live_vector_search_and_outcome_distribution[SP5-03-True-15-1-0] PASSED [ 26%]
tests/test_bigquery_and_conflicts.py::test_initial_workbench_state_and_cross_clause_conflict PASSED [ 31%]
tests/test_bigquery_and_conflicts.py::test_regulatory_lockout_detection_and_conflict_harmonization_lifecycle PASSED [ 36%]
tests/test_bigquery_and_conflicts.py::test_save_extracted_clauses_and_reset_workbench PASSED [ 42%]
tests/test_end_to_end_adversarial.py::test_fastmcp_registered_tool_inventory PASSED [ 47%]
tests/test_end_to_end_adversarial.py::test_fastapi_health_and_experience_layer_ui_routes PASSED [ 52%]
tests/test_end_to_end_adversarial.py::test_adversarial_extra_fields_rejected_by_strict_contract_model PASSED [ 57%]
tests/test_end_to_end_adversarial.py::test_fastapi_routes_end_to_end_lifecycle PASSED [ 63%]
tests/test_end_to_end_adversarial.py::test_fastmcp_tools_and_adversarial_lockout_and_conflict_flows PASSED [ 68%]
tests/test_ingestion_and_export.py::test_parse_vendor_redlined_docx_matches_golden_snapshot_100_percent PASSED [ 73%]
tests/test_ingestion_and_export.py::test_parse_boeing_baseline_docx_all_untouched PASSED [ 78%]
tests/test_ingestion_and_export.py::test_fallback_section_number_alignment_without_metadata_headers PASSED [ 84%]
tests/test_ingestion_and_export.py::test_compute_untracked_diff_html PASSED [ 89%]
tests/test_ingestion_and_export.py::test_generate_counter_proposal_docx_track_changes_and_comments PASSED [ 94%]
tests/test_ingestion_and_export.py::test_generate_deviation_matrix_xlsx_four_worksheets PASSED [100%]

======================== 19 passed in 241.45s (0:04:01) ========================
```
