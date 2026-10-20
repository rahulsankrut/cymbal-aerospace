---
name: clm-contract-consolidation
description: Verifies BigQuery historical precedents across all 4 redlined positions (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`), consolidates all SME and Contract Owner positions and user comments from `BA-2026-AV-8921_Working_Review.docx` into the final `BA-2026-AV-8921_Cymbal_Counter_Proposal.docx` (with Word Track Changes `<w:ins>`/`<w:del>` and user-attributed `<w:comment>` margins) and `BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`, and updates the Reviewer UI in Spark Canvas.
---

# Cymbal Aerospace CLM — Precedent Verification & Final Counter-Proposal Consolidation (`clm-contract-consolidation`)

## 1. When to Activate
Activate this skill in **Workflow 4 (Contract Owner Precedent Check & Final Consolidation)** whenever the user asks to:
- Check historical precedents across all redlined positions (or verify the remaining `GP1 §19 & §24` Limitation of Liability & IP Indemnity position) using BigQuery (`vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`),
- Consolidate all SME and Contract Owner decisions and user comments from **`BA-2026-AV-8921_Working_Review.docx`** into the final Counter-Proposal Word document (**`BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`**) and 4-tab Deviation Matrix (**`BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`**).

*(Note: SharePoint upload and Outlook vendor reply emails are called explicitly as separate steps when requested by the user.)*

---

## 2. Step-by-Step Execution

### Step 1 — Verify Historical Precedents Across All 4 Positions (`precedents --clause-id ALL`)
When asked to check BigQuery precedents across all 4 redlined clauses (`64` total historical Tier-1 Avionics deals, `16` per clause):

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py precedents --deal-id BA-2026-AV-8921 --clause-id ALL
```

- **`GP1-12` (Engineering / FAA Quality):** `88%` (`14/16` deals) **Held Firm** on 36-Month Warranty & 24-Hr FAA Source Inspection.
- **`GP1-19` (Legal / Liability & IP):** `69%` (`11/16` deals) **Tier-1 Compromise** — `2.0x PO ($90,000,000) Super-Cap` with uncapped Airworthiness Directive (AD) recall & IP combination indemnity carveouts.
- **`SP3-04` (Global Tax / Tariffs):** `63%` (`10/16` deals) **Tier-1 Compromise** — `50/50 shared tariff adjustment above 5.0%`, capped at `+2.0% ($900,000)` of FFP SOW.
- **`SP5-03` (Cyber / DFARS 252.204-7012):** `94%` (`15/16` deals) **Held Firm** on mandatory 72-Hour Cyber Incident Reporting & 24-Hour Forensic Media Preservation.

### Step 2 — Generate the Final Consolidated `.docx` & `.xlsx` (`consolidate`)
When asked to consolidate all approved positions and comments into the final Word and Excel package:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py consolidate --deal-id BA-2026-AV-8921 --output-dir .
```

This command:
1. Consolidates all accepted/edited counter-positions and human user comments (`w:author="Megan Bowen"`, `w:author="Rahul Kasanagottu"`, `w:author="Pradeep Gupta"`, `w:author="Alex Wilber"` — never system comments) from **`BA-2026-AV-8921_Working_Review.docx`** into **`./BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`** and **`./BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`**.
2. Updates **`./cymbal_clm_redline_workbench.html`** in the current directory.

### Step 3 — Open the Updated Reviewer UI & Provide File Links (Mandatory)
1. Open **`./cymbal_clm_redline_workbench.html`** in **Spark Canvas**.
2. Provide clickable links to **`./BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`** and **`./BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`**.
