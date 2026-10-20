# Competitive CLM & LegalTech UX Research Report: 12 UI Paradigms for Cymbal Aerospace (`BA-2026-AV-8921`)

**Author:** `researcher_clm_leaders` (Competitive UX Research Subagent)  
**Target Deal Context:** Cymbal Aerospace Deal `BA-2026-AV-8921` (*Apex AeroSystems — $45,000,000 Firm-Fixed-Price Avionics Subsystem, GP1 + SP3 + SP5*)  
**Dataset & Domain Anchors:**
- **12 Total Clauses:** 8 untouched auto-cleared baseline clauses + 4 material vendor redlines (`GP1-12` Warranty & FAA Source Inspection, `GP1-19` Liability Cap & IP Indemnity, `SP3-04` Section 232/301 Tariffs, `SP5-03` 72-Hr DFARS Cyber Reporting).
- **64 BigQuery Historical Precedents:** `16` Tier-1 Avionics deals per redlined clause (`vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`) with outcome distributions (`HELD_FIRM`, `COMPROMISE_TIER_1`, `ACCEPTED_VENDOR`) and cosine similarity scores (`text-embedding-005`).
- **Inter-Team Cross-Clause Conflict:** `CONFLICT-SP3-04-GP1-03` (`SP3 §4.1` uncapped >5% tariff surcharge vs. `GP1 §3.1` $45M Firm-Fixed-Price SOW lock) + 2 Regulatory Lockouts (`LOCKOUT-GP1-12-FAA` 14 CFR Part 21.140 and `LOCKOUT-SP5-03-DFARS` DFARS 252.204-7012).
- **Human-Attributed Word Comments (`w:author`):** All comments written to `BA-2026-AV-8921_Working_Review.docx` (`word/comments.xml`) are strictly attributed to the human reviewer (`Rahul Kasanagottu`, `Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`) — never a generic system/AI bot label.

---

## Executive Synthesis & Comparative Taxonomy

Modern Contract Lifecycle Management (CLM) and LegalTech AI platforms split into **four primary cognitive schools**:
1. **Document-Native & Word-Centric Paradigms (Variations 1, 9):** Prioritize spatial familiarity by keeping the contract sheet at the center of gravity and overlaying surgical floating popovers (`Ivo`, `Spellbook`, `Robin AI`) or native OOXML ribbons and margin balloons (`MS Word 365`).
2. **Playbook-Guided & Triage Paradigms (Variations 2, 3, 6):** Pair the document with structured guardrail intelligence (`Ironclad Jurist/AI Assist`), visual anomaly heatmaps (`Luminance`), or keyboard-first sequential decision wizards (`SpotDraft VerifAI` / `Superhuman`).
3. **Analytical, Diff-Matrix & Graph Paradigms (Variations 4, 5, 8, 10):** Treat contract negotiation as structured data or code inspection via 3-column synchronized diffs (`Litera Compare` / `Kira`), institutional dark data terminals (`Cymbal Capital` / `Bloomberg`), dependency graphs (`Cross-Clause Graph`), or line-numbered pull requests (`GitHub PR Diff`).
4. **Orchestration, Executive & Co-Pilot Paradigms (Variations 7, 11, 12):** Optimize for multi-party workflow tracking (`Linear`/`Outlook Kanban`), C-suite financial exposure sign-off (`Bento Deal Room` / `Icertis`), or generative prompt-to-canvas co-editing (`Harvey AI` / `Claude Artifacts`).

| # | Variation Name | Commercial Inspiration | Primary Cognitive Mode | Best Persona Fit |
| :--- | :--- | :--- | :--- | :--- |
| **V1** | **Document-Centric Floating Action Menu on Emerald Stage** | Ivo AI, Spellbook, Robin AI (`media_1792469698101_00b1ca98.png`) | Surgical in-place redline resolution | Domain SMEs (Tax, Eng, Cyber, Legal) & Contract Owner |
| **V2** | **Split-Pane Contract Reader + Playbook Guardrail Sidebar** | Ironclad AI Assist / Jurist | Playbook rule & precedent verification alongside doc | Corporate Legal (`Lee Gu`) & Contract Owner (`Rahul K.`) |
| **V3** | **Traffic-Light Clause Risk Heatmap & Deviation Radar** | Luminance Legal-Grade AI | Rapid visual anomaly triage across all 12 clauses | Contract Owner Intake & Risk/Compliance Leads |
| **V4** | **3-Column Synchronized Redline Matrix** | Litera Compare, Kira Systems | Simultaneous Proforma vs. Vendor vs. Counter comparison | Legal Counsel, Procurement Specialists, Redline Drafters |
| **V5** | **Institutional Dark Analytics Terminal + BigQuery Drawer** | Cymbal Capital (`view_1_portfolio.png`, `view_4_compliance.png`), Bloomberg | Quantitative precedent telemetry & vector search audit | Quantitative Tax/Procurement Analysts & Data-Driven Owners |
| **V6** | **Guided Step-by-Step Decision Wizard & Focus Mode** | SpotDraft VerifAI, Juro, Superhuman | Distraction-free, keyboard-driven (`J/K/A/R/C`) queue | Time-constrained SME Approvers (FAA, Cyber, Tax) |
| **V7** | **Multi-SME Swimlane & Live Outlook Thread Kanban Board** | Linear, Jira, Microsoft Outlook Deep-Link | Asynchronous cross-team routing & email polling state | Contract Owner (`Rahul Kasanagottu`) & PMO |
| **V8** | **Cross-Clause Dependency & Financial Impact Graph Explorer** | Palantir Foundry, Neo4j Bloom, System Architecture | Structural conflict detection (`SP3 §4.1` ↔ `GP1 §3.1`) | Procurement Lead, Tax Director (`Pradeep Gupta`), Systems Eng |
| **V9** | **MS Word Ribbon & Margin Balloon Track-Changes Simulator** | Microsoft Word 365 Desktop (OOXML `<w:del>`, `<w:ins>`, `<w:comment>`) | Zero-learning-curve legal document editing & margin balloons | Traditional Legal Counsel & External Vendor Counterparts |
| **V10** | **GitHub Pull Request / Code Review Style Clause Diff** | GitHub PR Review, GitLab Diff, Critique | Line-numbered unified/split diff with inline review threads | Cyber SME (`Alex Wilber`), Software/Avionics QA (`Megan Bowen`) |
| **V11** | **Executive Bento Deal Room & CFO/GC Approval Cockpit** | Icertis Executive Cockpit, Apple Bento UI | Dollarized risk waterfall, precedent rings & 1-click sign-off | VP Procurement, CFO, General Counsel (1:30 PM & 4:00 PM Gates) |
| **V12** | **Conversational AI Co-Pilot + Live Contract Canvas Split** | Harvey AI, Claude Artifacts, Gemini Canvas | Natural-language prompt-to-rewrite with live document diff | Contract Owner & Legal SMEs iterating custom counter-clauses |

