# `specs/03_mcp_and_rest_contract.md` — Cymbal Aerospace CLM Interface & Skill Contract

## 1. FastMCP Tool Signatures (`/mcp`)

All FastMCP tools validate inputs and outputs using `specs/02_domain_models.py` and execute against `vertex-ai-demos-468803.boeing_clm`.

### Tool 1: `ingest_vendor_redline`
- **Signature:**
  ```python
  def ingest_vendor_redline(
      deal_id: str = "BA-2026-AV-8921",
      vendor_docx_path: str = "specs/04_golden_fixtures/Vendor_Redlined_GP1.docx",
      baseline_docx_path: str = "specs/04_golden_fixtures/Cymbal_GP1_Standard.docx",
  ) -> dict:
  ```
- **Contract:** Parses the 12-clause `.docx` files via `boeing_clm.ingestion.docx_track_changes`, validates each clause against `ExtractedClauseDiff` (`8` untouched, `4` redlined), updates `boeing_clm.deal_clause_deviations`, logs `INGESTED_REDLINE` in `boeing_clm.sme_review_events`, and returns `DealWorkbenchState.model_dump()`.

### Tool 2: `analyze_clause_precedents`
- **Signature:**
  ```python
  def analyze_clause_precedents(
      clause_id: str,
      vendor_redline_text: str = "",
      supplier_tier: str = "Tier-1 Avionics",
      top_k: int = 5,
  ) -> dict:
  ```
- **Contract:** Executes live BigQuery `VECTOR_SEARCH` (`COSINE` distance with `boeing_clm.text_embedding_005`) against `boeing_clm.historical_clause_exceptions` (`64` Tier-1 Avionics deals, `16` per redlined clause) plus SQL `COUNTIF` outcome distribution aggregation, returning `PrecedentSearchResult.model_dump()`.

### Tool 3: `record_sme_position`
- **Signature:**
  ```python
  def record_sme_position(
      deal_id: str,
      clause_id: str,
      sme_team: str,
      selected_option_key: str,
      selected_counter_text: str,
      sme_reviewer: str,
      sme_rationale: str,
  ) -> dict:
  ```
- **Contract:** Validates via `SMEReviewSubmission`, updates `boeing_clm.deal_clause_deviations`, appends to `boeing_clm.sme_review_events` with human user attribution (`sme_reviewer`), runs `conflict_detector` against `boeing_clm.clause_conflict_rules`, triggers SSE notify, and returns `DealWorkbenchState.model_dump()`.

### Tool 4: `harmonize_clause_conflict`
- **Signature:**
  ```python
  def harmonize_clause_conflict(
      deal_id: str = "BA-2026-AV-8921",
      rule_id: str = "CONFLICT-SP3-04-GP1-03",
      actor: str = "Pradeep Gupta",
  ) -> dict:
  ```
- **Contract:** Looks up `harmonized_resolution_text` from `boeing_clm.clause_conflict_rules`, updates the conflicting clause (`SP3-04`) to `APPROVED` with `selected_option_key="custom_harmonized"`, logs `CONFLICT_HARMONIZED` to `boeing_clm.sme_review_events`, triggers SSE notify, and returns `DealWorkbenchState.model_dump()`.

### Tool 5: `export_counter_proposal_package`
- **Signature:**
  ```python
  def export_counter_proposal_package(
      deal_id: str = "BA-2026-AV-8921",
  ) -> dict:
  ```
- **Contract:** Generates:
  1. Counter-proposal `.docx` (`BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`) with native Word `<w:del>`/`<w:ins>` Track Changes and human-user-attributed `<w:comment>` rationales (`w:author="Megan Bowen"`, `w:author="Rahul Kasanagottu"`, `w:author="Pradeep Gupta"`, `w:author="Alex Wilber"` — never system comments) across all 12 clauses,
  2. Working Review `.docx` (`BA-2026-AV-8921_Working_Review.docx`) where accepted clauses have their accepted text applied cleanly in `word/document.xml` plus user comments in `word/comments.xml`,
  3. 4-tab SharePoint Deviation Matrix `.xlsx` (`Executive Summary`, `Clause Sign-Off Matrix`, `BigQuery Precedents`, `Immutable SME Audit Trail`).

### Tool 6: `reset_deal_workbench`
- **Signature:**
  ```python
  def reset_deal_workbench(
      deal_id: str = "BA-2026-AV-8921",
  ) -> dict:
  ```
- **Contract:** Resets `boeing_clm.deal_clause_deviations` for `BA-2026-AV-8921` to the canonical initial workbench state, triggers SSE notify, and returns `DealWorkbenchState.model_dump()`.

---

## 2. Cloud Run FastAPI REST Routes (`/api/*`)

