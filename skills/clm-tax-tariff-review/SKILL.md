---
name: clm-tax-tariff-review
description: Reviews Customs, Duties, and Section 232/301 Tariff pass-through redlines (`SP3 §4.1`) for Deal BA-2026-AV-8921, checks BigQuery historical Tax precedents (`16` Tier-1 Avionics deals, `63%` 50/50 split capped at `+2.0%` FFP), resolves the Cross-Clause Conflict against the `$45M` Firm-Fixed-Price SOW (`GP1 §3.1`), updates `BA-2026-AV-8921_Working_Review.docx` with the user's comment (`Pradeep Gupta`), and renders the interactive Document-Style Tax Reviewer UI in Spark Canvas. Pair with `clm-comms` (`send-sme-reply`) to email the SME update back to the Contract Owner's Outlook Inbox.
---

# Cymbal Aerospace CLM — Global Tax & Tariff SME Review (`clm-tax-tariff-review`)

## 1. When to Activate
Activate this skill in **Workflow 2 (SME Specialist Review — Second Spark Window)** whenever the user (acting as the Tax SME, `Pradeep Gupta`) asks to:
- Review the Customs, Duties, and Section 232/301 Tariff redline on **`SP3 §4.1`** for **Deal `BA-2026-AV-8921`**,
- Check historical Tier-1 Avionics Tax precedents in BigQuery (`vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`),
- Detect and harmonize the Cross-Clause Conflict between **`SP3 §4.1`** (*100% uncapped tariff pass-through >5%*) and **`GP1 §3.1`** (*`$45,000,000` Firm-Fixed-Price SOW ceiling*),
- Propose counter-language and save the Tax SME review comment to **`BA-2026-AV-8921_Working_Review.docx`**.

---

## 2. Step-by-Step Execution

### Step 1 — Run the Tax SME Review & Conflict Harmonization Engine (`tax-review`)
Execute:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py tax-review --deal-id BA-2026-AV-8921
```

This command:
1. Queries the **16 historical Tier-1 Avionics Tax precedents** in BigQuery (`63%` — `10/16` deals resolved with a **50/50 shared tariff adjustment above a 5.0% threshold, strictly capped at +2.0% / `$900,000` of FFP SOW**).
2. Harmonizes Cross-Clause Conflict **`CONFLICT-SP3-04-GP1-03`** against **`GP1 §3.1`** (`$45,000,000` Firm-Fixed-Price SOW).
3. Updates **`BA-2026-AV-8921_Working_Review.docx`** with the harmonized counter-position and a Word comment attributed directly to the human user (**`Pradeep Gupta`** — not a system comment).
4. Generates **`./cymbal_clm_tax_reviewer_workbench.html`** (the dedicated Tax SME Document-Style Reviewer UI) and updates **`./cymbal_clm_redline_workbench.html`**.

### Step 2 — Send the SME Review Update Email to the Contract Owner's Inbox via `clm-comms`
If the user also asks to send the Tax SME counter-proposal back to the Contract Owner via Outlook email, run:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py send-sme-reply --deal-id BA-2026-AV-8921
```

### Step 3 — Open the Interactive Document-Style Tax Reviewer UI in Spark Canvas (Mandatory)
Always open/render **`./cymbal_clm_tax_reviewer_workbench.html`** in **Spark Canvas** so the Tax Reviewer can inspect the inline Counter-Position change (orange-red strikethrough + coral highlight) and use the floating action menu (`✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, `💬 Comment` as `Pradeep Gupta`).
