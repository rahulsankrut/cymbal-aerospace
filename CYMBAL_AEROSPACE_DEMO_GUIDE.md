# Cymbal Aerospace CLM Demo Guide — Step-by-Step Live Script (`Deal BA-2026-AV-8921`)

## Pre-Demo Reset ("Bake CLM demo")

Before starting the demo, run (or say **`"Bake CLM demo"`** in chat):
```bash
"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" --full
```
- **Outlook Inbox**: Seeded with **5 fresh Cymbal Aerospace emails** (including Adele Vance's `[URGENT REDLINE] Deal BA-2026-AV-8921` email with `Vendor_Redlined_GP1.docx` and `Apex_AeroSystems_Redline_Transmittal_Memo.docx` attached).
- **Outlook Drafts**: Completely empty (**`0` drafts**) so **Spark** creates the real Outlook drafts live during the demo when prompted.
- **Outlook Calendar**: Seeded with **6 Cymbal Aerospace meetings** today/this week so `chief-of-staff` naturally surfaces Deal `BA-2026-AV-8921`.

---

## The 8-Step End-to-End Demo Workflow (`Deal BA-2026-AV-8921`)

| Step | Persona / Window | Action | Skill / Connector Invoked |
| :--- | :--- | :--- | :--- |
| **1. Bake Demo** | Pre-Demo CLI / Chat | Seeds Adele Vance's vendor redline email (`Vendor_Redlined_GP1.docx` + Transmittal Memo attached) into Outlook `Inbox` and resets Deal `BA-2026-AV-8921` | `scripts/bake_demo.py --full` |
| **2. Review Vendor Email** | Contract Owner (Window 1) | Reviews Adele Vance's urgent email in Outlook and inspects the attached redlined contract (`Vendor_Redlined_GP1.docx`) | `gemini-enterprise-connectors` (M365 Mail) |
| **3. Upload to SharePoint** | Contract Owner (Window 1) | Uploads `Vendor_Redlined_GP1.docx` to the vendor's contract folder in SharePoint (`/sites/CymbalAerospace/Shared Documents/BA-2026-AV-8921`) | `gemini-enterprise-connectors` (M365 SharePoint) |
| **4. Playbook & Precedent Comparison View** | Contract Owner (Window 1) | Compares the redlined contract against the Cymbal Playbook and BigQuery historical precedents and renders the interactive HTML workbench | `clm-contract-intake` (`scripts/intake.py`) |
| **5. Route to SME Owners via Outlook** | Contract Owner (Window 1) | Finds the respective SME domain owners for the 4 redlined clauses, drafts templated routing emails, and sends them via Outlook | `clm-comms` (`scripts/outlook_comms.py route-smes --send`) |
| **6. Schedule Status Monitor** | Contract Owner (Window 1) | Creates a scheduled job (`/schedule`) in Spark to monitor the Outlook Inbox for SME responses and alert when updates arrive | `automation` (`/schedule`) + `clm-comms` (`scripts/outlook_comms.py poll-inbox`) |
| **7. Tax SME Review (2nd Window)** | Tax SME — Pradeep Gupta (Window 2) | Reviews `SP3 §4.1` from a Tax perspective (with full-document context toggle), resolves the `GP1 §3.1` Fixed-Price SOW conflict, and sends approval/thoughts back to the Contract Owner | `clm-tax-tariff-review` (`scripts/tax_review.py`) + `clm-comms` (`send-sme-reply --clause-id SP3-04`) |
| **8. Owner Review, Consolidate & Send Counter-Proposal** | Contract Owner (Window 1) | Reviews SME edits, accepts remaining or alternate positions, generates the Counter-Proposal `.docx` (with Track Changes & comments) and Deviation Matrix `.xlsx`, and sends it back to the vendor | `clm-contract-consolidation` (`record_position.py`, `consolidate.py`) + `clm-comms` (`draft-vendor-reply --send`) |

---

## Step-by-Step Live Demo Prompts for Spark

### Step 1 — Pre-Demo Reset
> **`"Bake CLM demo"`**

### Step 2 — Owner Reviews Vendor Email & Redlined Doc (Window 1: Contract Owner)
> *"Check my Outlook Inbox for Adele Vance's email on Deal BA-2026-AV-8921 and summarize the attached redlined contract and transmittal memo."*

### Step 3 — Owner Uploads Redlined Doc to Vendor/Contract SharePoint Folder (Window 1: Contract Owner)
> *"Upload the attached Vendor_Redlined_GP1.docx to the BA-2026-AV-8921 contract folder for Apex AeroSystems in SharePoint."*

### Step 4 — Playbook & Historical Precedent Comparison HTML View (Window 1: Contract Owner)
> *"Compare the vendor redlined contract against our Cymbal Playbook and historical precedents in BigQuery, and open the interactive comparison workbench."*

### Step 5 — Route Redlined Clauses to Respective SME Owners via Outlook (Window 1: Contract Owner)
> *"Find the respective SME owners for the redlined clauses, draft the review emails using our standard routing template, and send them out via Outlook."*
*(Note: Use `"draft the review emails..."` to save to Outlook `Drafts` or `"send them out via Outlook"` to dispatch immediately.)*

### Step 6 — Create Scheduled Job to Monitor SME Responses & Alert (Window 1: Contract Owner)
> *"/schedule Monitor my Outlook Inbox every 5 minutes (and run an initial check now) for SME review responses on Deal BA-2026-AV-8921, update the review status, and alert me when replies arrive."*

### Step 7 — Tax Owner Persona Reviews & Approves in Second Chat (Window 2: Tax SME — Pradeep Gupta)
- **Prompt 7A (Tax Perspective Review):**
  > *"Review the tariff redline in SP3 §4.1 for Deal BA-2026-AV-8921 from a Tax perspective against our Playbook and BigQuery precedents, check for any conflict with the GP1 §3.1 Fixed-Price SOW, and open the Tax review workbench."*
- **Prompt 7B (Approve & Send Thoughts to Contract Owner):**
  > *"Approve the 50/50 tariff split capped at 2.0% ($900,000) harmonized with GP1 §3.1 and send my Tax review response back to the Contract Owner via Outlook."*

### Step 8 — Owner Reviews Edits, Accepts Positions, Consolidates Counter-Proposal & Sends to Vendor (Window 1: Contract Owner)
- **Prompt 8A (Review Edits & Accept Remaining / Alternate Positions):**
  > *"Check the latest SME review status and historical precedents for Deal BA-2026-AV-8921, and accept the recommended counter-positions for the remaining clauses so all 4 redlined sections are finalized."*
  *(Or click **`✓ Accept changes`** directly on each clause inside the HTML Review Workbench.)*
- **Prompt 8B (Consolidate Counter-Proposal & Send Back to Vendor):**
  > *"Consolidate all approved counter-positions and reviewer comments into the final Counter-Proposal Word document and Deviation Matrix Excel sheet, and send the counter-proposal package back to Adele Vance at Apex AeroSystems via Outlook."*

---

## Plugin & Per-Skill Script Architecture (`plugins/cymbal-aerospace-clm/`)

All skills, rules, sidecar configurations, and per-skill CLI scripts are packaged as a standard Antigravity plugin in `plugins/cymbal-aerospace-clm/`:
- `plugins/cymbal-aerospace-clm/plugin.json` — Plugin manifest
- `plugins/cymbal-aerospace-clm/skills/clm-contract-intake/scripts/intake.py` — OOXML `.docx` parser, Playbook comparison, and BigQuery precedent evaluation
- `plugins/cymbal-aerospace-clm/skills/clm-tax-tariff-review/scripts/tax_review.py` — `SP3-04` Tax/Tariff review, cross-clause `GP1-03` FFP harmonization, and full-document context toggle
- `plugins/cymbal-aerospace-clm/skills/clm-contract-consolidation/scripts/precedents.py`, `record_position.py`, `consolidate.py` — Precedent verification, SME position recording, and `.docx`/`.xlsx` consolidation
- `plugins/cymbal-aerospace-clm/skills/clm-comms/scripts/outlook_comms.py` — Microsoft Graph Outlook draft/send routing, SME reply delivery, Inbox polling (`poll-inbox`), and vendor transmittal

---

## Interactive Review Workbench Reference (What to Show in the UI)

Whenever the Review Workbench opens in Canvas (or in the Antigravity UI Sidecar):
- **Word Doc & Playbook Review**: Shows the 12-clause contract with the **8 unchanged clauses auto-collapsed into 1-line strips** so the 4 redlined clauses (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) are immediately visible. In the Tax SME view (`--persona tax`), the UI focuses on `SP3-04` & `GP1-03` by default with a **`📄 Show All 12 Contract Clauses (Full Context)`** toggle in the header so the SME can inspect the entire contract for context at any time.
- **Sticky 3-Tab Right Inspector**:
  - **`🎯 Decision & Counter`**: Click **`✓ Accept changes`**, **`✕ Reject changes`**, **`✦ Rewrite with Input`** (calls live Vertex AI `gemini-2.5-flash` with `<untrusted_vendor_redline>` XML sandwiching), or select Playbook Options A/B/C.
  - **`📊 Precedents (16)`**: Inspect the 16 BigQuery historical Tier-1 deals and click **`📋 Use Language`** on any precedent row.
  - **`💬 Comments`**: Add or edit a Word margin comment attributed directly to the human reviewer (`w:author="Rahul Kasanagottu"`, `w:author="Pradeep Gupta"`, etc.), which is saved immediately to `BA-2026-AV-8921_Working_Review.docx`.
- **Top Surface Mode Switcher**: Switch between **`📄 Word Doc & Playbook Review`**, **`⚖️ 3-Column Compare`**, **`🕸️ Dependency Graph`**, and **`🏛️ Pre-Consolidation Gate`**.
