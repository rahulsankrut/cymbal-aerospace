# Teamwork Briefing — Phase 2: CLM User Interface & Experience Research, Skill Discovery, & 12-Variation Mockup Lab

## 1. Mission
Conduct a rigorous, multi-agent UX research and design exploration for **Cymbal Aerospace CLM (`BA-2026-AV-8921`)**, discover and safely install helpful UI/UX skills, synthesize a comprehensive UX Architecture Plan, and build an interactive **12-Variation CLM UI Mockup Lab (`cymbal_clm_ui_lab_12_variations.html`)** with a built-in User Testing & Notes Evaluator so the user can test every competing UX paradigm side-by-side, take notes, score each variation, and choose which features to incorporate into the production skills.

## 2. Frozen Domain Contracts (Do Not Modify Without Approval)
- `specs/01_bq_schema.sql`
- `specs/02_domain_models.py`
- `specs/03_mcp_and_rest_contract.md`
- `skills/cymbal_clm_seed.json`

## 3. Research & Design Subagent Roster
1. **`researcher_clm_leaders` (`research` / `self`)**:
   - Research competing commercial AI CLM & LegalTech UX paradigms:
     1. **Spellbook / Robin AI / Ivo (Word-Native Floating Action Card on Emerald Stage)** — inspired by the user's screenshot (`media_1792469698101_00b1ca98.png`)
     2. **Ironclad AI Assist / Jurist (Split Document + Playbook Guardrail Sidebar)**
     3. **Luminance Legal-Grade AI (Traffic-Light Risk Heatmap & Clause Deviance Radar)**
     4. **Icertis Contract Intelligence (Enterprise Obligation, Guardrail & Financial Exposure Cockpit)**
     5. **Litera Kira / Compare (3-Column Synchronized Diff: Baseline vs. Vendor Redline vs. Counter-Proposal)**
     6. **SpotDraft VerifAI / Juro (Guided Step-by-Step Decision Wizard & Approver Sign-Off Flow)**
     7. **Cymbal Institutional Dark Terminal (Bloomberg/Cymbal Capital Style with Live BigQuery SQL & Vector Search Drawer)** — inspired by Cymbal Capital screenshots (`view_1_portfolio.png`, `view_4_compliance.png`)
     8. **Kanban / Multi-SME Routing & Live Outlook Thread Board (Linear / Jira Style SME Workflow)**
     9. **Interactive Redline Timeline & Negotiation Round Replay (GitHub PR / Version Diff Scrubbing)**
     10. **Cross-Clause Dependency & Conflict Graph Explorer (Visual Node Graph linking `SP3 §4.1` <-> `GP1 §3.1` FFP Ceiling & FAA/DFARS Lockouts)**
     11. **Executive Decision Brief & One-Click Redline Approval Deck (Bento Grid Deal Room)**
     12. **Conversational AI Co-Pilot + Live Redline Canvas Split-View (Harvey / Claude Artifacts / Canvas Style)**
   - Output file: `.agents/teamwork/researcher_clm_leaders/handoff.md`

2. **`researcher_ui_skills` (`self`)**:
   - Search `modern-web-guidance` (`npx -y modern-web-guidance@latest search ...`), local Antigravity skills (`generative_ui`, `building-data-apps`, `a11y-debugging`), and public skill repositories for UI/UX design skills.
   - Retrieve relevant `modern-web-guidance` best practices (popovers/floating menus, view transitions, container queries, `:has()` state styling, accessible focus management).
   - Safely author and install a reusable **`clm-ux-design-system`** skill in `.agents/skills/clm-ux-design-system/SKILL.md` (and sync to `skills/clm-ux-design-system/SKILL.md`) encoding the discovered UI patterns, typography, color tokens, redline diff micro-interactions, and accessibility rules.
   - Output file: `.agents/teamwork/researcher_ui_skills/handoff.md`

3. **`researcher_ux_patterns` (`self`)**:
   - Analyze the 4 Cymbal Aerospace CLM workflows (`clm-contract-intake`, `clm-comms`, `clm-tax-tariff-review`, `clm-contract-consolidation`) and map out the cognitive ergonomics for both personas:
     - **Contract Owner / Procurement Lead (Rahul Kasanagottu)**
     - **Domain SME Reviewers (Pradeep Gupta — Tax, Megan Bowen — FAA/Eng, Alex Wilber — Cyber, Lee Gu — Legal)**
   - Design the UX Evaluation Matrix & Note-Taking Harness requirements so the user can test all 12 variations interactively, rate them (1–5 stars), tag pros/cons, and export/save their design decisions directly to `ux_evaluation_notes.json` or clipboard.
   - Output file: `.agents/teamwork/researcher_ux_patterns/handoff.md`
