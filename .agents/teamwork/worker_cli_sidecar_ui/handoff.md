# Handoff Report: `worker_cli_sidecar_ui`

## Executive Summary

All 5 mission tasks in `DISPATCH.md` have been implemented and verified in `skills/clm_cli.py`, `scripts/bake_demo.py`, and synced across `plugins/cymbal-aerospace-clm/`, `.agents/skills/`, `.agents/plugins/`, `~/.gemini/config/plugins/`, and `~/ge_spark_workspace/`:

1. **Task 1 (`reset` & `bake_demo.py` Zero Pre-Created `.html` Files)**:
   - Removed `generate_canvas_workbench_html(state)` from `cmd == "reset"` in `skills/clm_cli.py`.
   - Added automatic cleanup of any stale `cymbal_clm_*.html` / `*.html` files in `Path.cwd()`, `ROOT`, and `~/ge_spark_workspace` during `clm_cli.py reset` and `bake_demo.py:stage_1_reset_deal_and_sync_skills()`.
   - Added the `render-widget` CLI subcommand (`clm_cli.py render-widget --deal-id <ID> [--output-path <PATH>]`) so the main agent can generate a fresh inline triage widget on demand.

2. **Task 2 (`clm_cli.py` Multi-Deal Fidelity, Precedents `top_k=16` & Live Gemini Rewrite)**:
   - Added `_adapt_text_for_deal()` and `_adapt_obj_for_deal()` + `_overlay_golden_docx_onto_clauses()` so Deals 2 (`BA-2026-TR-5510` / `Vanguard Propulsion Systems` / `TRA-500` / `$38,000,000`) and 3 (`BA-2026-LG-7740` / `Meridian Landing Gear Systems` / `TLG-800` / `$52,000,000`) parse `specs/04_golden_fixtures/Vanguard_Working_Review_TR5510.docx` and `specs/04_golden_fixtures/Meridian_Working_Review_LG7740.docx` via `parse_redlined_docx(..., baseline_docx_path=None)` with zero `"FCC-900"` or `"$45,000,000"` string contamination.
   - Removed the contradictory `"or 1.5x ($78,000,000) floor"` phrase from Deal 3's `GP1-19` counter text so it matches `Meridian_Working_Review_LG7740.docx` (`$104,000,000 (2.0x Total PO Value)`).
   - Updated `fetch_live_precedents_map(state_or_deal_id, clauses_opt=None, top_k=16)` to default to `top_k=16`, pass `top_k=top_k` and deal-specific `supplier_tier` into `search_redlined_clauses_parallel`, and key `_LIVE_PRECEDENTS_CACHE` by `(deal_id, top_k)`.
   - Updated `rewrite_clause_with_gemini()` to default `call_live_gemini: bool = True`, check `GOOGLE_API_KEY` / `GEMINI_API_KEY` first then fall back to `genai.Client(vertexai=True, project=..., location=...)`, and wrap `user_instruction` inside `<user_negotiation_guidance>...</user_negotiation_guidance>`.

