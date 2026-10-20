# Argolis Gemini Enterprise (`connectors-demo_1787861880280`) & Spark Setup Runbook — Cymbal Aerospace CLM

This guide documents the **Cymbal Aerospace Contract Lifecycle Management (CLM)** platform deployed in your Argolis project (`vertex-ai-demos-468803`), wired into **Gemini Enterprise (`connectors-demo_1787861880280`) / Spark (`~/ge_spark_workspace/skills`)**, and packaged as a **Dual-Runtime Antigravity UI Sidecar Plugin** ([`plugin.json`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/plugin.json) + [`sidecar.json`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/sidecars/cymbal-clm-workbench/sidecar.json)):

1. **4 Focused `clm-*` Skills** (synced to `skills/`, `.agents/skills/`, and `~/ge_spark_workspace/skills/`):
   - [`clm-contract-intake`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/skills/clm-contract-intake/SKILL.md) — Contract intake, SharePoint upload, **Cymbal Tier-1 Avionics Playbook (`GP1 / SP3 / SP5`)** diff, BigQuery precedent check across all 4 positions (`64` deals, `16` per clause), SME owner lookup, `BA-2026-AV-8921_Working_Review.docx` initialization, and **Pastel Word 365 & Playbook Review Workbench UI**.
   - [`clm-comms`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/skills/clm-comms/SKILL.md) — Dedicated Microsoft Outlook Graph API communications (`route-smes`, `send-sme-reply`, `poll-inbox`, `draft-vendor-reply`) so `Bake CLM demo` leaves Outlook `Drafts` at **`0`** until prompted live.
   - [`clm-tax-tariff-review`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/skills/clm-tax-tariff-review/SKILL.md) — Tax SME Playbook review on `SP3 §4.1`, 16 BigQuery Tax precedents (`63%` 50/50 split above `5.0%` threshold, capped at **`+2.0% ($900,000)`**), `CONFLICT-SP3-04-GP1-03` harmonization with `GP1 §3.1` (`$45M` FFP SOW), and **Pastel Tax SME Reviewer Workbench UI**.
   - [`clm-contract-consolidation`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/skills/clm-contract-consolidation/SKILL.md) — Owner precedent check across all 4 positions (`precedents --clause-id ALL`), consolidation of `BA-2026-AV-8921_Working_Review.docx` into sanitized **`BA-2026-AV-8921_Cymbal_Counter_Proposal.docx`** and **`BA-2026-AV-8921_SharePoint_Deviation_Matrix.xlsx`** with human-user-attributed Word comments (`w:author="<User>"`), and live SharePoint upload.
2. **BigQuery Connector (`vertex-ai-demos-468803.boeing_clm`)**:
   - Tables: `active_deals`, `proforma_clauses`, `deal_clause_deviations`, `historical_clause_exceptions` (64 Tier-1 Avionics precedents with 768-dim `text_embedding_005` vectors), `clause_conflict_rules`, `sme_review_events`.
3. **Cloud Run Custom MCP & REST Server (`https://boeing-clm-engine-5udif2v3cq-uc.a.run.app`) + Host Loopback Bridge (`http://127.0.0.1:58921`)**:
   - Exposes `/mcp` (6 FastMCP tools), REST endpoints (`/api/deals/BA-2026-AV-8921/...`), and the local Dual-Runtime Sidecar / Spark Canvas Loopback Bridge (`GET /`, `GET /tax-workbench`, `GET /ui-lab`, `GET /preload.js`, `POST /api/review`, `POST /run`, `GET /api/download/working-docx`, `GET /api/download/counter-docx`).

---

## Live 4-Workflow Demo Script

See [`CYMBAL_AEROSPACE_DEMO_GUIDE.md`](file:///Users/rahulsankrut/Desktop/code/Cymbal%20Aerospace/CYMBAL_AEROSPACE_DEMO_GUIDE.md) for the pre-demo reset command (`Bake CLM demo`) and the exact 4-workflow copy-paste prompts.
