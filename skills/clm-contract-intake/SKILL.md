---
name: clm-contract-intake
description: Fetches Apex AeroSystems' redlined contract (`Vendor_Redlined_GP1.docx`), stores it in the Deal BA-2026-AV-8921 SharePoint folder alongside the Cymbal Standard (`Cymbal_GP1_Standard.docx`), compares all 12 clauses against the Cymbal Tier-1 Avionics Playbook (Preferred Standard, Pre-Approved Tier-1 Fallbacks, Regulatory Lockout Guardrails, and BigQuery historical precedents across all 4 redlined positions), identifies the 4 SME owners, initializes the Working Review Document (`BA-2026-AV-8921_Working_Review.docx`), and renders the interactive Word 365 & Playbook Reviewer UI in Spark Canvas. Pair with `clm-comms` to save/send the 4 SME routing emails in Microsoft Outlook.
---

# Cymbal Aerospace CLM — Contract Intake, Playbook Comparison & Document Reviewer UI (`clm-contract-intake`)

## 1. When to Activate
Activate this skill in **Workflow 1 (Contract Owner Intake & Playbook Evaluation)** whenever the user asks to:
- Check Adele Vance's inbound email for **Deal `BA-2026-AV-8921`** (*Apex AeroSystems — $45M FCC-900 Flight Control Computer Subsystem*) and upload the attached **`Vendor_Redlined_GP1.docx`** to SharePoint (`sites/CymbalAerospace/Shared Documents/BA-2026-AV-8921`),
- Compare the vendor markup against the **Cymbal Tier-1 Avionics Playbook** (which defines the Playbook Preferred Standard, Pre-Approved Tier-1 Fallback rules, Regulatory/Cross-Clause Lockouts, and BigQuery historical precedents across `64` Tier-1 Avionics deals),
- Identify the **4 SME Owners** (`Engineering`, `Legal`, `Tax`, `Cyber`), initialize the working review document (**`BA-2026-AV-8921_Working_Review.docx`**), and open the interactive **Word 365 & Playbook Reviewer UI** in Spark Canvas.

---

## 2. Step-by-Step Execution

### Option A — If the User Only Asks to Check Email & Upload the Redlined Contract to SharePoint (`upload-redline`)
If the user's prompt asks to check Adele Vance's email and upload `Vendor_Redlined_GP1.docx` to SharePoint (without yet asking to compare or open the workbench):

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py upload-redline --deal-id BA-2026-AV-8921
```
This locates Adele Vance's inbound email (`Vendor_Redlined_GP1.docx` & `Apex_AeroSystems_Redline_Transmittal_Memo.docx`), copies `Vendor_Redlined_GP1.docx` into the workspace, and uploads it live to SharePoint (`https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-AV-8921/Vendor_Redlined_GP1.docx`) alongside `Cymbal_GP1_Standard.docx`.

### Option B — Compare Against Cymbal Playbook & BigQuery Precedents and Open the Review Workbench (`ingest`)
When the user asks to compare the vendor redlined contract against our Cymbal Playbook / historical precedents and open the review UI:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py ingest --deal-id BA-2026-AV-8921
```

This command:
1. Ensures **`Vendor_Redlined_GP1.docx`** is uploaded to SharePoint alongside **`Cymbal_GP1_Standard.docx`**.
2. Parses all **12 clauses** (`8` untouched fast-tracked + `4` redlined exceptions: `GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) against the **Cymbal Tier-1 Avionics Playbook** and retrieves the **BigQuery historical precedent distribution** (`16` Tier-1 Avionics deals per position = `64` total deals).
3. Identifies the **4 SME Owners** (`Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`).
4. Initializes **`BA-2026-AV-8921_Working_Review.docx`** so any edits, approvals, or user comments submitted from the UI are immediately saved to the working review document.
5. Generates **`./cymbal_clm_redline_workbench.html`** in the current directory.

### Step 3 — Open the Interactive Reviewer UI in Spark Canvas (Mandatory When Running `ingest`)
Always open/render **`./cymbal_clm_redline_workbench.html`** in **Spark Canvas** (or provide the clickable artifact link `[Open Cymbal CLM Playbook Review Workbench](./cymbal_clm_redline_workbench.html)`).
