---
name: clm-tax-tariff-review
description: Reviews Customs, Duties, and Section 232/301 Tariff redlines (SP3 §4.1), queries BigQuery Tax precedents, detects and harmonizes cross-clause conflicts with the Firm-Fixed-Price SOW ceiling (GP1 §3.1), records the Tax SME's user-attributed Word comment into the Working Review .docx, and renders the Tunneled + Full-12-Clause Tax Reviewer UI in Spark Canvas.
---

# Cymbal Aerospace CLM — Global Tax & Tariff SME Review (`clm-tax-tariff-review`)

Use this skill when the Global Tax & Trade Compliance SME (or user) reviews the **Customs, Duties & Section 232/301 Tariffs** redline (`SP3-04` / `SP3 §4.1`), checks historical Tax/Tariff precedents in BigQuery, resolves cross-clause pricing conflicts against the Firm-Fixed-Price SOW ceiling (`GP1 §3.1`), and opens the **Tax SME Reviewer UI** in Canvas.

> **Single-Responsibility Boundary**: This skill evaluates the Tax/Tariff clause (`SP3-04`), harmonizes its cross-clause conflict, updates `<deal_id>_Working_Review.docx`, and renders `cymbal_clm_tax_reviewer_workbench.html`. Do **NOT** automatically send or draft Outlook emails or upload files to SharePoint inside this skill. If the user subsequently asks to email the Tax SME review reply to the Contract Owner, use `clm-comms`.

---

## Step 1 — Run the Tax & Tariff SME Review Script

Execute `scripts/tax_review.py`:

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-tax-tariff-review/scripts/tax_review.py \
  --deal-id BA-2026-AV-8921 \
  --actor "Pradeep Gupta"
```

*(Fallback path if running directly from the repository root: `python3 skills/clm-tax-tariff-review/scripts/tax_review.py --deal-id BA-2026-AV-8921 --actor "Pradeep Gupta"`)*

### What the Script Computes Live:
1. **Cross-Clause Conflict Harmonization**: Evaluates `CONFLICT-SP3-04-GP1-03` between `SP3 §4.1` (Tariffs) and `GP1 §3.1` (Firm-Fixed-Price SOW ceiling) and applies the harmonized counter-position (`cross_clause_conflict_resolved`).
2. **Live BigQuery Tax Precedent Search**: Queries `boeing_clm.historical_clause_exceptions` for `SP3-04` (`bigquery_tax_precedents`) to return the live outcome distribution (`distribution`) and top historical supplier matches (`precedents`).
3. **Working Review `.docx` Update**: Saves the harmonized counter-language and the Tax SME's comment (`w:author` set to `--actor`) into `<deal_id>_Working_Review.docx`.
4. **Tunneled + Full-Context Tax Reviewer UI**: Generates `cymbal_clm_tax_reviewer_workbench.html` in the current working directory, featuring both the **🎯 Tunneled Tax View (`SP3 §4.1` Focus)** and **📄 Full 12-Clause Contract Context** (`⚡ Inspect GP1 §3.1` + `Jump to Clause` selector).

---

## Step 2 — Present the Live Tax & Tariff Review Summary

Using the JSON output returned by `scripts/tax_review.py`:
1. **Cross-Clause Conflict Analysis**:
   - Report the conflict rule (`cross_clause_conflict_resolved.rule_id`), the conflicting SOW clause (`conflicting_clause`), and `resolution_status`.
2. **Live BigQuery Tax Precedents**:
   - Report the live distribution from `bigquery_tax_precedents.distribution` (`total_matches`, `compromise_tier_1_pct`, `held_firm_pct`, `accepted_vendor_pct`) and summarize the top historical supplier matches from `bigquery_tax_precedents.precedents`.
3. **Harmonized Counter-Language & Working `.docx` Attribution**:
   - Quote `cross_clause_conflict_resolved.harmonized_counter_language` verbatim and confirm that the comment was recorded in `working_review_docx` under `w:author` = `comment_author_user`.
4. **Open the Tax SME Reviewer UI (Antigravity Sidecar + Spark Canvas)**:
   - Output the clickable Antigravity Sidecar pills `[Cymbal Tax & Tariff Review](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/tax-workbench)` and `[Cymbal CLM Workbench](sidecar://cymbal-aerospace-clm/cymbal-clm-workbench/)` alongside the Spark Canvas file link `[cymbal_clm_tax_reviewer_workbench.html](cymbal_clm_tax_reviewer_workbench.html)` so the reviewer can inspect `SP3 §4.1` in Tunneled Focus or expand Playbook guidance, BigQuery precedents, and the full 12-clause contract on demand.
