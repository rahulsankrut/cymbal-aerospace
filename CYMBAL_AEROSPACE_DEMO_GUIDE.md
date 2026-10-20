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

## Step-by-Step Live Demo Prompts for Spark

### Optional Opening — Morning Briefing (`chief-of-staff`)
> *"What are my top priorities today?"*

---

### Workflow 1 — Contract Owner Intake, Playbook Comparison & SME Routing
**Window 1 (Contract Owner — Rahul Kasanagottu):**

**Prompt 1A (Check Email & Upload Redlined Contract to SharePoint):**
> *"Check Adele Vance's email on Deal BA-2026-AV-8921 and upload the attached redlined contract to the BA-2026-AV-8921 folder in SharePoint."*

**Prompt 1B (Compare Against Playbook & Open Review Workbench):**
> *"Compare the vendor redlined contract against our Cymbal Playbook and historical precedents in BigQuery, and open the review workbench."*

**Prompt 1C (Route Redlined Clauses to SMEs via Outlook):**
> *"Draft emails in Outlook to route the 4 redlined sections to their respective SME owners for review."*
*(Or say *"Send emails in Outlook..."* to send immediately instead of saving to `Drafts`.)*

---

### Workflow 2 — Tax SME Review in Second Window
**Window 2 (Tax SME — Pradeep Gupta):**

**Prompt 2A (Review Tariff Redline & Resolve SOW Conflict):**
> *"Review the tariff redline in SP3 §4.1 for Deal BA-2026-AV-8921 against our Playbook and historical precedents in BigQuery, resolve any conflict with the GP1 §3.1 Fixed-Price SOW, and open the Tax review workbench."*

**Prompt 2B (Send SME Recommendation Back to Contract Owner):**
> *"Send our recommended Tax counter-position back to the Contract Owner via Outlook."*

---

### Workflow 3 — Email Progress Polling
**Window 1 (Contract Owner — Rahul Kasanagottu):**

**Prompt 3A (Poll Outlook Inbox for SME Replies):**
> *"Check my Outlook Inbox for SME review replies on Deal BA-2026-AV-8921 and update the review workbench."*
*(Or to schedule recurring polling: *"Schedule a recurring check every 5 minutes (and run the first check now) to poll my Outlook Inbox for SME replies on Deal BA-2026-AV-8921."*)*

---

### Workflow 4 — Final Precedent Check, Consolidation & Vendor Reply
**Window 1 (Contract Owner — Rahul Kasanagottu):**

**Prompt 4A (Verify Precedents Across All 4 Redlined Positions):**
> *"Check our historical precedents in BigQuery across all 4 redlined positions, including GP1 §19 Limitation of Liability and IP Indemnity."*

**Prompt 4B (Consolidate Final Counter-Proposal Package):**
> *"Consolidate all approved counter-positions and reviewer comments into the final Counter-Proposal Word document and Deviation Matrix Excel sheet."*

**Prompt 4C (Explicitly Upload Final Package to SharePoint):**
> *"Upload the final Counter-Proposal Word document and Deviation Matrix Excel sheet to the BA-2026-AV-8921 folder in SharePoint."*

**Prompt 4D (Draft Reply Email to Vendor with Attachments):**
> *"Draft a reply email to Adele Vance in Outlook with the final Counter-Proposal Word document and Deviation Matrix attached."*
*(Or say *"Send the reply email to Adele Vance..."* to send immediately.)*

---

## Interactive Review Workbench Reference (What to Show in the UI)

Whenever the Review Workbench opens in Canvas (or in the Antigravity UI Sidecar):
- **Word Doc & Playbook Review**: Shows the 12-clause contract with the **8 unchanged clauses auto-collapsed into 1-line strips** so the 4 redlined clauses (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) are immediately visible.
- **Sticky 3-Tab Right Inspector**:
  - **`🎯 Decision & Counter`**: Click **`✓ Accept changes`**, **`✕ Reject changes`**, **`✦ Rewrite with Input`** (or `↺ Revert to Recommended Counter`), or select Playbook Options A/B/C.
  - **`📊 Precedents (16)`**: Inspect the 16 BigQuery historical Tier-1 deals and click **`📋 Use Language`** on any precedent row.
  - **`💬 Comments`**: Add or edit a Word margin comment attributed directly to the human reviewer (`w:author="Rahul Kasanagottu"`, `w:author="Pradeep Gupta"`, etc.), which is saved immediately to `BA-2026-AV-8921_Working_Review.docx` and synced to SharePoint.
- **Top Surface Mode Switcher**: Switch between **`📄 Word Doc & Playbook Review`**, **`⚖️ 3-Column Compare`**, **`🕸️ Dependency Graph`**, and **`🏛️ Pre-Consolidation Gate`**.
