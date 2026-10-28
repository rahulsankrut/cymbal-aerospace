## 2026-10-21T21:10:00-05:00 — worker_cli_sidecar_ui
You are `worker_cli_sidecar_ui` (`worker`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/clm_comprehensive_audit_and_plan.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/scratch/audit_sidecar_arch_realness.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/scratch/audit_ui_ux_a11y.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/scratch/audit_legal_ooxml.md`
- `skills/clm_cli.py`, `scripts/bake_demo.py`

### Strict Ownership Scope
- **Allowed to edit**: `skills/clm_cli.py`, `skills/cymbal_clm_seed.json`, `scripts/bake_demo.py` (and syncing to `plugins/cymbal-aerospace-clm/` + `.agents/skills/` via `stage_1_reset_deal_and_sync_skills()`)
- **Forbidden to edit**: `specs/*`, `src/boeing_clm/*`, `tests/*`
- **Forbidden git commands**: NEVER run `git commit` or `git push`.

### Mission & Acceptance Criteria
1. **Never Pre-Create `.html` Files on `reset` / `bake_demo.py` (User `/grill-me` Decision 3)**:
   - In `cmd_reset` (`skills/clm_cli.py:6351-6378`), DO NOT call `generate_canvas_workbench_html(state)`! Instead, remove any stale `cymbal_clm_*.html` files in `Path.cwd()` and `Path.home() / "ge_spark_workspace"` during `reset` so zero `.html` files are pre-created on disk after baking.
   - Only when a skill command (`ingest`, `precedents`, `harmonize` / `resolve-conflict`, `consolidate`, `export`, `poll`, `render-widget`) or the live sidecar (`GET /?deal_id=...`) is invoked does `clm_cli.py` dynamically generate the HTML for the specific deal (`--deal-id`) the user asked about.
   - Keep each skill invocation's generated HTML strictly focused on the single deal the user asked about (do NOT add a multi-deal switcher tab inside the single-deal HTML view).

2. **Multi-Deal Real `.docx` Ingestion & Gemini Vertex AI ADC (`[P0-REAL-01]`, `[P0-REAL-03]`, `[P1-REAL-01]`)**:
   - In `build_deal_initial_state(deal_id)` and `parse_and_ingest_real_docx(deal_id, vendor_docx_path, baseline_docx_path)` (`skills/clm_cli.py:210-505`), eliminate Deal 1 `"FCC-900"` contamination in Deals 2 (`BA-2026-TR-5510`) and 3 (`BA-2026-LG-7740`) by parsing their real golden `.docx` fixtures (`specs/04_golden_fixtures/Vanguard_Working_Review_TR5510.docx` for `BA-2026-TR-5510` and `specs/04_golden_fixtures/Meridian_Working_Review_LG7740.docx` for `BA-2026-LG-7740`) via `boeing_clm.ingestion.docx_track_changes.parse_redlined_docx`, populating all 12 clauses with their genuine `TRA-500` and `TLG-800` baseline/redline/diff/comment text!
   - In `rewrite_clause_with_gemini()` (`skills/clm_cli.py:2245`), initialize `genai.Client(api_key=api_key)` when `GOOGLE_API_KEY` or `GEMINI_API_KEY` is set, otherwise `genai.Client(vertexai=True, project=os.environ.get("GOOGLE_CLOUD_PROJECT", GCP_PROJECT), location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"))` so live Gemini 2.5 Flash executes via Application Default Credentials.
   - In `fetch_live_precedents_map(state: Dict[str, Any], top_k: int = 16)` (`skills/clm_cli.py:591`), accept `top_k: int = 16` so `cmd_precedents` (`skills/clm_cli.py:6216`) never raises `TypeError`.

3. **Dual-Track Comments, Regex Sanitization, Surgical `<w:del>`/`<w:ins>` & Formula `.xlsx` in `skills/clm_cli.py` (`[P0-LEGAL-01..03]`, `[P1-LEGAL-01..06]`, `[P2-LEGAL-01..03]`)**:
   - In `RECOMMENDED_COUNTER_DEFAULTS` (`skills/clm_cli.py:92-198`) and `build_deal_initial_state`:
     - Add `external_justification` (`<75 words`, collegial commercial/regulatory justification with zero precedent `%`, zero `CONFLICT-`/`LOCKOUT-` IDs, zero walk-away floors, zero internal URLs) and `negotiation_analogy` (real-world analogy for live supplier calls per `explanations-for-redlines` skill) alongside internal `user_comment` / `sme_rationale`.
     - Remove `"or 1.5x ($78,000,000) floor"` from Deal 3 (`BA-2026-LG-7740`)'s `GP1-19` `selected_counter_text` (`skills/clm_cli.py:392-399`) so it proposes clean `2.0x ($104,000,000)` General Liability Cap with `2.5x ($130,000,000)` Super-Cap and never leaks Cymbal's internal walk-away floor!
   - In `_render_docx_bytes(state, apply_accepted_clean)` (`skills/clm_cli.py:727-895`):
     - Replace whole-paragraph `_append_del_run` + `_append_ins_run` with word-level surgical `<w:del>`/`<w:ins>` (`_append_surgical_tracked_diff`) using `difflib.SequenceMatcher` over `re.findall(r'\S+\s*|\s+', text)`.
     - When `apply_accepted_clean=False` (generating external `{deal_id}_Cymbal_Counter_Proposal.docx`):
       - Attribute all `<w:del>`, `<w:ins>`, and `<w:comment>` elements to `"Cymbal Aerospace Legal & Procurement"` (never individual SME names).
       - Write the sanitized `external_justification` into `word/comments.xml` (while keeping full SME names and precedent `%` inside `{deal_id}_Working_Review.docx` when `apply_accepted_clean=True`).
     - Add `<w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>` inside `<w:r>` wrapping `<w:commentReference>`, and strip emojis (`✅`, `⚠️`, `⏳`) from `Heading 2`.
   - In `assert_external_docx_sanitized(docx_path)` (`skills/clm_cli.py:990-1035`):
     - Enforce strict regex checks across both `word/document.xml` and `word/comments.xml` for internal precedent percentages (`\b\d+(?:\.\d+)?%\s*(?:precedent|held firm|compromise|tier-1|deals)\b`, `\(\d+\s*(?:of|/)\s*\d+\s*deals?\)`), internal rule IDs (`CONFLICT-`, `LOCKOUT-`), walk-away floors (`walk-away`, `\bfloor\b`), individual SME names (`Pradeep Gupta`, `Megan Bowen`, `Alex Wilber`, `Miriam Graham`, `Diego Siciliani`), and internal URLs (`boeing_clm`, `sharepoint.com`, `127.0.0.1`), and scrub `docProps/core.xml` `dc:creator` / `cp:lastModifiedBy` to `"Cymbal Aerospace Legal & Procurement"`.
   - In `build_fresh_docx_and_xlsx(state, out_dir)` (`skills/clm_cli.py:897-989`):
     - Upgrade the `.xlsx` generation to use real Excel formulas (`=COUNTA`, `=COUNTIF`, `=COUNTIFS`, `=IF`), banker font colors (`0000FF` blue inputs, `000000` black formulas, `008000` green cross-sheet links), proper number formats (`$#,##0`, `0.0%`), and add the 5th `5_Portfolio_Tabular_Review` worksheet.

4. **Sidecar Loopback Bridge Hardening (`[P0-SIDE-01..03]`)**:
   - In `serve_loopback_bridge` (`skills/clm_cli.py:5462-5848`):
     - Switch from `HTTPServer` to `ThreadingHTTPServer` (`from http.server import ThreadingHTTPServer`).
     - Parse `parsed_url = urllib.parse.urlparse(self.path)`, `clean_path = parsed_url.path`, and `qs = urllib.parse.parse_qs(parsed_url.query)` in both `do_GET` and `do_POST`.
     - Extract `deal_id` from `qs.get("deal_id", [None])[0]` (or JSON body `payload.get("deal_id")`) and pass it to `load_local_state(deal_id)` across all routes (`GET /`, `GET /api/state`, `GET /api/download/working-docx`, `GET /api/download/counter-docx`, `GET /api/download/matrix-xlsx`, `POST /api/review`, `POST /api/harmonize`, `POST /api/rewrite`).
     - Validate `ANTIGRAVITY_SIDECAR_UI_TOKEN` when set in `os.environ` (checking `qs.get("token")` or `X-Sidecar-Token` header or `Referer` containing `token=`).
     - Allowlist `POST /run` subcommands (`ingest`, `precedents`, `position`, `harmonize`, `resolve-conflict`, `poll`, `poll-inbox`, `consolidate`, `export`, `draft-vendor-reply`, `reset`, `render-widget`).

5. **Single-Deal HTML Template Fixes (`[P0-REAL-02]`, `[P0-UI-01..07]`, `[P1-UI-02..10]`)**:
   - In `generate_inline_triage_widget_html()` (`skills/clm_cli.py:4864-4906`):
     - Replace inline quote-interpolated `onclick="selectClause('${cid}', ...)"` and `onclick="applyDecision('${cid}', ...)"` with `data-clause-id="${cid}"` and `data-option-key="..."` + clean JS event listeners (`onclick="selectClause(this.dataset.clauseId)"` / `onclick="applyDecision(this.dataset.clauseId, this.dataset.optionKey)"`) so `.agents/skills/web-craft/scripts/validator.py` reports `0` errors!
   - In `generate_canvas_workbench_html()`:
     - Add `resolveActiveConflict(ruleId, sourceClauseId)` to `window.app` and wire the Conflict Banner button (`skills/clm_cli.py:3252`) to `onclick="window.app.resolveActiveConflict('${cf.rule_id}', '${cf.source_clause_id}')"` so clicking it on Deal 2 (`BA-2026-TR-5510`) calls `POST ${API_BASE}/api/harmonize` with `deal_id`, updates both `GP1-19` and `GP1-03` to `APPROVED` in `this.state.clauses`, clears `this.state.active_conflicts`, and re-renders cleanly!
     - Replace hardcoded Deal 1 strings (`BA-2026-AV-8921`, `$45,000,000`, `SP3-04`) in `renderPastelDependencyGraph()` (`skills/clm_cli.py:2884-2928`) and `renderPreConsolidationGate()` (`skills/clm_cli.py:3455-3512`) with dynamic `this.state.deal` values.
     - Add a collapsible **"Negotiation Analogy for Live Calls"** drawer (`explanations-for-redlines` skill) in the Playbook & Counter-Position Inspector tab displaying `clause.negotiation_analogy` (internal live-call talking points) alongside the sanitized external margin comment preview (`clause.external_justification`).
     - Make `.embedded-agent-dock` collapsible (`collapsed` class toggle button so on compact viewports `<= 820px` height it collapses to a `40px` bar, plus `padding-bottom: 84px` on `.right-copilot`) so it never occludes `.right-copilot`.
     - Enforce the `12px` minimum font floor across CSS rules (`9.5px–11.5px` → `12px`), and add GAR accessibility attributes (`role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`, `tabindex="0"` + `onkeydown` on clickable clause/matrix rows, `aria-label` on `<select>` and inputs, `aria-live="polite"` on `#toast`, and `:focus-visible` outline).

### Verification Gate
1. Run `stage_1_reset_deal_and_sync_skills()` via `python3 -c 'from scripts.bake_demo import stage_1_reset_deal_and_sync_skills; stage_1_reset_deal_and_sync_skills()'` and verify `ls *.html` shows NO pre-created `.html` files after reset!
2. Run a temporary validation check generating the workbench HTML and inline widget HTML to `/tmp/`, run `.agents/skills/web-craft/scripts/validator.py`, `.agents/skills/docx/scripts/validate.py`, `.agents/skills/xlsx/scripts/validate.py`, and `.agents/skills/xlsx/scripts/scan_errors.py`, and write the exact outputs to `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/worker_cli_sidecar_ui/handoff.md`.
