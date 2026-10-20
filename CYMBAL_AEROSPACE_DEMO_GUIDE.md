# Cymbal Aerospace CLM Demo Guide — 4-Workflow Live Script (`Deal BA-2026-AV-8921`)

## Pre-Demo Reset ("Bake CLM demo")

Before starting the demo, run (or say **`"Bake CLM demo"`** in chat):
```bash
"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" --full
```
- **Outlook Inbox**: Seeded with **5 fresh Cymbal Aerospace emails** (rolled to TODAY's date, including Adele Vance's `[URGENT REDLINE] Deal BA-2026-AV-8921` email with `Vendor_Redlined_GP1.docx` and `Apex_AeroSystems_Redline_Transmittal_Memo.docx` attached).
- **Outlook Drafts**: Completely empty (**`0` drafts**) so **Spark** creates the real Outlook drafts live during the demo via `clm-comms`.
- **Outlook Calendar**: Seeded with **6 Cymbal Aerospace meetings** today/this week so `chief-of-staff` (*"What are my top priorities today?"*) naturally surfaces Deal `BA-2026-AV-8921` and today's 1:30 PM & 4:00 PM decision gates.
- **4 Focused CLM Skills**:
  1. **`clm-contract-intake`** — Uploads `Vendor_Redlined_GP1.docx` to SharePoint alongside `Cymbal_GP1_Standard.docx`, evaluates all 12 clauses against the **Cymbal Tier-1 Avionics Contract Playbook (`GP1 / SP3 / SP5`)** and **64 BigQuery historical precedents** (`16` per exception clause), identifies the 4 SME owners (`Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`), initializes **`BA-2026-AV-8921_Working_Review.docx`**, and opens the **Pastel Word 365 & Playbook Review Workbench** in Spark Canvas / Antigravity UI Sidecar.
  2. **`clm-comms`** — Creates/sends the 4 SME routing emails in real Microsoft Outlook `Drafts` (`route-smes`), delivers SME reply emails to the Contract Owner's `Inbox` (`send-sme-reply`), polls Outlook `Inbox` for SME replies (`poll-inbox`), and creates/sends the final vendor reply email with `.docx` & `.xlsx` attachments (`draft-vendor-reply`).
  3. **`clm-tax-tariff-review`** — Reviews `SP3 §4.1` (Customs, Duties & Section 232/301 Tariffs) in a second Spark window, checks the 16 BigQuery Tax precedents (`63%` 50/50 split above `5.0%` threshold, capped at **`+2.0% ($900,000)`** of FFP PO value), harmonizes `CONFLICT-SP3-04-GP1-03` against `GP1 §3.1` (`$45M` FFP SOW), writes `Pradeep Gupta`'s Word comment into `BA-2026-AV-8921_Working_Review.docx`, and opens the **Pastel Tax SME Playbook Workbench**.
  4. **`clm-contract-consolidation`** — Verifies BigQuery historical precedents across all 4 redlined positions (`precedents --clause-id ALL`), consolidates all accepted/edited counter-positions and human user comments (`w:author`) from `BA-2026-AV-8921_Working_Review.docx` into **`BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`** (passing the `assert_external_docx_sanitized` gate) and **`BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`**, and uploads both live to SharePoint.

---

## Pastel Word 365 & Playbook Review Workbench UI (Spark Canvas + Antigravity UI Sidecar)

Whenever [`cymbal_clm_redline_workbench.html`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/cymbal_clm_redline_workbench.html) or [`cymbal_clm_tax_reviewer_workbench.html`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/cymbal_clm_tax_reviewer_workbench.html) opens (or in the Antigravity right-hand UI Sidecar via [`sidecar.json`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/sidecars/cymbal-clm-workbench/sidecar.json)):

1. **Unified Top Pastel Header & 4 Surface Mode Tabs**:
   - **`📄 Word Doc & Playbook Review`**: Full 12-clause Word 365 document sheet with the **8 unchanged `[0] CLEAR` clauses auto-collapsed into 1-line `.untouched-strip` bars** (expandable individually or via `📂 Expand 8 Unchanged`) so the 4 redlined clauses (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) are immediately visible.
   - **`⚖️ 3-Column Compare`**: Side-by-side matrix comparing (1) Cymbal Playbook Preferred Standard & Guardrail, (2) Apex AeroSystems Redline vs. Playbook Standard, and (3) Playbook Counter-Position + Embedded BigQuery Precedents (`📋 Use Language` one-click loader).
   - **`🕸️ Dependency Graph`**: Interactive SVG Cross-Clause Conflict & Regulatory Lockout topology (`SP3 §4.1` $\leftrightarrow$ `GP1 §3.1` FFP SOW Ceiling; `GP1 §12.2` FAA 14 CFR Part 21.140; `SP5 §3.2` DFARS 252.204-7012).
   - **`🏛️ Pre-Consolidation Gate`**: 4-Position Readiness Matrix + **3 One-Click Agent Co-Pilot Triggers** (`📧 Route 4 SME Emails in Outlook`, `🔄 Poll Outlook for SME Replies`, `📦 Consolidate & Draft Vendor Reply`) powered by `window.sidecar.agent.sendMessage` in Antigravity Sidecar mode and `POST /run` in Spark Canvas mode.