---

## Detailed Analysis of All 12 Variations

---

### Variation 1: Document-Centric Floating Action Menu on Emerald Stage (Ivo / Spellbook / Robin AI Style)

#### 1. Core UX Metaphor & Inspiration
Directly modeled after the user's reference screenshot (`media_1792469698101_00b1ca98.png`) and modern Word-integrated AI contract assistants (**Ivo AI**, **Spellbook**, **Robin AI**). The metaphor is a **focused legal paper sheet resting on a rich emerald-green desk stage**, accompanied by an elevated, high-contrast **Floating Action Card** hovering over the right edge of the document. Rather than overwhelming the reviewer with multi-tab enterprise chrome, it brings the exact clause under review and its 4 core resolution actions (`✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, `💬 Comment`) into immediate visual proximity.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Centered radial emerald stage (`border-radius: 16px`, `padding: 32px`) housing a crisp white document card (`max-width: 780px`, `border-radius: 12px`, `box-shadow: 0 18px 40px rgba(0,0,0,0.22)`) overlapped on the right by a floating white action menu card (`width: 280px`, `border-radius: 12px`, `box-shadow: 0 20px 44px rgba(0,0,0,0.28)`). Below or collapsible beneath the stage sits a clean Precedent & Comment Drawer.
- **Color Palette:**
  - **Stage Background:** Deep Emerald radial gradient (`#237a5b` to `#1d694d`).
  - **Document Surface:** Pure warm white (`#fcfcfa` / `#ffffff`) with `#0f172a` primary heading ink and `#94a3b8` muted preamble context text.
  - **Inline Diff Tokens:** Rejected vendor redline rendered in **orange-red strikethrough** (`#e04f33`, `2px` solid line-through); proposed Cymbal counter-position rendered in **warm coral/salmon highlight pill** (`background: #f9d8d0`, `color: #1e293b`, subtle bottom border `#e04f33`).
  - **Action Menu Accents:** Dark charcoal icon circle (`#18181b`) for `Rewrite with Input`, hover row highlight (`#f1f5f9`), crisp check (`✓`), cross (`✕`), and speech bubble (`💬`) icons.
- **Typography:** Clean geometric sans-serif (`Inter` / `-apple-system`) for both document headings (`18px` bold) and clause prose (`15px`, `line-height: 1.75`) to match `media_1792469698101_00b1ca98.png`.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- **Pending Review State (Default):** The clause paragraph displays a direct word-level diff between the vendor's unacceptable markup (shown with orange-red strikethrough `<del class="counter-del">`) and Cymbal's recommended Playbook counter-position (shown with coral highlight `<ins class="counter-ins">`). Surrounding untouched preamble text is softly dimmed (`color: #94a3b8`) to draw the eye immediately to the operative redline.
- **Clean Accepted State (`✓ Accept changes` clicked):** The orange-red strikethroughs and coral highlights dissolve smoothly into a clean, authoritative contract paragraph (`#0f172a`) framed by a subtle emerald left border (`4px solid #10b981`) and a `"✓ Change Accepted in Working Doc"` pill, with a 1-click toggle (`🔍 Inspect Redline Strikethrough`) to restore the markup view at any time.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **User Comments (`w:author`):** Clicking `💬 Comment` opens an inline drawer directly beneath the clause pre-populated with the active human reviewer's identity (`Rahul Kasanagottu` for Owner or `Pradeep Gupta` / `Megan Bowen` / `Lee Gu` / `Alex Wilber` for SMEs). Submitting writes `<w:comment w:author="Pradeep Gupta">` into `BA-2026-AV-8921_Working_Review.docx` and renders an inline author badge on the document sheet.
- **BigQuery Precedents (64 Deals):** A compact horizontal distribution bar (`16` Tier-1 Avionics deals for the active clause) and expandable precedent cards sit just below the emerald stage, allowing the reviewer to click any historical deal (e.g., `Safran`, `Spirit AeroSystems`, `Thales`) to inject its language into `✦ Rewrite with Input`.

#### 5. Best Persona Fit
- **Primary:** Domain SME Reviewers (`Pradeep Gupta` in Tax, `Megan Bowen` in Engineering/FAA, `Alex Wilber` in Cyber, `Lee Gu` in Legal) who want an intuitive, low-friction approval surface, as well as the Contract Owner (`Rahul Kasanagottu`) during live executive demos.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Exact visual match to the user's target reference screenshot (`media_1792469698101_00b1ca98.png`).
  - Highest visual polish and lowest cognitive load for single-clause counter-position review.
  - Makes the distinction between rejected text (strikethrough), proposed text (coral highlight), and accepted clean text crystal clear.
- **Cons:**
  - Focuses primarily on one active clause at a time; requires a clause switcher pill bar or full-doc toggle to scan all 12 clauses simultaneously.

---

### Variation 2: Split-Pane Contract Reader + Playbook Guardrail & Precedent Sidebar (Ironclad AI Assist / Jurist Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Ironclad AI Assist** and **Ironclad Jurist**. The core metaphor is a **synchronized two-column legal workbench**: the left 60% of the viewport is a continuous, scrollable full-contract reader showing all 12 clauses in context, while the right 40% is an intelligent **Playbook Guardrail & Precedent Copilot Sidebar** that dynamically locks onto whichever clause is clicked or scrolled into view.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Full-height (`calc(100vh - 120px)`) CSS Grid (`grid-template-columns: 7fr 5fr`, `gap: 20px`). Left pane has sticky document navigation pills (`All 12`, `4 Redlined`, `1 Conflict`) and continuous paper scroll; right pane has sticky tabs (`Playbook Guardrails`, `BQ Precedents (16)`, `Word Comments`).
- **Color Palette:**
  - **App Shell:** Cool enterprise alabaster (`#f8fafc`) with slate borders (`#e2e8f0`).
  - **Playbook Guardrail Cards:** Indigo AI accent (`#4f46e5` / `#eef2ff`) for AI-recommended Tier-1 fallbacks, crimson (`#dc2626` / `#fef2f2`) for FAA/DFARS regulatory lockouts, and amber (`#d97706` / `#fffbeb`) for cross-clause conflicts.
