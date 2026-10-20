# Cymbal Aerospace CLM Demo Guide — 4-Workflow Live Script (`Deal BA-2026-AV-8921`)

## Pre-Demo Reset ("Bake CLM demo")

Before starting the demo, run:
```bash
"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" --full
```
- **Outlook Inbox**: Seeded with **5 fresh Cymbal Aerospace emails** (including Adele Vance's `[URGENT REDLINE] Deal BA-2026-AV-8921` email with `Vendor_Redlined_GP1.docx` attached).
- **Outlook Drafts**: Completely empty (**`0` drafts**) so **Spark** creates the real Outlook drafts live during the demo via `clm-comms`.
- **Outlook Calendar**: Seeded with **6 Cymbal Aerospace meetings** today/this week so `chief-of-staff` naturally surfaces Deal `BA-2026-AV-8921`.
- **4 Focused CLM Skills**:
  1. `clm-contract-intake` — Uploads `Vendor_Redlined_GP1.docx` to SharePoint alongside `Cymbal_GP1_Standard.docx`, compares all 12 clauses with BigQuery historical precedents across all 4 positions (`64` deals, `16` per position), identifies the 4 SME owners, initializes `BA-2026-AV-8921_Working_Review.docx`, and opens the **Document-Style Counter-Position Reviewer UI** in Canvas.
  2. `clm-comms` — Creates/sends the 4 SME routing emails in real Microsoft Outlook `Drafts` (`route-smes`), delivers SME reply emails to the Contract Owner's `Inbox` (`send-sme-reply`), polls Outlook `Inbox` for SME replies (`poll-inbox`), and creates/sends the final vendor reply email with `.docx` & `.xlsx` attachments (`draft-vendor-reply`).
  3. `clm-tax-tariff-review` — Reviews `SP3 §4.1` (Customs, Duties & Section 232/301 Tariffs) in a second Spark window, checks the 16 BigQuery Tax precedents (`63%` 50/50 split capped at `+2%` FFP), harmonizes the Cross-Clause Conflict against `GP1 §3.1` (`$45M` FFP SOW), writes the Tax Reviewer's user comment (`Pradeep Gupta`) to `BA-2026-AV-8921_Working_Review.docx`, and opens the Tax Reviewer UI in Canvas.
  4. `clm-contract-consolidation` — Verifies BigQuery historical precedents across all 4 redlined positions (`precedents --clause-id ALL`), consolidates all accepted/edited counter-positions and human user comments from `BA-2026-AV-8921_Working_Review.docx` into `BA-2026-AV-8921_Cymbal_Counter_Proposal.docx` and `BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`, and uploads both live to SharePoint.

---

## Interactive Document-Style Counter-Position Reviewer UI (Canvas)

Whenever `cymbal_clm_redline_workbench.html` or `cymbal_clm_tax_reviewer_workbench.html` opens in Spark Canvas:
- **Document-Style Counter-Position Diff**: Shows a white contract page on an emerald-green stage (`#237a5b`) displaying the **exact inline Counter-Position change that the reviewer/owner needs to accept**:
  - **Orange-Red Strikethrough (`#e04f33`)** on the rejected/replaced vendor redline span,
  - **Coral-Peach Highlight (`#f9d8d0`)** on the proposed Counter-Position language.
- **Floating Action Menu Card**:
  - **`✦ Rewrite with Input`**: Edit the counter-position text inline or pick a Playbook preset (`Tier-1 Compromise`, `Hold Firm`, `Accept Vendor`) and watch the inline strikethrough + coral highlight diff update live.
  - **`✓ Accept changes`**: Approves the counter-position and saves it directly into **`BA-2026-AV-8921_Working_Review.docx`**.
  - **`✕ Reject changes`**: Rejects the vendor markup (reverts to Cymbal baseline) and saves to **`BA-2026-AV-8921_Working_Review.docx`**.
  - **`💬 Comment`**: Adds or edits a Word margin comment **attributed directly to the human user** (e.g., `Rahul Kasanagottu`, `Pradeep Gupta`, `Megan Bowen`, `Alex Wilber` — never a system comment) and saves it into **`BA-2026-AV-8921_Working_Review.docx`**.

---

## Live 4-Workflow Prompts for Spark

### Optional Opening — Morning Briefing (`chief-of-staff`)
> *"What are my top priorities today?"*

### Workflow 1 — Contract Owner Intake, Proforma Diff & SME Email Routing (`clm-contract-intake` + `clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Check Adele Vance's urgent email on Deal BA-2026-AV-8921, upload the attached Vendor_Redlined_GP1.docx to the BA-2026-AV-8921 SharePoint folder alongside our Cymbal_GP1_Standard.docx proforma, compare the redlines using our CLM intake skill and open the interactive Document Reviewer UI in Canvas, and route the 4 redlined sections to the respective SME owners via Outlook."*

### Workflow 2 — Tax SME Review in Second Window (`clm-tax-tariff-review` + `clm-comms`)
**Window 2 (Tax SME — Pradeep Gupta):**
> *"As the Global Tax & Tariff SME, use our Tax review skill to review SP3 §4.1 for Deal BA-2026-AV-8921, check our historical Tier-1 tariff precedents in BigQuery and resolve any conflict with the GP1 §3.1 Firm-Fixed-Price SOW, open the Tax Reviewer UI in Canvas, and send our recommended counter-position back to the Contract Owner via Outlook email."*

### Workflow 3 — Scheduled / On-Demand Email Progress Polling (`clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Schedule a recurring check every 5 minutes (and run the first check right now) using our CLM comms skill to poll my Outlook Inbox for SME review replies on Deal BA-2026-AV-8921 and update the Canvas Workbench."*

### Workflow 4 — Owner Precedent Check across All Positions, Final Consolidation & Vendor Reply (`clm-contract-consolidation` + `clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Check the historical precedents in BigQuery across all 4 redlined positions (including GP1 §19 Limitation of Liability & IP Indemnity), consolidate all approved SME positions and user comments into the final Counter-Proposal Word document and SharePoint Deviation Matrix Excel workbook, upload them to SharePoint, and create the reply email to Adele Vance in Outlook with both files attached."*
