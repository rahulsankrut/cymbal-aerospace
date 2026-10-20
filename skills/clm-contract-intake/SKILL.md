---
name: clm-contract-intake
description: Compares Apex AeroSystems' redlined contract (`Vendor_Redlined_GP1.docx`) against the Cymbal Tier-1 Avionics Playbook (`Cymbal_GP1_Standard.docx` — Preferred Standard, Pre-Approved Tier-1 Fallbacks, Regulatory Lockout Guardrails, and BigQuery historical precedents across all 4 redlined positions), identifies the 4 SME owners, initializes the Working Review Document (`BA-2026-AV-8921_Working_Review.docx`), and renders the interactive Word 365 & Playbook Reviewer UI in Spark Canvas.
---

# Cymbal Aerospace CLM — Contract Intake, Playbook Comparison & Document Reviewer UI (`clm-contract-intake`)

## 1. When to Activate
Activate this skill in **Workflow 1 (Contract Playbook Evaluation)** whenever the user asks to:
- Compare the vendor redlined contract (**`Vendor_Redlined_GP1.docx`**) against the **Cymbal Tier-1 Avionics Playbook** (which defines the Playbook Preferred Standard, Pre-Approved Tier-1 Fallback rules, Regulatory/Cross-Clause Lockouts, and BigQuery historical precedents across `64` Tier-1 Avionics deals),
- Identify the **4 SME Owners** (`Engineering`, `Legal`, `Tax`, `Cyber`), initialize the working review document (**`BA-2026-AV-8921_Working_Review.docx`**), and open the interactive **Word 365 & Playbook Reviewer UI** in Spark Canvas.

*(Note: Do NOT use this skill just to upload files to SharePoint or send Outlook emails — SharePoint uploads and Outlook routing are called explicitly as separate steps.)*

---

## 2. Step-by-Step Execution

### Step 1 — Run the CLM Playbook Comparison Engine (`ingest`)
Run the following command in your current working directory:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py ingest --deal-id BA-2026-AV-8921
```

This command:
1. Parses all **12 clauses** (`8` untouched fast-tracked + `4` redlined exceptions: `GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) against the **Cymbal Tier-1 Avionics Playbook** and retrieves the **BigQuery historical precedent distribution** (`16` Tier-1 Avionics deals per position = `64` total deals).
2. Identifies the **4 SME Owners** (`Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`).
3. Initializes **`BA-2026-AV-8921_Working_Review.docx`** so any edits, approvals, or user comments submitted from the UI are immediately saved to the working review document.
4. Generates **`./cymbal_clm_redline_workbench.html`** in the current directory.

### Step 2 — Open the Interactive Reviewer UI in Spark Canvas (Mandatory)
Always open/render **`./cymbal_clm_redline_workbench.html`** in **Spark Canvas** (or provide the clickable artifact link `[Open Cymbal CLM Playbook Review Workbench](./cymbal_clm_redline_workbench.html)`).