- **Typography:** Serif or high-legibility legal body font (`Georgia` or `Inter` `14.5px`) in the left contract reader; crisp UI sans-serif (`Inter` `13px`) with monospace badges (`JetBrains Mono`) in the right Playbook sidebar.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- **In the Left Document Reader:** All 8 untouched clauses render in clean black text with a subtle green `"✓ Auto-Cleared Proforma"` margin tag. The 4 redlined clauses (`GP1-12`, `GP1-19`, `SP3-04`, `SP5-03`) highlight inline `<del>` and `<ins>` spans.
- **One-Click Playbook Application:** In the right sidebar, each Playbook tier (`Tier-1 Compromise`, `Hold Firm`, `Accept Vendor`) is presented as a card with a `[Apply to Contract]` button. Clicking it animates the left document clause from redline diff to clean accepted text in real time.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Built directly into the right sidebar's **Precedent Intelligence Card**, showing the `n=16` distribution bar for the active clause alongside top cosine-similarity matches (`96.2%`, `94.0%`) that can be inserted with one click.
- **User Comments (`w:author`):** Displayed in a dedicated sidebar comment composer and inline badge attached to the active clause card, showing the human author (`e.g., Lee Gu — Corporate Legal`) and syncing to `word/comments.xml`.

#### 5. Best Persona Fit
- **Primary:** Corporate Legal Counsel (`Lee Gu`) and Senior Contract Owners (`Rahul Kasanagottu`) who never want to lose sight of the full 12-clause contract context while evaluating playbook rules and historical precedents.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Eliminates context switching between the full 12-clause contract and the AI Playbook/BigQuery precedent evidence.
  - Industry-standard layout familiar to enterprise CLM users (Ironclad, Agiloft, DocuSign CLM).
- **Cons:**
  - Denser horizontal information layout than Variation 1; on narrower viewports, the 60/40 split leaves less horizontal breathing room per line.

---

### Variation 3: Traffic-Light Clause Risk Heatmap & Deviation Radar (Luminance Legal-Grade AI Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Luminance Legal-Grade AI** (Corporate / Autopilot view). Luminance's signature UX innovation is the **Clause Anomaly Heatmap & Traffic-Light Matrix**, which visually maps every clause of an incoming third-party or vendor-redlined contract into a proportional grid of **Red (Critical Blocker / Regulatory Lockout)**, **Amber (Negotiable Deviation / Cross-Clause Conflict)**, and **Green (Standard / Untouched Proforma)** tiles before the lawyer reads a single sentence.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Top **12-Tile Interactive Clause Heatmap Grid** + **Radar/Deviation Distribution Strip** occupying the upper 35% of the screen, paired with a lower **Deep-Dive Clause Inspector & Resolution Deck** occupying the bottom 65%.
- **Color Palette:**
  - **Red Traffic-Light (`CRITICAL`):** `#ef4444` border/badge, `#fef2f2` surface (`GP1-12` FAA Lockout, `SP5-03` DFARS Lockout, `SP3-04` FFP Conflict).
  - **Amber Traffic-Light (`HIGH / NEGOTIABLE`):** `#f59e0b` border/badge, `#fffbeb` surface (`GP1-19` Liability Cap & IP Indemnity).
  - **Green Traffic-Light (`AUTO-CLEARED / RESOLVED`):** `#10b981` border/badge, `#ecfdf5` surface (`GP1-01`, `GP1-03`, `GP1-07`, `GP1-09`, `GP1-14`, `GP1-15`, `SP3-01`, `SP5-01`, plus any redlined clause once accepted).
- **Typography:** Bold tabular numbers (`JetBrains Mono`) for deviation percentages, cosine distances from Cymbal Proforma baseline, and risk scores; clean sans-serif for clause inspection.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Clicking any tile in the 12-clause heatmap opens its inline diff in the lower Inspector Deck.
- When a reviewer accepts a counter-position (or resolves the `SP3-04` conflict), the corresponding tile in the top heatmap **physically transitions from Red/Amber to Emerald Green (`✓ RESOLVED`)**, giving an immediate macro-level visual reward as the deal moves toward 100% green readiness.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Each heatmap tile displays a mini **Precedent Anomaly Gauge** (e.g., `"0% Historical Vendor Acceptance in 16 Deals"` on `GP1-12` and `SP5-03`, immediately justifying the Red traffic light). The lower inspector lists the exact BigQuery rows.
- **User Comments (`w:author`):** Heatmap tiles display a comment indicator icon (`💬 1`) with a hover tooltip showing the human author (`Megan Bowen`, `Pradeep Gupta`, etc.), editable in the lower inspector.

#### 5. Best Persona Fit
- **Primary:** Contract Owner (`Rahul Kasanagottu`) at **Workflow 1 (Intake Triage)** and **Workflow 4 (Pre-Dispatch Audit)**, where the primary goal is spotting which of the 12 clauses deviate from standard and tracking how many Red/Amber blockers remain.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Instant macro-level situational awareness across all 12 clauses (`8 Green`, `1 Amber`, `3 Red`).
  - Gamified visual progress as Red/Amber tiles flip to Green upon SME sign-off.
- **Cons:**
  - Less document-like than Variations 1 or 9; treats clauses as discrete modular tiles rather than continuous prose.

---

### Variation 4: 3-Column Synchronized Redline Matrix — Proforma vs. Vendor Markup vs. Clean Counter-Position (Litera Compare / Kira Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Litera Compare** and **Litera Kira**. In high-stakes aerospace and M&A negotiations, legal and procurement teams frequently struggle with "redline-on-redline" confusion (understanding whether a strikethrough is deleting the buyer's original proforma or deleting the vendor's redline). The **3-Column Synchronized Redline Matrix** eliminates this ambiguity by placing **Column 1 (Cymbal Proforma Baseline)**, **Column 2 (Apex AeroSystems Vendor Redline vs. Proforma)**, and **Column 3 (Cymbal Proposed Counter-Position + Live Editable Preview)** side by side in horizontally aligned rows.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Full-width (`100%`) 3-column comparison grid (`grid-template-columns: repeat(3, 1fr)`, `gap: 12px`) with synchronized row heights per clause and a sticky top column header bar. Below each 3-column clause row sits an expandable **Precedent & Word Comment Action Bar**.
- **Color Palette:**
  - **Column 1 Header (Cymbal GP1/SP3/SP5 Proforma):** Slate/Navy (`#f1f5f9` bg, `#0f172a` text, `#cbd5e1` border).
  - **Column 2 Header (Apex AeroSystems Redline):** Rose/Crimson tint (`#fef2f2` bg, `#991b1b` text, `#fecaca` border) with red strikethroughs on deleted Cymbal text and red/amber highlights on vendor insertions.
  - **Column 3 Header (Cymbal Counter-Position to Accept):** Emerald/Mint tint (`#ecfdf5` bg, `#065f46` text, `#a7f3d0` border) with a toggle between `Counter Diff vs. Vendor` (showing orange-red strikethrough on rejected vendor asks) and `Clean Final Text`.
