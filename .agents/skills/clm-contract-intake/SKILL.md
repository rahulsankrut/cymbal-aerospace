---
name: clm-contract-intake
description: Fetches Apex AeroSystems' redlined contract (`Vendor_Redlined_GP1.docx`), stores it in the Deal BA-2026-AV-8921 SharePoint folder alongside the Cymbal Proforma (`Cymbal_GP1_Standard.docx`), compares all 12 clauses with BigQuery historical precedents across all 4 redlined positions, identifies the 4 SME owners, initializes the Working Review Document (`BA-2026-AV-8921_Working_Review.docx`), and renders the interactive Document-Style Redline & Counter-Position Reviewer UI in Spark Canvas. Pair with `clm-comms` to save/send the 4 SME routing emails in Microsoft Outlook.
---

# Cymbal Aerospace CLM — Contract Intake, Proforma Diff & Document Reviewer UI (`clm-contract-intake`)

## 1. When to Activate
Activate this skill in **Workflow 1 (Contract Owner Intake & Routing)** whenever the user asks to:
- Check Adele Vance's inbound email for **Deal `BA-2026-AV-8921`** (*Apex AeroSystems — $45M FCC-900 Flight Control Computer Subsystem*),
- Fetch the attached **`Vendor_Redlined_GP1.docx`** and store it in the same SharePoint folder (`sites/CymbalAerospace/Shared Documents/BA-2026-AV-8921`) as the Cymbal Proforma (**`Cymbal_GP1_Standard.docx`**),
- Compare the vendor markup against the Cymbal Proforma clause-by-clause with BigQuery historical precedents (`64` Tier-1 Avionics deals across all 4 positions),
- Identify the **4 SME Owners** (`Engineering`, `Legal`, `Tax`, `Cyber`), initialize the working review document (**`BA-2026-AV-8921_Working_Review.docx`**), and open the interactive **Document-Style Redline & Counter-Position Reviewer UI** in Spark Canvas.

---

## 2. Step-by-Step Execution

### Step 1 — Run the CLM Intake Engine (`ingest`)
Run the following command in your current working directory:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py ingest --deal-id BA-2026-AV-8921
```

This command:
1. Uploads **`Vendor_Redlined_GP1.docx`** to SharePoint (`https://36zrbd.sharepoint.com/sites/CymbalAerospace/Shared%20Documents/BA-2026-AV-8921/Vendor_Redlined_GP1.docx`) alongside **`Cymbal_GP1_Standard.docx`**.
2. Parses all **12 clauses** (`8` untouched fast-tracked + `4` redlined exceptions: `GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) and retrieves the **BigQuery historical precedent distribution** (`16` Tier-1 Avionics deals per position = `64` total deals) for every position.
3. Identifies the **4 SME Owners** (`Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`).
4. Initializes **`BA-2026-AV-8921_Working_Review.docx`** so any edits, approvals, or user comments submitted from the UI are immediately saved to the working review document.
5. Generates **`./cymbal_clm_redline_workbench.html`** in the current directory.

### Step 2 — If the User Also Asked to Route to SMEs via Email, Run `clm-comms` (`route-smes`)
If the user's prompt also asks to route the redlined sections to the SME owners via email (or create the Outlook drafts):

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py route-smes --deal-id BA-2026-AV-8921
```
*(Add `--send` if the user explicitly asked to send the 4 SME emails immediately instead of saving them in Outlook `Drafts`.)*

### Step 3 — Open the Interactive Document-Style Reviewer UI in Spark Canvas (Mandatory)
Always open/render **`./cymbal_clm_redline_workbench.html`** in **Spark Canvas** (or provide the clickable artifact link `[Open Cymbal CLM Document Reviewer Workbench](./cymbal_clm_redline_workbench.html)`).

The UI renders a **Document-Style Counter-Position Reviewer** on an emerald stage where the reviewer or contract owner can:
- See the exact **inline Counter-Position change to accept** (with **orange-red strikethrough** on rejected vendor markup and **coral highlight** on the proposed counter-position change),
- Click **`✦ Rewrite with Input`** to edit the counter-position text or pick a Playbook preset (`Tier-1 Compromise`, `Hold Firm`, `Accept Vendor`),
- Click **`✓ Accept changes`** or **`✕ Reject changes`**,
- Click **`💬 Comment`** to add or edit a comment **attributed to the human user** (e.g., `Rahul Kasanagottu` or the SME's name — never a system comment), which is written directly into **`BA-2026-AV-8921_Working_Review.docx`** until the final consolidated document is created.
