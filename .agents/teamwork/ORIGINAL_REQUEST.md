# Original User Request (Immutable)

Boeing wanted our help in solving contract lifecycle management. The cycle goes something like Boeing has a proforma on the contract, they send it to vendor with that and some additional information.
The vendor makes some redlines and asks Boeing to change position. The Boeing owner works with various teams at Boeing like Legal, Tax, Engineering, Cyber, etc. to review their position. The owner or other entities research on past exceptions, positions, etc. and make manual updates or agree to the position. The owner consolidates and sends as response.

Key Requirements Locked via `/grill-me` and `/plan`:
1. **Pure Gemini Agent (Spark) + M365 Connectors in Argolis**: Use `vertex-ai-demos-468803` (`boeing_clm` dataset), established M365 connectors (`ms-sharepoint`, `ms-outlook`, `ms-onedrive`, `ms-teams`), 5 single-file `SKILL.md` skills for Canvas, and a unified FastMCP + FastAPI backend.
2. **Strict Live BigQuery Only (Zero Mock/Local Fallback)**: All vector search (`VECTOR_SEARCH` + `ML.GENERATE_EMBEDDING` with `text-embedding-005`), statistical distribution aggregations (`COUNTIF`), SME state persistence, and cross-clause conflict rules (`clause_conflict_rules`) run strictly against live BigQuery (`vertex-ai-demos-468803.boeing_clm`).
3. **Zero Backend LLM Calls**: Python backend is 100% deterministic (OOXML `.docx` parser, `.docx`/`.xlsx` exporters, BigQuery SQL/Vector Search, declarative conflict evaluator). All generative reasoning stays in Gemini Agent (Spark).
4. **Contract-First Spec-Driven Multi-Agent Build (`specs/`)**:
   - `specs/01_bq_schema.sql` (Database Contract)
   - `specs/02_domain_models.py` (Shared Pydantic v2 Contract with `ConfigDict(extra="forbid")`)
   - `specs/03_mcp_and_rest_contract.md` (Interface Contract)
   - `specs/04_golden_fixtures/` (`Boeing_GP1_Standard.docx`, `Vendor_Redlined_GP1.docx`, `expected_extracted_diffs.json`)
