# Cymbal Aerospace CLM Demo Guide — 3-Document Portfolio Workflow (`BA-2026-AV-8921`, `BA-2026-TR-5510`, `BA-2026-LG-7740`)

Instead of forcing a single contract through every lifecycle stage in one session, the Contract Owner works across **3 active Tier-1 supplier contracts**, each pre-staged at one of the **3 key stages of the CLM lifecycle**:

| Stage | Deal ID & Supplier | Subsystem & Value | Pre-Baked State after `"Bake CLM demo"` | What You Demo |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1: Fresh Intake, SME Routing & `/schedule` Monitor** *(+ Optional Tax SME Window)* | **`BA-2026-AV-8921`** — **Apex AeroSystems Inc.** *(Adele Vance)* | `$45,000,000` Flight Control Computers (`FCC-900`) | Unread vendor redline email in Outlook `Inbox` with `Vendor_Redlined_GP1.docx` + Transmittal Memo attached (`4 PENDING` redlines) | Review vendor email → upload `.docx` to SharePoint → open the **Progressive-Disclosure CLM Workbench** (`cymbal_clm_redline_workbench.html` in Spark Canvas or `[Cymbal CLM Workbench]` Sidecar) showing only the 4 redlined statements upfront, with on-demand expansion for `📘 Playbook Guidance`, `📊 Historical Intelligence`, and `⚡ Route / Approve / Counter-Position` → route emails to 4 SME owners → create `/schedule` Inbox monitor *(+ optional Window 2 Tax SME review)* |
| **Stage 2: Middle-Stage Conflict Resolution (Finance vs. Legal in Working `.docx`)** | **`BA-2026-TR-5510`** — **Vanguard Thrust Systems Corp.** *(Marcus Vance)* | `$38,000,000` Thrust Reverser Actuators (`TRA-500`) | `BA-2026-TR-5510_Working_Review.docx` (in SharePoint & Outlook `Inbox`) contains a live `.docx` conflict between **Finance (`Diego Siciliani` in `GP1 §3.1`)** and **Legal (`Miriam Graham` in `GP1 §19`)** | Open the compared view for `BA-2026-TR-5510` in the **CLM Workbench** → inspect the Finance vs. Legal conflict in the working `.docx` (3.5% discount for 1.0x cap vs. Legal's 1.5x minimum cap) → resolve so **Legal takes precedence over everything** → send resolution email to Finance & Legal |
| **Stage 3: Final Consolidation & Vendor Counter-Proposal Dispatch** | **`BA-2026-LG-7740`** — **Meridian Landing Gear Corp.** *(Lidia Holloway)* | `$52,000,000` Titanium Landing Gear (`TLG-800`) | `BA-2026-LG-7740_Working_Review.docx` (in SharePoint & Outlook `Inbox`) has SME approvals recorded (`GP1-12`, `SP3-04`, `SP5-03` `APPROVED`) and `GP1-19` ready for final Owner acceptance | Review SME edits on `BA-2026-LG-7740` in the **CLM Workbench** → accept remaining/alternate position on `GP1 §19` → consolidate final Counter-Proposal `.docx` & Deviation Matrix `.xlsx` → send counter-proposal email back to Lidia Holloway at Meridian |

---

## Progressive-Disclosure UI + Sidecar Experience Highlights (Antigravity & Gemini Enterprise "Spark")

Every CLM analysis turn outputs a single clean Canvas/Sidecar file (`cymbal_clm_redline_workbench.html` or `cymbal_clm_tax_reviewer_workbench.html`) designed around **Minimum-Viable Progressive Disclosure** (with 4 live selectable UI layout options at the top of the workbench):

1. **Layer 0 (Default Initial View — Minimum High-Value Signal)**:
   - Displays **only the Redlined Statements Needing Attention** (`GP1 §12.2`, `GP1 §19.1`, `SP3 §4.1`, `SP5 §3.2`) with inline `<del>` / `<ins>` word diffs, risk/conflict badges, and assigned SME owners.
   - The **8 unmodified baseline clauses** are tucked into a single compact banner (`✓ 8 Unmodified Playbook Clauses Auto-Cleared — [Show 8 Unchanged Clauses ▾]`).
2. **Layers 1 & 2 (Non-Linear On-Demand Expansion Per Clause)**:
   - Each redlined clause provides independent, on-demand expansion toggles (all closed by default so the user is never overwhelmed):
     - **`[📘 Playbook Guidance & Conflict Check ▾]`**: Expands Cymbal Playbook Preferred Standard, Pre-Approved Tier-1 Fallback, Regulatory Lockout citations (`14 CFR Part 21.140`, `DFARS 252.204-7012`), and cross-clause SOW conflict analysis (`GP1 §3.1`).
     - **`[📊 Historical Intelligence (16 BigQuery Deals) ▾]`**: Expands live BigQuery `VECTOR_SEARCH` outcome distribution bars (`% Held Firm` vs. `% Compromise` vs. `% Accepted Vendor`) and the top 5 matching historical contracts with 1-click `📋 Use Language`.
     - **`[⚡ Route to SME / Approve / Counter-Position ▾]`**: Expands 1-click SME email routing (`📧 Route to SME`), Playbook Option A/B/C radio cards, live Vertex AI Gemini (`gemini-2.5-flash`) custom clause rewrite, and human-attributed Word comments (`w:author`) saved directly to `<Deal-ID>_Working_Review.docx`.
3. **4 Selectable Progressive-Disclosure Layout Options Built Into the Workbench Header**:
   - **`🎯 Option A: Redline Cards + Expandable Drawers`** *(Default — Linear / GitHub PR File-Card Style)*
   - **`🪄 Option B: Clean Document + Slide-Over Drawer`** *(Notion / Modern Word Style — zero permanent sidebars; clicking any redline slides out a floating right context drawer)*
   - **`📋 Option C: Compact Triage Matrix + Row Drawers`** *(Stripe / Superhuman Style — 4-row executive triage table with inline aspect drawers)*
   - **`🔦 Option D: Single-Clause Spotlight + Progressive Tiles`** *(Arc / Focused Decision Studio Style — 1 clause at a time with 3 expandable Bento tiles underneath)*
   - Plus classic deep-dive modes: `📄 Full 3-Pane Word View`, `⚖️ 3-Column Compare`, `🕸️ Dependency Graph`, and `🏛️ Pre-Consolidation Gate`.
4. **Sticky Embedded Sidecar Agent Chat Dock (`#embedded-agent-dock`)**:
   - Docked at the bottom of the Sidecar / Canvas Workbench (`💬 Embedded Sidecar Agent Chat` + active clause context).
   - Clicking 1-click workflow chips (**`📧 Route 4 SME Drafts`**, **`🔄 Poll Inbox Replies`**, **`📊 Ask About Precedents`**, **`📦 Consolidate .docx & .xlsx`**) or typing a prompt dispatches the instruction + active clause context directly back to the **Main Agent conversation** via `window.sidecar.agent.sendMessage(msg)` (and answers inline via `/api/ask-agent` when running in Spark Canvas or browser mode).

---

## Pre-Demo Reset ("Bake CLM demo")

Before starting the demo, run (or say **`"Bake CLM demo"`** in chat):
```bash
"/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.venv/bin/python" "/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/scripts/bake_demo.py" --full
```
- **Resets all 3 Portfolio Deals**:
  - `BA-2026-AV-8921` (Apex AeroSystems — Stage 1 Intake)
  - `BA-2026-TR-5510` (Vanguard Thrust Systems — Stage 2 Finance vs. Legal `.docx` Conflict)
  - `BA-2026-LG-7740` (Meridian Landing Gear — Stage 3 Ready for Final Consolidation)
- **Outlook Inbox**: Seeded with **7 fresh Cymbal Aerospace emails** covering all 3 deals (including Adele Vance's `[URGENT REDLINE] Deal BA-2026-AV-8921`, Miriam Graham's `[CONFLICT ESCALATION] Deal BA-2026-TR-5510` with `BA-2026-TR-5510_Working_Review.docx` attached, and Lidia Holloway's `[FINAL STAGE READY] Deal BA-2026-LG-7740` with `BA-2026-LG-7740_Working_Review.docx` attached).
- **Outlook Drafts**: Completely empty (**`0` drafts**) so **Spark** creates/sends the real Outlook emails live during the demo when prompted.

---

## Stage 1 — Doc 1 (`BA-2026-AV-8921` — Apex AeroSystems, `$45M` FCC-900): Intake, SharePoint Upload, Playbook Compare, SME Routing & `/schedule` Monitor

### 1.1 Owner Reviews Vendor Email & Redlined Doc (Window 1: Contract Owner)
> *"Check my Outlook Inbox for Adele Vance's email on Deal BA-2026-AV-8921 and summarize the attached redlined contract and transmittal memo."*

### 1.2 Owner Uploads Redlined Doc to Vendor/Contract SharePoint Folder (Window 1: Contract Owner)
> *"Upload the attached Vendor_Redlined_GP1.docx to the BA-2026-AV-8921 contract folder for Apex AeroSystems in SharePoint."*

### 1.3 Playbook & Historical Precedent Comparison HTML View (Window 1: Contract Owner)
> *"Compare the vendor redlined contract for Deal BA-2026-AV-8921 against our Cymbal Playbook and historical precedents in BigQuery, and open the interactive comparison workbench."*

- **What to Show in the UI**:
  1. **Progressive-Disclosure Redline View (Default Initial View)**: Point out that the initial view shows **only the 4 Redlined Statements Needing Attention** (`GP1 §12.2`, `GP1 §19.1`, `SP3 §4.1`, `SP5 §3.2`) while the 8 unmodified clauses are tucked into a 1-line summary bar.
  2. **Non-Linear On-Demand Expansion**: Click any clause's **`[📘 Playbook Guidance ▾]`**, **`[📊 Historical Intelligence (n=16) ▾]`**, or **`[⚡ Route / Approve / Counter ▾]`** toggle to expand just that layer on demand—or use the top layout switcher to compare **Option A (Exception Cards)**, **Option B (Clean Doc + Slide-Over Drawer)**, **Option C (Triage Matrix)**, and **Option D (Spotlight + Progressive Tiles)**.

### 1.4 Route Redlined Clauses to Respective SME Owners via Outlook (Window 1: Contract Owner)
> *"Find the respective SME owners for the redlined clauses on Deal BA-2026-AV-8921, draft the review emails using our standard routing template, and send them out via Outlook."*
*(Tip: You can also trigger this directly from inside the Workbench by clicking **`📧 Route 4 SME Drafts`** in the bottom **Embedded Sidecar Agent Chat Dock** or inside any clause's **`⚡ Route / Approve / Counter`** drawer!)*

### 1.5 Create Scheduled Job (`/schedule`) to Monitor SME Responses & Alert (Window 1: Contract Owner)
> *"/schedule Monitor my Outlook Inbox every 5 minutes (and run an initial check now) for SME review responses on Deal BA-2026-AV-8921, update the review status, and alert me when replies arrive."*

### 1.6 Optional Second Chat — Tax SME Reviews & Approves Doc 1 (Window 2: Tax SME — Pradeep Gupta)
- **Prompt 1.6A (Tax Perspective Review with Full-Doc Context Toggle):**
  > *"Review the tariff redline in SP3 §4.1 for Deal BA-2026-AV-8921 from a Tax perspective against our Playbook and BigQuery precedents, check for any conflict with the GP1 §3.1 Fixed-Price SOW, and open the Tax review workbench."*
  *(Tip: Open `cymbal_clm_tax_reviewer_workbench.html` in Spark Canvas or click the `[Cymbal Tax & Tariff Review]` Sidecar pill to open the Tunneled Tax Workbench, then toggle **`📄 Full 12-Clause Contract View`** in the top header to inspect `GP1 §3.1` alongside `SP3 §4.1`.)*
- **Prompt 1.6B (Approve & Send Thoughts to Contract Owner):**
  > *"Approve the 50/50 tariff split capped at 2.0% ($900,000) harmonized with GP1 §3.1 and send my Tax review response back to the Contract Owner via Outlook."*

---

## Stage 2 — Doc 2 (`BA-2026-TR-5510` — Vanguard Thrust Systems, `$38M` TRA-500): Finance vs. Legal Conflict Resolution in the Working `.docx`

On Deal `BA-2026-TR-5510`, **Finance (`Diego Siciliani`, VP Procurement Finance)** and **Corporate Legal (`Miriam Graham`, VP Corporate Legal & IP)** directly updated `BA-2026-TR-5510_Working_Review.docx` with conflicting edits:
- **Finance (`GP1 §3.1`)**: Accepted a **3.5% (`$1,330,000`) unit-price discount** in exchange for lowering the `GP1 §19` General Liability Cap to **1.0x (`$38,000,000`)**.
- **Legal (`GP1 §19.1 & §24.1`)**: Enforced Corporate Legal's minimum **1.5x (`$57,000,000`) General Liability Cap** (with `2.5x` Super-Cap) and strictly prohibited trading away liability caps for commercial unit-price discounts (`CONFLICT-GP1-19-GP1-03-FINANCE-LEGAL`).

### 2.1 Inspect the Finance vs. Legal Conflict in the Working `.docx` (Window 1: Contract Owner)
> *"Open the Playbook and working document comparison view for Deal BA-2026-TR-5510 (Vanguard Thrust Systems) so I can inspect the conflict between Finance and Legal."*
*(In the Workbench, inspect the prominent conflict banner for `GP1 §3.1` and `GP1 §19.1`, and expand the comments/playbook drawer to read Diego Siciliani's and Miriam Graham's conflicting `.docx` margin comments.)*

### 2.2 Resolve Conflict (Legal Takes Precedence Over Everything) & Send Resolution Email (Window 1: Contract Owner)
> *"Resolve the conflict on Deal BA-2026-TR-5510 so that Legal takes precedence over Finance—enforcing Legal's minimum 1.5x ($57M) liability cap in GP1 §19 and restoring the standard $38M Firm-Fixed-Price schedule in GP1 §3.1—and send an email via Outlook to Finance and Legal confirming that Legal guardrails take precedence."*
*(Or click **`⚖️ Resolve Conflict: Legal Takes Precedence`** directly inside the HTML Review Workbench, then use the bottom **Embedded Sidecar Agent Chat Dock** to tell the Main Agent to send the resolution email to Finance and Legal.)*

---

## Stage 3 — Doc 3 (`BA-2026-LG-7740` — Meridian Landing Gear, `$52M` TLG-800): Owner Review, Consolidation & Vendor Counter-Proposal Dispatch

On Deal `BA-2026-LG-7740`, Engineering (`GP1 §12.2`), Tax (`SP3 §4.1`), and Cyber (`SP5 §3.2`) have already recorded their approvals in `BA-2026-LG-7740_Working_Review.docx`, leaving `GP1 §19` ready for the Contract Owner's final review.

### 3.1 Review SME Edits & Accept Final Position (Window 1: Contract Owner)
> *"Check the SME review status and working document for Deal BA-2026-LG-7740 (Meridian Landing Gear) and open the review workbench so I can review the edits and finalize GP1 §19."*
*(In the Full Sidecar Workbench, notice `GP1-12`, `SP3-04`, and `SP5-03` show green `[✓]` badges in the Left Navigator Tree while `GP1-19` shows amber `[M]`.)*

### 3.2 Consolidate Counter-Proposal `.docx` & `.xlsx` and Send Back to Vendor (Window 1: Contract Owner)
> *"Accept the recommended 2.0x ($104M) Tier-1 Super-Cap position on GP1 §19 for Deal BA-2026-LG-7740, consolidate the final Counter-Proposal Word document and Deviation Matrix Excel sheet, and send the counter-proposal package back to Lidia Holloway at Meridian Landing Gear via Outlook."*
*(Tip: You can also click **`✓ Accept Selected Counter-Position & Save to Working .docx`** on `GP1 §19` in the Right Inspector, then click the **`📦 Consolidate .docx & .xlsx`** chip in the bottom **Embedded Sidecar Agent Chat Dock**!)*

---

## Plugin & Per-Skill Script Architecture (`plugins/cymbal-aerospace-clm/`)

All skills, rules, sidecar configurations, and per-skill CLI scripts are packaged as a standard Antigravity plugin in `plugins/cymbal-aerospace-clm/` and accept `--deal-id` (`BA-2026-AV-8921` / `doc1`, `BA-2026-TR-5510` / `doc2`, or `BA-2026-LG-7740` / `doc3`):
- `plugins/cymbal-aerospace-clm/plugin.json` — Plugin manifest
- `plugins/cymbal-aerospace-clm/skills/clm-contract-intake/scripts/intake.py` — OOXML `.docx` parser, Playbook comparison, and BigQuery precedent evaluation across all 3 deals
- `plugins/cymbal-aerospace-clm/skills/clm-tax-tariff-review/scripts/tax_review.py` — `SP3-04` Tax/Tariff review, cross-clause `GP1-03` FFP harmonization, and full-document context toggle
- `plugins/cymbal-aerospace-clm/skills/clm-contract-consolidation/scripts/precedents.py`, `record_position.py`, `resolve_conflict.py`, `consolidate.py` — Precedent verification, SME position recording, Finance vs. Legal conflict resolution (`resolve_conflict.py`), and `.docx`/`.xlsx` consolidation
- `plugins/cymbal-aerospace-clm/skills/clm-comms/scripts/outlook_comms.py` — Microsoft Graph Outlook draft/send routing (`route-smes`), SME reply delivery (`send-sme-reply`), Inbox polling (`poll-inbox`), conflict resolution notification (`send-conflict-resolution`), and vendor transmittal (`draft-vendor-reply`)
