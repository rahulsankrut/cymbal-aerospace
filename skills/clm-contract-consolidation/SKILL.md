---
name: clm-contract-consolidation
description: Queries BigQuery historical precedents across redlined positions, records SME or Contract Owner review positions and user-attributed Word comments into the Working Review .docx, and consolidates all approved positions into the final Counter-Proposal .docx (with OOXML Track Changes <w:ins>/<w:del> and <w:comment> margins) and 4-Tab SharePoint Deviation Matrix .xlsx.
---

# Cymbal Aerospace CLM — Precedent Verification & Contract Consolidation (`clm-contract-consolidation`)

Use this skill when the Contract Owner or reviewer asks to:
1. Verify BigQuery historical precedents for a specific clause (e.g., `GP1-19`) or across all redlined clauses (`ALL`).
2. Record a review decision (`hold_firm`, `compromise_tier_1`, `accept_vendor`, or `custom_counter`) and a human-attributed Word comment (`w:author`) into `<deal_id>_Working_Review.docx`.
3. Consolidate all recorded positions and comments from `<deal_id>_Working_Review.docx` into the final `<deal_id>_Cymbal_Counter_Proposal.docx` and `<deal_id>_SharePoint_Deviation_Matrix.xlsx`.

> **Single-Responsibility Boundary**: This skill performs BigQuery precedent verification, Working Review `.docx` position recording, and local `.docx` + `.xlsx` package generation ONLY. Do **NOT** auto-upload files to SharePoint or auto-draft/send Outlook emails inside this skill. Uploading to SharePoint (via the SharePoint connector) or drafting/sending the vendor reply email (via `clm-comms`) must only occur when explicitly requested by the user.

---

## Step 1 — Verify BigQuery Precedents (`scripts/precedents.py`)

To inspect live BigQuery `VECTOR_SEARCH` precedents for a specific clause (e.g., `GP1-19`) or across all redlined positions (`ALL`):

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-consolidation/scripts/precedents.py \
  --deal-id BA-2026-AV-8921 \
  --clause-id ALL
```

*(Or pass `--clause-id GP1-19` to focus on a single clause.)*

---

## Step 2 — Record a Clause Position & User Comment (`scripts/record_position.py`)

When a reviewer or Contract Owner approves or updates a counter-position for a clause (or when syncing an SME decision into `<deal_id>_Working_Review.docx`):

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-consolidation/scripts/record_position.py \
  --deal-id BA-2026-AV-8921 \
  --clause-id GP1-19 \
  --sme-team LEGAL \
  --option compromise_tier_1 \
  --counter-text "<approved_counter_language>" \
  --reviewer "Rahul Kasanagottu" \
  --rationale "<reviewer_word_comment>"
```

This updates the clause state, writes the accepted change and `<w:comment w:author="...">` into `<deal_id>_Working_Review.docx`, and refreshes `cymbal_clm_redline_workbench.html`.

---

## Step 2B — Resolve Cross-Department Conflict in the Working Review `.docx` (`scripts/resolve_conflict.py`)

When the Contract Owner inspects the Stage 2 middle-stage contract (`Deal BA-2026-TR-5510` — Vanguard Thrust Systems Corp.) where **Finance (`Diego Siciliani` in `GP1 §3.1`)** and **Legal (`Miriam Graham` in `GP1 §19`)** have recorded conflicting edits in `BA-2026-TR-5510_Working_Review.docx` (Finance traded a lower `1.0x` Liability Cap for a `3.5%` unit-price discount, while Legal requires a minimum `1.5x` Liability Cap with zero cap-for-discount trade-offs), and the Owner rules that **Legal takes precedence**:

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-consolidation/scripts/resolve_conflict.py \
  --deal-id BA-2026-TR-5510 \
  --actor "Rahul Kasanagottu"
```

This resolves `CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL` in favor of Legal (`1.5x` Liability Cap enforced in `GP1-19` and standard `$38M` Firm-Fixed-Price restored in `GP1-03`), updates `BA-2026-TR-5510_Working_Review.docx`, and refreshes `cymbal_clm_redline_workbench.html`.

---

## Step 3 — Consolidate the Final `.docx` & `.xlsx` Package (`scripts/consolidate.py`)

When the user asks to consolidate a contract (such as Stage 3 `Deal BA-2026-LG-7740` — Meridian Landing Gear Corp., or `BA-2026-AV-8921`) into the final Word Counter-Proposal and Excel Deviation Matrix:

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-contract-consolidation/scripts/consolidate.py \
  --deal-id BA-2026-LG-7740 \
  --output-dir . \
  --approve-recommended
```

*(Pass `--deal-id BA-2026-LG-7740` for Doc 3 Meridian Landing Gear, `--deal-id BA-2026-TR-5510` for Doc 2 Vanguard Thrust Systems, or `--deal-id BA-2026-AV-8921` for Doc 1 Apex AeroSystems.)*

### What `scripts/consolidate.py` Produces:
1. **`<deal_id>_Working_Review.docx`**: Clean working contract with accepted changes applied in-place and user-attributed `<w:comment>` margins.
2. **`<deal_id>_Cymbal_Counter_Proposal.docx`**: Official external redlined Word contract with native OOXML `<w:del>`, `<w:ins>`, and `<w:comment>` balloons attributed to each human reviewer, verified by `assert_external_docx_sanitized()` so zero internal playbook markers leak externally.
3. **`<deal_id>_SharePoint_Deviation_Matrix.xlsx`**: 4-tab Excel workbook (`Executive Summary`, `Clause Sign-Off Matrix`, `BigQuery Precedents`, `Immutable Audit Trail`).
4. **`cymbal_clm_redline_workbench.html`**: Refreshed interactive Reviewer UI in the current working directory.

---

## Step 4 — Present the Consolidation Summary

Using the live JSON output from the scripts:
1. Report `status`, `approved_redlined_clauses_count`, and `pending_redlined_clauses_count`.
2. Present a summary table of the redlined clauses showing each clause's final status, selected option, reviewer name (`w:author`), and counter-language.
3. Provide clickable Markdown links to:
   - `[Cymbal CLM Workbench](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/)` and `[Cymbal Tax & Tariff Review](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/tax-workbench)` (Antigravity Sidecar pills)
   - `[cymbal_clm_redline_workbench.html](cymbal_clm_redline_workbench.html)` (to open the Reviewer UI in Spark Canvas)
   - `[<deal_id>_Working_Review.docx](<deal_id>_Working_Review.docx)`
   - `[<deal_id>_Cymbal_Counter_Proposal.docx](<deal_id>_Cymbal_Counter_Proposal.docx)`
   - `[<deal_id>_SharePoint_Deviation_Matrix.xlsx](<deal_id>_SharePoint_Deviation_Matrix.xlsx)`
