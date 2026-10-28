# Cymbal Aerospace Contract Lifecycle Management (CLM) Plugin

Standard Antigravity & Gemini Enterprise (Spark) Plugin for end-to-end Aerospace Supplier Contract Redline Intake, Playbook & BigQuery Precedent Analysis, Cross-Clause Conflict Harmonization, Word 365 Track Changes & Comments Generation, and Microsoft Outlook Routing.

## Included Customizations

- **Skills (`skills/`)**:
  - `clm-contract-intake`: Parses supplier `.docx` redlines against the Cymbal Tier-1 Avionics Playbook (`scripts/intake.py`), queries BigQuery `VECTOR_SEARCH` precedents in parallel across redlined positions, identifies SME owners, initializes the Working Review Document (`<deal_id>_Working_Review.docx`), and renders the **Progressive-Disclosure Pastel Word 365 & Playbook Reviewer UI** with the **Embedded Sidecar Agent Chat Dock**.
  - `clm-tax-tariff-review`: Executes Global Tax & Trade SME analysis on Customs, Duties & Section 232/301 Tariffs (`scripts/tax_review.py`), queries BigQuery Tax precedents, resolves cross-clause Firm-Fixed-Price SOW conflicts (`CONFLICT-SP3-04-GP1-03`), and renders the **Tunneled + Full-12-Clause Tax Reviewer UI** with the **Embedded Sidecar Agent Chat Dock**.
  - `clm-contract-consolidation`: Queries BigQuery historical precedents (`scripts/precedents.py`), records SME/Owner review positions and human-attributed Word comments (`scripts/record_position.py`), resolves cross-functional Finance vs. Legal `.docx` conflicts (`scripts/resolve_conflict.py`), and consolidates approved positions into the final `.docx` (with OOXML `<w:ins>`, `<w:del>`, and `<w:comment>`) and 4-tab `.xlsx` Deviation Matrix (`scripts/consolidate.py`).
  - `clm-comms`: Routes SME review emails in Microsoft Outlook, delivers SME review replies, polls Outlook Inbox (paired with Spark `/schedule`), sends cross-clause conflict resolution notifications, and drafts/sends the final vendor counter-proposal transmittal email (`scripts/outlook_comms.py`).
  - `clm-ux-design-system`: Reusable design system and layout guidelines for the Pastel Word 365 & Playbook CLM Reviewer UI (Progressive-Disclosure Options, 3-Pane Workbench, and Embedded Sidecar Agent Chat Dock).
- **Rules (`rules/AGENTS.md`)**:
  - Enforces real backend execution (live `.docx` parsing, parallel BigQuery `VECTOR_SEARCH`, Vertex AI Gemini 2.5 Flash rewrites) and strict single-responsibility skill boundaries (never bundling unrequested SharePoint uploads or email sends into CLM analysis skills).
- **Sidecar (`sidecars/cymbal-clm-workbench/`)**:
  - Auxiliary pane web views for the CLM Redline Workbench (`/`), Tax SME Reviewer (`/tax-workbench`), and Progressive-Disclosure UX Evaluation Lab (`/ui-lab`), bridged to `/preload.js` (`window.sidecar.agent.sendMessage` & `window.sidecar.ui.toggleAuxPane`) and `/api/ask-agent`.
