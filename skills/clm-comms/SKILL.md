---
name: clm-comms
description: CLM Email Routing, SME Reply Delivery, Outlook Inbox Polling, and Vendor Counter-Proposal Transmittal for Cymbal Aerospace (Deal BA-2026-AV-8921). Use whenever the user asks Spark to save or send the 4 SME review routing emails in Microsoft Outlook, send an SME review reply back to the Contract Owner's Inbox, poll Outlook Inbox for SME review updates, or save/send the final consolidated Counter-Proposal email with .docx and .xlsx attachments back to the vendor.
---

# Cymbal Aerospace CLM — Communications & Outlook Sync (`clm-comms`)

This skill handles all Microsoft Outlook email communications for Cymbal Aerospace Contract Lifecycle Management (`Deal BA-2026-AV-8921` — Apex AeroSystems `$45,000,000` FCC-900 Flight Control Computer Subsystem) via Microsoft Graph (`m365-admin@rahulsankrut.demo.altostrat.com`).

> **Why `clm-comms` is separate from CLM document analysis skills:**
> During `Bake CLM demo`, the Outlook `Drafts` folder is wiped completely clean (`0` drafts) so that **Spark** creates the real Outlook drafts live during the demo when prompted!

---

## 1. Subcommands Available

### A. Workflow 1 — Route Redlined Clauses to the 4 SME Owners (`route-smes`)

When the Contract Owner asks Spark to route the 4 redlined clauses (`GP1 §12.2`, `GP1 §19 & §24`, `SP3 §4.1`, `SP5 §3.2`) to the respective SME owners via Outlook:

- **Default (Save 4 Ready-to-Send Drafts in Outlook `Drafts` folder):**
```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py route-smes --deal-id BA-2026-AV-8921
```
- **If the user explicitly says *"send now"* (Send immediately via Outlook):**
```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py route-smes --deal-id BA-2026-AV-8921 --send
```

This creates (or sends) 4 rich HTML emails in `m365-admin@rahulsankrut.demo.altostrat.com`'s real Microsoft Outlook `Drafts` folder:
1. **Engineering & Quality (`GP1 §12.2`)** → `Megan Bowen <MeganB@36zrbd.onmicrosoft.com>` (includes FAA 14 CFR Part 21.140 lockout warning + `88%` Held Firm precedent stat)
2. **Corporate Legal & Aviation IP (`GP1 §19 & §24`)** → `Lee Gu <LeeG@36zrbd.onmicrosoft.com>` (includes `69%` Tier-1 `2.0x PO / $90M Super-Cap` precedent stat)
3. **Global Tax, Customs & Trade (`SP3 §4.1`)** → `Pradeep Gupta <PradeepG@36zrbd.onmicrosoft.com>` (includes Cross-Clause Conflict alert against `GP1 §3.1` `$45M` FFP SOW + `63%` `50/50 shared cap` precedent stat)
4. **Supplier Cyber Defense (`SP5 §3.2`)** → `Alex Wilber <AlexW@36zrbd.onmicrosoft.com>` (includes DoD DFARS 252.204-7012 72-hour lockout warning + `94%` Held Firm precedent stat)

---

### B. Workflow 2 — Send SME Review Update Back to Contract Owner's Inbox (`send-sme-reply`)

When the Tax SME (or any SME in Workflow 2) finishes reviewing their clause and asks Spark to send their recommended counter-position back to the Contract Owner via Outlook email:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py send-sme-reply --deal-id BA-2026-AV-8921
```

This delivers the SME review update emails (`[SME REVIEW UPDATE: TAX — SP3 §4.1]`, `[SME REVIEW UPDATE: ENGINEERING — GP1 §12.2]`, `[SME REVIEW UPDATE: CYBER — SP5 §3.2]`) directly into the Contract Owner's real Microsoft Outlook `Inbox` (`m365-admin@rahulsankrut.demo.altostrat.com`).

---

### C. Workflow 3 — Poll Contract Owner's Outlook Inbox for SME Progress (`poll-inbox`)

When the Contract Owner (or a scheduled `/schedule` job in Spark) polls Outlook to check which SMEs have replied and what clauses remain pending:

```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py poll-inbox --deal-id BA-2026-AV-8921
```

**Mandatory Step After Running `poll-inbox`:**
1. Open the updated **`./cymbal_clm_redline_workbench.html`** in Spark Canvas so the user sees the live progress tracker (`3 of 4 Redlined Clauses Approved via SME Email Replies: Engineering GP1-12 ✅, Tax SP3-04 ✅, Cyber SP5-03 ✅; Remaining: GP1-19`) and the updated `BA-2026-AV-8921_Working_Review.docx`.
2. Summarize the detected Outlook Inbox SME emails and highlight that `GP1-19` (*Limitation of Liability & IP Indemnity*) is ready for final precedent verification and consolidation.

---

### D. Workflow 4 — Create or Send Final Vendor Counter-Proposal Email (`draft-vendor-reply`)

When the Contract Owner finishes consolidating the counter-proposal and asks Spark to create (or send) the transmittal email back to Adele Vance (`AdeleV@36zrbd.onmicrosoft.com`) at Apex AeroSystems with both `.docx` and `.xlsx` files attached:

- **Default (Save in Outlook `Drafts` folder with `.docx` & `.xlsx` attached):**
```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py draft-vendor-reply --deal-id BA-2026-AV-8921 --output-dir .
```
- **If the user explicitly says *"send now"*:**
```bash
python3 ~/ge_spark_workspace/skills/clm_cli.py draft-vendor-reply --deal-id BA-2026-AV-8921 --output-dir . --send
```
