#!/usr/bin/env python3
"""
Builds the 12-Variation Interactive Cymbal Aerospace CLM UI Mockup Lab (`cymbal_clm_ui_lab_12_variations.html`)
synthesizing the Teamwork UX research across 12 competing CLM & LegalTech paradigms:
  V1: Emerald Stage & Floating Action Menu (Ivo / Spellbook / User Screenshot Baseline)
  V2: Split-Pane Contract Reader + Playbook Guardrail Sidebar (Ironclad AI Assist / Jurist)
  V3: Traffic-Light Clause Risk Heatmap & Deviation Radar (Luminance Legal-Grade AI)
  V4: 3-Column Synchronized Diff Matrix (Litera Compare / Kira Systems)
  V5: Cymbal Institutional Dark Terminal + Live BigQuery SQL Drawer (Bloomberg / Cymbal Capital)
  V6: Guided 4-Step Decision Wizard & Keyboard Focus Mode (SpotDraft VerifAI / Superhuman)
  V7: Multi-SME Swimlane & Live Microsoft Outlook Thread Kanban Board (Linear / Jira + Outlook)
  V8: Cross-Clause Dependency & Financial Impact Graph Explorer (Palantir / Systems Traceability)
  V9: Authentic MS Word 365 Ribbon & Right-Margin Balloon Simulator (Word Desktop Track Changes)
  V10: GitHub Pull Request / Code Review Style Clause Diff (PR #8921 Unified/Split + Commit Suggestion)
  V11: Executive Bento Deal Room & CFO / General Counsel Approval Cockpit (Icertis / Apple Bento)
  V12: Conversational AI Co-Pilot + Live Contract Canvas Split View (Harvey AI / Claude Artifacts / Spark Canvas)

Includes a persistent, collapsible **UX Test Lab & Notes Evaluator Drawer** so the user can test all 12 variations,
rate each (1-5 stars), check off components to incorporate, take freeform notes (auto-saved to localStorage +
`http://127.0.0.1:58921/api/ux-notes`), and export their synthesis as Markdown or `ux_evaluation_notes.json`.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED_PATH = ROOT / "skills" / "cymbal_clm_seed.json"


def build_lab_html() -> str:
    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    initial_state = seed["initial_state"]
    precedents = seed["precedents"]

    recommended_defaults = {
        "GP1-12": {
            "option": "hold_firm",
            "reviewer": "Megan Bowen",
            "role": "Chief Airworthiness & Quality DER",
            "guardrail_code": "LOCKOUT-GP1-12-FAA (14 CFR Part 21.140)",
            "guardrail_type": "REGULATORY_LOCKOUT",
            "counter_text": (
                "12.2 (a) Airworthiness & Hardware/Firmware Warranty: Seller warrants all Goods, including FCC-900 "
                "flight control hardware, triplex voting channels, and embedded DO-178C DAL-A avionics firmware, to be "
                "free from defects in design, material, and workmanship for thirty-six (36) months from initial aircraft "
                "delivery to Cymbal Aerospace's airline customer, and Seller shall repair or replace defective "
                "flight-critical LRUs on an Aircraft-on-Ground (AOG) 24-hour turnaround basis at Seller's expense. "
                "(b) Regulatory Source Surveillance: Cymbal Aerospace and Federal Aviation Administration (FAA) "
                "representatives may conduct unannounced source inspections at Seller's facility at any time to verify "
                "AS9100 Rev D quality compliance, FAA 14 CFR Part 21.140 production certificate airworthiness conformity, "
                "and sub-tier test bench calibration records."
            ),
            "user_comment": (
                "Hold firm on 36-month warranty from aircraft delivery and unannounced FAA/Cymbal source inspections "
                "at any time per mandatory 14 CFR Part 21.140 / PC-700 airworthiness requirements (88% Held Firm precedent)."
            ),
        },
        "GP1-19": {
            "option": "compromise_tier_1",
            "reviewer": "Rahul Kasanagottu",
            "role": "Contract Owner / Corporate Legal Playbook",
            "guardrail_code": "PLAYBOOK-GP1-19-SUPERCAP (2.0x PO / $90M)",
            "guardrail_type": "COMMERCIAL_NEGOTIABLE",
            "counter_text": (
                "19.1 Seller's aggregate liability for general direct commercial damages arising out of or related to "
                "this Contract shall not exceed two hundred percent (200% / 2.0x) of the total Purchase Order value "
                "($90,000,000), excluding (a) breaches of confidentiality or DFARS cybersecurity obligations, (b) gross "
                "negligence or willful misconduct, (c) Airworthiness Directive (AD) or flight-safety recall costs, and "
                "(d) Seller's Section 24 intellectual property indemnification obligations including system-level avionics "
                "bus integration (for which liability remains uncapped)."
            ),
            "user_comment": (
                "Counter with Tier-1 Playbook 2.0x PO ($90,000,000) Super-Cap while preserving uncapped carveouts for "
                "confidentiality/cyber breaches, flight-safety AD recalls, and system-level IP combination indemnity (69% precedent match)."
            ),
        },
        "SP3-04": {
            "option": "compromise_tier_1",
            "reviewer": "Pradeep Gupta",
            "role": "VP Global Tax, Customs & Trade",
            "guardrail_code": "CONFLICT-SP3-04-GP1-03 (Clashes with $45M FFP SOW Lock)",
            "guardrail_type": "CROSS_CLAUSE_CONFLICT",
            "counter_text": (
                "4.1 All unit prices are DDP Everett/Renton facility. Any verified new Section 232/301 tariff increase "
                "exceeding 5.0% on raw titanium forgings or semiconductor wafers shall be shared 50/50 between Buyer and "
                "Seller, strictly capped at a maximum aggregate adjustment of 2.0% ($900,000) of the GP1 §3.1 Firm-Fixed-Price SOW unit price."
            ),
            "user_comment": (
                "Harmonized cross-clause conflict with GP1 §3.1 ($45M FFP ceiling): 50/50 shared tariff split above 5.0% "
                "threshold, strictly capped at +2.0% ($900,000) of the Firm-Fixed-Price SOW value (63% BigQuery precedent)."
            ),
        },
        "SP5-03": {
            "option": "hold_firm",
            "reviewer": "Alex Wilber",
            "role": "CISO & Defense Cyber Compliance Lead",
            "guardrail_code": "LOCKOUT-SP5-03-DFARS (DFARS 252.204-7012 72-Hr)",
            "guardrail_type": "REGULATORY_LOCKOUT",
            "counter_text": (
                "3.2 Cyber Incident Reporting & Forensic Media Preservation: Seller shall rapidly report any cyber "
                "incident affecting Covered Defense Information (CDI), flight control firmware repositories, or Cymbal "
                "engineering networks to Cymbal Aerospace CSIRT and the DoD via DIBNet within seventy-two (72) hours "
                "of discovery per mandatory DFARS 252.204-7012(c) flow-down requirements, and shall isolate and preserve "
                "all affected system images, memory dumps, and telemetry logs for ninety (90) days."
            ),
            "user_comment": (
                "Hold firm on mandatory 72-hour cyber incident reporting and 90-day forensic image preservation per "
                "DoD DFARS 252.204-7012(c) statutory flow-down (94% Held Firm precedent across 16 Tier-1 deals)."
            ),
        },
    }

    lab_payload = {
        "deal": initial_state,
        "precedents": precedents,
        "defaults": recommended_defaults,
    }
    payload_json = json.dumps(lab_payload)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light dark" />
  <title>Cymbal Aerospace CLM — 12-Variation Interactive UI/UX Mockup Lab (BA-2026-AV-8921)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    :root {{
      color-scheme: light dark;
      interpolate-size: allow-keywords;
      --font-sans: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, sans-serif;
      --font-mono: "JetBrains Mono", "SFMono-Regular", Menlo, Consolas, monospace;
      --font-serif: "Cambria", "Georgia", "Times New Roman", serif;
    }}
    * {{ box-sizing: border-box; font-family: var(--font-sans); }}
    body {{
      margin: 0;
      padding: 0;
      background: #faf8f5;
      color: #1e293b;
      font-size: 13.5px;
      padding-bottom: 84px;
    }}
    .tabular-nums {{ font-variant-numeric: tabular-nums; font-family: var(--font-mono); }}
    /* Pastel Semantic Redline Diff Tokens (WCAG AA + Non-Color Strikethrough/Border) */
    del.diff-del {{
      color: #9f1239;
      text-decoration: line-through solid #e11d48 2px;
      background: #ffe4e6;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 500;
    }}
    ins.diff-ins {{
      background: #dcfce7;
      color: #065f46;
      text-decoration: none;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 600;
      border-bottom: 2px solid #34d399;
    }}
    del.dark-del {{
      color: #9f1239;
      text-decoration: line-through solid #f43f5e 2px;
      background: #ffe4e6;
      padding: 1px 5px;
      border-radius: 4px;
    }}
    ins.dark-ins {{
      background: #dcfce7;
      color: #065f46;
      text-decoration: none;
      padding: 2px 6px;
      border-radius: 4px;
      border-bottom: 2px solid #34d399;
      font-weight: 600;
    }}
    /* Variation 1 Pastel Sage/Periwinkle Stage */
    .emerald-stage {{
      background: linear-gradient(135deg, #e0e7ff 0%, #dbeafe 50%, #d1fae5 100%);
      border: 1px solid #c7d2fe;
      border-radius: 16px;
      padding: 28px 32px;
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    }}
    .legal-sheet {{
      background: #ffffff;
      border-radius: 14px;
      padding: 30px 36px;
      box-shadow: 0 12px 32px rgba(15, 23, 42, 0.08);
      border: 1px solid #cbd5e1;
      color: #0f172a;
    }}
    .floating-action-menu {{
      background: #ffffff;
      border-radius: 14px;
      padding: 8px;
      box-shadow: 0 12px 28px rgba(15, 23, 42, 0.10);
      border: 1px solid #c7d2fe;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}
    .floating-action-btn {{
      display: flex;
      align-items: center;
      gap: 11px;
      width: 100%;
      padding: 11px 14px;
      border: none;
      background: transparent;
      text-align: left;
      font-size: 14px;
      font-weight: 600;
      color: #1e293b;
      border-radius: 9px;
      cursor: pointer;
      transition: background 0.14s ease, transform 0.1s ease;
    }}
    .floating-action-btn:hover {{ background: #eef2ff; color: #312e81; }}
    .floating-action-btn.active-accept {{ background: #dcfce7; color: #065f46; font-weight: 700; }}
    .var-tab {{
      padding: 7px 11px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      border: 1px solid #c7d2fe;
      background: rgba(255, 255, 255, 0.85);
      color: #312e81;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .var-tab:hover {{ background: #e0e7ff; color: #1e1b4b; }}
    .var-tab.active {{
      background: #dcfce7;
      color: #065f46;
      border-color: #86efac;
      box-shadow: 0 2px 8px rgba(16, 185, 129, 0.18);
    }}
    .star-btn {{
      font-size: 20px;
      background: transparent;
      border: none;
      cursor: pointer;
      color: #cbd5e1;
      transition: transform 0.1s ease, color 0.1s ease;
      padding: 0 2px;
    }}
    .star-btn.lit {{ color: #f59e0b; }}
    .star-btn:hover {{ transform: scale(1.18); }}
    textarea.auto-grow {{
      field-sizing: content;
      min-height: 58px;
      max-height: 180px;
      width: 100%;
      resize: vertical;
    }}
    @media (forced-colors: active) {{
      del.diff-del {{ outline: 1px dashed GrayText; }}
      ins.diff-ins {{ outline: 2px solid Highlight; }}
    }}
  </style>
</head>
<body>

  <!-- ===================================================================== -->
  <!-- TOP STICKY LAB COMMAND BAR: PASTEL EDITION + MASTER WORKBENCH LINK    -->
  <!-- ===================================================================== -->
  <header class="sticky top-0 z-40 border-b border-indigo-200 shadow-sm" style="background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 52%, #f3e8ff 100%); color: #312e81;">
    <div class="max-w-[1540px] mx-auto px-4 py-2.5 flex flex-col gap-2">
      <div class="flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <span class="px-2.5 py-1 rounded-md bg-white/80 text-indigo-900 border border-indigo-300 text-xs font-extrabold tracking-wider">
            CYMBAL AEROSPACE CLM • PASTEL UX LAB (12 VARIATIONS)
          </span>
          <a href="http://127.0.0.1:58921/workbench" target="_blank" class="px-3 py-1 rounded-md bg-emerald-100 hover:bg-emerald-200 text-emerald-900 border border-emerald-300 text-xs font-extrabold no-underline">
            ★ Open Synthesized Master Pastel Workbench (/workbench) ↗
          </a>
          <span id="headerStatusBadge" class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-300">
            0 / 4 Clauses Accepted
          </span>
        </div>

        <!-- Persona & Demo State Quick-Controls -->
        <div class="flex flex-wrap items-center gap-2">
          <label class="text-xs text-indigo-900 font-semibold flex items-center gap-1.5">
            <span>👤 Active Reviewer (w:author):</span>
            <select id="globalPersonaSelect" onchange="changeGlobalPersona(this.value)" class="bg-white text-indigo-950 border border-indigo-300 rounded-md px-2 py-1 text-xs font-bold">
              <option value="Rahul Kasanagottu">Rahul Kasanagottu (Contract Owner)</option>
              <option value="Pradeep Gupta">Pradeep Gupta (VP Global Tax — SP3 §4.1)</option>
              <option value="Megan Bowen">Megan Bowen (FAA DER & QA — GP1 §12.2)</option>
              <option value="Lee Gu">Lee Gu (VP Aviation Legal — GP1 §19)</option>
              <option value="Alex Wilber">Alex Wilber (CISO Cyber — SP5 §3.2)</option>
            </select>
          </label>

          <div class="flex items-center gap-1 bg-white/80 p-1 rounded-lg border border-indigo-200">
            <button onclick="setDemoPreset('intake')" class="px-2 py-1 rounded text-xs font-semibold bg-indigo-50 hover:bg-indigo-100 text-indigo-900" title="Reset to Workflow 1 Intake (0/4 accepted, SP3-04 conflict active)">
              🔄 W1: Intake (0/4)
            </button>
            <button onclick="setDemoPreset('polled')" class="px-2 py-1 rounded text-xs font-semibold bg-sky-50 hover:bg-sky-100 text-sky-900" title="Simulate Workflow 3 Polled Inbox (3/4 SMEs approved, GP1-19 open)">
              📬 W3: 3/4 Polled
            </button>
            <button onclick="setDemoPreset('consolidated')" class="px-2 py-1 rounded text-xs font-semibold bg-emerald-50 hover:bg-emerald-100 text-emerald-900" title="Simulate Workflow 4 All 4 Accepted & Consolidated">
              ✅ W4: 4/4 Accepted
            </button>
          </div>

          <a href="http://127.0.0.1:58921/api/download/working-docx" target="_blank" class="px-2.5 py-1 rounded-md text-xs font-bold bg-indigo-100 hover:bg-indigo-200 text-indigo-900 border border-indigo-300 no-underline">
            ⬇️ Working .docx
          </a>
          <button onclick="openComparisonModal()" class="px-3 py-1 rounded-md text-xs font-extrabold bg-amber-100 hover:bg-amber-200 text-amber-950 border border-amber-300 cursor-pointer">
            📊 My UX Notes & Export (<span id="ratedCountBadge">0/12</span>)
          </button>
        </div>
      </div>

      <!-- 12 Variation Switcher Strip -->
      <div class="flex items-center gap-1.5 overflow-x-auto pb-1" id="variationTabsBar" role="tablist" aria-label="12 CLM UI Variations">
      </div>
    </div>
  </header>

  <!-- ===================================================================== -->
  <!-- ACTIVE VARIATION DESCRIPTION & CLAUSE SELECTOR SUB-BAR                -->
  <!-- ===================================================================== -->
  <section class="bg-white border-b border-slate-200 shadow-xs">
    <div class="max-w-[1540px] mx-auto px-4 py-2.5 flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <span id="varParadigmBadge" class="px-2.5 py-1 rounded-md text-xs font-extrabold bg-emerald-100 text-emerald-900">
          V1 • Ivo / Spellbook Word-Native Paradigm
        </span>
        <div>
          <h1 id="varTitleHeading" tabindex="-1" class="text-sm font-extrabold text-slate-900 m-0 outline-none">
            Variation 1: Emerald Stage &amp; Floating Action Popover
          </h1>
          <p id="varSubtitleText" class="text-xs text-slate-500 m-0">
            Matches your uploaded screenshot (media_1792469698101_00b1ca98.png) — Orange-red strikethrough + coral counter-position highlight + floating 4-button action menu.
          </p>
        </div>
      </div>

      <!-- Active Redlined Clause Selector Pills (Shared across single-clause views) -->
      <div class="flex flex-wrap items-center gap-1.5" id="globalClausePills">
      </div>
    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- MAIN STAGE: RENDERS ANY OF THE 12 VARIATIONS DYNAMICALLY              -->
  <!-- ===================================================================== -->
  <main class="max-w-[1540px] mx-auto px-4 py-5" id="variationStageContainer">
  </main>

  <!-- ===================================================================== -->
  <!-- PERSISTENT BOTTOM UX EVALUATOR & NOTE-TAKING HARNESS (PASTEL EDITION) -->
  <!-- ===================================================================== -->
  <aside id="uxEvaluatorBar" class="fixed bottom-0 inset-x-0 z-50 border-t-2 border-indigo-200 shadow-lg transition-all" style="background: linear-gradient(135deg, #eef2ff 0%, #f3e8ff 100%); color: #1e1b4b;">
    <!-- Compact Bar -->
    <div class="max-w-[1540px] mx-auto px-4 py-2.5 flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <button onclick="toggleEvalDrawer()" class="px-3 py-1.5 rounded-lg bg-emerald-100 hover:bg-emerald-200 text-emerald-950 border border-emerald-300 font-extrabold text-xs cursor-pointer flex items-center gap-1.5">
          <span id="evalToggleIcon">▲</span>
          <span>📝 Rate &amp; Take Notes on <strong id="evalBarVarLabel">V1</strong></span>
        </button>

        <!-- Quick Star Rating in Bar -->
        <div class="flex items-center gap-1" id="quickStarsBar" title="Rate this UI variation (1 to 5 stars)">
        </div>

        <!-- Quick Verdict Select -->
        <select id="quickVerdictSelect" onchange="setVariationVerdict(this.value)" class="bg-white text-indigo-950 border border-indigo-300 rounded-md px-2.5 py-1 text-xs font-bold">
          <option value="">— Select Verdict —</option>
          <option value="PRIMARY_CANDIDATE">🏆 Primary Production Candidate</option>
          <option value="CHERRY_PICK">🧩 Cherry-Pick Specific Components</option>
          <option value="PERSONA_SPECIFIC">🔄 Keep as Secondary / Persona View</option>
          <option value="SKIP">❌ Skip / Don't Use</option>
        </select>
      </div>

      <!-- Quick Inline Note Input -->
      <div class="flex-1 min-w-[260px] max-w-[600px] flex items-center gap-2">
        <input
          id="quickNoteInput"
          type="text"
          placeholder="Type quick test notes for this variation (auto-saved)..."
          oninput="updateVariationNote(this.value)"
          class="w-full bg-white text-slate-900 border border-indigo-300 rounded-md px-3 py-1.5 text-xs focus:border-indigo-500 outline-none"
        />
      </div>

      <div class="flex items-center gap-2">
        <span id="evalSaveIndicator" class="text-xs text-emerald-800 font-bold">✓ Auto-saved</span>
        <button onclick="prevVariation()" class="px-2.5 py-1 rounded bg-white hover:bg-indigo-50 text-indigo-950 border border-indigo-200 text-xs font-bold cursor-pointer">← Prev</button>
        <button onclick="nextVariation()" class="px-2.5 py-1 rounded bg-white hover:bg-indigo-50 text-indigo-950 border border-indigo-200 text-xs font-bold cursor-pointer">Next →</button>
        <button onclick="openComparisonModal()" class="px-3 py-1.5 rounded-lg bg-amber-100 hover:bg-amber-200 text-amber-950 border border-amber-300 font-extrabold text-xs cursor-pointer">
          📋 Copy / Export All Notes
        </button>
      </div>
    </div>

    <!-- Expanded Drawer for Detailed Component Cherry-Picking & Pros/Cons -->
    <div id="evalExpandedDrawer" style="display:none;" class="border-t border-indigo-200 bg-white/95 px-4 py-4">
      <div class="max-w-[1540px] mx-auto grid grid-cols-1 md:grid-cols-12 gap-4">
        <div class="md:col-span-5 space-y-2">
          <div class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">
            🧩 Cherry-Pick Components to Keep from <span id="drawerVarName">V1</span>:
          </div>
          <div id="keepComponentsGrid" class="grid grid-cols-2 gap-1.5 text-xs">
          </div>
        </div>
        <div class="md:col-span-4 space-y-2">
          <div class="text-xs font-extrabold uppercase tracking-wider text-indigo-800">
            🏷️ Quick Pros / Cons Tags:
          </div>
          <div id="quickTagsGrid" class="flex flex-wrap gap-1.5">
          </div>
        </div>
        <div class="md:col-span-3 space-y-2">
          <div class="text-xs font-extrabold uppercase tracking-wider text-amber-900">
            📓 Detailed Notes for <span id="drawerVarName2">V1</span>:
          </div>
          <textarea
            id="drawerNoteTextarea"
            oninput="updateVariationNote(this.value)"
            placeholder="What do you like or want to change in this variation?"
            class="w-full h-24 bg-white text-slate-900 border border-indigo-300 rounded-lg p-2.5 text-xs outline-none focus:border-indigo-500"
          ></textarea>
        </div>
      </div>
    </div>
  </aside>

  <!-- ===================================================================== -->
  <!-- MODAL: COMPARE ALL 12 VARIATIONS & EXPORT NOTES TO CHAT / JSON        -->
  <!-- ===================================================================== -->
  <dialog id="comparisonModal" class="rounded-2xl border border-slate-300 shadow-2xl p-0 w-full max-w-5xl bg-white text-slate-900 backdrop:bg-slate-950/70">
    <div class="p-5 bg-slate-900 text-white flex items-center justify-between rounded-t-2xl">
      <div>
        <h2 class="text-base font-extrabold m-0">📊 Your 12-Variation UX Evaluation Summary &amp; Feature Synthesis</h2>
        <p class="text-xs text-slate-400 m-0 mt-0.5">
          Copy the generated Markdown summary below and paste it into the chat so we can merge your favorite patterns into the production skills.
        </p>
      </div>
      <button onclick="document.getElementById('comparisonModal').close()" class="px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs font-bold text-white cursor-pointer">
        ✕ Close
      </button>
    </div>
    <div class="p-5 space-y-4 max-h-[78vh] overflow-y-auto">
      <div class="space-y-1.5">
        <label class="text-xs font-extrabold uppercase tracking-wider text-slate-700">
          🎯 Overall Synthesis / How You Want to Combine These Variations:
        </label>
        <textarea
          id="overallSynthesisInput"
          oninput="saveOverallSynthesis(this.value)"
          placeholder="Example: Use V1's Emerald Stage & Floating Action Menu as the main Clause Review tab, add V4's 3-Column Compare tab, keep V5's collapsible BigQuery SQL drawer, and include V11's Executive Exposure Waterfall in the header..."
          class="w-full h-20 border border-slate-300 rounded-lg p-3 text-xs"
        ></textarea>
      </div>

      <div id="comparisonTableContainer" class="overflow-x-auto border border-slate-200 rounded-xl">
      </div>

      <div class="space-y-1.5">
        <div class="flex items-center justify-between">
          <span class="text-xs font-extrabold uppercase tracking-wider text-slate-700">📋 Ready-to-Paste Markdown Decision Plan</span>
          <div class="flex gap-2">
            <button onclick="copyMarkdownSummary()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs cursor-pointer">
              📋 Copy Markdown to Clipboard
            </button>
            <button onclick="downloadJsonNotes()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs cursor-pointer">
              ⬇️ Download ux_evaluation_notes.json
            </button>
          </div>
        </div>
        <pre id="markdownPreviewBox" class="bg-slate-950 text-emerald-300 p-4 rounded-xl text-xs overflow-x-auto whitespace-pre-wrap font-mono max-h-56"></pre>
      </div>
    </div>
  </dialog>

<script>
const LAB_DATA = {payload_json};

const VARIATIONS_META = [
  {{
    id: 'V1',
    short: 'V1 • Emerald Floating',
    paradigm: 'V1 • Ivo / Spellbook / Robin AI Word-Native Paradigm',
    title: 'Variation 1: Emerald Stage & Floating Action Menu (Screenshot Match)',
    subtitle: 'Centered white legal paper on an emerald stage with orange-red strikethrough + coral counter-position highlight + floating 4-button action menu.',
    bestFor: 'All Personas • Surgical Clause Review'
  }},
  {{
    id: 'V2',
    short: 'V2 • Ironclad Split',
    paradigm: 'V2 • Ironclad AI Assist / Jurist Split-Pane Paradigm',
    title: 'Variation 2: Continuous 12-Clause Contract Reader + Sticky Playbook Sidebar',
    subtitle: 'Left 60% full scrolling 12-clause contract in context; Right 40% sticky Playbook Guardrails, 16-deal BigQuery Precedents, and 1-click option cards.',
    bestFor: 'Corporate Legal (Lee Gu) & Contract Owner'
  }},
  {{
    id: 'V3',
    short: 'V3 • Luminance Heatmap',
    paradigm: 'V3 • Luminance Legal-Grade AI Anomaly Radar',
    title: 'Variation 3: 12-Clause Traffic-Light Risk Heatmap & Deviation Radar',
    subtitle: 'Proportional 12-tile traffic-light matrix (Red Lockout/Conflict, Amber Negotiable, Green Auto-Cleared) that flips to Emerald Green as clauses are accepted.',
    bestFor: 'Workflow 1 Intake Triage & Risk Audit'
  }},
  {{
    id: 'V4',
    short: 'V4 • Litera 3-Col',
    paradigm: 'V4 • Litera Compare / Kira 3-Column Matrix',
    title: 'Variation 4: 3-Column Synchronized Redline Matrix (Proforma | Vendor | Counter)',
    subtitle: 'Side-by-side aligned columns eliminating redline-on-redline confusion: Col 1 Proforma Baseline, Col 2 Apex Redline, Col 3 Live Editable Counter-Proposal.',
    bestFor: 'Legal & Procurement Redline Drafters'
  }},
  {{
    id: 'V5',
    short: 'V5 • Cymbal Dark SQL',
    paradigm: 'V5 • Cymbal Capital / Bloomberg Institutional Dark Terminal',
    title: 'Variation 5: Institutional Dark Analytics Terminal + BigQuery SQL Drawer',
    subtitle: 'Matches Cymbal Capital dark screenshots — high-density clause blotter, cosine similarity meters, and expandable Underlying BigQuery SQL drawer.',
    bestFor: 'Tax (Pradeep Gupta) & Cloud/Data Evaluators'
  }},
  {{
    id: 'V6',
    short: 'V6 • SpotDraft Wizard',
    paradigm: 'V6 • SpotDraft VerifAI / Superhuman Keyboard Focus Mode',
    title: 'Variation 6: Guided 4-Step Exception Wizard with Keyboard Shortcuts (J/K/A/R/C)',
    subtitle: 'Hides the 8 untouched clauses and steps sequentially through Exception 1 of 4 → 4 of 4 for <90-second distraction-free SME sign-off.',
    bestFor: 'Time-Constrained Domain SMEs'
  }},
  {{
    id: 'V7',
    short: 'V7 • Outlook Kanban',
    paradigm: 'V7 • Linear / Jira Swimlanes + Microsoft Outlook Live Hub',
    title: 'Variation 7: Multi-SME Kanban Board & Live Outlook Email Thread Drawer',
    subtitle: 'Tracks all 12 clauses across 4 workflow columns (Auto-Cleared, Routed in Outlook, Conflict Flagged, Approved in Working .docx) with live email previews.',
    bestFor: 'Rahul Kasanagottu (Workflow 1 & 3 Comms)'
  }},
  {{
    id: 'V8',
    short: 'V8 • Conflict Graph',
    paradigm: 'V8 • Palantir Foundry / Systems Traceability Ontology Graph',
    title: 'Variation 8: Interactive Cross-Clause Dependency & Regulatory Lockout Graph',
    subtitle: 'Visual SVG node graph connecting SP3 §4.1 Tariffs ↔ GP1 §3.1 $45M FFP SOW Lock, FAA 14 CFR Part 21.140, and DoD DFARS 252.204-7012.',
    bestFor: 'Pradeep Gupta (Tax) & Systems Compliance'
  }},
  {{
    id: 'V9',
    short: 'V9 • MS Word 365',
    paradigm: 'V9 • Authentic Microsoft Word 365 Desktop Track-Changes Simulator',
    title: 'Variation 9: MS Word 365 Review Ribbon + 8.5"×11" Sheet + Right-Margin Balloons',
    subtitle: 'Pixel-faithful Word desktop preview with All Markup / Simple Markup / No Markup toggle and right-margin <w:comment w:author="..."> balloons.',
    bestFor: 'Traditional Counsel & Counterparty Preview'
  }},
  {{
    id: 'V10',
    short: 'V10 • GitHub PR Diff',
    paradigm: 'V10 • GitHub Pull Request / Critique Code-Review Diff',
    title: 'Variation 10: PR #8921 Line-Numbered Diff + Automated Regulatory CI Checks',
    subtitle: 'Treats vendor markup as a Pull Request with file tree, Unified/Split line diffs, failing FAA/DFARS/FFP CI checks, and "± Commit suggestion" blocks.',
    bestFor: 'Alex Wilber (Cyber) & Megan Bowen (QA)'
  }},
  {{
    id: 'V11',
    short: 'V11 • Exec Bento Room',
    paradigm: 'V11 • Icertis Executive Cockpit / Apple Bento Grid',
    title: 'Variation 11: Executive Bento Deal Room & Dollarized Exposure Waterfall',
    subtitle: 'Translates redlines into Dollarized Exposure ($45M FFP vs. +$18.5M Vendor Ask vs. $900K Tariff Cap), SVG Precedent Rings, and 1-Click Executive Sign-Off.',
    bestFor: 'VP Procurement, CFO & General Counsel Gates'
  }},
  {{
    id: 'V12',
    short: 'V12 • AI Co-Pilot Split',
    paradigm: 'V12 • Harvey AI / Claude Artifacts / Spark Canvas Co-Pilot',
    title: 'Variation 12: Conversational AI Co-Pilot + Live Contract Artifact Canvas',
    subtitle: 'Left 400px interactive prompt studio with 1-click rewrite chips; Right live updating contract canvas and human Word comment margin.',
    bestFor: 'Spark Desktop Users & Custom Clause Iteration'
  }}
];

const KEEP_COMPONENT_OPTIONS = [
  'Emerald Stage & Paper Card',
  'Floating 4-Action Menu (Rewrite/Accept/Reject/Comment)',
  'Orange-Red Strike + Coral Counter Diff',
  'Clean Accepted Text Resolution Toggle',
  '3-Column Synchronized Diff (Proforma|Vendor|Counter)',
  'Collapsible BigQuery SQL & Vector Search Drawer',
  '12-Clause Traffic-Light Risk Heatmap',
  'Cross-Clause Dependency & Conflict SVG Graph',
  'MS Word Right-Margin Comment Balloons (w:author)',
  'GitHub PR Suggested Change Commit Box',
  'Outlook SME Routing & Inbox Thread Preview',
  'Executive Financial Exposure Waterfall & Rings'
];

const QUICK_TAGS = [
  '+ Crystal-clear counter diff',
  '+ Love Accept -> Clean Doc flow',
  '+ Great for SME review',
  '+ Great for Contract Owner',
  '+ Strong BigQuery precedent UX',
  '+ Clear human comment attribution',
  '+ Feels like real Word / Litera',
  '- Too dense / busy',
  '- Needs wider text column',
  '- Combine with another view'
];

// Shared Reactive Lab State across all 12 Variations
window.CLMLabState = {{
  activeVariation: 'V1',
  activeClauseId: 'GP1-19',
  activePersona: 'Rahul Kasanagottu',
  wordMarkupMode: 'all', // for V9: 'all' | 'simple' | 'clean'
  prDiffMode: 'split',   // for V10: 'split' | 'unified'
  sqlDrawerOpen: true,   // for V5
  rewriteDrawerOpen: false,
  commentDrawerOpen: false,
  copilotMessages: [
    {{ role: 'assistant', text: 'Parsed 12 clauses in Deal BA-2026-AV-8921 ($45M FFP). 8 clauses auto-cleared; 4 redlined exceptions matched against 64 BigQuery Tier-1 Avionics precedents (16 per clause). Click any prompt chip below or type an instruction to rewrite the active clause.' }}
  ],
  clauses: {{}}
}};

function initClauseState(presetMode) {{
  const rawClauses = LAB_DATA.deal.clauses;
  rawClauses.forEach(c => {{
    const cid = c.clause_id;
    const def = LAB_DATA.defaults[cid] || {{}};
    let accepted = false;
    let showClean = false;
    if (presetMode === 'polled' && (cid === 'GP1-12' || cid === 'SP3-04' || cid === 'SP5-03')) {{
      accepted = true;
      showClean = true;
    }} else if (presetMode === 'consolidated' && c.has_redline) {{
      accepted = true;
      showClean = true;
    }}
    window.CLMLabState.clauses[cid] = {{
      ...c,
      selected_option: def.option || 'compromise_tier_1',
      counter_text: def.counter_text || c.boeing_baseline_text,
      reviewer_name: def.reviewer || 'Rahul Kasanagottu',
      reviewer_role: def.role || 'Contract Owner',
      guardrail_code: def.guardrail_code || 'STANDARD',
      guardrail_type: def.guardrail_type || 'STANDARD',
      user_comment: def.user_comment || '',
      accepted: accepted,
      show_clean: showClean
    }};
  }});
}}
initClauseState('intake');

// Load or initialize UX Evaluation Notes from localStorage
const EVAL_STORAGE_KEY = 'cymbal_clm_12_variations_eval_v1';
let uxEvalNotes = {{
  overall_synthesis: '',
  variations: {{}}
}};
try {{
  const saved = localStorage.getItem(EVAL_STORAGE_KEY);
  if (saved) uxEvalNotes = JSON.parse(saved);
}} catch (e) {{}}

VARIATIONS_META.forEach(v => {{
  if (!uxEvalNotes.variations[v.id]) {{
    uxEvalNotes.variations[v.id] = {{
      id: v.id,
      title: v.title,
      rating: 0,
      verdict: '',
      keep_components: [],
      tags: [],
      notes: ''
    }};
  }}
}});

function persistEvalNotes() {{
  try {{
    localStorage.setItem(EVAL_STORAGE_KEY, JSON.stringify(uxEvalNotes));
  }} catch (e) {{}}
  const el = document.getElementById('evalSaveIndicator');
  if (el) {{
    el.textContent = '✓ Saved (' + new Date().toLocaleTimeString() + ')';
  }}
  updateRatedCountBadge();
  // Also asynchronously persist to host loopback bridge if available
  fetch('http://127.0.0.1:58921/api/ux-notes', {{
    method: 'POST',
    headers: {{ 'Content-Type': 'application/json' }},
    body: JSON.stringify(uxEvalNotes)
  }}).catch(() => {{}});
}}

function escapeHtml(s) {{
  return String(s || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}}

function computeWordDiffHtml(oldText, newText, darkTheme = false) {{
  const a = String(oldText || '').trim().split(/\\s+/);
  const b = String(newText || '').trim().split(/\\s+/);
  const m = a.length, n = b.length;
  const dp = Array.from({{ length: m + 1 }}, () => new Int32Array(n + 1));
  for (let i = m - 1; i >= 0; i--) {{
    for (let j = n - 1; j >= 0; j--) {{
      if (a[i] === b[j]) dp[i][j] = 1 + dp[i + 1][j + 1];
      else dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
    }}
  }}
  const delClass = darkTheme ? 'dark-del' : 'diff-del';
  const insClass = darkTheme ? 'dark-ins' : 'diff-ins';
  let i = 0, j = 0;
  const out = [];
  let dels = [], ins = [];
  const flush = () => {{
    if (dels.length) {{
      out.push(`<del class="${{delClass}}" title="Replaced text">${{escapeHtml(dels.join(' '))}}</del>`);
      dels = [];
    }}
    if (ins.length) {{
      out.push(`<ins class="${{insClass}}" title="Proposed Cymbal Counter-Position">${{escapeHtml(ins.join(' '))}}</ins>`);
      ins = [];
    }}
  }};
  while (i < m && j < n) {{
    if (a[i] === b[j]) {{
      flush();
      out.push(escapeHtml(a[i]));
      i++; j++;
    }} else if (dp[i + 1][j] >= dp[i][j + 1]) {{
      dels.push(a[i++]);
    }} else {{
      ins.push(b[j++]);
    }}
  }}
  while (i < m) dels.push(a[i++]);
  while (j < n) ins.push(b[j++]);
  flush();
  return out.join(' ');
}}

// Sync accepted/edited position to BA-2026-AV-8921_Working_Review.docx via Loopback Bridge
async function syncClauseToWorkingDocx(cid) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  try {{
    await fetch('http://127.0.0.1:58921/api/review', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{
        clause_id: cid,
        sme_team: c.sme_team,
        option: c.selected_option,
        counter_text: c.counter_text,
        reviewer_name: c.reviewer_name,
        user_comment: c.user_comment
      }})
    }});
  }} catch (e) {{}}
}}

function acceptClauseChange(cid, optionKey) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  if (optionKey) {{
    c.selected_option = optionKey;
    if (optionKey === 'hold_firm') c.counter_text = c.boeing_baseline_text;
    else if (optionKey === 'accept_vendor') c.counter_text = c.vendor_redline_text;
    else if (optionKey === 'compromise_tier_1') c.counter_text = LAB_DATA.defaults[cid].counter_text;
  }}
  c.accepted = true;
  c.show_clean = true;
  syncClauseToWorkingDocx(cid);
  renderAll();
}}

function rejectVendorChange(cid) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.selected_option = 'hold_firm';
  c.counter_text = c.boeing_baseline_text;
  c.accepted = true;
  c.show_clean = true;
  syncClauseToWorkingDocx(cid);
  renderAll();
}}

function toggleCleanView(cid) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.show_clean = !c.show_clean;
  renderAll();
}}

function updateClauseCounterText(cid, newText) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.counter_text = newText;
  c.selected_option = 'custom_counter';
  c.show_clean = false;
  // Update live diff preview if inside V1/V2/V12 without losing textarea focus
  const liveDiffEl = document.getElementById('liveDiffPreview_' + cid);
  if (liveDiffEl) {{
    liveDiffEl.innerHTML = computeWordDiffHtml(c.vendor_redline_text, newText, window.CLMLabState.activeVariation === 'V5');
  }}
}}

function updateClauseComment(cid, newComment) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.user_comment = newComment;
}}

function updateClauseReviewer(cid, newReviewer) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.reviewer_name = newReviewer;
}}

function changeGlobalPersona(personaName) {{
  window.CLMLabState.activePersona = personaName;
  const activeC = window.CLMLabState.clauses[window.CLMLabState.activeClauseId];
  if (activeC) activeC.reviewer_name = personaName;
  // Auto-select the clause owned by that SME
  if (personaName === 'Pradeep Gupta') window.CLMLabState.activeClauseId = 'SP3-04';
  else if (personaName === 'Megan Bowen') window.CLMLabState.activeClauseId = 'GP1-12';
  else if (personaName === 'Lee Gu') window.CLMLabState.activeClauseId = 'GP1-19';
  else if (personaName === 'Alex Wilber') window.CLMLabState.activeClauseId = 'SP5-03';
  renderAll();
}}

function setDemoPreset(mode) {{
  initClauseState(mode);
  renderAll();
}}

function selectVariation(varId) {{
  const applySwitch = () => {{
    window.CLMLabState.activeVariation = varId;
    renderAll();
    const heading = document.getElementById('varTitleHeading');
    if (heading) heading.focus({{ preventScroll: true }});
  }};
  if (document.startViewTransition) {{
    document.startViewTransition(applySwitch);
  }} else {{
    applySwitch();
  }}
}}

function prevVariation() {{
  const idx = VARIATIONS_META.findIndex(v => v.id === window.CLMLabState.activeVariation);
  const prevIdx = (idx - 1 + VARIATIONS_META.length) % VARIATIONS_META.length;
  selectVariation(VARIATIONS_META[prevIdx].id);
}}

function nextVariation() {{
  const idx = VARIATIONS_META.findIndex(v => v.id === window.CLMLabState.activeVariation);
  const nextIdx = (idx + 1) % VARIATIONS_META.length;
  selectVariation(VARIATIONS_META[nextIdx].id);
}}

function selectClause(cid) {{
  window.CLMLabState.activeClauseId = cid;
  renderAll();
}}

// Helper: Render Precedent Distribution Bar & Top Deals Table for a Clause
function renderPrecedentBlockHtml(cid, dark = false) {{
  const prec = LAB_DATA.precedents[cid] || {{}};
  const dist = prec.distribution || {{}}; const stats = {{ held_firm_pct: dist.held_firm_pct ?? 88, compromise_pct: dist.compromise_tier_1_pct ?? 12, accepted_vendor_pct: dist.accepted_vendor_pct ?? 0, held_firm_count: dist.held_firm_count ?? 14, compromise_count: dist.compromise_tier_1_count ?? 2, accepted_vendor_count: dist.accepted_vendor_count ?? 0 }};
  const deals = (prec.precedents || []).slice(0, 5);
  const surfaceCls = dark ? 'bg-slate-900 border-slate-800 text-slate-200' : 'bg-slate-50 border-slate-200 text-slate-800';
  const subTextCls = dark ? 'text-slate-400' : 'text-slate-500';

  const rows = deals.map(d => `
    <tr class="border-t ${{dark ? 'border-slate-800' : 'border-slate-200'}} text-xs">
      <td class="py-2 px-2.5 font-bold">${{escapeHtml(d.supplier_name)}}</td>
      <td class="py-2 px-2.5 tabular-nums ${{subTextCls}}">${{escapeHtml(d.contract_id)}} (${{escapeHtml(d.boeing_program)}})</td>
      <td class="py-2 px-2.5">
        <span class="px-2 py-0.5 rounded-full text-xs font-bold ${{d.outcome_category === 'HELD_FIRM' ? 'bg-emerald-500/20 text-emerald-600' : 'bg-blue-500/20 text-blue-600'}}">
          ${{escapeHtml(d.outcome_category)}}
        </span>
      </td>
      <td class="py-2 px-2.5 tabular-nums font-bold text-blue-500">${{(Number(d.similarity_score || 0.85) * 100).toFixed(1)}}%</td>
      <td class="py-2 px-2.5 text-xs ${{subTextCls}}">${{escapeHtml(d.final_agreed_language).slice(0, 125)}}…</td>
      <td class="py-2 px-2.5 text-right">
        <button onclick="adoptPrecedentLanguage('${{cid}}', ${{JSON.stringify(d.final_agreed_language).replace(/"/g, '&quot;')}})" class="px-2 py-1 rounded text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white cursor-pointer">
          Use Language
        </button>
      </td>
    </tr>
  `).join('');

  return `
    <figure class="p-4 rounded-xl border ${{surfaceCls}} space-y-3 m-0">
      <figcaption class="flex flex-wrap items-center justify-between gap-2">
        <span class="text-xs font-extrabold uppercase tracking-wider">
          📊 BigQuery Precedent Telemetry (<code>vertex-ai-demos-468803.boeing_clm</code> • n=16 Tier-1 Deals for ${{cid}})
        </span>
        <span class="text-xs font-bold tabular-nums">
          <span class="text-emerald-600">● Held Firm: ${{stats.held_firm_pct}}% (${{stats.held_firm_count}}/16)</span> &nbsp;|&nbsp;
          <span class="text-blue-600">● Tier-1 Compromise: ${{stats.compromise_pct}}% (${{stats.compromise_count}}/16)</span> &nbsp;|&nbsp;
          <span class="text-amber-600">● Vendor Ask: ${{stats.accepted_vendor_pct}}% (${{stats.accepted_vendor_count}}/16)</span>
        </span>
      </figcaption>
      <div class="h-3 rounded-full overflow-hidden flex bg-slate-200">
        <div style="width:${{stats.held_firm_pct}}%;background:#10b981;"></div>
        <div style="width:${{stats.compromise_pct}}%;background:#2563eb;"></div>
        <div style="width:${{stats.accepted_vendor_pct}}%;background:#f59e0b;"></div>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="text-xs ${{subTextCls}}">
              <th class="py-1.5 px-2.5">Tier-1 Supplier</th>
              <th class="py-1.5 px-2.5">Deal / Program</th>
              <th class="py-1.5 px-2.5">Outcome</th>
              <th class="py-1.5 px-2.5">Cosine Sim</th>
              <th class="py-1.5 px-2.5">Agreed Counter-Language</th>
              <th class="py-1.5 px-2.5 text-right">Action</th>
            </tr>
          </thead>
          <tbody>${{rows}}</tbody>
        </table>
      </div>
    </figure>
  `;
}}

function adoptPrecedentLanguage(cid, text) {{
  const c = window.CLMLabState.clauses[cid];
  if (!c) return;
  c.counter_text = text;
  c.selected_option = 'custom_counter';
  c.show_clean = false;
  renderAll();
}}

// ============================================================================
// VARIATION 1: EMERALD STAGE & FLOATING ACTION CARD (SCREENSHOT MATCH)
// ============================================================================
function renderV1() {{
  const cid = window.CLMLabState.activeClauseId;
  const c = window.CLMLabState.clauses[cid];
  const diffHtml = computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false);

  const bodyHtml = c.show_clean ? `
    <div class="bg-emerald-50 border border-emerald-300 border-l-4 border-l-emerald-600 p-4 rounded-xl space-y-2">
      <div class="flex flex-wrap items-center justify-between gap-2">
        <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-900">
          ✓ Change Accepted &amp; Written Cleanly to BA-2026-AV-8921_Working_Review.docx (by ${{escapeHtml(c.reviewer_name)}})
        </span>
        <button onclick="toggleCleanView('${{cid}}')" class="px-2.5 py-1 rounded-md border border-emerald-400 bg-white text-emerald-900 text-xs font-bold cursor-pointer">
          🔍 Inspect Redline Strikethrough
        </button>
      </div>
      <p class="text-base leading-relaxed text-slate-900 font-medium m-0">${{escapeHtml(c.counter_text)}}</p>
    </div>
  ` : `
    <div id="liveDiffPreview_${{cid}}" class="text-base leading-relaxed text-slate-900 p-3.5 rounded-xl border border-slate-200 bg-white">
      ${{diffHtml}}
    </div>
  `;

  return `
    <div class="space-y-4">
      <div class="emerald-stage grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        <!-- White Legal Sheet -->
        <div class="lg:col-span-9 legal-sheet space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 pb-3">
            <div>
              <div class="text-xs font-bold uppercase tracking-wider text-emerald-700">
                Master Subcontract Agreement — Cymbal GP1 / SP3 / SP5 (Deal BA-2026-AV-8921)
              </div>
              <h2 class="text-xl font-extrabold text-slate-900 mt-0.5">
                ${{escapeHtml(c.clause_ref)}} — ${{escapeHtml(c.clause_title)}}
              </h2>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-extrabold ${{c.accepted ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-900'}}">
              ${{c.accepted ? '✓ ACCEPTED IN WORKING DOC' : '⏳ COUNTER-POSITION READY FOR REVIEW'}}
            </span>
          </div>

          <p class="text-xs text-slate-400 leading-relaxed m-0">
            This Master Subcontract Agreement is entered into by and between Cymbal Aerospace Corporation ("Buyer") and Apex AeroSystems Inc. ("Seller") for 300 Shipsets of the FCC-900 Flight Control Computer Subsystem ($45,000,000 Firm-Fixed-Price). Guardrail: <strong>${{escapeHtml(c.guardrail_code)}}</strong>.
          </p>

          ${{bodyHtml}}

          <!-- Rewrite with Input Drawer -->
          <div id="v1RewriteBox" style="display:${{window.CLMLabState.rewriteDrawerOpen ? 'block' : 'none'}};" class="p-4 rounded-xl bg-slate-50 border border-slate-300 space-y-2.5">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-xs font-extrabold uppercase text-slate-800">✦ Rewrite Counter-Position (Live Diff Updates as You Type)</span>
              <div class="flex gap-1.5">
                <button onclick="acceptClauseChange('${{cid}}','hold_firm')" class="px-2.5 py-1 rounded bg-white border border-slate-300 text-xs font-bold cursor-pointer">Hold Firm (Baseline)</button>
                <button onclick="acceptClauseChange('${{cid}}','compromise_tier_1')" class="px-2.5 py-1 rounded bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs font-bold cursor-pointer">★ Recommended Tier-1 Counter</button>
                <button onclick="acceptClauseChange('${{cid}}','accept_vendor')" class="px-2.5 py-1 rounded bg-rose-50 border border-rose-300 text-rose-900 text-xs font-bold cursor-pointer">Accept Vendor Ask</button>
              </div>
            </div>
            <textarea oninput="updateClauseCounterText('${{cid}}', this.value)" class="auto-grow w-full p-3 rounded-lg border border-slate-300 text-sm bg-white text-slate-900">${{escapeHtml(c.counter_text)}}</textarea>
          </div>

          <!-- Human Reviewer Comment Card (w:author) -->
          <div class="p-4 rounded-xl bg-blue-50/70 border border-blue-200 space-y-2">
            <div class="flex flex-wrap items-center justify-between gap-2">
              <span class="text-xs font-extrabold uppercase tracking-wider text-blue-950">
                💬 Word Margin Comment (<code>w:comment</code>) — Added as Human User (Not System):
              </span>
              <div class="flex items-center gap-2">
                <span class="text-xs font-bold text-slate-600">Author (w:author):</span>
                <input type="text" value="${{escapeHtml(c.reviewer_name)}}" oninput="updateClauseReviewer('${{cid}}', this.value)" class="px-2.5 py-1 rounded border border-blue-300 bg-white text-xs font-bold text-slate-900" />
              </div>
            </div>
            <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-2.5 rounded-lg border border-blue-200 bg-white text-xs text-slate-800">${{escapeHtml(c.user_comment)}}</textarea>
          </div>
        </div>

        <!-- Floating 4-Action Menu Card (Matching Screenshot) -->
        <div class="lg:col-span-3 space-y-3">
          <div class="floating-action-menu">
            <button class="floating-action-btn" onclick="window.CLMLabState.rewriteDrawerOpen=!window.CLMLabState.rewriteDrawerOpen;renderAll();">
              <span class="w-6 h-6 rounded-full bg-slate-900 text-white inline-flex items-center justify-center text-xs">✦</span>
              <span>Rewrite with Input</span>
            </button>
            <div class="h-px bg-slate-200 my-0.5"></div>
            <button class="floating-action-btn ${{c.accepted ? 'active-accept' : ''}}" onclick="acceptClauseChange('${{cid}}')">
              <span class="w-6 h-6 inline-flex items-center justify-center text-base font-extrabold text-emerald-700">✓</span>
              <span>Accept changes</span>
            </button>
            <div class="h-px bg-slate-200 my-0.5"></div>
            <button class="floating-action-btn" onclick="rejectVendorChange('${{cid}}')">
              <span class="w-6 h-6 inline-flex items-center justify-center text-base font-extrabold text-rose-700">✕</span>
              <span>Reject changes (Hold Firm)</span>
            </button>
            <div class="h-px bg-slate-200 my-0.5"></div>
            <button class="floating-action-btn" onclick="syncClauseToWorkingDocx('${{cid}}');alert('Saved comment as ' + window.CLMLabState.clauses['${{cid}}'].reviewer_name + ' to BA-2026-AV-8921_Working_Review.docx!');">
              <span class="w-6 h-6 inline-flex items-center justify-center text-sm">💬</span>
              <span>Comment (as ${{escapeHtml(c.reviewer_name.split(' ')[0])}})</span>
            </button>
          </div>

          <div class="p-3.5 rounded-xl bg-white/95 text-slate-800 shadow-lg space-y-1.5 text-xs">
            <div class="font-extrabold text-slate-900 uppercase">Diff Legend</div>
            <div><del class="diff-del">Orange-Red Strike</del> = Rejected vendor ask</div>
            <div><ins class="diff-ins">Coral Highlight</ins> = Proposed Cymbal counter</div>
            <div class="pt-1 text-slate-500">Clicking <strong>✓ Accept changes</strong> resolves markup into clean contract text in <code>BA-2026-AV-8921_Working_Review.docx</code>.</div>
          </div>
        </div>
      </div>

      ${{renderPrecedentBlockHtml(cid, false)}}
    </div>
  `;
}}

// ============================================================================
// VARIATION 2: IRONCLAD AI ASSIST SPLIT-PANE READER + PLAYBOOK SIDEBAR
// ============================================================================
function renderV2() {{
  const activeCid = window.CLMLabState.activeClauseId;
  const activeClause = window.CLMLabState.clauses[activeCid];

  const allClausesHtml = Object.values(window.CLMLabState.clauses).map(c => {{
    const isSelected = c.clause_id === activeCid;
    const borderCls = isSelected ? 'border-2 border-indigo-600 ring-4 ring-indigo-500/15 bg-indigo-50/20' : 'border border-slate-200 bg-white hover:border-slate-300';
    let contentHtml = '';
    if (!c.has_redline) {{
      contentHtml = `<p class="text-xs text-slate-600 leading-relaxed m-0">${{escapeHtml(c.boeing_baseline_text)}}</p>`;
    }} else if (c.show_clean) {{
      contentHtml = `<p class="text-sm text-emerald-950 bg-emerald-50 p-3 rounded-lg border-l-4 border-emerald-600 font-medium m-0">${{escapeHtml(c.counter_text)}}</p>`;
    }} else {{
      contentHtml = `<div class="text-sm leading-relaxed text-slate-900">${{computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)}}</div>`;
    }}
    return `
      <article onclick="if('${{c.has_redline}}'==='true') selectClause('${{c.clause_id}}')" class="p-4 rounded-xl ${{borderCls}} transition cursor-pointer space-y-2">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <span class="font-extrabold text-xs text-slate-900">${{escapeHtml(c.clause_ref)}} — ${{escapeHtml(c.clause_title)}}</span>
          ${{!c.has_redline
            ? '<span class="px-2 py-0.5 rounded-full text-xs font-bold bg-slate-100 text-slate-600">✓ Untouched Baseline</span>'
            : (c.accepted
                ? `<span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">✓ Accepted by ${{escapeHtml(c.reviewer_name)}}</span>`
                : `<span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-100 text-rose-800">⚠️ Redlined • ${{escapeHtml(c.sme_team)}}</span>`)
          }}
        </div>
        ${{contentHtml}}
      </article>
    `;
  }}).join('');

  return `
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
      <!-- Left 7 Cols: Continuous 12-Clause Contract Scroll -->
      <div class="lg:col-span-7 bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3 max-h-[76vh] overflow-y-auto">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3 sticky top-0 bg-white z-10">
          <div>
            <h2 class="text-sm font-extrabold text-slate-900 m-0">📄 Full 12-Clause Contract Reader (<code>BA-2026-AV-8921_Working_Review.docx</code>)</h2>
            <p class="text-xs text-slate-500 m-0">Click any of the 4 redlined clauses to load its Playbook Guardrails &amp; BigQuery Precedents on the right.</p>
          </div>
          <span class="text-xs font-bold text-indigo-600">Ironclad AI Assist Split View</span>
        </div>
        ${{allClausesHtml}}
      </div>

      <!-- Right 5 Cols: Sticky Playbook Guardrail & Precedent Copilot Sidebar -->
      <div class="lg:col-span-5 bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-4 sticky top-20">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3">
          <div>
            <span class="px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 text-xs font-extrabold">${{escapeHtml(activeClause.sme_team)}} PLAYBOOK COPILOT</span>
            <h3 class="text-base font-extrabold text-slate-900 mt-1 mb-0">${{escapeHtml(activeClause.clause_ref)}} — ${{escapeHtml(activeClause.clause_title)}}</h3>
          </div>
          <button onclick="toggleCleanView('${{activeCid}}')" class="px-2.5 py-1 rounded border border-slate-300 text-xs font-bold cursor-pointer">
            ${{activeClause.show_clean ? '🔍 Show Diff' : '📄 Show Clean'}}
          </button>
        </div>

        <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-950">
          <strong>Guardrail / Lockout:</strong> ${{escapeHtml(activeClause.guardrail_code)}}
        </div>

        <!-- 3 Playbook Tier Cards -->
        <div class="space-y-2">
          <div class="text-xs font-extrabold uppercase text-slate-600">Select Playbook Position to Apply to Contract:</div>
          <div class="p-3 rounded-xl border-2 border-emerald-500 bg-emerald-50/40 space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-extrabold text-emerald-950">★ Recommended Counter-Position (${{escapeHtml(LAB_DATA.defaults[activeCid].option)}})</span>
              <button onclick="acceptClauseChange('${{activeCid}}', '${{LAB_DATA.defaults[activeCid].option}}')" class="px-3 py-1 rounded-md bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold cursor-pointer">
                ✓ Apply &amp; Accept in Doc
              </button>
            </div>
            <textarea oninput="updateClauseCounterText('${{activeCid}}', this.value)" class="auto-grow w-full p-2 rounded border border-emerald-300 bg-white text-xs text-slate-900">${{escapeHtml(activeClause.counter_text)}}</textarea>
          </div>

          <div class="flex gap-2">
            <button onclick="acceptClauseChange('${{activeCid}}','hold_firm')" class="flex-1 py-2 px-3 rounded-lg border border-slate-300 bg-slate-50 hover:bg-slate-100 text-xs font-bold cursor-pointer">
              🛡️ Apply Option A: Hold Firm Baseline
            </button>
            <button onclick="acceptClauseChange('${{activeCid}}','accept_vendor')" class="flex-1 py-2 px-3 rounded-lg border border-rose-300 bg-rose-50 hover:bg-rose-100 text-rose-900 text-xs font-bold cursor-pointer">
              ⚠️ Apply Option C: Accept Vendor
            </button>
          </div>
        </div>

        <!-- Author & Comment -->
        <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-extrabold text-slate-700">💬 Word Margin Comment (w:author):</span>
            <input type="text" value="${{escapeHtml(activeClause.reviewer_name)}}" oninput="updateClauseReviewer('${{activeCid}}', this.value)" class="px-2 py-0.5 rounded border border-slate-300 bg-white text-xs font-bold" />
          </div>
          <textarea oninput="updateClauseComment('${{activeCid}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 bg-white text-xs">${{escapeHtml(activeClause.user_comment)}}</textarea>
        </div>

        ${{renderPrecedentBlockHtml(activeCid, false)}}
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 3: LUMINANCE TRAFFIC-LIGHT RISK HEATMAP & ANOMALY RADAR
// ============================================================================
function renderV3() {{
  const activeCid = window.CLMLabState.activeClauseId;
  const activeC = window.CLMLabState.clauses[activeCid];

  const tilesHtml = Object.values(window.CLMLabState.clauses).map(c => {{
    let colorCls = 'bg-emerald-50 border-emerald-300 text-emerald-950';
    let statusDot = '🟢 Auto-Cleared';
    if (c.has_redline) {{
      if (c.accepted) {{
        colorCls = 'bg-emerald-100 border-emerald-500 text-emerald-950 shadow-xs';
        statusDot = '🟢 Accepted (' + c.reviewer_name.split(' ')[0] + ')';
      }} else if (c.clause_id === 'GP1-19') {{
        colorCls = 'bg-amber-50 border-amber-400 text-amber-950';
        statusDot = '🟡 Negotiable Super-Cap';
      }} else {{
        colorCls = 'bg-rose-50 border-rose-400 text-rose-950';
        statusDot = '🔴 Lockout / FFP Conflict';
      }}
    }}
    const activeRing = c.clause_id === activeCid ? 'ring-4 ring-slate-900/20 scale-[1.02]' : '';
    return `
      <div onclick="if('${{c.has_redline}}'==='true') selectClause('${{c.clause_id}}')" class="p-3 rounded-xl border-2 ${{colorCls}} ${{activeRing}} transition cursor-pointer flex flex-col justify-between gap-2">
        <div class="flex items-center justify-between gap-1">
          <span class="font-extrabold text-xs tabular-nums">${{escapeHtml(c.clause_ref)}}</span>
          <span class="text-xs font-bold">${{statusDot}}</span>
        </div>
        <div class="text-xs font-bold leading-snug">${{escapeHtml(c.clause_title)}}</div>
        <div class="text-xs opacity-75 flex justify-between">
          <span>${{escapeHtml(c.sme_team)}}</span>
          <span>${{c.has_redline ? 'Click to Inspect →' : '100% Proforma'}}</span>
        </div>
      </div>
    `;
  }}).join('');

  return `
    <div class="space-y-5">
      <!-- Top 12-Clause Luminance Traffic-Light Matrix -->
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3">
        <div class="flex flex-wrap items-center justify-between gap-2">
          <div>
            <h2 class="text-sm font-extrabold text-slate-900 m-0">🚦 Luminance-Style 12-Clause Risk &amp; Anomaly Heatmap</h2>
            <p class="text-xs text-slate-500 m-0">Red/Amber tiles automatically flip to Emerald Green (🟢 Accepted) as you approve each counter-position below.</p>
          </div>
          <div class="flex gap-3 text-xs font-bold">
            <span class="text-rose-600">🔴 Critical Lockout / Conflict</span>
            <span class="text-amber-600">🟡 Commercial Deviation</span>
            <span class="text-emerald-600">🟢 Cleared / Accepted</span>
          </div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
          ${{tilesHtml}}
        </div>
      </div>

      <!-- Lower Surgical Inspector re-using Emerald Diff Card -->
      ${{renderV1()}}
    </div>
  `;
}}

// ============================================================================
// VARIATION 4: LITERA COMPARE 3-COLUMN SYNCHRONIZED REDLINE MATRIX
// ============================================================================
function renderV4() {{
  const redlinedIds = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];
  const rowsHtml = redlinedIds.map(cid => {{
    const c = window.CLMLabState.clauses[cid];
    const vendorDiffHtml = computeWordDiffHtml(c.boeing_baseline_text, c.vendor_redline_text, false);
    const counterDiffHtml = c.show_clean
      ? `<div class="p-3 rounded-lg bg-emerald-100/70 border-l-4 border-emerald-600 text-slate-900 font-medium">${{escapeHtml(c.counter_text)}}</div>`
      : computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false);

    return `
      <div class="bg-white border border-slate-300 rounded-2xl overflow-hidden shadow-xs">
        <!-- Clause Row Banner -->
        <div class="bg-slate-900 text-white px-4 py-2.5 flex flex-wrap items-center justify-between gap-2">
          <div class="flex items-center gap-2.5">
            <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 text-xs font-extrabold">${{escapeHtml(c.sme_team)}}</span>
            <span class="font-extrabold text-sm">${{escapeHtml(c.clause_ref)}} — ${{escapeHtml(c.clause_title)}}</span>
            <span class="text-xs text-amber-300 font-mono">(${{escapeHtml(c.guardrail_code)}})</span>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="toggleCleanView('${{cid}}')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-bold text-white cursor-pointer">
              ${{c.show_clean ? '🔍 Show Counter Diff' : '📄 Show Clean Text'}}
            </button>
            <button onclick="acceptClauseChange('${{cid}}')" class="px-3 py-1 rounded bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-extrabold cursor-pointer">
              ${{c.accepted ? '✓ Accepted in Working Doc' : '✓ Accept Column 3 Counter'}}
            </button>
          </div>
        </div>

        <!-- 3 Synchronized Columns -->
        <div class="grid grid-cols-1 lg:grid-cols-3 divide-y lg:divide-y-0 lg:divide-x divide-slate-200">
          <!-- Col 1: Cymbal Proforma -->
          <div class="p-4 bg-slate-50/60 space-y-2">
            <div class="text-xs font-extrabold uppercase tracking-wider text-slate-600">
              1. Cymbal Proforma Baseline (<code>Cymbal_GP1_Standard.docx</code>)
            </div>
            <p class="text-xs leading-relaxed text-slate-700 m-0">${{escapeHtml(c.boeing_baseline_text)}}</p>
          </div>

          <!-- Col 2: Apex Vendor Markup -->
          <div class="p-4 bg-rose-50/30 space-y-2">
            <div class="text-xs font-extrabold uppercase tracking-wider text-rose-800">
              2. Apex AeroSystems Redline (<code>Vendor_Redlined_GP1.docx</code>)
            </div>
            <div class="text-xs leading-relaxed text-slate-800">${{vendorDiffHtml}}</div>
            <div class="p-2 rounded bg-rose-100/60 text-rose-950 text-xs">
              <strong>Vendor Margin Note:</strong> ${{escapeHtml(c.vendor_comment)}}
            </div>
          </div>

          <!-- Col 3: Cymbal Counter-Position -->
          <div class="p-4 bg-emerald-50/30 space-y-2.5">
            <div class="flex items-center justify-between">
              <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-900">
                3. Cymbal Counter-Position (<code>Working_Review.docx</code>)
              </span>
              <span class="text-xs font-bold text-emerald-700">${{c.accepted ? '✓ LOCKED' : 'Editable'}}</span>
            </div>
            <div class="text-xs leading-relaxed text-slate-900">${{counterDiffHtml}}</div>
            <details class="text-xs">
              <summary class="font-bold text-blue-700 cursor-pointer">✦ Edit Counter Text or Word Comment (w:author=${{escapeHtml(c.reviewer_name)}})</summary>
              <div class="pt-2 space-y-2">
                <textarea oninput="updateClauseCounterText('${{cid}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 bg-white text-xs">${{escapeHtml(c.counter_text)}}</textarea>
                <div class="flex items-center gap-2">
                  <span class="font-bold">Comment Author:</span>
                  <input type="text" value="${{escapeHtml(c.reviewer_name)}}" oninput="updateClauseReviewer('${{cid}}', this.value)" class="px-2 py-0.5 rounded border border-slate-300 bg-white text-xs font-bold" />
                </div>
                <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 bg-white text-xs">${{escapeHtml(c.user_comment)}}</textarea>
              </div>
            </details>
          </div>
        </div>
      </div>
    `;
  }}).join('');

  return `<div class="space-y-4">${{rowsHtml}}</div>`;
}}

// ============================================================================
// VARIATION 5: CYMBAL INSTITUTIONAL DARK TERMINAL + BIGQUERY SQL DRAWER
// ============================================================================
function renderV5() {{
  const cid = window.CLMLabState.activeClauseId;
  const c = window.CLMLabState.clauses[cid];
  const darkDiffHtml = c.show_clean
    ? `<div class="p-4 rounded-xl bg-emerald-950/60 border border-emerald-500/50 text-emerald-200 text-sm leading-relaxed">✓ <strong>COMMITTED TO WORKING .DOCX (${{escapeHtml(c.reviewer_name)}}):</strong><br/>${{escapeHtml(c.counter_text)}}</div>`
    : `<div id="liveDiffPreview_${{cid}}" class="p-4 rounded-xl bg-slate-950 border border-slate-800 text-slate-100 text-sm leading-relaxed">${{computeWordDiffHtml(c.vendor_redline_text, c.counter_text, true)}}</div>`;

  const blotterRows = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'].map(id => {{
    const item = window.CLMLabState.clauses[id];
    const dist = LAB_DATA.precedents[id].distribution || {{}}; const st = {{ held_firm_pct: dist.held_firm_pct ?? 88, compromise_pct: dist.compromise_tier_1_pct ?? 12 }};
    const isSel = id === cid;
    return `
      <tr onclick="selectClause('${{id}}')" class="border-b border-slate-800/80 cursor-pointer ${{isSel ? 'bg-blue-950/50' : 'hover:bg-slate-900/80'}} text-xs">
        <td class="py-2.5 px-3 font-mono font-bold text-blue-400">${{escapeHtml(item.clause_ref)}}</td>
        <td class="py-2.5 px-3 font-semibold text-slate-200">${{escapeHtml(item.clause_title)}}</td>
        <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-xs">${{escapeHtml(item.sme_team)}}</span></td>
        <td class="py-2.5 px-3 tabular-nums text-emerald-400 font-bold">${{st.held_firm_pct}}% Firm / ${{st.compromise_pct}}% Comp</td>
        <td class="py-2.5 px-3 font-mono text-slate-300">${{escapeHtml(item.reviewer_name)}}</td>
        <td class="py-2.5 px-3">
          <span class="px-2 py-0.5 rounded-full text-xs font-bold ${{item.accepted ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40' : 'bg-amber-500/20 text-amber-300 border border-amber-500/40'}}">
            ${{item.accepted ? 'COMMITTED' : 'OPEN EXCEPTION'}}
          </span>
        </td>
      </tr>
    `;
  }}).join('');

  const sqlText = `WITH redline_query AS (
  SELECT ml_generate_embedding_result AS query_embedding
  FROM ML.GENERATE_EMBEDDING(
    MODEL vertex-ai-demos-468803.boeing_clm.text_embedding_005,
    (SELECT '${{cid}}: ${{c.clause_title.replace(/'/g, "")}}' AS content)
  )
)
SELECT
  base.contract_id,
  base.supplier_name,
  base.boeing_program,
  base.negotiation_outcome,
  ROUND(1 - distance, 4) AS cosine_similarity,
  base.final_agreed_language
FROM VECTOR_SEARCH(
  TABLE vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions,
  'redline_embedding',
  TABLE redline_query,
  top_k => 16,
  distance_type => 'COSINE',
  options => '{{"use_brute_force": true}}'
)
WHERE base.clause_id = '${{cid}}'
ORDER BY cosine_similarity DESC;`;

  return `
    <div class="bg-[#090d16] text-slate-100 rounded-2xl p-6 border border-slate-800 shadow-2xl space-y-5">
      <!-- Top Institutional Header & 4 KPI Cards (Cymbal Capital Style) -->
      <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-extrabold text-white">C</div>
          <div>
            <div class="flex items-center gap-2">
              <span class="font-extrabold tracking-wide text-sm text-white">CYMBAL AEROSPACE CLM TERMINAL</span>
              <span class="px-2 py-0.5 rounded text-xs font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">PROD</span>
            </div>
            <div class="text-xs font-mono text-slate-400">vertex-ai-demos-468803.boeing_clm • text-embedding-005</div>
          </div>
        </div>
        <div class="flex gap-2">
          <button onclick="acceptClauseChange('${{cid}}')" class="px-3.5 py-1.5 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-extrabold text-xs cursor-pointer">
            ✓ Execute Counter-Position Commit (${{cid}})
          </button>
          <button onclick="toggleCleanView('${{cid}}')" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs cursor-pointer">
            ${{c.show_clean ? '🔍 Inspect Diff' : '📄 Clean View'}}
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
        <div class="p-4 rounded-xl bg-[#111827] border border-slate-800">
          <div class="text-xs text-slate-400 uppercase font-semibold">FIRM-FIXED-PRICE CEILING (GP1 §3.1)</div>
          <div class="text-2xl font-extrabold text-white mt-1 tabular-nums">$45,000,000</div>
          <div class="text-xs text-emerald-400 mt-1">300 FCC-900 Shipsets @ $150K</div>
        </div>
        <div class="p-4 rounded-xl bg-[#111827] border border-slate-800">
          <div class="text-xs text-slate-400 uppercase font-semibold">SUPER-CAP COUNTER (GP1 §19)</div>
          <div class="text-2xl font-extrabold text-white mt-1 tabular-nums">$90,000,000 <span class="text-xs text-emerald-400">2.0x PO</span></div>
          <div class="text-xs text-slate-400 mt-1">69% Tier-1 Precedent (11/16 Deals)</div>
        </div>
        <div class="p-4 rounded-xl bg-[#111827] border border-slate-800">
          <div class="text-xs text-slate-400 uppercase font-semibold">HARMONIZED TARIFF CAP (SP3 §4.1)</div>
          <div class="text-2xl font-extrabold text-amber-400 mt-1 tabular-nums">$900,000 <span class="text-xs">+2.0% Max</span></div>
          <div class="text-xs text-slate-400 mt-1">50/50 Split &gt;5% (63% Precedent)</div>
        </div>
        <div class="p-4 rounded-xl bg-[#111827] border border-slate-800">
          <div class="text-xs text-slate-400 uppercase font-semibold">REGULATORY LOCKOUTS ENFORCED</div>
          <div class="text-2xl font-extrabold text-rose-400 mt-1 tabular-nums">2 MANDATORY</div>
          <div class="text-xs text-slate-400 mt-1">FAA Part 21.140 &amp; DFARS 72-Hr</div>
        </div>
      </div>

      <!-- Active Exception Blotter Matrix -->
      <div class="rounded-xl bg-[#111827] border border-slate-800 overflow-hidden">
        <div class="px-4 py-3 border-b border-slate-800 flex justify-between items-center">
          <span class="text-xs font-extrabold uppercase tracking-wider text-slate-300">Active Redline Exception Blotter (Click Row to Inspect)</span>
          <span class="text-xs font-mono text-slate-400">4 Redlined Clauses • 64 Historical Precedents</span>
        </div>
        <table class="w-full text-left border-collapse">
          <thead>
            <tr class="border-b border-slate-800 text-xs text-slate-400 uppercase">
              <th class="py-2 px-3">Clause</th>
              <th class="py-2 px-3">Title</th>
              <th class="py-2 px-3">Domain</th>
              <th class="py-2 px-3">BQ Precedent Split (n=16)</th>
              <th class="py-2 px-3">Reviewer (w:author)</th>
              <th class="py-2 px-3">Status</th>
            </tr>
          </thead>
          <tbody>${{blotterRows}}</tbody>
        </table>
      </div>

      <!-- Dark Diff & Rewrite Terminal -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <div class="lg:col-span-8 space-y-3">
          <div class="text-xs font-mono font-bold text-blue-400 uppercase">
            &gt;_ Active Clause Diff Inspector: ${{escapeHtml(c.clause_ref)}} (${{escapeHtml(c.guardrail_code)}})
          </div>
          ${{darkDiffHtml}}
          <textarea oninput="updateClauseCounterText('${{cid}}', this.value)" class="auto-grow w-full p-3 rounded-xl bg-[#111827] border border-slate-700 text-slate-100 text-xs font-mono">${{escapeHtml(c.counter_text)}}</textarea>
        </div>
        <div class="lg:col-span-4 p-4 rounded-xl bg-[#111827] border border-slate-800 space-y-2.5">
          <div class="text-xs font-mono font-bold text-emerald-400 uppercase">💬 Word Comment (<code>word/comments.xml</code>)</div>
          <label class="block text-xs text-slate-400">Human Reviewer (w:author):
            <input type="text" value="${{escapeHtml(c.reviewer_name)}}" oninput="updateClauseReviewer('${{cid}}', this.value)" class="w-full mt-1 px-2.5 py-1.5 rounded bg-slate-950 border border-slate-700 text-white text-xs font-bold" />
          </label>
          <label class="block text-xs text-slate-400">Comment Body:
            <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full mt-1 p-2.5 rounded bg-slate-950 border border-slate-700 text-slate-200 text-xs">${{escapeHtml(c.user_comment)}}</textarea>
          </label>
        </div>
      </div>

      <!-- Collapsible Underlying BigQuery SQL Drawer (Cymbal Capital Screenshot Pattern) -->
      <div class="rounded-xl bg-[#0d1322] border border-slate-800 overflow-hidden">
        <div onclick="window.CLMLabState.sqlDrawerOpen=!window.CLMLabState.sqlDrawerOpen;renderAll();" class="px-4 py-3 bg-slate-900/90 flex items-center justify-between cursor-pointer">
          <span class="font-mono text-xs font-bold text-blue-400">&gt;_ Underlying BigQuery SQL (VECTOR_SEARCH Precedent Engine — ${{cid}})</span>
          <span class="text-xs text-slate-400">${{window.CLMLabState.sqlDrawerOpen ? 'Hide SQL ▲' : 'Show SQL ▼'}}</span>
        </div>
        <div style="display:${{window.CLMLabState.sqlDrawerOpen ? 'block' : 'none'}};" class="p-4 space-y-4">
          <pre class="p-3.5 rounded-lg bg-slate-950 border border-slate-800 text-xs font-mono text-blue-300 overflow-x-auto m-0">${{escapeHtml(sqlText)}}</pre>
          ${{renderPrecedentBlockHtml(cid, true)}}
        </div>
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 6: SPOTDRAFT / SUPERHUMAN 4-STEP KEYBOARD WIZARD (FOCUS MODE)
// ============================================================================
function renderV6() {{
  const redlinedIds = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];
  const stepIdx = Math.max(0, redlinedIds.indexOf(window.CLMLabState.activeClauseId));
  const cid = redlinedIds[stepIdx];
  const c = window.CLMLabState.clauses[cid];
  const nextCid = redlinedIds[(stepIdx + 1) % redlinedIds.length];

  const stepperHtml = redlinedIds.map((id, i) => {{
    const item = window.CLMLabState.clauses[id];
    const active = id === cid;
    return `
      <button onclick="selectClause('${{id}}')" class="flex-1 p-3 rounded-xl border-2 text-left cursor-pointer transition ${{active ? 'border-indigo-600 bg-indigo-50/50' : (item.accepted ? 'border-emerald-400 bg-emerald-50/30' : 'border-slate-200 bg-white')}}">
        <div class="flex items-center justify-between text-xs font-bold">
          <span class="text-slate-500">STEP ${{i + 1}} OF 4</span>
          <span class="${{item.accepted ? 'text-emerald-700' : 'text-amber-700'}}">${{item.accepted ? '✓ Done' : '● Open'}}</span>
        </div>
        <div class="font-extrabold text-xs text-slate-900 mt-1">${{escapeHtml(item.clause_ref)}} — ${{escapeHtml(item.sme_team)}}</div>
      </button>
    `;
  }}).join('');

  return `
    <div class="max-w-4xl mx-auto space-y-4">
      <!-- Top 4-Step Progress Bar -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5">
        ${{stepperHtml}}
      </div>

      <!-- Center Zen Focus Card -->
      <div class="bg-white border-2 border-slate-200 rounded-2xl p-6 shadow-md space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-200 pb-3">
          <div>
            <span class="px-2.5 py-0.5 rounded-full bg-indigo-100 text-indigo-900 text-xs font-extrabold">
              EXCEPTION ${{stepIdx + 1}} OF 4 • ${{escapeHtml(c.guardrail_code)}}
            </span>
            <h2 class="text-xl font-extrabold text-slate-900 mt-1 mb-0">${{escapeHtml(c.clause_ref)}} — ${{escapeHtml(c.clause_title)}}</h2>
          </div>
          <span class="text-xs text-slate-500 font-mono">8 Untouched Clauses Auto-Cleared ✓</span>
        </div>

        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-base leading-relaxed">
          ${{c.show_clean
            ? `<div class="text-emerald-950 font-medium">✓ <strong>Accepted Clean Text:</strong> ${{escapeHtml(c.counter_text)}}</div>`
            : computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)
          }}
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
          <div class="space-y-1">
            <label class="text-xs font-extrabold text-slate-700">✦ Counter-Position Text:</label>
            <textarea oninput="updateClauseCounterText('${{cid}}', this.value)" class="auto-grow w-full p-2.5 rounded-lg border border-slate-300 text-xs">${{escapeHtml(c.counter_text)}}</textarea>
          </div>
          <div class="space-y-1">
            <label class="text-xs font-extrabold text-slate-700">💬 Human Reviewer Comment (w:author=${{escapeHtml(c.reviewer_name)}}):</label>
            <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-2.5 rounded-lg border border-slate-300 text-xs">${{escapeHtml(c.user_comment)}}</textarea>
          </div>
        </div>

        <!-- Superhuman-Style Keyboard Action Bar -->
        <div class="pt-3 border-t border-slate-200 flex flex-wrap items-center justify-between gap-2">
          <div class="flex flex-wrap gap-2">
            <button onclick="acceptClauseChange('${{cid}}');selectClause('${{nextCid}}');" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs cursor-pointer flex items-center gap-2">
              <kbd class="px-1.5 py-0.5 rounded bg-emerald-800 text-white font-mono">A</kbd>
              <span>Accept Counter &amp; Advance to Next →</span>
            </button>
            <button onclick="rejectVendorChange('${{cid}}');selectClause('${{nextCid}}');" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs cursor-pointer flex items-center gap-2">
              <kbd class="px-1.5 py-0.5 rounded bg-slate-950 text-white font-mono">H</kbd>
              <span>Hold Firm Baseline</span>
            </button>
            <button onclick="toggleCleanView('${{cid}}')" class="px-3 py-2 rounded-xl border border-slate-300 bg-white text-slate-800 font-bold text-xs cursor-pointer">
              ${{c.show_clean ? '🔍 Show Diff' : '📄 Preview Clean'}}
            </button>
          </div>
          <span class="text-xs text-slate-400 font-mono">Shortcuts: [J/K] Prev/Next Clause • [A] Accept</span>
        </div>
      </div>

      ${{renderPrecedentBlockHtml(cid, false)}}
    </div>
  `;
}}

// ============================================================================
// VARIATION 7: LINEAR / JIRA MULTI-SME SWIMLANE & OUTLOOK COMMS KANBAN BOARD
// ============================================================================
function renderV7() {{
  const all = Object.values(window.CLMLabState.clauses);
  const untouched = all.filter(c => !c.has_redline);
  const routed = all.filter(c => c.has_redline && !c.accepted && c.clause_id !== 'SP3-04');
  const conflicts = all.filter(c => c.has_redline && !c.accepted && c.clause_id === 'SP3-04');
  const approved = all.filter(c => c.has_redline && c.accepted);
  const activeC = window.CLMLabState.clauses[window.CLMLabState.activeClauseId];

  const renderCard = (c) => `
    <div onclick="selectClause('${{c.clause_id}}')" class="p-3.5 rounded-xl bg-white border-2 ${{c.clause_id === activeC.clause_id ? 'border-blue-600 shadow-md' : 'border-slate-200'}} space-y-2 cursor-pointer">
      <div class="flex items-center justify-between">
        <span class="font-mono font-extrabold text-xs text-slate-900">${{escapeHtml(c.clause_ref)}}</span>
        <span class="px-2 py-0.5 rounded text-xs font-bold bg-blue-50 text-blue-800">${{escapeHtml(c.sme_team)}}</span>
      </div>
      <div class="text-xs font-bold text-slate-800">${{escapeHtml(c.clause_title)}}</div>
      <div class="text-xs text-slate-500">👤 SME: <strong>${{escapeHtml(c.reviewer_name)}}</strong></div>
      <div class="pt-1 flex items-center justify-between gap-1">
        <span class="text-xs font-mono text-emerald-700">${{(LAB_DATA.precedents[c.clause_id].distribution.held_firm_pct)}}% Firm / ${{(LAB_DATA.precedents[c.clause_id].distribution.compromise_tier_1_pct)}}% Comp</span>
        ${{!c.accepted
          ? `<button onclick="event.stopPropagation();acceptClauseChange('${{c.clause_id}}')" class="px-2 py-1 rounded bg-emerald-600 text-white text-xs font-bold cursor-pointer">✓ Approve →</button>`
          : `<span class="text-xs font-extrabold text-emerald-700">✓ In Working .docx</span>`
        }}
      </div>
    </div>
  `;

  return `
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
      <!-- 4 Kanban Columns (8 Cols) -->
      <div class="lg:col-span-8 grid grid-cols-1 sm:grid-cols-4 gap-3">
        <div class="bg-slate-100 p-3 rounded-xl space-y-2">
          <div class="text-xs font-extrabold uppercase text-slate-600">1. Auto-Cleared (${{untouched.length}})</div>
          ${{untouched.map(u => `<div class="p-2.5 rounded-lg bg-white border border-slate-200 text-xs"><strong>${{escapeHtml(u.clause_ref)}}</strong> — ${{escapeHtml(u.clause_title)}} <span class="text-emerald-600 font-bold">✓</span></div>`).join('')}}
        </div>
        <div class="bg-blue-50/60 p-3 rounded-xl space-y-2.5">
          <div class="text-xs font-extrabold uppercase text-blue-900">2. Routed in Outlook (${{routed.length}})</div>
          ${{routed.map(renderCard).join('') || '<div class="text-xs text-slate-400 p-2">All routed SMEs resolved!</div>'}}
        </div>
        <div class="bg-amber-50/70 p-3 rounded-xl space-y-2.5">
          <div class="text-xs font-extrabold uppercase text-amber-900">3. Cross-Clause Conflict (${{conflicts.length}})</div>
          ${{conflicts.map(renderCard).join('') || '<div class="text-xs text-emerald-700 font-bold p-2">✓ SP3-04 Conflict Harmonized!</div>'}}
        </div>
        <div class="bg-emerald-50/70 p-3 rounded-xl space-y-2.5">
          <div class="text-xs font-extrabold uppercase text-emerald-900">4. Approved in .docx (${{approved.length}}/4)</div>
          ${{approved.map(renderCard).join('') || '<div class="text-xs text-slate-400 p-2">Click ✓ Approve on cards to move here.</div>'}}
        </div>
      </div>

      <!-- Right 4 Cols: Live Microsoft Outlook Comms & Inline Diff Drawer -->
      <div class="lg:col-span-4 bg-white border border-slate-200 rounded-2xl p-4 shadow-sm space-y-3">
        <div class="flex items-center justify-between border-b border-slate-200 pb-2.5">
          <span class="px-2.5 py-1 rounded bg-[#0078d4] text-white text-xs font-extrabold">📬 Microsoft Outlook (<code>clm-comms</code>)</span>
          <span class="text-xs font-mono text-slate-500">${{escapeHtml(activeC.clause_ref)}}</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs space-y-1">
          <div><strong>From:</strong> ${{escapeHtml(activeC.reviewer_name)}} &lt;${{escapeHtml(activeC.reviewer_name.split(' ')[0])}}@36zrbd.onmicrosoft.com&gt;</div>
          <div><strong>To:</strong> Rahul Kasanagottu &lt;m365-admin@rahulsankrut.demo.altostrat.com&gt;</div>
          <div><strong>Subject:</strong> [SME REVIEW UPDATE: ${{escapeHtml(activeC.sme_team)}}] Deal BA-2026-AV-8921 — ${{escapeHtml(activeC.clause_ref)}}</div>
        </div>
        <div class="p-3 rounded-xl border border-slate-200 text-xs leading-relaxed">
          ${{activeC.show_clean ? escapeHtml(activeC.counter_text) : computeWordDiffHtml(activeC.vendor_redline_text, activeC.counter_text, false)}}
        </div>
        <div class="space-y-1">
          <label class="text-xs font-bold text-slate-700">💬 Human Reviewer Comment (w:author=${{escapeHtml(activeC.reviewer_name)}}):</label>
          <textarea oninput="updateClauseComment('${{activeC.clause_id}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 text-xs">${{escapeHtml(activeC.user_comment)}}</textarea>
        </div>
        <button onclick="acceptClauseChange('${{activeC.clause_id}}')" class="w-full py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs cursor-pointer">
          ✓ Sync SME Approval &amp; Comment into Working_Review.docx
        </button>
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 8: CROSS-CLAUSE DEPENDENCY & REGULATORY LOCKOUT SVG GRAPH
// ============================================================================
function renderV8() {{
  const cid = window.CLMLabState.activeClauseId;
  const c = window.CLMLabState.clauses[cid];
  const sp3Accepted = window.CLMLabState.clauses['SP3-04'].accepted;

  return `
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
      <!-- Left 7 Cols: Interactive SVG Ontology & Conflict Graph -->
      <div class="lg:col-span-7 bg-slate-950 text-white rounded-2xl p-5 border border-slate-800 shadow-xl space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-sm font-extrabold text-white m-0">🕸️ Cross-Clause Dependency &amp; Regulatory Lockout Graph</h2>
            <p class="text-xs text-slate-400 m-0">Click any clause node in the SVG graph to inspect its regulatory lockouts or cross-clause FFP ceiling conflicts.</p>
          </div>
          <span class="px-2.5 py-1 rounded text-xs font-bold ${{sp3Accepted ? 'bg-emerald-500/20 text-emerald-300' : 'bg-rose-500/20 text-rose-300'}}">
            ${{sp3Accepted ? '✓ CONFLICT-SP3-04-GP1-03 HARMONIZED' : '⚡ CONFLICT-SP3-04-GP1-03 ACTIVE'}}
          </span>
        </div>

        <svg viewBox="0 0 760 420" class="w-full h-auto bg-slate-900 rounded-xl border border-slate-800">
          <!-- Edges -->
          <line x1="380" y1="210" x2="150" y2="90" stroke="#3b82f6" stroke-width="2.5" />
          <line x1="380" y1="210" x2="610" y2="90" stroke="#a855f7" stroke-width="2.5" />
          <line x1="380" y1="210" x2="150" y2="330" stroke="${{sp3Accepted ? '#10b981' : '#f59e0b'}}" stroke-width="3" />
          <line x1="380" y1="210" x2="610" y2="330" stroke="#ef4444" stroke-width="2.5" />
          <!-- Cross-Clause Conflict Edge between SP3-04 (150,330) and GP1-03 FFP Ceiling (380,70) -->
          <line x1="150" y1="330" x2="380" y2="75" stroke="${{sp3Accepted ? '#10b981' : '#ef4444'}}" stroke-width="3.5" stroke-dasharray="${{sp3Accepted ? '0' : '8,5'}}" />

          <!-- GP1-03 $45M FFP Lock Node -->
          <g transform="translate(285,35)">
            <rect width="190" height="52" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2" />
            <text x="95" y="22" text-anchor="middle" fill="#6ee7b7" font-size="11" font-weight="bold">GP1 §3.1 — $45M FFP Lock</text>
            <text x="95" y="39" text-anchor="middle" fill="#cbd5e1" font-size="10">Zero Uncapped Surcharges</text>
          </g>

          <!-- Center Hub: Deal BA-2026-AV-8921 -->
          <g transform="translate(290,178)">
            <rect width="180" height="64" rx="14" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" />
            <text x="90" y="26" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Deal BA-2026-AV-8921</text>
            <text x="90" y="45" text-anchor="middle" fill="#38bdf8" font-size="10.5">64 BigQuery Precedents</text>
          </g>

          <!-- Node 1: GP1-12 (Engineering / FAA) -->
          <g transform="translate(45,55)" onclick="selectClause('GP1-12')" style="cursor:pointer;">
            <rect width="210" height="72" rx="12" fill="${{cid==='GP1-12' ? '#1e3a8a' : '#111827'}}" stroke="${{window.CLMLabState.clauses['GP1-12'].accepted ? '#10b981' : '#ef4444'}}" stroke-width="2.5" />
            <text x="105" y="24" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">GP1 §12.2 Warranty &amp; FAA</text>
            <text x="105" y="43" text-anchor="middle" fill="#fca5a5" font-size="10">🔒 FAA 14 CFR Part 21.140</text>
            <text x="105" y="59" text-anchor="middle" fill="#6ee7b7" font-size="10">88% Held Firm (14/16 Deals)</text>
          </g>

          <!-- Node 2: GP1-19 (Legal / IP) -->
          <g transform="translate(505,55)" onclick="selectClause('GP1-19')" style="cursor:pointer;">
            <rect width="210" height="72" rx="12" fill="${{cid==='GP1-19' ? '#1e3a8a' : '#111827'}}" stroke="${{window.CLMLabState.clauses['GP1-19'].accepted ? '#10b981' : '#f59e0b'}}" stroke-width="2.5" />
            <text x="105" y="24" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">GP1 §19 &amp; §24 Liability</text>
            <text x="105" y="43" text-anchor="middle" fill="#fde68a" font-size="10">⚖️ $90M (2.0x PO) Super-Cap</text>
            <text x="105" y="59" text-anchor="middle" fill="#93c5fd" font-size="10">69% Compromise (11/16 Deals)</text>
          </g>

          <!-- Node 3: SP3-04 (Tax / Tariffs) -->
          <g transform="translate(45,295)" onclick="selectClause('SP3-04')" style="cursor:pointer;">
            <rect width="210" height="72" rx="12" fill="${{cid==='SP3-04' ? '#1e3a8a' : '#111827'}}" stroke="${{sp3Accepted ? '#10b981' : '#f59e0b'}}" stroke-width="2.5" />
            <text x="105" y="24" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">SP3 §4.1 Tariffs &amp; Duties</text>
            <text x="105" y="43" text-anchor="middle" fill="${{sp3Accepted ? '#6ee7b7' : '#fda4af'}}" font-size="10">${{sp3Accepted ? '✓ Capped at +2.0% ($900K)' : '⚡ Clashes w/ GP1 §3.1 FFP'}}</text>
            <text x="105" y="59" text-anchor="middle" fill="#93c5fd" font-size="10">63% Shared Cap (10/16 Deals)</text>
          </g>

          <!-- Node 4: SP5-03 (Cyber / DFARS) -->
          <g transform="translate(505,295)" onclick="selectClause('SP5-03')" style="cursor:pointer;">
            <rect width="210" height="72" rx="12" fill="${{cid==='SP5-03' ? '#1e3a8a' : '#111827'}}" stroke="${{window.CLMLabState.clauses['SP5-03'].accepted ? '#10b981' : '#ef4444'}}" stroke-width="2.5" />
            <text x="105" y="24" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">SP5 §3.2 Cyber Reporting</text>
            <text x="105" y="43" text-anchor="middle" fill="#fca5a5" font-size="10">🔒 DoD DFARS 72-Hr Mandate</text>
            <text x="105" y="59" text-anchor="middle" fill="#6ee7b7" font-size="10">94% Held Firm (15/16 Deals)</text>
          </g>
        </svg>
      </div>

      <!-- Right 5 Cols: Active Node Harmonization & Diff Surgery Inspector -->
      <div class="lg:col-span-5 bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3.5">
        <div class="flex items-center justify-between">
          <span class="px-2.5 py-1 rounded bg-slate-900 text-white text-xs font-extrabold">NODE INSPECTOR • ${{escapeHtml(c.clause_ref)}}</span>
          <button onclick="acceptClauseChange('${{cid}}')" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-extrabold cursor-pointer">
            ⚡ Harmonize &amp; Accept in Working .docx
          </button>
        </div>
        <div class="p-3.5 rounded-xl border border-slate-200 text-sm leading-relaxed">
          ${{c.show_clean ? escapeHtml(c.counter_text) : computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)}}
        </div>
        <div class="space-y-1">
          <label class="text-xs font-bold text-slate-700">💬 Reviewer Comment (w:author=${{escapeHtml(c.reviewer_name)}}):</label>
          <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 text-xs">${{escapeHtml(c.user_comment)}}</textarea>
        </div>
        ${{renderPrecedentBlockHtml(cid, false)}}
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 9: AUTHENTIC MS WORD 365 RIBBON & RIGHT-MARGIN BALLOON SIMULATOR
// ============================================================================
function renderV9() {{
  const mode = window.CLMLabState.wordMarkupMode;
  const redlinedIds = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];

  const clausesHtml = redlinedIds.map((cid, idx) => {{
    const c = window.CLMLabState.clauses[cid];
    let textBlock = '';
    if (mode === 'clean' || c.show_clean) {{
      textBlock = `<p class="text-sm leading-relaxed text-slate-900 m-0" style="font-family:var(--font-serif);">${{escapeHtml(c.counter_text)}}</p>`;
    }} else if (mode === 'simple') {{
      textBlock = `<div class="pl-3 border-l-4 border-red-600 text-sm leading-relaxed text-slate-900" style="font-family:var(--font-serif);">${{escapeHtml(c.counter_text)}}</div>`;
    }} else {{
      textBlock = `<div class="text-sm leading-relaxed text-slate-900" style="font-family:var(--font-serif);">${{computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)}}</div>`;
    }}

    return `
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 py-4 border-b border-slate-200 items-start">
        <!-- 8.5x11 Page Prose Column (8 Cols) -->
        <div class="lg:col-span-8 pr-4 space-y-2">
          <div class="flex items-center justify-between">
            <h3 class="text-sm font-bold text-slate-900 m-0" style="font-family:var(--font-serif);">${{escapeHtml(c.clause_ref)}} — ${{escapeHtml(c.clause_title)}}</h3>
            <div class="flex gap-1.5">
              <button onclick="acceptClauseChange('${{cid}}')" class="px-2.5 py-0.5 rounded bg-[#185abd] text-white text-xs font-bold cursor-pointer">
                ${{c.accepted ? '✓ Accepted' : '✓ Accept Change'}}
              </button>
              <button onclick="toggleCleanView('${{cid}}')" class="px-2 py-0.5 rounded border border-slate-300 text-xs cursor-pointer">
                ${{c.show_clean ? 'Show Markup' : 'Clean'}}
              </button>
            </div>
          </div>
          ${{textBlock}}
        </div>

        <!-- Right-Margin Word Comment Balloon Gutter (4 Cols) -->
        <div class="lg:col-span-4 pl-3 border-l-2 border-dashed border-red-300 space-y-2">
          <div class="p-3 rounded-xl bg-amber-50/70 border border-amber-300 shadow-xs space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-extrabold text-slate-900">💬 ${{escapeHtml(c.reviewer_name)}}</span>
              <span class="text-xs text-slate-500 font-mono">w:comment #${{idx + 1}}</span>
            </div>
            <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-1.5 rounded bg-white border border-amber-200 text-xs text-slate-800">${{escapeHtml(c.user_comment)}}</textarea>
          </div>
        </div>
      </div>
    `;
  }}).join('');

  return `
    <div class="rounded-2xl overflow-hidden border border-slate-300 shadow-xl bg-[#e5e7eb]">
      <!-- MS Word Royal Blue Title Bar -->
      <div class="bg-[#185abd] text-white px-4 py-2 flex items-center justify-between text-xs">
        <div class="flex items-center gap-3">
          <span class="font-extrabold tracking-wide">W &nbsp; BA-2026-AV-8921_Working_Review.docx — Microsoft Word 365 Simulator</span>
          <span class="px-2 py-0.5 rounded bg-white/20 text-white font-semibold">Saved to SharePoint</span>
        </div>
        <a href="http://127.0.0.1:58921/api/download/working-docx" target="_blank" class="px-2.5 py-1 rounded bg-white text-[#185abd] font-extrabold no-underline">
          ⬇️ Open in Real MS Word (.docx)
        </a>
      </div>

      <!-- MS Word Review Ribbon -->
      <div class="bg-[#f3f2f1] border-b border-slate-300 px-4 py-2 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex items-center gap-2">
          <span class="font-bold text-slate-700">Tracking Mode:</span>
          <button onclick="window.CLMLabState.wordMarkupMode='all';renderAll();" class="px-2.5 py-1 rounded ${{mode==='all' ? 'bg-[#185abd] text-white font-bold' : 'bg-white border border-slate-300'}} cursor-pointer">All Markup</button>
          <button onclick="window.CLMLabState.wordMarkupMode='simple';renderAll();" class="px-2.5 py-1 rounded ${{mode==='simple' ? 'bg-[#185abd] text-white font-bold' : 'bg-white border border-slate-300'}} cursor-pointer">Simple Markup</button>
          <button onclick="window.CLMLabState.wordMarkupMode='clean';renderAll();" class="px-2.5 py-1 rounded ${{mode==='clean' ? 'bg-[#185abd] text-white font-bold' : 'bg-white border border-slate-300'}} cursor-pointer">No Markup (Clean)</button>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="setDemoPreset('consolidated')" class="px-3 py-1 rounded bg-emerald-600 text-white font-bold cursor-pointer">✓ Accept All 4 Changes in Document</button>
        </div>
      </div>

      <!-- Centered 8.5" x 11" Paper Sheet with Right Margin Gutter -->
      <div class="p-6">
        <div class="max-w-6xl mx-auto bg-white rounded-sm shadow-xl p-8 space-y-2">
          <div class="border-b-2 border-slate-900 pb-3 mb-2">
            <h2 class="text-lg font-bold text-slate-900 m-0" style="font-family:var(--font-serif);">
              CYMBAL AEROSPACE CORPORATION — WORKING REVIEW CONTRACT (GP1 / SP3 / SP5)
            </h2>
            <p class="text-xs text-slate-600 m-0">Deal ID: BA-2026-AV-8921 • Supplier: Apex AeroSystems Inc. ($45,000,000 Firm-Fixed-Price) • Human Comments (w:author) Enabled</p>
          </div>
          ${{clausesHtml}}
        </div>
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 10: GITHUB PULL REQUEST / CODE REVIEW DIFF (PR #8921)
// ============================================================================
function renderV10() {{
  const cid = window.CLMLabState.activeClauseId;
  const c = window.CLMLabState.clauses[cid];

  const fileTreeHtml = Object.values(window.CLMLabState.clauses).map(item => `
    <div onclick="if('${{item.has_redline}}'==='true') selectClause('${{item.clause_id}}')" class="px-2.5 py-1.5 rounded-md text-xs font-mono flex items-center justify-between cursor-pointer ${{item.clause_id === cid ? 'bg-blue-50 text-blue-700 font-bold' : 'hover:bg-slate-100 text-slate-700'}}">
      <span>📄 clauses/${{escapeHtml(item.clause_id)}}.md</span>
      ${{!item.has_redline
        ? '<span class="text-slate-400">0</span>'
        : (item.accepted ? '<span class="text-emerald-600 font-bold">✓</span>' : '<span class="text-rose-600 font-bold">M</span>')
      }}
    </div>
  `).join('');

  return `
    <div class="bg-white border border-slate-300 rounded-2xl overflow-hidden shadow-xs">
      <!-- GitHub PR Top Header -->
      <div class="bg-[#f6f8fa] border-b border-slate-300 px-5 py-3.5 flex flex-wrap items-center justify-between gap-3">
        <div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full bg-emerald-600 text-white text-xs font-bold">🜉 Open PR #8921</span>
            <h2 class="text-base font-extrabold text-slate-900 m-0">Merge <code>apex-aero:vendor-redline-v1</code> into <code>cymbal:gp1-sp3-sp5-main</code></h2>
          </div>
          <div class="text-xs text-slate-500 mt-1 font-mono">4 of 12 clause files modified • Automated CI Checks: FAA 14 CFR Part 21.140, DFARS 252.204-7012, GP1 §3.1 FFP Ceiling</div>
        </div>
        <button onclick="acceptClauseChange('${{cid}}')" class="px-3.5 py-1.5 rounded-md bg-[#1f883d] hover:bg-[#1a7f37] text-white font-bold text-xs cursor-pointer">
          ± Commit Counter-Position Suggestion (${{cid}})
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12">
        <!-- Left File Tree (3 Cols) -->
        <div class="lg:col-span-3 border-r border-slate-200 p-3 space-y-1 bg-slate-50/50">
          <div class="text-xs font-extrabold uppercase text-slate-500 px-2 pb-1">Files Changed (12)</div>
          ${{fileTreeHtml}}
        </div>

        <!-- Right Diff Hunk & Suggested Change Box (9 Cols) -->
        <div class="lg:col-span-9 p-5 space-y-4">
          <div class="border border-slate-300 rounded-xl overflow-hidden">
            <div class="bg-[#f6f8fa] px-4 py-2 border-b border-slate-300 flex items-center justify-between font-mono text-xs">
              <span>clauses/${{cid}}_${{c.sme_team.toLowerCase()}}.md (${{escapeHtml(c.guardrail_code)}})</span>
              <span class="font-bold ${{c.accepted ? 'text-emerald-700' : 'text-rose-700'}}">${{c.accepted ? '✓ CI Check Passing (Counter Committed)' : '❌ CI Check Failing on Vendor Ask'}}</span>
            </div>
            <div class="divide-y divide-slate-200 font-mono text-xs">
              <div class="p-3 bg-[#ffebe9] text-rose-950 flex gap-3">
                <span class="text-rose-400 select-none">− 12</span>
                <div><strong>[Vendor Redline]:</strong> ${{escapeHtml(c.vendor_redline_text)}}</div>
              </div>
              <div class="p-3 bg-[#dafbe1] text-emerald-950 flex gap-3">
                <span class="text-emerald-600 select-none">+ 12</span>
                <div><strong>[Cymbal Counter]:</strong> ${{computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)}}</div>
              </div>
            </div>

            <!-- GitHub Suggested Change Commit Block -->
            <div class="p-4 bg-slate-50 border-t border-slate-200 space-y-2.5">
              <div class="flex items-center justify-between">
                <span class="text-xs font-extrabold text-slate-800">± Suggested Counter-Position Change (Editable before Commit)</span>
                <button onclick="acceptClauseChange('${{cid}}')" class="px-3 py-1 rounded bg-[#1f883d] text-white text-xs font-bold cursor-pointer">
                  Commit suggestion to Working_Review.docx
                </button>
              </div>
              <textarea oninput="updateClauseCounterText('${{cid}}', this.value)" class="auto-grow w-full p-2.5 rounded border border-slate-300 bg-white text-xs font-mono">${{escapeHtml(c.counter_text)}}</textarea>
              <div class="flex items-center gap-2 pt-1">
                <span class="text-xs font-bold">PR Review Comment Author (w:author):</span>
                <input type="text" value="${{escapeHtml(c.reviewer_name)}}" oninput="updateClauseReviewer('${{cid}}', this.value)" class="px-2 py-0.5 rounded border border-slate-300 bg-white text-xs font-bold" />
              </div>
              <textarea oninput="updateClauseComment('${{cid}}', this.value)" class="auto-grow w-full p-2 rounded border border-slate-300 bg-white text-xs">${{escapeHtml(c.user_comment)}}</textarea>
            </div>
          </div>

          ${{renderPrecedentBlockHtml(cid, false)}}
        </div>
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 11: EXECUTIVE BENTO DEAL ROOM & APPROVAL COCKPIT
// ============================================================================
function renderV11() {{
  const redlinedIds = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];
  const cardsHtml = redlinedIds.map(cid => {{
    const c = window.CLMLabState.clauses[cid];
    const dist = LAB_DATA.precedents[cid].distribution || {{}}; const st = {{ held_firm_pct: dist.held_firm_pct ?? 88, compromise_pct: dist.compromise_tier_1_pct ?? 12 }};
    return `
      <div class="p-4 rounded-2xl bg-white border-2 ${{c.accepted ? 'border-emerald-500' : 'border-slate-200'}} shadow-xs flex flex-col justify-between space-y-3">
        <div class="space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded bg-slate-900 text-white text-xs font-extrabold">${{escapeHtml(c.clause_ref)}}</span>
            <span class="text-xs font-bold ${{c.accepted ? 'text-emerald-700' : 'text-amber-700'}}">${{c.accepted ? '✓ Signed Off' : '⏳ Pending Gate'}}</span>
          </div>
          <h3 class="text-sm font-extrabold text-slate-900 m-0">${{escapeHtml(c.clause_title)}}</h3>
          <div class="text-xs text-slate-500">👤 Owner: <strong>${{escapeHtml(c.reviewer_name)}}</strong> • Precedent: <strong>${{st.held_firm_pct >= 50 ? st.held_firm_pct + '% Firm' : st.compromise_pct + '% Comp'}}</strong></div>
          <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs leading-relaxed">
            ${{c.show_clean ? escapeHtml(c.counter_text) : computeWordDiffHtml(c.vendor_redline_text, c.counter_text, false)}}
          </div>
        </div>
        <div class="space-y-2 pt-2 border-t border-slate-100">
          <input type="text" value="${{escapeHtml(c.user_comment)}}" oninput="updateClauseComment('${{cid}}', this.value)" class="w-full px-2.5 py-1 rounded border border-slate-200 text-xs" placeholder="Executive sign-off comment..." />
          <div class="flex gap-1.5">
            <button onclick="acceptClauseChange('${{cid}}')" class="flex-1 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs cursor-pointer">
              ✓ Approve Position
            </button>
            <button onclick="toggleCleanView('${{cid}}')" class="px-2.5 py-1.5 rounded-lg border border-slate-300 text-xs font-bold cursor-pointer">
              ${{c.show_clean ? 'Diff' : 'Clean'}}
            </button>
          </div>
        </div>
      </div>
    `;
  }}).join('');

  return `
    <div class="space-y-5">
      <!-- Top Bento Row: Financial Waterfall + Precedent Confidence + Batch Sign-Off -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <div class="lg:col-span-5 p-5 rounded-2xl bg-slate-900 text-white space-y-3">
          <div class="text-xs font-extrabold uppercase tracking-wider text-emerald-400">💰 Dollarized Financial Exposure Waterfall</div>
          <div class="grid grid-cols-3 gap-2.5 text-center">
            <div class="p-3 rounded-xl bg-slate-800">
              <div class="text-xs text-slate-400">Base FFP PO</div>
              <div class="text-lg font-extrabold tabular-nums text-white">$45.0M</div>
            </div>
            <div class="p-3 rounded-xl bg-rose-950/70 border border-rose-500/40">
              <div class="text-xs text-rose-300">Vendor Ask Risk</div>
              <div class="text-lg font-extrabold tabular-nums text-rose-400">+$18.5M</div>
            </div>
            <div class="p-3 rounded-xl bg-emerald-950/70 border border-emerald-500/40">
              <div class="text-xs text-emerald-300">Protected Counter</div>
              <div class="text-lg font-extrabold tabular-nums text-emerald-400">+$0.9M Cap</div>
            </div>
          </div>
          <p class="text-xs text-slate-300 m-0">
            Caps Section 232/301 tariff exposure at <strong>+2.0% ($900K)</strong> of GP1 §3.1 FFP and enforces a <strong>$90M (2.0x PO) Super-Cap</strong> with uncapped AD recall &amp; IP indemnity.
          </p>
        </div>

        <div class="lg:col-span-4 p-5 rounded-2xl bg-white border border-slate-200 space-y-3">
          <div class="text-xs font-extrabold uppercase tracking-wider text-slate-600">📊 BigQuery 64-Deal Precedent Confidence</div>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200"><strong>GP1 §12.2:</strong> 88% Held Firm (14/16)</div>
            <div class="p-2.5 rounded-xl bg-blue-50 border border-blue-200"><strong>GP1 §19:</strong> 69% 2x Super-Cap (11/16)</div>
            <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200"><strong>SP3 §4.1:</strong> 63% Shared Cap (10/16)</div>
            <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200"><strong>SP5 §3.2:</strong> 94% Held Firm (15/16)</div>
          </div>
        </div>

        <div class="lg:col-span-3 p-5 rounded-2xl bg-gradient-to-br from-emerald-600 to-teal-700 text-white flex flex-col justify-between">
          <div>
            <div class="text-xs font-extrabold uppercase tracking-wider text-emerald-100">⚡ Executive 4:00 PM Gate</div>
            <h3 class="text-base font-extrabold mt-1">1-Click Batch Consolidation</h3>
            <p class="text-xs text-emerald-100">Approve all 4 recommended counter-positions and write human comments to <code>Working_Review.docx</code>.</p>
          </div>
          <button onclick="setDemoPreset('consolidated')" class="w-full py-2.5 rounded-xl bg-white text-emerald-950 font-extrabold text-xs cursor-pointer shadow-md">
            ✓ Approve All 4 &amp; Update Working .docx
          </button>
        </div>
      </div>

      <!-- Second Bento Row: 4 Equal Sign-Off Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        ${{cardsHtml}}
      </div>
    </div>
  `;
}}

// ============================================================================
// VARIATION 12: HARVEY / CLAUDE ARTIFACTS AI CO-PILOT + LIVE CANVAS SPLIT
// ============================================================================
function renderV12() {{
  const cid = window.CLMLabState.activeClauseId;
  const c = window.CLMLabState.clauses[cid];

  const msgsHtml = window.CLMLabState.copilotMessages.map(m => `
    <div class="p-3 rounded-xl text-xs leading-relaxed ${{m.role==='user' ? 'bg-slate-900 text-white ml-6' : 'bg-indigo-50 border border-indigo-200 text-slate-800 mr-4'}}">
      <div class="font-extrabold text-xs mb-1">${{m.role==='user' ? '👤 You (' + escapeHtml(window.CLMLabState.activePersona) + ')' : '✦ Spark CLM Co-Pilot'}}</div>
      <div>${{escapeHtml(m.text)}}</div>
    </div>
  `).join('');

  return `
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
      <!-- Left 4 Cols: Conversational Prompt Studio -->
      <div class="lg:col-span-4 bg-white border border-slate-200 rounded-2xl p-4 shadow-sm flex flex-col justify-between space-y-3">
        <div class="space-y-3">
          <div class="border-b border-slate-200 pb-2.5 flex items-center justify-between">
            <span class="font-extrabold text-xs text-indigo-900 uppercase">✦ Spark CLM Co-Pilot Prompt Studio</span>
            <span class="text-xs font-mono text-slate-500">Active: ${{cid}}</span>
          </div>
          <div class="space-y-2 max-h-64 overflow-y-auto pr-1">
            ${{msgsHtml}}
          </div>
          <div class="space-y-1.5 pt-2 border-t border-slate-100">
            <div class="text-xs font-bold text-slate-600">1-Click Prompt Chips (Updates Right Canvas Live):</div>
            <div class="flex flex-wrap gap-1.5">
              <button onclick="runCopilotPrompt('Apply 50/50 tariff split capped at 2.0% ($900,000) of GP1 §3.1 FFP', 'SP3-04', 'compromise_tier_1')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 text-xs font-semibold text-left cursor-pointer">
                "Cap SP3 §4.1 tariffs at 2.0% ($900K) FFP"
              </button>
              <button onclick="runCopilotPrompt('Apply 2.0x PO ($90,000,000) Super-Cap with uncapped AD recall & IP', 'GP1-19', 'compromise_tier_1')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 text-xs font-semibold text-left cursor-pointer">
                "Apply $90M (2x PO) Super-Cap on GP1 §19"
              </button>
              <button onclick="runCopilotPrompt('Hold firm on unannounced FAA Part 21.140 source inspections & 36-mo warranty', 'GP1-12', 'hold_firm')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 text-xs font-semibold text-left cursor-pointer">
                "Hold firm on FAA Part 21.140 (GP1 §12.2)"
              </button>
              <button onclick="runCopilotPrompt('Hold firm on mandatory 72-hour DFARS 252.204-7012 cyber reporting', 'SP5-03', 'hold_firm')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-indigo-50 text-xs font-semibold text-left cursor-pointer">
                "Enforce 72-Hr DFARS reporting (SP5 §3.2)"
              </button>
            </div>
          </div>
        </div>

        <div class="flex gap-2 pt-2 border-t border-slate-200">
          <input id="copilotCustomInput" type="text" placeholder="Instruct Co-Pilot to rewrite ${{cid}}..." class="flex-1 px-3 py-1.5 rounded-lg border border-slate-300 text-xs" onkeydown="if(event.key==='Enter') submitCustomCopilotPrompt()" />
          <button onclick="submitCustomCopilotPrompt()" class="px-3 py-1.5 rounded-lg bg-indigo-600 text-white font-bold text-xs cursor-pointer">Send</button>
        </div>
      </div>

      <!-- Right 8 Cols: Live Updating Contract Artifact Canvas -->
      <div class="lg:col-span-8">
        ${{renderV1()}}
      </div>
    </div>
  `;
}}

function runCopilotPrompt(promptText, targetCid, optionKey) {{
  window.CLMLabState.activeClauseId = targetCid;
  window.CLMLabState.copilotMessages.push({{ role: 'user', text: promptText }});
  acceptClauseChange(targetCid, optionKey);
  window.CLMLabState.copilotMessages.push({{
    role: 'assistant',
    text: `Updated ${{targetCid}} on the live Contract Canvas and wrote accepted change + comment (w:author="${{window.CLMLabState.clauses[targetCid].reviewer_name}}") to BA-2026-AV-8921_Working_Review.docx.`
  }});
  renderAll();
}}

function submitCustomCopilotPrompt() {{
  const input = document.getElementById('copilotCustomInput');
  if (!input || !input.value.trim()) return;
  const txt = input.value.trim();
  const cid = window.CLMLabState.activeClauseId;
  window.CLMLabState.copilotMessages.push({{ role: 'user', text: txt }});
  window.CLMLabState.clauses[cid].user_comment = txt;
  window.CLMLabState.copilotMessages.push({{
    role: 'assistant',
    text: `Applied your instruction and updated the human reviewer comment (w:author="${{window.CLMLabState.clauses[cid].reviewer_name}}") on ${{cid}}.`
  }});
  input.value = '';
  renderAll();
}}

// ============================================================================
// MASTER RENDER ORCHESTRATOR & UX EVALUATOR HARNESS
// ============================================================================
function renderHeaderTabsAndPills() {{
  const activeVarId = window.CLMLabState.activeVariation;
  const tabsBar = document.getElementById('variationTabsBar');
  tabsBar.innerHTML = VARIATIONS_META.map(v => {{
    const ev = uxEvalNotes.variations[v.id] || {{ rating: 0 }};
    const starBadge = ev.rating > 0 ? `<span class="text-amber-300">★${{ev.rating}}</span>` : '';
    return `
      <button role="tab" aria-selected="${{v.id === activeVarId}}" onclick="selectVariation('${{v.id}}')" class="var-tab ${{v.id === activeVarId ? 'active' : ''}}">
        <span>${{escapeHtml(v.short)}}</span>
        ${{starBadge}}
      </button>
    `;
  }}).join('');

  const meta = VARIATIONS_META.find(v => v.id === activeVarId) || VARIATIONS_META[0];
  document.getElementById('varParadigmBadge').textContent = meta.paradigm;
  document.getElementById('varTitleHeading').textContent = meta.title;
  document.getElementById('varSubtitleText').textContent = meta.subtitle;

  const redlinedIds = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];
  const acceptedCount = redlinedIds.filter(id => window.CLMLabState.clauses[id].accepted).length;
  const headerBadge = document.getElementById('headerStatusBadge');
  headerBadge.textContent = `${{acceptedCount}} / 4 Clauses Accepted in Working .docx`;
  headerBadge.className = acceptedCount === 4
    ? 'px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40'
    : 'px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/20 text-amber-300 border border-amber-500/40';

  const pillsContainer = document.getElementById('globalClausePills');
  pillsContainer.innerHTML = redlinedIds.map(id => {{
    const c = window.CLMLabState.clauses[id];
    const active = id === window.CLMLabState.activeClauseId;
    return `
      <button onclick="selectClause('${{id}}')" class="px-3 py-1 rounded-lg text-xs font-bold border cursor-pointer transition ${{active ? 'bg-slate-900 text-white border-slate-900' : 'bg-slate-100 text-slate-700 border-slate-300 hover:bg-slate-200'}}">
        ${{escapeHtml(c.clause_ref)}} (${{escapeHtml(c.sme_team)}}) ${{c.accepted ? '✓' : '●'}}
      </button>
    `;
  }}).join('');
}}

function renderEvaluatorControls() {{
  const vId = window.CLMLabState.activeVariation;
  const ev = uxEvalNotes.variations[vId];
  document.getElementById('evalBarVarLabel').textContent = vId;
  document.getElementById('drawerVarName').textContent = vId;
  document.getElementById('drawerVarName2').textContent = vId;

  // Stars 1..5
  const starsHtml = [1, 2, 3, 4, 5].map(n => `
    <button onclick="setVariationRating(${{n}})" class="star-btn ${{ev.rating >= n ? 'lit' : ''}}" title="Rate ${{n}} of 5 stars">★</button>
  `).join('');
  document.getElementById('quickStarsBar').innerHTML = starsHtml;

  document.getElementById('quickVerdictSelect').value = ev.verdict || '';
  document.getElementById('quickNoteInput').value = ev.notes || '';
  document.getElementById('drawerNoteTextarea').value = ev.notes || '';

  // Keep component checkboxes
  document.getElementById('keepComponentsGrid').innerHTML = KEEP_COMPONENT_OPTIONS.map(comp => {{
    const checked = (ev.keep_components || []).includes(comp);
    return `
      <label class="flex items-center gap-2 p-1.5 rounded bg-slate-900 border border-slate-800 cursor-pointer">
        <input type="checkbox" ${{checked ? 'checked' : ''}} onchange="toggleKeepComponent(${{JSON.stringify(comp).replace(/"/g, '&quot;')}})" />
        <span>${{escapeHtml(comp)}}</span>
      </label>
    `;
  }}).join('');

  // Quick Pros/Cons tags
  document.getElementById('quickTagsGrid').innerHTML = QUICK_TAGS.map(tag => {{
    const active = (ev.tags || []).includes(tag);
    return `
      <button onclick="toggleQuickTag(${{JSON.stringify(tag).replace(/"/g, '&quot;')}})" class="px-2.5 py-1 rounded-full text-xs font-bold cursor-pointer border ${{active ? 'bg-blue-600 text-white border-blue-400' : 'bg-slate-900 text-slate-300 border-slate-700'}}">
        ${{escapeHtml(tag)}}
      </button>
    `;
  }}).join('');

  updateRatedCountBadge();
}}

function updateRatedCountBadge() {{
  const rated = Object.values(uxEvalNotes.variations).filter(
    v => v.rating > 0 || (v.notes && v.notes.trim()) || (v.keep_components && v.keep_components.length)
  ).length;
  const badge = document.getElementById('ratedCountBadge');
  if (badge) badge.textContent = `${{rated}}/12`;
}}

function setVariationRating(stars) {{
  const vId = window.CLMLabState.activeVariation;
  uxEvalNotes.variations[vId].rating = stars;
  persistEvalNotes();
  renderHeaderTabsAndPills();
  renderEvaluatorControls();
}}

function setVariationVerdict(verdict) {{
  const vId = window.CLMLabState.activeVariation;
  uxEvalNotes.variations[vId].verdict = verdict;
  persistEvalNotes();
}}

function updateVariationNote(text) {{
  const vId = window.CLMLabState.activeVariation;
  uxEvalNotes.variations[vId].notes = text;
  const qInput = document.getElementById('quickNoteInput');
  const dInput = document.getElementById('drawerNoteTextarea');
  if (qInput && qInput.value !== text) qInput.value = text;
  if (dInput && dInput.value !== text) dInput.value = text;
  persistEvalNotes();
}}

function toggleKeepComponent(comp) {{
  const vId = window.CLMLabState.activeVariation;
  const arr = uxEvalNotes.variations[vId].keep_components || [];
  const idx = arr.indexOf(comp);
  if (idx >= 0) arr.splice(idx, 1);
  else arr.push(comp);
  uxEvalNotes.variations[vId].keep_components = arr;
  persistEvalNotes();
  renderEvaluatorControls();
}}

function toggleQuickTag(tag) {{
  const vId = window.CLMLabState.activeVariation;
  const arr = uxEvalNotes.variations[vId].tags || [];
  const idx = arr.indexOf(tag);
  if (idx >= 0) arr.splice(idx, 1);
  else arr.push(tag);
  uxEvalNotes.variations[vId].tags = arr;
  persistEvalNotes();
  renderEvaluatorControls();
}}

function toggleEvalDrawer() {{
  const d = document.getElementById('evalExpandedDrawer');
  const icon = document.getElementById('evalToggleIcon');
  const isHidden = d.style.display === 'none';
  d.style.display = isHidden ? 'block' : 'none';
  icon.textContent = isHidden ? '▼' : '▲';
}}

function saveOverallSynthesis(val) {{
  uxEvalNotes.overall_synthesis = val;
  persistEvalNotes();
  refreshComparisonModalContent();
}}

function generateMarkdownReport() {{
  const lines = [
    '# Cymbal Aerospace CLM — User UX Evaluation & Feature Selection Notes',
    '',
    `**Overall Synthesis / Combination Plan:** ${{uxEvalNotes.overall_synthesis || '(Add overall synthesis notes above)'}}`,
    '',
    '## Rated & Reviewed Variations',
  ];
  VARIATIONS_META.forEach(m => {{
    const ev = uxEvalNotes.variations[m.id];
    if (ev.rating > 0 || ev.verdict || (ev.keep_components && ev.keep_components.length) || (ev.tags && ev.tags.length) || (ev.notes && ev.notes.trim())) {{
      lines.push(`### ${{m.id}} — ${{m.title}}`);
      lines.push(`- **Rating:** ${{ev.rating ? '★'.repeat(ev.rating) + ' (' + ev.rating + '/5)' : 'Unrated'}} | **Verdict:** ${{ev.verdict || 'Unspecified'}}`);
      if (ev.keep_components && ev.keep_components.length) {{
        lines.push(`- **Keep Components:** ${{ev.keep_components.join(', ')}}`);
      }}
      if (ev.tags && ev.tags.length) {{
        lines.push(`- **Tags:** ${{ev.tags.join(', ')}}`);
      }}
      if (ev.notes && ev.notes.trim()) {{
        lines.push(`- **Notes:** ${{ev.notes.trim()}}`);
      }}
      lines.push('');
    }}
  }});
  return lines.join('\\n');
}}

function refreshComparisonModalContent() {{
  document.getElementById('overallSynthesisInput').value = uxEvalNotes.overall_synthesis || '';
  const rows = VARIATIONS_META.map(m => {{
    const ev = uxEvalNotes.variations[m.id];
    return `
      <tr class="border-t border-slate-200 text-xs">
        <td class="py-2 px-3 font-extrabold text-slate-900">
          <button onclick="document.getElementById('comparisonModal').close();selectVariation('${{m.id}}')" class="text-blue-600 hover:underline font-extrabold cursor-pointer bg-transparent border-none p-0">${{m.id}}</button>
        </td>
        <td class="py-2 px-3 font-semibold">${{escapeHtml(m.short)}}</td>
        <td class="py-2 px-3 text-amber-500 font-bold">${{ev.rating ? '★'.repeat(ev.rating) : '—'}}</td>
        <td class="py-2 px-3 font-mono text-xs">${{escapeHtml(ev.verdict || '—')}}</td>
        <td class="py-2 px-3 text-xs text-emerald-700">${{escapeHtml((ev.keep_components || []).join(', ') || '—')}}</td>
        <td class="py-2 px-3 text-xs text-slate-700">${{escapeHtml(ev.notes || '—')}}</td>
      </tr>
    `;
  }}).join('');
  document.getElementById('comparisonTableContainer').innerHTML = `
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="bg-slate-100 text-xs font-extrabold text-slate-600 uppercase">
          <th class="py-2 px-3">ID</th>
          <th class="py-2 px-3">Variation</th>
          <th class="py-2 px-3">Rating</th>
          <th class="py-2 px-3">Verdict</th>
          <th class="py-2 px-3">Cherry-Picked Components</th>
          <th class="py-2 px-3">Your Notes</th>
        </tr>
      </thead>
      <tbody>${{rows}}</tbody>
    </table>
  `;
  document.getElementById('markdownPreviewBox').textContent = generateMarkdownReport();
}}

function openComparisonModal() {{
  refreshComparisonModalContent();
  document.getElementById('comparisonModal').showModal();
}}

function copyMarkdownSummary() {{
  const md = generateMarkdownReport();
  navigator.clipboard.writeText(md).then(() => {{
    alert('Copied Markdown UX Evaluation Summary to clipboard! Paste it directly in the chat when ready.');
  }});
}}

function downloadJsonNotes() {{
  const blob = new Blob([JSON.stringify(uxEvalNotes, null, 2)], {{ type: 'application/json' }});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'ux_evaluation_notes.json';
  a.click();
}}

function renderAll() {{
  renderHeaderTabsAndPills();
  renderEvaluatorControls();
  const stage = document.getElementById('variationStageContainer');
  const v = window.CLMLabState.activeVariation;
  if (v === 'V1') stage.innerHTML = renderV1();
  else if (v === 'V2') stage.innerHTML = renderV2();
  else if (v === 'V3') stage.innerHTML = renderV3();
  else if (v === 'V4') stage.innerHTML = renderV4();
  else if (v === 'V5') stage.innerHTML = renderV5();
  else if (v === 'V6') stage.innerHTML = renderV6();
  else if (v === 'V7') stage.innerHTML = renderV7();
  else if (v === 'V8') stage.innerHTML = renderV8();
  else if (v === 'V9') stage.innerHTML = renderV9();
  else if (v === 'V10') stage.innerHTML = renderV10();
  else if (v === 'V11') stage.innerHTML = renderV11();
  else if (v === 'V12') stage.innerHTML = renderV12();
}}

// Global Keyboard Shortcuts for V6 & Quick Variation Navigation
document.addEventListener('keydown', (e) => {{
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return;
  const redlined = ['GP1-12', 'GP1-19', 'SP3-04', 'SP5-03'];
  const idx = redlined.indexOf(window.CLMLabState.activeClauseId);
  if (e.key === 'j' || e.key === 'J') {{
    selectClause(redlined[(idx + 1) % redlined.length]);
  }} else if (e.key === 'k' || e.key === 'K') {{
    selectClause(redlined[(idx - 1 + redlined.length) % redlined.length]);
  }} else if (e.key === 'a' || e.key === 'A') {{
    acceptClauseChange(window.CLMLabState.activeClauseId);
  }}
}});

renderAll();
</script>
</body>
</html>
"""
    return html


def main() -> None:
    html_content = build_lab_html()
    targets = [
        ROOT / "cymbal_clm_ui_lab_12_variations.html",
        Path.home() / "ge_spark_workspace" / "cymbal_clm_ui_lab_12_variations.html",
    ]
    for t in targets:
        try:
            t.parent.mkdir(parents=True, exist_ok=True)
            t.write_text(html_content, encoding="utf-8")
            print(f"Wrote {t} ({len(html_content):,} bytes)")
        except Exception as exc:
            print(f"Skipped {t}: {exc}")


if __name__ == "__main__":
    main()
