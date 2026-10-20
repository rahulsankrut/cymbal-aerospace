## 2026-10-16T18:13:00-05:00 — worker_bq
You are `worker_bq` (`worker` / `[ROLE: implementer]`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/ORIGINAL_REQUEST.md`
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- Frozen specs:
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/01_bq_schema.sql`
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/02_domain_models.py` (or `from boeing_clm.models import ...`)
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/04_golden_fixtures/expected_extracted_diffs.json`

### Strict Ownership Scope
- **Allowed to create/edit**:
  - `sql/02_seed_data.sql`
  - `sql/03_vector_search_queries.sql`
  - `setup_bigquery.py`
  - `src/boeing_clm/storage/__init__.py`
  - `src/boeing_clm/storage/repository.py`
  - `src/boeing_clm/intelligence/__init__.py`
  - `src/boeing_clm/intelligence/precedent_engine.py`
  - `src/boeing_clm/intelligence/conflict_detector.py`
  - `tests/test_bigquery_and_conflicts.py`
  - `.agents/teamwork/worker_bq/handoff.md`
- **Forbidden to edit**: `specs/*`, `src/boeing_clm/ingestion/*`, `src/boeing_clm/export/*`, `src/boeing_clm/server/*`, `src/boeing_clm/ui/*`.

### Mission & Technical Requirements
1. **Seed Live BigQuery (`vertex-ai-demos-468803.boeing_clm`) via `setup_bigquery.py` & `sql/02_seed_data.sql`**:
   - Populate `proforma_clauses` with all 12 canonical clauses (`GP1-01`, `GP1-03`, `GP1-05`, `GP1-07`, `GP1-09`, `GP1-12`, `GP1-15`, `GP1-19`, `GP1-28`, `SP3-02`, `SP3-04`, `SP5-03`) including realistic `standard_text`, `fallback_tier_1_text` (Boeing Playbook Tier-1 Compromise), `fallback_tier_2_text`, `regulatory_lockout` (`TRUE` for `GP1-12` FAA 14 CFR Part 21 and `SP5-03` DFARS 252.204-7012; `FALSE` for others), `regulatory_citation`, and `guardrail_summary`.
   - Populate `historical_clause_exceptions` with **64 realistic historical precedent rows** across `GP1-12` (16 rows: e.g. 14 `HELD_FIRM`, 2 `COMPROMISE_TIER_1`, 0 `ACCEPTED_VENDOR`), `GP1-19` (16 rows: e.g. 4 `HELD_FIRM`, 11 `COMPROMISE_TIER_1`, 1 `ACCEPTED_VENDOR`), `SP3-04` (16 rows: e.g. 5 `HELD_FIRM`, 10 `COMPROMISE_TIER_1`, 1 `ACCEPTED_VENDOR`), and `SP5-03` (16 rows: e.g. 15 `HELD_FIRM`, 1 `COMPROMISE_TIER_1`, 0 `ACCEPTED_VENDOR`) across real aerospace suppliers (`Honeywell Aerospace`, `Collins Aerospace`, `Safran Landing Systems`, `Spirit AeroSystems`, `Thales Avionics`, `BAE Systems`, `Moog Aircraft Group`, `Parker Aerospace`, `L3Harris`, `Meggitt`, `GKN Aerospace`, `Curtiss-Wright`, etc.) and programs (`787`, `737-MAX`, `777X`, `BDS`).
   - Run `ML.GENERATE_EMBEDDING` using `MODEL \`vertex-ai-demos-468803.boeing_clm.text_embedding_005\`` in BigQuery so every row in `proforma_clauses` and `historical_clause_exceptions` has a live `768`-dimensional `embedding` vector in BigQuery!
   - Seed `clause_conflict_rules` with:
     - `CONFLICT-SP3-04-GP1-03` (`CROSS_CLAUSE_CONFLICT`, `source_clause_id='SP3-04'`, `target_clause_id='GP1-03'`, `source_sme_team='TAX'`, `target_sme_team='PROCUREMENT'`, `trigger_option_keys=['accept_vendor']`, `forbidden_patterns=['exceeding five percent (5%)', 'passed through 100%', 'uncapped']`, `required_patterns=['capped at a maximum aggregate adjustment of 2.0%']`, `severity='CRITICAL_CONFLICT'`, `conflict_title='Cross-Clause Conflict: SP3 §4.1 Tariff Pass-Through Violates GP1 §3.1 Firm-Fixed-Price SOW Cap'`, `conflict_description='Global Tax approved a >5% Section 232/301 tariff surcharge pass-through on SP3 §4.1, which directly violates Procurement Firm-Fixed-Price SOW Cap in GP1 §3.1 ($45M ceiling).'`, `harmonized_option_key='custom_harmonized'`, `harmonized_resolution_text='4.1 All unit prices are DDP Boeing Everett/Renton facility. Any verified new Section 232/301 tariff increase exceeding 5.0% on raw titanium forgings or semiconductor wafers shall be shared 50/50 between Boeing and Seller, strictly capped at a maximum aggregate adjustment of 2.0% of the GP1 §3.1 Firm-Fixed-Price SOW unit price.'`)
     - `LOCKOUT-GP1-12-FAA` (`REGULATORY_LOCKOUT` on `GP1-12` when `accept_vendor` is selected or `thirty (30) days prior written notice` is retained, citing `FAA 14 CFR Part 21.140 / AS9100 Rev D mandatory unannounced right of access`).
     - `LOCKOUT-SP5-03-DFARS` (`REGULATORY_LOCKOUT` on `SP5-03` when `accept_vendor` is selected or `ten (10) business days` is retained, citing `DoD DFARS 252.204-7012 mandatory 72-hour cyber incident reporting`).
   - Seed `active_deals`, `deal_clause_deviations` (from `specs/04_golden_fixtures/expected_extracted_diffs.json`, with initial state where `GP1-12` is `APPROVED` (`hold_firm`), `GP1-19` is `APPROVED` (`compromise_tier_1`), `SP5-03` is `APPROVED` (`hold_firm`), and `SP3-04` is in `CONFLICT` (`accept_vendor`) so the cross-clause conflict between Tax and Procurement is immediately live and inspectable!), and `sme_review_events`.

2. **Required Public Interface (`src/boeing_clm/storage/repository.py`)**:
   ```python
   class BigQueryCLMRepository:
       def __init__(self, project_id: str = GCP_PROJECT_ID, dataset: str = BQ_DATASET): ...
       def get_deal_workbench_state(self, deal_id: str = "BA-2026-AV-8921", include_precedents: bool = True) -> DealWorkbenchState: ...
       def save_extracted_clauses(self, deal_id: str, diffs: list[ExtractedClauseDiff], source_surface: str = "GEMINI_AGENT_MCP") -> DealWorkbenchState: ...
       def search_clause_precedents(self, clause_id: str, vendor_redline_text: str = "", supplier_tier: str = "Tier-1 Avionics", top_k: int = 5) -> PrecedentSearchResult: ...
       def record_sme_submission(self, submission: SMEReviewSubmission) -> DealWorkbenchState: ...
       def harmonize_conflict(self, deal_id: str = "BA-2026-AV-8921", rule_id: str = "CONFLICT-SP3-04-GP1-03", actor: str = "Lead Contract Owner (M. Vance)", source_surface: str = "EXPERIENCE_LAYER_UI") -> DealWorkbenchState: ...
       def reset_deal_workbench(self, deal_id: str = "BA-2026-AV-8921", source_surface: str = "EXPERIENCE_LAYER_UI") -> DealWorkbenchState: ...
   ```
   - `search_clause_precedents` (delegating to `precedent_engine.py`) MUST run live BigQuery SQL using `VECTOR_SEARCH` (or cosine similarity with `ML.GENERATE_EMBEDDING` on `boeing_clm.text_embedding_005`) and compute `OutcomeDistribution` (`total_matches`, `held_firm_count`, `held_firm_pct`, `compromise_tier_1_count`, `compromise_tier_1_pct`, `accepted_vendor_count`, `accepted_vendor_pct`) dynamically via SQL `COUNTIF`!
   - Remember: Add job label `labels={"datacloud": "antigravity"}` in `bigquery.QueryJobConfig` for all queries!

### Verification Gate
Run `/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/python setup_bigquery.py` and `/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/pytest tests/test_bigquery_and_conflicts.py -v` and paste the exact output in `.agents/teamwork/worker_bq/handoff.md`.
