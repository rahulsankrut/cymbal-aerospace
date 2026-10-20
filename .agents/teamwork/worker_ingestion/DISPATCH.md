## 2026-10-16T18:13:00-05:00 — worker_ingestion
You are `worker_ingestion` (`worker` / `[ROLE: implementer]`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/ORIGINAL_REQUEST.md`
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- Frozen specs:
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/02_domain_models.py` (or `from boeing_clm.models import ...`)
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/04_golden_fixtures/build_golden_fixtures.py`
  - `/Users/rahulsankrut/Desktop/code/boeing/specs/04_golden_fixtures/expected_extracted_diffs.json`

### Strict Ownership Scope
- **Allowed to create/edit**:
  - `src/boeing_clm/ingestion/__init__.py`
  - `src/boeing_clm/ingestion/docx_track_changes.py`
  - `src/boeing_clm/ingestion/clause_segmenter.py`
  - `src/boeing_clm/ingestion/diff_engine.py`
  - `src/boeing_clm/export/__init__.py`
  - `src/boeing_clm/export/docx_generator.py`
  - `src/boeing_clm/export/xlsx_generator.py`
  - `tests/test_ingestion_and_export.py`
  - `.agents/teamwork/worker_ingestion/handoff.md`
- **Forbidden to edit**: `specs/*`, `src/boeing_clm/storage/*`, `src/boeing_clm/intelligence/*`, `src/boeing_clm/server/*`, `src/boeing_clm/ui/*`.

### Required Public Function Signatures (Exact Contract for Server Integration)
1. `src/boeing_clm/ingestion/docx_track_changes.py`:
   ```python
   def parse_redlined_docx(docx_path: str | Path) -> list[ExtractedClauseDiff]:
   ```
   - Must parse `word/document.xml` and `word/comments.xml` inside the `.docx` zip archive using `lxml.etree` (NOT regex on plain text).
   - Must extract Heading 2 metadata headers (`[clause_id] clause_ref — clause_title | SME_TEAM=... | OWNER=... | RISK=... | REG=...`) via `clause_segmenter.py`, and if a generic `.docx` without metadata tags is uploaded, gracefully align by section numbers (`12.2`, `19`, `4.1`, `3.2`, etc.).
   - Must reconstruct `boeing_baseline_text` (regular `<w:r><w:t>` + `<w:del><w:r><w:delText>`), `vendor_redline_text` (regular `<w:r><w:t>` + `<w:ins><w:r><w:t>`), `insertions`, `deletions`, `vendor_comments` (linked via `w:commentRangeStart` / `word/comments.xml`), `diff_html` (`<span class="diff-del">...</span>` and `<span class="diff-add">...</span>` via `diff_engine.py`), and `has_redline` (`True` if insertions or deletions exist, `False` if untouched).
   - When run on `specs/04_golden_fixtures/Vendor_Redlined_GP1.docx`, `[d.model_dump() for d in parse_redlined_docx(...)]` MUST match `specs/04_golden_fixtures/expected_extracted_diffs.json` 100% (12 clauses total: 8 untouched, 4 redlined)!

2. `src/boeing_clm/export/docx_generator.py`:
   ```python
   def generate_counter_proposal_docx(state: DealWorkbenchState, output_path: str | Path) -> Path:
   ```
   - Must generate a complete 12-clause `.docx` contract with:
     - Executive Summary header & metadata table for `state.deal_id` (`state.vendor_name`, `state.contract_value_usd`, `state.status`).
     - All 12 clauses in order. For redlined clauses (`has_redline=True`), inject **real Word Track Changes XML nodes** (`<w:del>` containing `clause.vendor_redline_text` if rejected/modified and `<w:ins>` authored by `"Boeing CLM Counter-Proposal"` containing `clause.selected_counter_text`), plus inject `word/comments.xml` containing each SME's `clause.sme_rationale` linked via `<w:commentRangeStart>` / `<w:commentRangeEnd>` / `<w:commentReference>`!

3. `src/boeing_clm/export/xlsx_generator.py`:
   ```python
   def generate_deviation_matrix_xlsx(state: DealWorkbenchState, output_path: str | Path) -> Path:
   ```
   - Must use `openpyxl` to build a styled 4-worksheet SharePoint Deviation Matrix `.xlsx`:
     - Sheet 1: `Executive Summary` (Deal metadata, clause counts, conflict status, M365 SharePoint link)
     - Sheet 2: `Clause Sign-Off Matrix` (All 12 clauses, SME Team, Risk Level, Regulatory Flag, Baseline, Vendor Redline, Selected Counter-Position, SME Status, Reviewer)
     - Sheet 3: `BigQuery Precedents` (Outcome distribution % and top historical precedent citations for each redlined clause)
     - Sheet 4: `Immutable Audit Trail` (All `state.recent_events`)

### Verification Gate
Run `/Users/rahulsankrut/Desktop/code/boeing/.venv/bin/pytest tests/test_ingestion_and_export.py -v` and record the exact output in `.agents/teamwork/worker_ingestion/handoff.md`.