- **Typography:** Tightly calibrated `13.5px` body copy with identical `line-height: 1.65` across all 3 columns so corresponding sentences align horizontally.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Column 2 always preserves the historical forensic diff (`Proforma → Vendor Redline`).
- Column 3 has an instant header toggle (`[Show Counter Diff]` vs. `[Show Clean Accepted Text]`) and an inline `[✓ Accept & Lock Column 3]` button per clause, plus live inline editing right inside Column 3.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** A compact **Precedent Strip** spans across the top of each 3-column clause row showing the 16-deal BigQuery breakdown (`e.g., GP1-19: 69% Tier-1 Compromise [11/16] | 25% Held Firm [4/16] | 6% Vendor [1/16]`) with quick-fill buttons that populate Column 3.
- **User Comments (`w:author`):** Attached directly beneath Column 3 as a Word Comment Footer (`Author: Rahul Kasanagottu / SME`), showing the exact rationale that will be embedded in the exported `.docx` and `.xlsx` deviation matrix.

#### 5. Best Persona Fit
- **Primary:** Detail-oriented Procurement Negotiators, Legal Drafters, and Export/Consolidation Reviewers (`Workflow 4: clm-contract-consolidation`) who must verify the exact delta across all three versions before generating the final `.docx` and 4-tab `.xlsx`.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Zero ambiguity about "what changed from Proforma to Vendor" vs. "what changed from Vendor to Counter-Proposal."
  - Mirrors the structure of the exported SharePoint `BA-2026-AV-8921_Deviation_Matrix.xlsx`.
- **Cons:**
  - Requires wide desktop horizontal real estate (`>= 1280px`) to display three columns of legal prose comfortably.

---

### Variation 5: Institutional Dark Analytics Terminal with Collapsible BigQuery SQL & Vector Search Drawer (Cymbal Capital / Bloomberg Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by the **Cymbal Capital Institutional Dark Terminal** screenshots (`view_1_portfolio.png` and `view_4_compliance.png`) and the **Bloomberg Terminal**. This variation reframes contract review as **quantitative risk & precedent intelligence**: every vendor redline is treated as an institutional risk position backed by live **BigQuery Vector Search (`text-embedding-005`)**, cosine similarity telemetry, dollarized exposure metrics (`$45M FFP`, `$90M 2x Super-Cap`, `$900K 2% Tariff Cap`), and an inspectable **BigQuery SQL & Vector Search Execution Drawer**.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** High-density institutional dark workspace:
  - **Top Telemetry Ticker & KPI Bar:** 4 dark glass metric cards (`Deal Exposure: $45.0M FFP`, `BigQuery Corpus: 64 Tier-1 Precedents (16/Clause)`, `Active Conflicts: 1 Critical`, `Regulatory Lockouts: 2 Active`).
  - **Main Split Grid (`4fr 8fr`):** Left clause blotter table with risk badges and similarity scores; right split between the **Dark-Mode Redline Diff Inspector** and the **Collapsible BigQuery SQL & Vector Search Telemetry Drawer**.
- **Color Palette:**
  - **Primary Canvas:** Obsidian Slate (`#090d16` / `#0b1120`).
  - **Elevated Panels:** Midnight Navy (`#111827` / `#1e293b` borders).
  - **Semantic Neon Accents:** Emerald (`#10b981`) for approved/compromise precedents, Electric Blue (`#3b82f6`) for BigQuery vector search & SQL execution, Amber (`#f59e0b`) for `CONFLICT-SP3-04-GP1-03`, and Crimson (`#f43f5e`) for FAA/DFARS lockouts.
- **Typography:** Heavy use of `JetBrains Mono` / `SFMono-Regular` for SQL queries, cosine similarity scores (`0.962`), contract IDs (`CNT-2025-8841`), and dollar caps, paired with crisp `Inter` for clause text.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Dark-mode optimized high-contrast redline pills: deletions in glowing crimson tint (`background: rgba(244,63,94,0.18)`, `color: #fda4af`, `text-decoration: line-through`) and counter-insertions in glowing emerald/amber tint (`background: rgba(16,185,129,0.18)`, `color: #6ee7b7`).
- Clicking `[EXECUTE COUNTER-POSITION COMMIT]` switches the dark terminal panel to `COMMITTED CLEAN TEXT` and logs a timestamped audit row to the live event stream.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents & SQL Drawer (Star Feature):** Displays the actual parameterized BigQuery `VECTOR_SEARCH` SQL query against `vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`, execution latency (`142 ms`), embedding model (`text-embedding-005`), stacked horizontal distribution bars, and a sortable high-density precedent blotter table.
- **User Comments (`w:author`):** Styled as a **Compliance Audit Annotation** input where the human reviewer (`Pradeep Gupta`, `Rahul Kasanagottu`, etc.) signs off with their name and rationale, showing the exact XML `<w:comment w:author="...">` payload generated.

#### 5. Best Persona Fit
- **Primary:** Data-driven Tax & Procurement Analysts (`Pradeep Gupta`, `Rahul Kasanagottu`), Cloud/Data Architecture evaluators, and technical stakeholders who want to see **how BigQuery Vector Search powers the CLM recommendations under the hood**.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Unmatched technical credibility for Google Cloud / BigQuery demos — surfaces the `64`-deal dataset and vector search mechanics transparently.
  - Zero eye strain in low-light environments; cohesive with Cymbal Capital's institutional dark aesthetic.
- **Cons:**
  - Traditional corporate counsel who prefer white-paper MS Word metaphors may find a dark terminal unfamiliar for prose editing.

---

### Variation 6: Guided Step-by-Step Decision Wizard & Focus Mode (SpotDraft VerifAI / Superhuman Triage Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **SpotDraft VerifAI**, **Juro**, and **Superhuman's** keyboard-driven triage queue. Instead of showing all 12 clauses at once or requiring complex mouse navigation, this paradigm automatically **filters out the 8 untouched clauses** (parking them in a collapsed `"8 Untouched Clauses Auto-Cleared"` badge) and guides the user through a **4-Step Sequential Decision Wizard (`Exception 1 of 4 → 2 of 4 → 3 of 4 → 4 of 4`)** with full keyboard shortcut support (`J` / `K` to navigate, `A` to Accept Counter, `R` to Rewrite, `H` to Hold Firm, `C` to focus Comment).

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:**
  - **Top Segmented Progress Stepper:** 4 large connected step pills (`Step 1: GP1 §12.2 [FAA]`, `Step 2: GP1 §19 [Legal]`, `Step 3: SP3 §4.1 [Tax Conflict]`, `Step 4: SP5 §3.2 [Cyber]`) with completion checkmarks and a progress bar (`75% Complete — 3 of 4 Resolved`).
  - **Center Zen Focus Card (`max-width: 920px`):** Displays only the current exception, its BigQuery recommendation badge, the inline counter-position diff, the human comment box, and a prominent bottom **Keyboard Action Dock** (`[A] Accept & Next →`, `[R] Rewrite`, `[H] Hold Firm`, `[C] Add Comment`).