3. **Task 3 (Surgical Word-Level `.docx` Tracked Changes, Dual-Track Sanitization & 5-Tab `.xlsx` Matrix)**:
   - Implemented `_append_surgical_tracked_diff()` using `difflib.SequenceMatcher` on word tokens so `<w:del>` and `<w:ins>` wrap only changed spans while unchanged words sit in normal `<w:r>` runs.
   - Enforced dual-track attribution:
     - Internal `{deal_id}_Working_Review.docx` preserves individual SME author names (`Megan Bowen`, `Miriam Graham`, `Pradeep Gupta`, `Alex Wilber`, `Diego Siciliani`, `Rahul Kasanagottu`) and internal audit notes.
     - External `{deal_id}_Cymbal_Counter_Proposal.docx` sets `w:author="Cymbal Aerospace Legal & Procurement"` and `w:initials="CA"` on all `<w:ins>`, `<w:del>`, and `<w:comment>` elements, sets `doc.core_properties.author = "Cymbal Aerospace Legal & Procurement"`, omits the internal SharePoint URL row, and sanitizes comment text via `sanitize_external_comment_text()`.
   - Added `<w:rStyle w:val="CommentReference"/>` on the `<w:r>` wrapping `<w:commentReference>`, removed emojis from `Heading 2`, and set `tbl.autofit = False` with explicit column widths across all Word tables.
   - Expanded `assert_external_docx_sanitized()` with all 7 regex checks across `word/document.xml`, `word/comments.xml`, and `docProps/core.xml`, plus sanitized `create_outlook_vendor_counter_draft()`.
   - Upgraded `{deal_id}_SharePoint_Deviation_Matrix.xlsx` to 5 tabs (`Executive Summary`, `Clause Sign-Off Matrix`, `BigQuery Precedents`, `Immutable Audit Trail`, `5_Portfolio_Tabular_Review`) with live Excel formulas (`=COUNTA`, `=COUNTIF`, `=COUNTIFS`, `=IF`), materialized `<v>` cached values in `xl/worksheets/sheet1.xml`, banker color coding (blue `#0000FF` inputs, black `#000000` same-sheet formulas, green `#008000` cross-sheet links), explicit currency/percentage formats, and landscape fit-to-1-page-wide print setup.

4. **Task 4 (Sidecar Loopback Bridge Multi-Deal Query Routing, `ThreadingHTTPServer`, `POST /api/harmonize`, Security)**:
   - Switched `serve_loopback_bridge()` to `ThreadingHTTPServer(("127.0.0.1", port), BridgeHandler)`.
   - Parsed `clean_path` and `qs` in `do_GET` and `do_POST`, routing `?deal_id=` across `/`, `/workbench`, `/tax-workbench`, `/inline-widget`, `/api/state`, `/api/download/working-docx`, `/api/download/counter-docx`, and `/api/download/matrix-xlsx`.
   - Added `POST /api/harmonize` and updated `POST /api/review` to return updated `deal` and `clauses` maps so the sidecar UI updates in-place without full-page reloads.
   - Enforced `ANTIGRAVITY_SIDECAR_UI_TOKEN` validation when set and allowlisted `POST /run` CLI subcommands.

5. **Task 5 (Sidecar Workbench, Tax Workbench & Inline Widget Design/Validator Compliance)**:
   - Added `<meta name="artifact-type" content="tool" />` and `<meta name="design-style" content="briefing" />` to all 3 HTML generators.
   - Raised all sub-12px CSS font sizes to `>= 12px`, added `max-inline-size: 72ch` on `.doc-clause-body`, added `:focus-visible` outlines and ARIA roles (`role="tablist"`, `role="tab"`, `aria-selected`, `aria-live="polite"`), and replaced hardcoded `http://127.0.0.1:58921` links with relative `/preload.js` and `/api/download/...` paths.
   - Added collapsible `.embedded-agent-dock.collapsed`, `resolveActiveConflict()`, negotiation analogy drawer, dynamic deal strings across all 4 surface tabs (`DOC_REVIEW`, `COMPARE_3COL`, `GRAPH_VIEW`, `WATERFALL_CHECK`), and safe `data-*` attributes + `applyDecision()` in `generate_inline_triage_widget_html()`.

---

## Validator Results

- `.agents/skills/web-craft/scripts/validator.py`: **EXIT 0 (0 errors)** across `wb_*.html`, `tax_*.html`, and `widget_*.html` for all 3 deals.
- `.agents/skills/docx/scripts/validate.py`: **EXIT 0 (`OK: ... valid`)** across `{deal_id}_Working_Review.docx` and `{deal_id}_Cymbal_Counter_Proposal.docx` for all 3 deals.
- `.agents/skills/xlsx/scripts/validate.py` & `scan_errors.py`: **EXIT 0 (`OK: ... valid`, `{"errors": [], "count": 0}`)** across `{deal_id}_SharePoint_Deviation_Matrix.xlsx` for all 3 deals.
- Post-reset HTML check: **0 `.html` files** in repo root or `~/ge_spark_workspace` after `stage_1_reset_deal_and_sync_skills()`.
