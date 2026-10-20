---
name: clm-comms
description: CLM Email Routing, SME Reply Delivery, Outlook Inbox Polling (including Spark /schedule recurring automations), and Vendor Counter-Proposal Transmittal for Cymbal Aerospace. Use whenever the user asks to save or send the SME review routing emails in Microsoft Outlook, send an SME review reply back to the Contract Owner's Inbox, poll Outlook Inbox for SME review updates (on-demand or via /schedule), or save/send the final consolidated Counter-Proposal email with .docx and .xlsx attachments back to the vendor.
---

# Cymbal Aerospace CLM — Microsoft Outlook Communications & Scheduled Inbox Polling (`clm-comms`)

Use this skill ONLY when the user explicitly asks to perform an email communication action in Microsoft Outlook (`m365-admin@rahulsankrut.demo.altostrat.com`) via `scripts/outlook_comms.py`:
1. **Route SME Review Emails** (`route-smes` — save to `Drafts` or `--send` immediately)
2. **Send SME Review Reply to Contract Owner's Inbox** (`send-sme-reply` — e.g., `--clause-id SP3-04` for Tax SME reply, or `--clause-id GP1-12,SP3-04,SP5-03` for all 3 external SMEs)
3. **Poll Contract Owner's Outlook Inbox for SME Replies** (`poll-inbox` — runs on-demand or as the action inside a Spark `/schedule` recurring automation)
4. **Draft or Send Final Vendor Counter-Proposal Reply with `.docx` & `.xlsx` Attachments** (`draft-vendor-reply` — save to `Drafts` or `--send` immediately)

---

## Action 1 — Route the 4 SME Review Emails in Microsoft Outlook (`route-smes`)

When the Contract Owner asks to save the 4 SME review routing emails in Outlook `Drafts` (or send them immediately):

- **Save in Outlook `Drafts` (default)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py route-smes --deal-id BA-2026-AV-8921
  ```
- **Send immediately via Outlook (`--send`)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py route-smes --deal-id BA-2026-AV-8921 --send
  ```

Present a Markdown table from `outlook_sme_routing_emails` showing the SME Team, Recipient (`to`), Subject (`subject`), Clause (`clause_ref`), and Outlook Status (`status` / `outlook_folder`).

---

## Action 2 — Send an SME Review Reply Email to the Contract Owner's Inbox (`send-sme-reply`)

When an SME (such as Pradeep Gupta in Global Tax & Trade) finishes reviewing a clause and asks to send their SME review update email back to the Contract Owner's Outlook Inbox (`m365-admin@rahulsankrut.demo.altostrat.com`):

- **Send only the Tax SME reply (`--clause-id SP3-04`)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py send-sme-reply --deal-id BA-2026-AV-8921 --clause-id SP3-04
  ```
- **Deliver all 3 external SME replies (`--clause-id GP1-12,SP3-04,SP5-03` or `--clause-id ALL`)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py send-sme-reply --deal-id BA-2026-AV-8921 --clause-id ALL
  ```

Report the delivered email subject(s), sender(s), recipient (`recipient_contract_owner`), and delivery status from `sme_reply_emails_delivered_to_owner_inbox`.

---

## Action 3 — Poll Outlook Inbox for SME Replies (On-Demand or via Spark `/schedule`)

When the Contract Owner asks to poll their Outlook Inbox for SME review replies — either as an immediate check or by setting up a recurring **Spark `/schedule`** automation (`automation` skill):

```bash
python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py poll-inbox --deal-id BA-2026-AV-8921
```

### How `poll-inbox` Works with Spark `/schedule`:
- When the user invokes `/schedule` (or asks to schedule a recurring inbox poller for Deal `BA-2026-AV-8921`), configure the scheduled automation prompt to run `outlook_comms.py poll-inbox --deal-id BA-2026-AV-8921` (or check Outlook via `gemini-enterprise-connectors` and record each detected `[SME REVIEW UPDATE: ...]` decision via `record_position.py`).
- `poll-inbox` queries `m365-admin@rahulsankrut.demo.altostrat.com`'s live Outlook `Inbox` for messages matching `[SME REVIEW UPDATE: ...]`, parses which SME teams have replied (`sme_update_emails_detected`), updates only those clauses in `<deal_id>_Working_Review.docx` (`sme_positions_synced`), refreshes `cymbal_clm_redline_workbench.html`, and reports `progress_summary` and `remaining_for_owner_review`.

Present:
1. The detected SME reply emails from `sme_update_emails_detected` (sender, subject, received timestamp).
2. The updated clause sign-off tracker (`progress_summary` and `sme_positions_synced`) and any clauses still in `remaining_for_owner_review`.
3. A clickable Markdown link to `[cymbal_clm_redline_workbench.html](cymbal_clm_redline_workbench.html)` and `[BA-2026-AV-8921_Working_Review.docx](BA-2026-AV-8921_Working_Review.docx)`.

---

## Action 4 — Send Conflict Resolution Communication Email ("Legal Takes Precedence") (`send-conflict-resolution`)

When the Contract Owner resolves the Stage 2 Finance vs. Legal conflict on `Deal BA-2026-TR-5510` (Vanguard Thrust Systems Corp.) and asks to shoot an email back to Finance (`Diego Siciliani`) and Legal (`Miriam Graham`) confirming that **Corporate Legal Playbook guardrails take precedence over commercial discount trade-offs**:

- **Send immediately via Outlook (`--send`)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py send-conflict-resolution --deal-id BA-2026-TR-5510 --send
  ```
- **Save in Outlook `Drafts`**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py send-conflict-resolution --deal-id BA-2026-TR-5510
  ```

---

## Action 5 — Draft or Send the Final Vendor Counter-Proposal Reply (`draft-vendor-reply`)

When the Contract Owner asks to draft (or send) the official Counter-Proposal reply email to the vendor (e.g., `LidiaH@36zrbd.onmicrosoft.com` at Meridian Landing Gear Corp. for Stage 3 `BA-2026-LG-7740`, or `AdeleV@36zrbd.onmicrosoft.com` at Apex AeroSystems for `BA-2026-AV-8921`) with `<deal_id>_Cymbal_Counter_Proposal.docx` and `<deal_id>_SharePoint_Deviation_Matrix.xlsx` attached:

- **Send immediately via Outlook (`--send`)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py draft-vendor-reply --deal-id BA-2026-LG-7740 --output-dir . --send
  ```
- **Save in Outlook `Drafts` (default)**:
  ```bash
  python3 /Users/rahulsankrut/ge_spark_workspace/skills/clm-comms/scripts/outlook_comms.py draft-vendor-reply --deal-id BA-2026-LG-7740 --output-dir .
  ```

Report the recipient (`to`), CC list (`cc`), subject (`subject`), attached files (`attachments`), and Outlook folder/status (`outlook_folder`, `status`) from `outlook_vendor_counter_proposal_email`.