- **Color Palette:** Clean daylight canvas (`#f8fafc`), elevated white focus card (`#ffffff`), violet/blue focus rings (`#4f46e5`), and tactile keyboard keycap badges (`#1e293b` keycaps with `#f8fafc` mono labels).
- **Typography:** Large, scannable clause header (`20px` bold), generous `15.5px` reading font for the active clause, and `11px` monospace keycap hints.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Each step card shows the proposed counter-position diff prominently in the center.
- Pressing `A` or clicking **`✓ Accept Counter & Advance to Next Exception →`** flashes a green confirmation state (`✓ Saved to Working Doc`), marks the current step pill green in the top stepper, and smoothly advances (`300ms` transition) to the next unresolved redline. When all 4 are resolved, it reveals the **Final Consolidation & Export Celebration Card**.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Surfaced as a concise **"Why This Counter-Position?" AI Evidence Pill** at the top of the card (`"Backed by 88% [14/16] Tier-1 Avionics Precedents in BigQuery — Click to expand all 16 deals"`), preventing information overload while keeping full evidence 1 click away.
- **User Comments (`w:author`):** Pressing `C` focuses the inline human reviewer comment field (`Author: Megan Bowen / Pradeep Gupta / Rahul Kasanagottu`), which saves automatically when advancing to the next step.

#### 5. Best Persona Fit
- **Primary:** Busy Domain SMEs and Contract Owners who want to clear their review queue in under 90 seconds with zero distraction.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Fastest task completion time across all 12 variations; keyboard shortcuts (`J/K/A/R/C`) feel effortless.
  - Eliminates cognitive clutter by hiding the 8 untouched clauses by default.
- **Cons:**
  - Sequential wizard flow makes it slightly less obvious how `SP3 §4.1` (Step 3) interacts with `GP1 §3.1` unless highlighted by an inline cross-reference banner.

---

### Variation 7: Multi-SME Swimlane & Live Outlook Thread Kanban Board (Linear / Jira + Outlook Deep-Link Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Linear**, **Jira**, and **Ironclad Workflow Boards** integrated with **Microsoft 365 Outlook**. For the Contract Owner (`Rahul Kasanagottu`), the hardest part of Deal `BA-2026-AV-8921` is not reading one clause — it is **orchestrating 4 parallel SME reviews across Engineering, Legal, Tax, and Cyber via Outlook emails (`clm-comms`)**, tracking which SMEs have replied to the Inbox, resolving the Tax/Procurement conflict, and pushing all 4 clauses to `Consolidated in Working .docx`.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:**
  - **4-Column Workflow Kanban Board:**
    1. `1. Untouched / Auto-Cleared (8 Clauses)` (Collapsed compact column)
    2. `2. Routed to SME via Outlook (Pending Reply)`
    3. `3. Conflict / Exception Flagged (Needs Harmonization)`
    4. `4. SME Approved & Written to Working .docx`
  - **Slide-Over / Bottom Clause & Email Inspector Drawer:** Clicking any Kanban card opens both the **Live Outlook Email Thread Preview** (`From: PradeepG@36zrbd.onmicrosoft.com`, `Subject: [SME REVIEW UPDATE: TAX]...`) and the **Inline Redline & Counter-Position Editor**.
- **Color Palette:** Linear-style slate/zinc surface (`#f4f4f5` board background, `#ffffff` cards), domain color-coded avatars (`Engineering`: Cyan `#0891b2`, `Legal`: Purple `#7c3aed`, `Tax`: Amber `#d97706`, `Cyber`: Rose `#e11d48`), and Microsoft Outlook blue (`#0078d4`) badges for email sync status.
- **Typography:** Compact `13px` card titles, monospace clause IDs (`GP1-12`, `SP3-04`), and crisp email metadata headers.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Each Kanban card shows a mini preview of the redline delta and current selected option (`Hold Firm`, `Tier-1 Compromise`, `Harmonized 2% Cap`).
- Clicking `[✓ Approve & Move to Ready]` inside a card or its inspector drawer transitions the clause text to clean accepted language and **moves the card into Column 4 (`SME Approved & Written to Working .docx`)**.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **User Comments & Outlook Integration:** Shows the direct link between the SME's Outlook email reply and the `<w:comment w:author="...">` written into `BA-2026-AV-8921_Working_Review.docx`. Users can edit the author and comment text right inside the card inspector.
- **BigQuery Precedents:** Each Kanban card displays a mini 3-color precedent distribution bar (`n=16` deals) and similarity badge right on the card face, with the full 16-deal table in the drawer.

#### 5. Best Persona Fit
- **Primary:** Contract Owner / Procurement Lead (`Rahul Kasanagottu`) executing **Workflow 1 (`route-smes`)**, **Workflow 3 (`poll-inbox`)**, and **Workflow 4 (`consolidate`)**.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - The only paradigm that makes the **multi-agent / multi-SME Outlook email routing & polling lifecycle (`clm-comms`)** visually first-class.
  - Instantly answers *"Who are we waiting on before the 4:00 PM Executive Gate?"*
- **Cons:**
  - Kanban cards truncate long legal paragraphs, requiring a click into the detail drawer to read full clause prose.

---

### Variation 8: Cross-Clause Dependency & Financial Impact Graph Explorer (Interactive Node Graph + Split Inspector)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Palantir Foundry Ontology Graphs**, **Neo4j Bloom**, and **Systems Engineering Traceability Matrices**. Contracts in aerospace are not isolated paragraphs — they are interconnected financial and regulatory systems. When Apex AeroSystems redlines `SP3 §4.1` to pass through 100% of Section 232/301 tariffs above 5%, it creates a **structural collision (`CONFLICT-SP3-04-GP1-03`)** with `GP1 §3.1` ($45,000,000 Firm-Fixed-Price SOW Lock). Similarly, `GP1 §12.2` connects to **FAA 14 CFR Part 21.140 (`PC-700`)**, and `SP5 §3.2` connects to **DoD DFARS 252.204-7012**. This variation renders an interactive **SVG/Canvas Node-Link Dependency Graph** on the left/top paired with a **Live Clause & Conflict Harmonization Inspector** on the right/bottom.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Split-screen architecture (`7fr` Interactive SVG Dependency Graph Canvas + `5fr` Active Node Redline & Harmonization Inspector).
  - **Central Hub Node:** `Deal BA-2026-AV-8921 ($45M FFP)`
  - **Document Cluster Nodes:** `GP1 Base Proforma`, `SP3 International Tax`, `SP5 Cyber Defense`
  - **Clause & Regulatory Nodes:** `GP1-03 ($45M FFP Lock)` ⚡ *(pulsing red/amber conflict edge)* ⚡ `SP3-04 (Tariff Pass-Through)`; `GP1-12` 🔒 `FAA 14 CFR Part 21`; `SP5-03` 🔒 `DFARS 252.204-7012`; `GP1-19` ⚖️ `$90M 2x Super-Cap`.
