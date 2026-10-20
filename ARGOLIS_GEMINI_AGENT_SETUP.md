# Argolis Gemini Enterprise (`connectors-demo_1787861880280`) Setup & Walkthrough Runbook

This guide documents the **Contract Lifecycle Management (CLM)** platform deployed in your Argolis project (`vertex-ai-demos-468803`) and wired directly into your Gemini Enterprise environment **`connectors-demo_1787861880280` (`Connectors Demo`)**:
1. **5 Installed `clm-*` Skills** (registered in Vertex AI Skill Registry `us-central1` & Agent Registry `global`/`us-central1`, plus local `.zip` & `SKILL.md` bundles):
   - `clm-contract-intake`
   - `clm-legal-ip-review`
   - `clm-tax-tariff-review`
   - `clm-eng-faa-review`
   - `clm-contract-consolidation`
2. **BigQuery Connector (`vertex-ai-demos-468803.boeing_clm`)** attached to `connectors-demo_1787861880280` (`active_deals`, `proforma_clauses`, `deal_clause_deviations`, `historical_clause_exceptions`, `clause_conflict_rules`, `sme_review_events`).
3. **Cloud Run Custom MCP Server (`https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/mcp`)** exposed to `connectors-demo_1787861880280` and registered in Agent Registry (`us-central1` & `global`), providing the 6 deterministic OOXML & BigQuery tools (`ingest_vendor_redline`, `analyze_clause_precedents`, `record_sme_position`, `harmonize_clause_conflict`, `export_counter_proposal_package`, `reset_deal_workbench`).

---

## 1. Installed `clm-*` Skills Inventory

- [`skills/clm-contract-intake/SKILL.md`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-contract-intake/SKILL.md) ([`clm-contract-intake.zip`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-contract-intake.zip))
- [`skills/clm-legal-ip-review/SKILL.md`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-legal-ip-review/SKILL.md) ([`clm-legal-ip-review.zip`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-legal-ip-review.zip))
- [`skills/clm-tax-tariff-review/SKILL.md`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-tax-tariff-review/SKILL.md) ([`clm-tax-tariff-review.zip`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-tax-tariff-review.zip))
- [`skills/clm-eng-faa-review/SKILL.md`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-eng-faa-review/SKILL.md) ([`clm-eng-faa-review.zip`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-eng-faa-review.zip))
- [`skills/clm-contract-consolidation/SKILL.md`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-contract-consolidation/SKILL.md) ([`clm-contract-consolidation.zip`](file:///Users/rahulsankrut/Desktop/code/boeing/skills/clm-contract-consolidation.zip))

---

## 2. Live Endpoints & Connected Data Stores in `connectors-demo_1787861880280`

- **Cloud Run Service URL**: `https://boeing-clm-engine-5udif2v3cq-uc.a.run.app`
- **StreamableHTTP MCP Server Endpoint**: `https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/mcp`
- **Direct `.docx` / `.xlsx` Download Routes**:
  - `https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/api/deals/BA-2026-AV-8921/export/docx`
  - `https://boeing-clm-engine-5udif2v3cq-uc.a.run.app/api/deals/BA-2026-AV-8921/export/xlsx`

---

## 3. 5-Prompt Live Walkthrough Inside Gemini Enterprise (`connectors-demo_1787861880280`)

1. **Intake & Deterministic XML Diff (`clm-contract-intake`)**:
   > *"Use `clm-contract-intake` to run `ingest_vendor_redline` on `Vendor_Redlined_GP1.docx` for Deal `BA-2026-AV-8921`, open the 12-clause Redline Triage Matrix in Canvas showing the 8 untouched clauses vs. 4 material redlines with exact `<w:del>`, `<w:ins>`, and `<w:comment>` extractions, and send the Microsoft Teams routing notifications."*
2. **Corporate Legal Precedent Review (`clm-legal-ip-review`)**:
   > *"Use `clm-legal-ip-review` to run `analyze_clause_precedents` on `GP1-19` (`GP1 §19 & §24`), display the BigQuery outcome distribution and top 5 aerospace precedents, open the Tier-1 Compromise (`2.0x PO / $90M super-cap`) in Canvas, and commit Legal's approval via `record_sme_position`."*
3. **Engineering & Cyber Regulatory Lockouts (`clm-eng-faa-review`)**:
   > *"Use `clm-eng-faa-review` to analyze `GP1-12` (FAA 14 CFR Part 21 lockout) and `SP5-03` (DFARS 252.204-7012 72-hr cyber lockout) via `analyze_clause_precedents`, and commit our `Hold Firm` positions via `record_sme_position`."*
4. **Tax vs. Procurement Cross-Clause Conflict Harmonization (`clm-tax-tariff-review`)**:
   > *"Use `clm-tax-tariff-review` to inspect the active `CONFLICT-SP3-04-GP1-03` conflict between `SP3-04` (`SP3 §4.1` Tariffs) and `GP1-03` (`GP1 §3.1` Firm-Fixed-Price SOW Cap), and call `harmonize_clause_conflict` to apply the 50/50 split capped at +2.0% of the FFP unit price."*
5. **Final Consolidation, Native Track-Changes `.docx` Export & Outlook Draft (`clm-contract-consolidation`)**:
   > *"Use `clm-contract-consolidation` to run `export_counter_proposal_package` for Deal `BA-2026-AV-8921`, present the full 12-clause Counter-Proposal and direct `.docx`/`.xlsx` download links in Canvas, upload the files to SharePoint, and stage the Microsoft Outlook response draft to Apex AeroSystems."*
