# Teamwork Briefing — Boeing CLM on Gemini Agent (Spark)

## 1. Mission
Build and verify the production-grade Boeing CLM backend, OOXML `.docx`/`.xlsx` engine, live BigQuery Vector Search & Cross-Clause Conflict engine, unified FastMCP + FastAPI server, live 3-Stage Experience Layer UI, and 5 Gemini Agent `SKILL.md` packages in `/Users/rahulsankrut/Desktop/code/boeing`.

## 2. Frozen Specifications (DO NOT MODIFY)
No worker subagent may modify any file inside `specs/`:
- `specs/01_bq_schema.sql` — Canonical BigQuery DDL in `vertex-ai-demos-468803.boeing_clm`.
- `specs/02_domain_models.py` (also re-exported via `src/boeing_clm/models.py`) — Strict Pydantic v2 models with `ConfigDict(extra="forbid")`.
- `specs/03_mcp_and_rest_contract.md` — Exact FastMCP tool signatures and FastAPI routes.
- `specs/04_golden_fixtures/` — `Boeing_GP1_Standard.docx`, `Vendor_Redlined_GP1.docx` (12 clauses: 8 untouched, 4 redlined), and `expected_extracted_diffs.json`.

## 3. Global Invariants
1. **Zero Mock / Zero Local Fallback**: Every database query MUST execute against live BigQuery (`vertex-ai-demos-468803.boeing_clm`). Never catch exceptions to return fake in-memory data.
2. **Zero Backend LLM Calls**: All backend logic is strictly deterministic (`lxml` OOXML parsing, SQL + `VECTOR_SEARCH`, declarative `clause_conflict_rules` evaluation).
3. **Zero File Overlap**: Each parallel `worker` subagent may ONLY create or edit files inside its assigned ownership paths.
4. **Resource Attribution**: Any `gcloud` CLI command must prepend `CLOUDSDK_METRICS_ENVIRONMENT="${CLOUDSDK_METRICS_ENVIRONMENT:+$CLOUDSDK_METRICS_ENVIRONMENT }datacloud.antigravity"`, and any supported `bq` CLI mutation/query must include `--label datacloud:antigravity`.
5. **Python Environment**: Use `/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/python` and `/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/pytest`.