- **Color Palette:** Architectural blueprint dark/slate grid canvas (`#0f172a` with subtle `#1e293b` dot-matrix background) or crisp technical light blueprint, with animated dashed SVG edges (`stroke: #f59e0b` for active conflict, `stroke: #10b981` once harmonized, `stroke: #ef4444` for regulatory lockouts).
- **Typography:** Technical CAD/blueprint styling with monospace node codes (`CONFLICT-SP3-04-GP1-03`, `LOCKOUT-GP1-12-FAA`) and clean sans-serif inspector prose.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Clicking any clause node or conflict edge in the graph loads both sides of the dependency into the right inspector (e.g., showing `SP3 §4.1` redline alongside `GP1 §3.1` FFP baseline).
- Clicking **`⚡ Harmonize Conflict (Apply 50/50 Split Capped at 2% [$900K] FFP)`** updates the clause text to clean accepted language and **visually turns the pulsing red/amber graph edge between `SP3-04` and `GP1-03` into a solid emerald green link (`✓ HARMONIZED`)**.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Connected as satellite "Precedent Evidence Nodes" around each redlined clause (`16 Tier-1 Deals`), with full statistical breakdown in the right inspector.
- **User Comments (`w:author`):** Recorded directly in the right inspector (`Author: Pradeep Gupta — VP Global Tax`), explicitly documenting the cross-clause harmonization rationale for `word/comments.xml`.

#### 5. Best Persona Fit
- **Primary:** Global Tax SME (`Pradeep Gupta` in `clm-tax-tariff-review`), Procurement Systems Leads (`Rahul Kasanagottu`), and Airworthiness/Cyber Compliance Architects who need to visualize **cross-clause ripple effects and regulatory lockouts**.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Dramatically showcases why simple clause-by-clause review fails without **cross-clause conflict intelligence** (`SP3 §4.1` ↔ `GP1 §3.1`).
  - Highly memorable, differentiated visual centerpiece for executive and technical demos.
- **Cons:**
  - Graph canvas uses screen real estate that could otherwise show more text lines simultaneously.

---

### Variation 9: MS Word Ribbon & Margin Balloon Track-Changes Simulator (Authentic Word 365 Desktop Look)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Microsoft Word 365 Desktop (`Review` Tab → `Track Changes` → `All Markup` with Right-Margin Comment & Formatting Balloons)**. Because the Cymbal CLM engine ultimately produces a real OOXML `.docx` (`BA-2026-AV-8921_Working_Review.docx` and `Cymbal_Aerospace_Counter_Proposal_BA-2026-AV-8921.docx`) containing native `<w:del>`, `<w:ins>`, and `<w:comment>` elements, this variation gives users a **pixel-faithful MS Word 365 Track-Changes preview** directly in the browser before or after downloading the `.docx`.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:**
  - **Top MS Word 365 Title Bar & `Review` Ribbon:** Includes authentic Word controls: `All Markup | Simple Markup | No Markup (Clean) | Original`, `Accept ▼` (`Accept and Move to Next`, `Accept This Change`), `Reject ▼`, `Previous | Next`, `New Comment`, and `BigQuery Precedent Pane` toggle.
  - **8.5" × 11" Paper Sheet + Right Margin Balloon Gutter:** Centered white document canvas (`background: #ffffff`, `box-shadow: 0 4px 20px rgba(0,0,0,0.12)`) set against Word's classic workspace gray (`#e5e7eb`), with a dedicated `290px` right margin gutter joined to the text via dashed leader lines (`---`) pointing to `<w:comment>` and `<w:del>` balloons.
- **Color Palette:**
  - **Word Chrome:** Microsoft Word Royal Blue (`#185abd` / `#2b579a`) header bar, `#f3f2f1` ribbon surface.
  - **OOXML Track Changes:** Classic Word crimson red (`#c00000`) for strikethrough deletions `<w:del>` and underlined insertions `<w:ins>`, with author-colored margin comment cards (`Rahul Kasanagottu`, `Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`).
- **Typography:** Authentic document serif/sans (`Calibri` / `Cambria` / `Times New Roman` `11pt`/`14.5px`, `line-height: 1.65`) on the paper sheet; `Segoe UI` (`12px`) in the Ribbon and margin balloons.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Uses Word's exact 4-mode markup switcher in the Ribbon:
  - **`All Markup`:** Full inline `<w:del>` strikethroughs and `<w:ins>` underlines with dashed connector lines to right-margin comment balloons.
  - **`Simple Markup`:** Clean accepted counter-position text with a red vertical change bar (`|`) in the left page margin.
  - **`No Markup (Clean Counter)`:** Pure final contract text as it will read if accepted without markup.
  - Clicking **`✓ Accept Change`** on the Ribbon (or inside any clause) commits the counter-position and updates the margin balloon to `✓ Accepted by [Human User]`.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **User Comments (`w:author`) (Star Feature):** Rendered as authentic **Word Right-Margin Comment Balloons** showing the user avatar, full human name (`Pradeep Gupta`, `Megan Bowen`, `Lee Gu`, `Alex Wilber`, `Rahul Kasanagottu`), timestamp, and editable comment text — matching the exact `word/comments.xml` structure written into `BA-2026-AV-8921_Working_Review.docx`.
- **BigQuery Precedents (64 Deals):** Surfaced via a collapsible **Word Task Pane on the right/bottom** (similar to a Word Add-in pane) showing the 16-deal BigQuery breakdown and 1-click `[Insert Precedent Language]` buttons.

#### 5. Best Persona Fit
- **Primary:** General Counsel, Traditional Contract Managers, and External Vendor Reviewers who live inside Microsoft Word 365 all day and want total confidence in how `BA-2026-AV-8921_Working_Review.docx` looks.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Zero cognitive gap between the web workbench and the downloaded SharePoint `.docx` file.
  - Makes human-attributed `<w:comment w:author="...">` margin balloons look unmistakable and native.
- **Cons:**
  - Classic Word ribbon chrome takes up ~90px of vertical height and feels more traditional than modern AI-native interfaces like Variation 1.

---

### Variation 10: GitHub Pull Request / Code Review Style Clause Diff (`Unified` vs. `Split` Diff + Inline Review Threads)

