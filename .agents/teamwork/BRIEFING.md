# Cymbal Aerospace CLM — Phase 2 Audit Remediation Briefing (`BRIEFING.md`)

## 1. Mission & Non-Negotiable Constraints
1. **NEVER run `git commit` or `git push`**: The user explicitly instructed: *"from now on, Dont push anything to git until I ask you to."*
2. **Build a Real Product, Never Build For a Demo (`AGENTS.md` Rule #1)**:
   - All 3 portfolio deals (`BA-2026-AV-8921` Apex AeroSystems FCC-900, `BA-2026-TR-5510` Vanguard Thrust Systems TRA-500, `BA-2026-LG-7740` Meridian Landing Gear TLG-800) must parse real golden `.docx` fixtures in `specs/04_golden_fixtures/` (`Vendor_Redlined_GP1.docx`, `Vanguard_Working_Review_TR5510.docx`, `Meridian_Working_Review_LG7740.docx`) and query live BigQuery (`vertex-ai-demos-468803.boeing_clm`).
   - **Never pre-create `.html` files on `reset` or `bake_demo.py`**: Only the skills (`clm-contract-intake`, `clm-tax-tariff-review`, `clm-contract-consolidation`) and live sidecar server may dynamically generate HTML when invoked for a specific deal (`--deal-id`). Keep each skill invocation focused strictly on the single deal the user asked about (no multi-deal switcher tab inside the single-deal HTML view).
3. **Frozen Specs (`specs/*`)**:
   - No `worker` may alter `specs/*` (`specs/01_bq_schema.sql`, `specs/02_domain_models.py`, `specs/03_mcp_and_rest_contract.md`, `specs/04_golden_fixtures/*`).

## 2. Strict File Ownership Matrix (Zero File Overlap)
- **`worker_bq_portfolio`**:
  - Allowed to edit: `setup_bigquery.py`, `sql/*`, `src/boeing_clm/storage/*`, `src/boeing_clm/intelligence/*`, `src/boeing_clm/server/*`, `src/boeing_clm/ui/index.html`, `tests/test_bigquery_and_conflicts.py`
- **`worker_ooxml_export`**:
  - Allowed to edit: `src/boeing_clm/ingestion/*`, `src/boeing_clm/export/*`, `tests/test_ingestion_and_export.py`
- **`worker_cli_sidecar_ui`**:
  - Allowed to edit: `skills/clm_cli.py`, `skills/cymbal_clm_seed.json`, `scripts/bake_demo.py`
