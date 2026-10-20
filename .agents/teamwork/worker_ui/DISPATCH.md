## 2026-10-16T18:13:00-05:00 — worker_ui
You are `worker_ui` (`worker` / `[ROLE: implementer]`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/ORIGINAL_REQUEST.md`
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- Reference UI design from Jetski: `/Users/rahulsankrut/Downloads/boeing_clm_experience_layer.html`
- Frozen specs:
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/02_domain_models.py` (or `from boeing_clm.models import ...`)
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/03_mcp_and_rest_contract.md`

### Strict Ownership Scope
- **Allowed to create/edit**:
  - `src/boeing_clm/server/__init__.py`
  - `src/boeing_clm/server/mcp_server.py`
  - `src/boeing_clm/server/api_server.py`
  - `src/boeing_clm/ui/index.html`
  - `skills/boeing-contract-intake/SKILL.md`
  - `skills/boeing-legal-ip-review/SKILL.md`
  - `skills/boeing-tax-tariff-review/SKILL.md`
  - `skills/boeing-eng-faa-review/SKILL.md`
  - `skills/boeing-contract-consolidation/SKILL.md`
  - `ARGOLIS_GEMINI_AGENT_SETUP.md`
  - `Dockerfile`
  - `deploy_cloud_run.sh`
  - `.agents/teamwork/worker_ui/handoff.md`
- **Forbidden to edit**: `specs/*`, `src/boeing_clm/ingestion/*`, `src/boeing_clm/export/*`, `src/boeing_clm/storage/*`, `src/boeing_clm/intelligence/*`.

### Mission & Technical Requirements
1. **FastMCP Server (`src/boeing_clm/server/mcp_server.py`)**:
   - Create `mcp = FastMCP("Boeing-CLM-Engine")` implementing the exact 6 tools in `specs/03_mcp_and_rest_contract.md`:
     1. `ingest_vendor_redline`
     2. `analyze_clause_precedents`
     3. `record_sme_position`
     4. `harmonize_clause_conflict`
     5. `export_counter_proposal_package`
     6. `reset_deal_workbench`
   - Calls `BigQueryCLMRepository` (`from boeing_clm.storage.repository import BigQueryCLMRepository`), `parse_redlined_docx` (`from boeing_clm.ingestion.docx_track_changes import parse_redlined_docx`), `generate_counter_proposal_docx` (`from boeing_clm.export.docx_generator import generate_counter_proposal_docx`), and `generate_deviation_matrix_xlsx` (`from boeing_clm.export.xlsx_generator import generate_deviation_matrix_xlsx`).
   - Also notify SSE subscribers in `api_server.py` whenever a state-mutating MCP tool runs so the browser UI updates in real time!

2. **FastAPI Server (`src/boeing_clm/server/api_server.py`)**:
   - Implement all 10 routes in `specs/03_mcp_and_rest_contract.md` plus `GET /` serving `src/boeing_clm/ui/index.html` and `GET /health`.
   - Mount the FastMCP HTTP/SSE app on `/mcp` (or expose `/mcp`) so Cloud Run serves both the Experience Layer UI (`/`, `/api/*`) and the MCP server (`/mcp`) from one container!

3. **Live 3-Stage Experience Layer UI (`src/boeing_clm/ui/index.html`)**:
   - Upgrade `/Users/rahulsankrut/Downloads/boeing_clm_experience_layer.html` into a **100% live, API-backed application** (zero hardcoded clause arrays in JS—all data fetched from `GET /api/deals/BA-2026-AV-8921` and updated via `POST /api/...`):
     - Preserve the executive dark aerospace aesthetic (`--bg-0: #060a12`, `--accent-blue: #3b82f6`, JetBrains Mono, 3-stage stepper).
     - Add a top utility bar with:
       - Live BigQuery connection pill (`vertex-ai-demos-468803.boeing_clm • text-embedding-005`)
       - **"Upload / Re-Ingest Vendor .docx"** button (`POST /api/deals/BA-2026-AV-8921/ingest`) showing the 12 parsed clauses (`8 untouched`, `4 material redlines`)
       - **"Reset Deal State"** button (`POST /api/deals/BA-2026-AV-8921/reset`)
     - **Tab 1 (`1. Intake & Redline Diff`)**: Filter toggle (`Redlined Clauses (4)` vs `All Contract Clauses (12)`), live `<w:del>` / `<w:ins>` diff view, vendor `<w:comment>` callout, and Microsoft Teams / SharePoint SME routing statuses.
     - **Tab 2 (`2. SME Precedent Explorer (BQ)`)**: Dynamic BigQuery `OutcomeDistribution` bar (`Held Firm %`, `Compromise Tier-1 %`, `Accepted Vendor Ask %` with `n=total_matches`), live `VECTOR_SEARCH` cosine similarity cards (`similarity_score`, `contract_id`, `supplier_name`, `boeing_program`, `final_agreed_language`), regulatory lockout alert banner (`FAA 14 CFR Part 21` / `DFARS 252.204-7012`), SME radio option selector + editable counter-proposal textarea, and **"Commit SME Position to BigQuery"** button (`POST /api/deals/BA-2026-AV-8921/clauses/{clause_id}/position`).
     - **Tab 3 (`3. Consolidation Cockpit`)**: Multi-SME readiness cards (`ENGINEERING`, `LEGAL`, `TAX`, `CYBER`), live **Cross-Clause Conflict Alert** (`SP3 §4.1` vs `GP1 §3.1` Firm-Fixed-Price SOW Cap) with one-click **"Apply Harmonized Cap in BigQuery"** button (`POST /api/deals/BA-2026-AV-8921/conflicts/{rule_id}/harmonize`), live Immutable SME Audit Trail feed (`recent_events`), and one-click download buttons for:
       - **Download Counter-Proposal `.docx` (Native Word Track Changes)** (`/api/deals/BA-2026-AV-8921/export/docx`)
       - **Download SharePoint Deviation Matrix `.xlsx` (4 Tabs)** (`/api/deals/BA-2026-AV-8921/export/xlsx`)
       - **Preview M365 Outlook Draft & SharePoint/Teams Dispatch** modal (`/api/deals/BA-2026-AV-8921/export/package`)
     - Connect `EventSource('/api/events')` so any update from Gemini Agent MCP automatically refreshes the UI and displays a toast notification!

4. **5 Single-File Gemini Agent `SKILL.md` Packages + Setup & Deployment**:
   - Create single-file `SKILL.md` files (with YAML frontmatter `name` and `description`, optimized for Gemini Agent Canvas + our FastMCP tools + M365 connectors `ms-sharepoint`, `ms-outlook`, `ms-onedrive`, `ms-teams`):
     - `skills/boeing-contract-intake/SKILL.md`
     - `skills/boeing-legal-ip-review/SKILL.md`
     - `skills/boeing-tax-tariff-review/SKILL.md`
     - `skills/boeing-eng-faa-review/SKILL.md`
     - `skills/boeing-contract-consolidation/SKILL.md`
   - Create `ARGOLIS_GEMINI_AGENT_SETUP.md`, `Dockerfile`, and `deploy_cloud_run.sh`.

### Verification Gate
Verify syntax and imports of `mcp_server.py` and `api_server.py` and record full details in `.agents/teamwork/worker_ui/handoff.md`.