#### 1. Core UX Metaphor & Inspiration
Inspired by **GitHub Pull Request (`Files changed` tab)**, **GitLab Merge Requests**, and **Google Critique**. Legal contracts are essentially deterministic rule codebases; a vendor redline is a **Pull Request (`PR #8921: Apex AeroSystems Redline on GP1/SP3/SP5`)** proposing modifications to 4 of 12 files/clauses. Reviewers inspect line-numbered `Unified` or `Split` diffs, attach inline review comments to specific lines, click **`Suggested change`** blocks (which work just like GitHub's `± Commit suggestion`), and submit a formal review (`Approve with Counter-Commit`, `Request SME Changes`, `Comment`).

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:**
  - **Top PR Header:** `PR #8921: Merge Apex-AeroSystems:vendor-redline-v1 into Cymbal-Aerospace:gp1-sp3-sp5-main` • Status badge (`⚠️ 1 Conflict / 2 CI Regulatory Checks Failing`) • Diff stat bar (`+142 −98 lines across 4 of 12 clauses`).
  - **Left File Tree (`260px`) + Right Diff Stream (`1fr`):** Left tree lists all 12 clauses like source files (`clauses/GP1-12_warranty_faa.md [M]`, `clauses/SP3-04_tariffs.md [CONFLICT]`, `clauses/GP1-01_definitions.md [✓]`). Right stream shows collapsible file diff headers with `Unified | Split` toggle, line numbers (`12`, `13`, `14`), `-` red deletion lines, `+` green counter-proposal lines, and inline **`Suggested Counter-Position Commit`** boxes.
- **Color Palette:** GitHub Primer Light/Dark palette (`#ffffff` / `#f6f8fa` headers, `#d0d7de` borders, `#ffebe9` deletion line background with `#ff818266` word diff, `#dafbe1` insertion line background with `#abf2bc` word diff, `#1f883d` primary green `Commit suggestion` button).
- **Typography:** Monospace line numbers and clause paths (`JetBrains Mono` `12.5px`); clean `13.5px` prose inside diff hunks.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Each redlined clause displays:
  1. The `-` Vendor Redline hunk (flagged by automated CI checks like `❌ check/faa-14-cfr-part-21` or `❌ check/gp1-03-ffp-ceiling`).
  2. An embedded **`± Suggested Counter-Position Change (Backed by BigQuery Precedents)`** block.
- Clicking **`Commit Counter-Position Suggestion`** updates the clause hunk to a green `✓ Counter-Commit Applied` state showing the clean accepted text.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **User Comments (`w:author`):** Styled as **Inline PR Review Thread Comments** attached directly beneath the diff hunk, complete with the human author's avatar and name (`Alex Wilber`, `Megan Bowen`, `Pradeep Gupta`, `Lee Gu`, `Rahul Kasanagottu`) and a badge `"Synced to word/comments.xml"`.
- **BigQuery Precedents (64 Deals):** Rendered as an automated **"BigQuery Precedent Bot / CI Check Summary"** expandable card inside each clause diff header (`✓ bq-vector-search: 14/16 Tier-1 deals Held Firm [88%] — View 16 matched contracts`).

#### 5. Best Persona Fit
- **Primary:** Cybersecurity SME (`Alex Wilber`), Avionics Systems/Software QA (`Megan Bowen`), and Engineering-heavy aerospace organizations that love precision line-level diffs, automated policy checks (`CI/CD for Contracts`), and `Commit suggestion` workflows.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - GitHub's `Suggested change` + `Commit suggestion` pattern is arguably the clearest UX ever invented for reviewing and applying proposed text replacements.
  - Treats FAA, DFARS, and FFP SOW guardrails like failing CI checks that turn green once the counter-position is committed.
- **Cons:**
  - Non-technical legal reviewers may initially find line numbers and PR terminology (`Files changed`, `Commit`) unconventional.

---

### Variation 11: Executive Bento Deal Room & CFO/GC Approval Cockpit (Icertis / Apple Bento Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Icertis Contract Intelligence (Executive Obligation & Risk Cockpit)** and modern **Apple/Stripe Bento Grid Dashboards**. When the Contract Owner (`Rahul Kasanagottu`) enters the **1:30 PM Legal/Tax Alignment Gate** or the **4:00 PM VP Executive Sign-Off Gate**, executives do not want to scroll through 15 pages of boilerplate. They want a **high-impact Bento Deal Room** that translates legal redlines into **Dollarized Financial Exposure, Regulatory Compliance Status, BigQuery Precedent Confidence Rings, and 1-Click Counter-Position Approval Cards**.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Responsive 12-column **Bento Grid** with asymmetric modular cards:
  - **Bento Card A (Span 5): Financial Exposure Waterfall:** Visualizes the `$45.0M` Base FFP Contract Value vs. Vendor's Uncapped Ask (`+$18.5M+` tariff & liability exposure) vs. Cymbal Consolidated Counter-Proposal (`Capped at +2.0% [$900K] Tariff Ceiling + $90M 2x Super-Cap`).
  - **Bento Card B (Span 4): BigQuery 64-Deal Precedent Confidence Rings:** SVG donut/ring gauges for `GP1-12 (88% Hold Firm)`, `SP5-03 (94% Hold Firm)`, `GP1-19 (69% 2x Cap)`, and `SP3-04 (63% Shared Cap)`.
  - **Bento Card C (Span 3): Deal Readiness & SharePoint Export Gate:** Live status of `.docx` and 4-tab `.xlsx` artifacts + Outlook Vendor Reply Draft button.
  - **Bento Row 2 (4 Equal Span-3 Cards): The 4 Executive Clause Sign-Off Cards:** Each card shows the SME owner, inline redline vs. clean counter toggle, human comment input, and a 1-click **`✓ Approve Position`** button.
- **Color Palette:** Executive Navy (`#0a2540`) hero card, warm ivory/white Bento tiles (`#ffffff`), subtle gold/amber financial highlights (`#d97706`), and emerald approval badges (`#059669`).
- **Typography:** Large display numerals (`28px`–`32px` bold) for financial figures and percentages; concise `13.5px` executive clause summaries with expandable full legal text.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Each of the 4 Clause Bento Cards features a segmented pill toggle (`[Redline Diff]` | `[Clean Accepted Text]`) and a **`✓ Sign Off & Lock in Doc`** button that flips the card border to emerald green and updates the top Financial Exposure Waterfall in real time.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Visually summarized in the SVG Donut Rings and clickable per-clause drawers showing all 16 historical deals per position.
- **User Comments (`w:author`):** Displayed on each Bento card as an **Executive / SME Sign-Off Note** attributed to the human reviewer (`Rahul Kasanagottu`, `Pradeep Gupta`, `Lee Gu`, `Megan Bowen`, `Alex Wilber`) and written to `BA-2026-AV-8921_Working_Review.docx`.

#### 5. Best Persona Fit
- **Primary:** VP of Procurement, CFO, General Counsel, and Contract Owner (`Rahul Kasanagottu`) during executive decision gates and final consolidation (`clm-contract-consolidation`).

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Immediately answers the executive question: *"What is the dollar impact of Apex's redlines, how does our counter-proposal protect our $45M FFP margin, and is it backed by precedent?"*
  - Visually stunning, scannable at a glance, and ideal for C-suite briefings.
- **Cons:**
  - 4-across cards have narrower text columns for long clauses unless expanded into a modal or full-width drawer.

---

### Variation 12: Conversational AI Co-Pilot + Live Contract Canvas Split Workbench (Harvey AI / Claude Artifacts / Gemini Canvas Style)

#### 1. Core UX Metaphor & Inspiration
Inspired by **Harvey AI**, **Claude Artifacts**, and **Gemini Canvas**. In this paradigm, the user interacts with a **Left-Pane Legal & Tax AI Co-Pilot Thread** (equipped with 1-click prompt chips and natural-language rewrite instructions) while watching the **Right-Pane Live Contract Canvas** dynamically highlight diffs, run BigQuery precedent lookups, resolve cross-clause conflicts, and commit human-attributed Word comments in real time.

#### 2. Layout Geometry, Color Palette & Typography
- **Layout Geometry:** Full-viewport split workbench (`grid-template-columns: 420px 1fr`):
  - **Left Pane (`420px`): Conversational AI Co-Pilot & Prompt Studio:** Shows structured agent reasoning steps (`1. Parsed 12 clauses`, `2. Queried 64 BigQuery precedents`, `3. Flagged CONFLICT-SP3-04-GP1-03`), quick-action prompt chips (`"Draft 50/50 tariff cap at 2% FFP"`, `"Apply 88% FAA Hold Firm precedent"`, `"Tighten IP carveout to Boeing specs only"`), and a live prompt input bar that rewrites the active clause on the right canvas.
  - **Right Pane (`1fr`): Live Contract Artifact Canvas + Word Comment Gutter:** Renders the live working contract (`BA-2026-AV-8921_Working_Review.docx`) with an instant floating toolbar (`Counter Diff`, `Clean Accepted`, `Precedent Table (16)`, `Download .docx/.xlsx`) and a right-hand human user comment column.
- **Color Palette:** Warm AI studio neutral (`#f8fafc` left chat pane with `#eff6ff` / `#f5f3ff` AI reasoning cards; crisp `#ffffff` right artifact canvas on an `#e2e8f0` stage).
- **Typography:** Conversational `13.5px` sans-serif with monospace tool-call badges in the left pane; authoritative `14.5px` contract typography in the right canvas.

#### 3. How Inline Redlines vs. Clean Accepted Text Work
- Typing a custom instruction in the left Co-Pilot (or clicking a preset prompt chip like `"Cap Section 232/301 tariff sharing at 2.0% ($900K) of GP1 §3.1 FFP"`) streams an updated counter-position directly onto the right Contract Canvas, highlighting the newly proposed language in coral/emerald diff markup.
- Clicking **`✓ Accept in Canvas`** (either in the chat response card or on the canvas toolbar) locks in the clean accepted text.

#### 4. How User Comments (`w:author`) & BigQuery Precedents (64 Deals) Are Surfaced
- **BigQuery Precedents:** Surfaced both as **inline citation cards inside the Co-Pilot thread** (e.g., citing `Safran`, `Spirit AeroSystems`, `Honeywell`, `BAE Systems` from the 64-deal BigQuery table) and as an interactive tab on the right Canvas.
- **User Comments (`w:author`):** The right Canvas includes a dedicated **User Comment Margin Card** where the human user (`Rahul Kasanagottu` or SME) edits their comment author name and rationale, with a 1-click `"Use Co-Pilot Rationale as My Word Comment"` helper that attributes the final comment strictly to the human user (`w:author`).

#### 5. Best Persona Fit
- **Primary:** Gemini Enterprise (Spark) users, Contract Owners, and Legal/Tax SMEs who want a seamless bridge between **conversational agent prompting** and **direct visual manipulation of the contract document**.

#### 6. Trade-Offs (Pros & Cons)
- **Pros:**
  - Aligns naturally with the **Gemini Enterprise (Spark) + Canvas** mental model.
  - Makes iterative custom drafting (`✦ Rewrite with Input`) feel magical while preserving strict guardrail and precedent grounding.
- **Cons:**
  - Dedicates ~420px to the conversational thread even when the user is simply clicking through standard `Accept` / `Reject` buttons.

---

## Cross-Variation Synthesis: Key Feature Recommendations for the 12-Variation Mockup Lab (`cymbal_clm_ui_lab_12_variations.html`)

To allow the user to test all 12 paradigms side-by-side on Deal `BA-2026-AV-8921`, make notes, and decide which patterns to merge into the production Cymbal Aerospace CLM skills, the Mockup Lab should guarantee:

1. **Shared Live Deal State Across All 12 Variations:**
   - Editing a counter-position, accepting/rejecting a change, harmonizing `CONFLICT-SP3-04-GP1-03`, or editing a human reviewer comment (`w:author`) in **any** variation should immediately reflect across all 12 variations and sync with the local loopback API (`http://127.0.0.1:58921/api/review` & `/api/harmonize`) when running.
2. **Authentic Inline Redline vs. Clean Accepted Text Toggle in Every Variation:**
   - Every variation must support toggling between **Inline Diff View** (orange-red strikethrough on rejected vendor language + coral/emerald highlight on proposed counter-position) and **Clean Accepted Contract Text** once a change is accepted.
3. **Human-Attributed Word Comments (`w:author`) Everywhere:**
   - Every variation must expose the **Comment Author (`w:author`)** field (`Rahul Kasanagottu`, `Megan Bowen`, `Lee Gu`, `Pradeep Gupta`, `Alex Wilber`) and **Comment Text**, emphasizing that comments in `BA-2026-AV-8921_Working_Review.docx` belong to the human reviewer rather than a system bot.
4. **Full 64-Deal BigQuery Precedent Access (`16` Deals per Position):**
   - Every variation must surface the exact BigQuery statistical distribution (`GP1-12`: 88% Held Firm, `GP1-19`: 69% Tier-1 Compromise, `SP3-04`: 63% Shared Cap, `SP5-03`: 94% Held Firm) and individual historical supplier matches.
5. **Persistent User Testing & Note-Taking Evaluator Bar:**
   - Pin a non-intrusive **UX Lab Switcher & Evaluator Drawer** so the user can switch across Variations `1..12` in 1 click, rate each variation (`1–5 ★`), check off specific sub-features they want to keep (e.g., *"Keep V1 Emerald Floating Menu + V4 3-Column Toggle + V9 Word Margin Balloons"*), write freeform testing notes, and export/save their decisions to `ux_evaluation_notes.json`.