| Method & Route | Request Body / Params | Response Payload |
| :--- | :--- | :--- |
| `GET /api/deals/{deal_id}` | Path: `deal_id` | `DealWorkbenchState` (JSON) |
| `POST /api/deals/{deal_id}/ingest` | Optional multipart `file` (`.docx`), defaults to `Vendor_Redlined_GP1.docx` | `DealWorkbenchState` (JSON) |
| `GET /api/deals/{deal_id}/clauses/{clause_id}/precedents` | Path: `deal_id`, `clause_id` | `PrecedentSearchResult` (JSON) |
| `POST /api/deals/{deal_id}/clauses/{clause_id}/position` | Body: `SMEReviewSubmission` | `DealWorkbenchState` (JSON) |
| `POST /api/deals/{deal_id}/conflicts/{rule_id}/harmonize` | Optional Body: `{"actor": str}` | `DealWorkbenchState` (JSON) |
| `POST /api/deals/{deal_id}/reset` | None | `DealWorkbenchState` (JSON) |
| `GET /api/deals/{deal_id}/export/docx` | Path: `deal_id` | Binary `.docx` download |
| `GET /api/deals/{deal_id}/export/xlsx` | Path: `deal_id` | Binary `.xlsx` download |
| `GET /api/deals/{deal_id}/export/package` | Path: `deal_id` | JSON manifest with download URLs + Outlook draft + M365 actions |
| `GET /api/events` | None | `text/event-stream` (Server-Sent Events broadcasting state updates) |

---

## 3. Focused Cymbal Aerospace CLM Skills (`skills/*/SKILL.md` & `skills/clm_cli.py`)

| Skill Name | CLI Subcommand(s) | Purpose |
| :--- | :--- | :--- |
| **`clm-contract-intake`** | `ingest` | Uploads `Vendor_Redlined_GP1.docx` to SharePoint alongside `Cymbal_GP1_Standard.docx`, compares all 12 clauses with BigQuery historical precedents (`64` deals across 4 positions), identifies the 4 SME owners, initializes `BA-2026-AV-8921_Working_Review.docx`, and renders the interactive Document-Style Counter-Position Reviewer UI (`./cymbal_clm_redline_workbench.html`). |
| **`clm-comms`** | `route-smes [--send]`, `send-sme-reply`, `poll-inbox`, `draft-vendor-reply [--send]` | Dedicated Microsoft Outlook communications skill via Microsoft Graph (`m365-admin@rahulsankrut.demo.altostrat.com`). Keeps Outlook `Drafts` at `0` after `Bake CLM demo` so Spark creates/sends the 4 SME routing drafts, SME reply emails, Inbox polling updates, and final vendor reply draft live during the demo. |
| **`clm-tax-tariff-review`** | `tax-review`, `harmonize` | Reviews `SP3 §4.1` (Customs, Duties & Section 232/301 Tariffs), checks the 16 BigQuery Tax precedents (`63%` 50/50 split capped at `+2%` FFP), harmonizes `CONFLICT-SP3-04-GP1-03` against `GP1 §3.1` (`$45M` FFP SOW), writes `Pradeep Gupta`'s user comment to `BA-2026-AV-8921_Working_Review.docx`, and renders `./cymbal_clm_tax_reviewer_workbench.html`. |
| **`clm-contract-consolidation`** | `precedents --clause-id ALL`, `consolidate`, `export` | Verifies BigQuery historical precedents across all 4 positions (`GP1-12` `88%` Held Firm, `GP1-19` `69%` 2x PO Super-Cap, `SP3-04` `63%` 50/50 Shared Cap, `SP5-03` `94%` Held Firm), consolidates `BA-2026-AV-8921_Working_Review.docx` into `BA-2026-AV-8921_Cymbal_Counter_Proposal.docx` and `BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx` with human user comments, and uploads both live to SharePoint. |

---

## 4. Host Loopback Bridge & Interactive Document Reviewer API (`http://127.0.0.1:58921`)

| Method & Route | Purpose |
| :--- | :--- |
| `GET /health` | Health check (`{"status": "ok"}`) with CORS headers (`Access-Control-Allow-Origin: *`). |
| `POST /run` | Executes `clm_cli.py` on the host when called from inside a sandboxed Spark session so Microsoft Graph (Outlook & SharePoint) and Cloud Run calls always succeed. |
| `POST /api/review` | Receives live Document-Style Reviewer UI actions (`✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, `💬 Comment`), updates `cymbal_clm_state.json`, applies accepted changes cleanly to `BA-2026-AV-8921_Working_Review.docx` (`[✓ ACCEPTED BY <User>]` in `word/document.xml`), writes the human user's comment (`w:author="<User>"`) to `word/comments.xml`, and syncs the `.docx` files to SharePoint in the background. |
| `GET /api/download/working-docx` | Serves the live `BA-2026-AV-8921_Working_Review.docx` binary file (with accepted changes applied and user comments attached) directly to the browser. |
| `GET /api/download/counter-docx` | Serves the live `BA-2026-AV-8921_Cymbal_Counter_Proposal.docx` binary file (with full Word Track Changes against the vendor redline and user comments attached). |
