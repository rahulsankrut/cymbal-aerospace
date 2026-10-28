## 2026-10-21T21:10:00-05:00 — worker_ooxml_export
You are `worker_ooxml_export` (`worker`).

### Must Read First
- `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/BRIEFING.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/clm_comprehensive_audit_and_plan.md`
- `/Users/rahulsankrut/.gemini/antigravity/brain/54fb2f32-4fa5-4786-94de-957e5c70549f/scratch/audit_legal_ooxml.md`
- `.agents/skills/explanations-for-redlines/SKILL.md`, `.agents/skills/playbook-sanitization/SKILL.md`, `.agents/skills/tabular-review/SKILL.md`, `.agents/skills/docx/SKILL.md`, `.agents/skills/xlsx/SKILL.md`
- `src/boeing_clm/export/docx_generator.py`, `src/boeing_clm/export/xlsx_generator.py`, `tests/test_ingestion_and_export.py`

### Strict Ownership Scope
- **Allowed to edit**: `src/boeing_clm/ingestion/*`, `src/boeing_clm/export/*`, `tests/test_ingestion_and_export.py`
- **Forbidden to edit**: `specs/*`, `skills/*`, `scripts/*`, `src/boeing_clm/storage/*`, `src/boeing_clm/intelligence/*`, `src/boeing_clm/server/*`
- **Forbidden git commands**: NEVER run `git commit` or `git push`.

### Mission & Acceptance Criteria
1. **Upgrade `src/boeing_clm/export/docx_generator.py` (`[P0-LEGAL-01]`, `[P0-LEGAL-02]`, `[P1-LEGAL-01]`, `[P1-LEGAL-03]`, `[P2-LEGAL-01..03]`)**:
   - **Word-Level Surgical `<w:del>` / `<w:ins>` Diff (`_append_surgical_tracked_diff`)**:
     - Instead of striking the entire vendor paragraph and inserting the entire counter paragraph as two monolithic runs, tokenize `vendor_text` and `counter_text` with `re.findall(r'\S+\s*|\s+', text)` and use `difflib.SequenceMatcher(None, vendor_tokens, counter_tokens, autojunk=False).get_opcodes()`:
       - `"equal"` → emit regular `<w:r><w:t xml:space="preserve">`
       - `"delete"` → emit `<w:del>`
       - `"insert"` → emit `<w:ins>`
       - `"replace"` → emit `<w:del>` followed by `<w:ins>`
   - **External Counter-Proposal Sanitization & Dual-Track Comments**:
     - In `generate_counter_proposal_docx()`, attribute all `<w:del>`, `<w:ins>`, and `<w:comment>` elements in the external counter-proposal `.docx` to `"Cymbal Aerospace Legal & Procurement"` (never individual SME names like `"Pradeep Gupta"`, `"Megan Bowen"`, `"Alex Wilber"`, `"Miriam Graham"`, or `"Diego Siciliani"`).
     - Sanitize the external `<w:comment>` text written into `word/comments.xml` (`sanitize_counterparty_comment(clause)`): maximum `<75 words`, collegial commercial/regulatory justification, stripping any internal BigQuery precedent percentages (`\b\d+(?:\.\d+)?%\s*(?:precedent|held firm|compromise|tier-1|deals)\b` or `\(\d+\s*(?:of|/)\s*\d+\s*deals?\)`), internal conflict/lockout rule IDs (`CONFLICT-`, `LOCKOUT-`), internal walk-away floors (`floor`, `walk-away`), and internal URLs (`boeing_clm`, `sharepoint.com`, `127.0.0.1`).
   - **OOXML Compliance**:
     - Add `<w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>` inside the `<w:r>` wrapping `<w:commentReference>` (`[P2-LEGAL-01]`).
     - Strip any emojis (`✅`, `⚠️`, `⏳`) from `Heading 2` text (`[P2-LEGAL-03]`).
2. **Upgrade `src/boeing_clm/export/xlsx_generator.py` (`[P1-LEGAL-04..06]`, `xlsx` & `tabular-review` skills)**:
   - Replace hardcoded summary counts on `1_Executive_Summary` with real Excel formulas (`=COUNTA('2_Clause_Deviation_Matrix'!A2:A13)`, `=COUNTIF('2_Clause_Deviation_Matrix'!F2:F13,"YES")`, `=COUNTIF('2_Clause_Deviation_Matrix'!F2:F13,"NO")`, `=COUNTIFS('2_Clause_Deviation_Matrix'!F2:F13,"YES",'2_Clause_Deviation_Matrix'!G2:G13,"APPROVED")`, `=COUNTA('3_Cross_Clause_Conflict_Log'!A2:A20)`).
   - Add a `Total Matched Precedents` column on `4_BigQuery_Precedent_Benchmarks` using `=SUM(E2:G2)` (or `=C2+D2+E2` matching the Held Firm / Compromise / Accepted Vendor columns).
   - Apply institutional number formats (`$#,##0`, `0.0%`, `0.0"x"`) and banker font color coding (`0000FF` blue for hardcoded numeric inputs, `000000` black for same-sheet formulas, `008000` green for cross-sheet formula links).
   - Add a 5th worksheet `5_Portfolio_Tabular_Review` (`tabular-review` skill) with one row per deal (`BA-2026-AV-8921`, `BA-2026-TR-5510`, `BA-2026-LG-7740`), columns for `Deal ID`, `Supplier`, `Program`, `Value ($ USD)`, and each of the 4 key negotiated clauses (`GP1 §12.2 Warranty & FAA Inspection`, `GP1 §19 Limitation of Liability`, `SP3 §4.1 Customs & Tariffs`, `SP5 §3.2 DFARS Cyber Reporting`) showing `[Status] | Position | Verbatim Counter-Language`, plus a bottom summary row using live `=SUM(...)` and `=COUNTIF(...)` formulas.
3. **Update `tests/test_ingestion_and_export.py`**:
   - Add unit tests verifying:
     - `parse_redlined_docx` parses all 3 golden fixtures (`Vendor_Redlined_GP1.docx`, `Vanguard_Working_Review_TR5510.docx`, `Meridian_Working_Review_LG7740.docx`) with 12 clauses each and zero `"FCC-900"` contamination in `TR5510` or `LG7740`.
     - `generate_counter_proposal_docx` passes `.agents/skills/docx/scripts/validate.py`, produces word-level surgical `<w:del>`/`<w:ins>` alongside regular `<w:r>` runs, and contains zero internal SME names, precedent percentages, or `CONFLICT-`/`LOCKOUT-` strings in `word/comments.xml`.
     - `generate_deviation_matrix_xlsx` produces real `=` formulas, includes `5_Portfolio_Tabular_Review`, and passes `.agents/skills/xlsx/scripts/recalc_pure_python.py`, `.agents/skills/xlsx/scripts/scan_errors.py` (`status == "clean"`), and `.agents/skills/xlsx/scripts/validate.py`.

### Verification Gate
Run:
`"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/pytest" tests/test_ingestion_and_export.py -v`
and write the exact output to `/Users/rahulsankrut/Desktop/code/boeing/.agents/teamwork/worker_ooxml_export/handoff.md`.
