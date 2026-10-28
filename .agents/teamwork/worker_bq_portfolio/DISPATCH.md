## 2026-10-21T21:10:00-05:00 — worker_bq_portfolio
You are `worker_bq_portfolio` (`worker`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/clm_comprehensive_audit_and_plan.md`
- Frozen specs: `specs/01_bq_schema.sql`, `specs/02_domain_models.py`, `specs/03_mcp_and_rest_contract.md`
- `setup_bigquery.py`, `src/boeing_clm/storage/repository.py`, `src/boeing_clm/intelligence/conflict_detector.py`, `src/boeing_clm/server/api_server.py`, `src/boeing_clm/ui/index.html`, `tests/test_bigquery_and_conflicts.py`

### Strict Ownership Scope
- **Allowed to edit**: `setup_bigquery.py`, `sql/*`, `src/boeing_clm/storage/*`, `src/boeing_clm/intelligence/*`, `src/boeing_clm/server/*`, `src/boeing_clm/ui/index.html`, `tests/test_bigquery_and_conflicts.py`
- **Forbidden to edit**: `specs/*`, `skills/*`, `scripts/*`, `src/boeing_clm/ingestion/*`, `src/boeing_clm/export/*`
- **Forbidden git commands**: NEVER run `git commit` or `git push`.

### Mission & Acceptance Criteria
1. **Seed All 3 Portfolio Deals & Conflict Rule into BigQuery (`[P0-REAL-01]`)**:
   - Update `setup_bigquery.py` and `src/boeing_clm/storage/repository.py` so that `active_deals` in `vertex-ai-demos-468803.boeing_clm` includes all 3 deals:
     - `BA-2026-AV-8921` (Apex AeroSystems, Tier-1 Avionics, 787 / 737-MAX Flight Control Display Units FCC-900, `$45,000,000`, status `INGESTED`)
     - `BA-2026-TR-5510` (Vanguard Thrust Systems Corp., Tier-1 Propulsion & Actuation, 777X / 787 Thrust Reverser Actuators TRA-500, `$38,000,000`, status `CONFLICT_DETECTED`)
     - `BA-2026-LG-7740` (Meridian Landing Gear Corp., Tier-1 Structural & Landing Gear, 787-10 Titanium Main Landing Gear Assemblies TLG-800, `$52,000,000`, status `IN_SME_REVIEW`)
   - Seed `CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL` (`CROSS_CLAUSE_CONFLICT` between `GP1-19` `LEGAL` and `GP1-03` `PROCUREMENT`) in `clause_conflict_rules` (and `src/boeing_clm/intelligence/conflict_detector.py` / `src/boeing_clm/storage/repository.py`) so that `repository.get_deal_workbench_state(deal_id)`, `repository.harmonize_clause_conflict(deal_id, rule_id, actor)`, and `repository.reset_deal_workbench(deal_id)` work cleanly for all 3 deals (`BA-2026-AV-8921`, `BA-2026-TR-5510`, `BA-2026-LG-7740`).
   - Run `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python setup_bigquery.py` to seed live BigQuery (`vertex-ai-demos-468803.boeing_clm`).
2. **Fix `src/boeing_clm/ui/index.html` DOM Target Errors (`[P0-UI-02]`)**:
   - In `src/boeing_clm/ui/index.html:834-840`, guard `document.getElementById('custom-counter-textarea')` with a null check (since it is dynamically rendered inside `active-clause-container`) and remove the dead `document.getElementById('precedent-bar')` lookup so `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python .agents/skills/web-craft/scripts/validator.py src/boeing_clm/ui/index.html` passes with `0` errors.
3. **Add Unit & Integration Tests (`tests/test_bigquery_and_conflicts.py`)**:
   - Add test coverage verifying `get_deal_workbench_state` and `reset_deal_workbench` for `BA-2026-AV-8921`, `BA-2026-TR-5510`, and `BA-2026-LG-7740`, and `harmonize_clause_conflict` for `CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL` on `BA-2026-TR-5510` (followed by resetting `BA-2026-TR-5510` back to its initial conflict state).

### Verification Gate
Run:
1. `"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" .agents/skills/web-craft/scripts/validator.py src/boeing_clm/ui/index.html`
2. `"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/pytest" tests/test_bigquery_and_conflicts.py -v`
and write the exact output to `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/worker_bq_portfolio/handoff.md`.