2. **Local Word Sheet Bar & Compare Basis Switcher**:
   - **Compare Basis**: Toggle live between **`vs. Playbook Counter-Position`** (Pastel Rose `<del>` on rejected vendor language + Pastel Mint `<ins>` on Cymbal's Playbook counter-position) and **`vs. Cymbal Playbook Preferred Standard`**.
   - **Word Markup Mode**: Switch between `All Markup (<del>/<ins>)`, `Simple Markup`, `Clean Future Version`, and `PR Stacked Diff (-/+)`.
3. **Sticky 3-Tab Right Inspector (`🎯 Decision & Counter` | `📊 Precedents (16)` | `💬 Comments`)**:
   - **4 Primary Review Actions**: **`✓ Accept changes`**, **`✕ Reject changes`**, **`✦ Rewrite with Input`** (live inline editor + `↺ Revert to Recommended Counter` / `↺ Revert to Original Proforma Baseline`), and **`💬 Comment`**.
   - **`🎯 Decision & Counter`**: 3-bullet ASD-STE100 Playbook & Precedent synthesis card, full untruncated counter-position preview, and interactive Playbook Option A/B/C cards with `★ RECOMMENDED` and `REGULATORY LOCKOUT VIOLATION` badges.
   - **`📊 Precedents (16)`**: BigQuery `VECTOR_SEARCH` distribution bar (`Held Firm %` / `Compromise %` / `Vendor Ask %`) + 5 executed Tier-1 aerospace precedent deals with one-click **`📋 Use Language`**.
   - **`💬 Comments`**: Vendor transmittal margin balloon + human reviewer Word comment balloon (`w:author="Rahul Kasanagottu"`, `w:author="Pradeep Gupta"`, `w:author="Megan Bowen"`, `w:author="Alex Wilber"`) saved directly into `word/comments.xml` of **`BA-2026-AV-8921_Working_Review.docx`** and synced live to SharePoint.

---

## Live 4-Workflow Prompts for Spark

### Optional Opening — Morning Briefing (`chief-of-staff`)
> *"What are my top priorities today?"*

### Workflow 1 — Contract Owner Intake, Playbook Diff & SME Email Routing (`clm-contract-intake` + `clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Check Adele Vance's urgent email on Deal BA-2026-AV-8921, upload the attached Vendor_Redlined_GP1.docx to the BA-2026-AV-8921 SharePoint folder alongside our Cymbal_GP1_Standard.docx baseline, compare the vendor redlines against our Cymbal Tier-1 Avionics Playbook and historical BigQuery precedents using our CLM intake skill, open the Pastel Word 365 & Playbook Review Workbench in Canvas, and route the 4 redlined sections to the respective SME owners via Outlook."*

### Workflow 2 — Tax SME Playbook Review & Conflict Harmonization in Second Window (`clm-tax-tariff-review` + `clm-comms`)
**Window 2 (Tax SME — Pradeep Gupta):**
> *"As the Global Tax & Tariff SME, use our Tax review skill to review SP3 §4.1 for Deal BA-2026-AV-8921 against the Cymbal Tax Playbook, check our 16 historical Tier-1 tariff precedents in BigQuery, harmonize the conflict with the GP1 §3.1 Firm-Fixed-Price SOW using the 50/50 tariff split capped at 2.0% ($900,000), open the Tax Reviewer Workbench in Canvas, and send our recommended counter-position back to the Contract Owner via Outlook email."*

### Workflow 3 — Scheduled / On-Demand Email Progress Polling (`clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Schedule a recurring check every 5 minutes (and run the first check right now) using our CLM comms skill to poll my Outlook Inbox for SME review replies on Deal BA-2026-AV-8921 and update the Canvas Workbench."*

### Workflow 4 — Owner Precedent Check Across All 4 Positions, Sanitized Consolidation & Vendor Reply (`clm-contract-consolidation` + `clm-comms`)
**Window 1 (Contract Owner — Rahul Kasanagottu):**
> *"Check the historical precedents in BigQuery across all 4 redlined positions (including GP1 §19 Limitation of Liability & IP Indemnity), consolidate all approved SME counter-positions and human user comments from our Working Review document into the final sanitized Cymbal Counter-Proposal Word document and SharePoint Deviation Matrix Excel workbook, upload them to SharePoint, and create the reply email to Adele Vance in Outlook with both files attached."*
