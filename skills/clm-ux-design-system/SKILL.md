---
name: clm-ux-design-system
description: Reusable UI/UX Design System skill for Cymbal Aerospace CLM and Enterprise Legal/Financial Contract Review Workbenches (Deal BA-2026-AV-8921). Codifies multi-theme design tokens (Emerald Document Stage, Institutional Dark Terminal, Daylight Legal Paper), semantic Contract Redline Diffs (<del>, <ins>, clean accepted state), Floating Context Menus (Popover API + CSS Anchor Positioning), Human-Attributed Inline Word Comments (w:author), BigQuery Precedent Distribution Visualizations, and modern-web-guidance patterns (:has(), interpolate-size, @container, View Transitions, and WCAG 2.2 AA accessibility).
---

# Cymbal Aerospace CLM — Enterprise Legal & Financial UX Design System (`clm-ux-design-system`)

## 1. When to Activate
Activate this skill whenever designing, building, or refining HTML/CSS/JS interfaces for **Cymbal Aerospace CLM (`BA-2026-AV-8921`)**, Spark Canvas artifacts, or the **12-Variation CLM UI Mockup Lab (`cymbal_clm_ui_lab_12_variations.html`)**:
- Rendering **Contract Redline Diffs** (`GP1 §12.2`, `GP1 §19 & §24`, `SP3 §4.1`, `SP5 §3.2`) comparing Cymbal Proforma baseline, Vendor Redline markup, and Cymbal Counter-Position.
- Building **Floating Action Toolbars & Context Menus** (`✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, `💬 Comment`) tethered to redlined clauses.
- Designing **Inline Word-Style Margin Comments (`w:comment`)** strictly attributed to the human reviewer (`Rahul Kasanagottu`, `Pradeep Gupta`, `Megan Bowen`, `Lee Gu`, `Alex Wilber` — never system/bot comments).
- Visualizing **BigQuery Historical Precedent Distributions** (`N = 16` Tier-1 Avionics deals per clause; `64` total deals across `% Held Firm`, `% Tier-1 Compromise`, `% Accepted Vendor Ask`) and Cross-Clause Conflict graphs (`CONFLICT-SP3-04-GP1-03`).
- Implementing multi-theme / multi-density workbenches spanning **Word-Native Emerald Stage** (Spellbook/Ivo style), **Institutional Dark Terminal** (Cymbal Capital / Bloomberg style), and **Daylight Legal Paper** (Ironclad/Litera style).

---

## 2. Foundation & CSP-Safe Environment Setup

### 2.1 Antigravity & Spark Canvas HTML Boilerplate
Always include `<meta name="color-scheme" content="light dark">` in `<head>` to prevent Flash of Un-themed Content (FOUC) and load the allowlisted Antigravity Tailwind script when targeting Spark Canvas or standalone HTML workbenches:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <!-- MANDATORY (modern-web-guidance: dark-mode): Declare support for both light and dark themes -->
  <meta name="color-scheme" content="light dark" />
  <title>BA-2026-AV-8921 | Cymbal Aerospace CLM Workbench</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
```

### 2.2 Multi-Theme & Multi-Density Token Architecture (`design-token-reactivity`, `dark-mode`, `color`)
Borrowing from **J.P. Morgan Salt Design System** (touch/low/medium/high density scaling), **IBM Carbon** (AI explainability tokens), and **GitHub Primer** (diff polarity tokens), define semantic tokens on `:root` and scope theme/density overrides via `[data-theme]` and `@container style()`:

```css
:root {
  /* MANDATORY (modern-web-guidance: dark-mode & animate-to-intrinsic-sizes) */
  color-scheme: light dark;
  interpolate-size: allow-keywords;

  /* Typography */
  --font-sans: 'Inter', 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-serif: 'Newsreader', 'Source Serif 4', 'Georgia', serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', ui-monospace, monospace;

  /* Theme 1 (Default): Emerald Document Stage (Ivo / Spellbook Word-Native) */
  --stage-bg-light: #064e3b;       /* Deep Emerald backdrop */
  --stage-bg-dark: #022c22;
  --paper-surface-light: #ffffff;  /* Crisp Legal Paper sheet */
  --paper-surface-dark: #0f172a;
  --ink-primary-light: #0f172a;
  --ink-primary-dark: #f8fafc;
  --ink-muted-light: #475569;
  --ink-muted-dark: #94a3b8;
  --border-subtle-light: #e2e8f0;
  --border-subtle-dark: #1e293b;

  /* Reactive light-dark() tokens with media-query fallback */
  --stage-bg: var(--stage-bg-light);
  --paper-surface: var(--paper-surface-light);
  --ink-primary: var(--ink-primary-light);
  --ink-muted: var(--ink-muted-light);
  --border-subtle: var(--border-subtle-light);

  @media (prefers-color-scheme: dark) {
    --stage-bg: var(--stage-bg-dark);
    --paper-surface: var(--paper-surface-dark);
    --ink-primary: var(--ink-primary-dark);
    --ink-muted: var(--ink-muted-dark);
    --border-subtle: var(--border-subtle-dark);
  }

  @supports (color: light-dark(white, black)) {
    --stage-bg: light-dark(var(--stage-bg-light), var(--stage-bg-dark));
    --paper-surface: light-dark(var(--paper-surface-light), var(--paper-surface-dark));
    --ink-primary: light-dark(var(--ink-primary-light), var(--ink-primary-dark));
    --ink-muted: light-dark(var(--ink-muted-light), var(--ink-muted-dark));
    --border-subtle: light-dark(var(--border-subtle-light), var(--border-subtle-dark));
  }

  /* Redline Diff Polarity Tokens (WCAG 2.2 AA 4.5:1 Text Contrast Verified) */
  --diff-del-bg: light-dark(#fee2e2, rgba(239, 68, 68, 0.22));
  --diff-del-text: light-dark(#991b1b, #fca5a5);
  --diff-del-strike: light-dark(#dc2626, #f87171);

  --diff-ins-bg: light-dark(#ffedd5, rgba(249, 115, 22, 0.24));
  --diff-ins-text: light-dark(#9a3412, #fdba74);
  --diff-ins-border: light-dark(#ea580c, #fb923c);

  --diff-accepted-bg: light-dark(#dcfce7, rgba(16, 185, 129, 0.2));
  --diff-accepted-text: light-dark(#166534, #6ee7b7);
  --diff-accepted-border: light-dark(#16a34a, #34d399);

  /* Precedent Telemetry Tokens */
  --prec-hold-firm: #059669;       /* Emerald 600 — Held Firm (88% Eng, 94% Cyber) */
  --prec-compromise: #d97706;      /* Amber 600 — Tier-1 Compromise (69% Legal, 63% Tax) */
  --prec-vendor-ask: #dc2626;      /* Red 600 — Accepted Vendor Ask (0%–6%) */

  /* Density Tokens (Salt Design System pattern: compact | comfortable | spacious) */
  --density: comfortable;
  --clause-pad-compact: 0.625rem 0.875rem;
  --clause-pad-comfortable: 1.125rem 1.5rem;
  --clause-pad-spacious: 1.75rem 2.25rem;
}

/* Theme 2: Cymbal Institutional Dark Terminal (Bloomberg / Cymbal Capital Style) */
[data-theme="institutional-dark"] {
  color-scheme: dark;
  --stage-bg: #070b14;
  --paper-surface: #0d1322;
  --ink-primary: #f1f5f9;
  --ink-muted: #94a3b8;
  --border-subtle: #1e293b;
}

/* Theme 3: Daylight Legal Paper (Ironclad / Litera Clean Workspace) */
[data-theme="daylight-paper"] {
  color-scheme: light;
  --stage-bg: #f1f5f9;
  --paper-surface: #ffffff;
  --ink-primary: #0f172a;
  --ink-muted: #475569;
  --border-subtle: #cbd5e1;
}

/* Density Reactivity: Fallback [data-density] + Progressive Enhancement @container style() */
:where([data-density="compact"]) .clm-clause-card { padding: var(--clause-pad-compact); }
:where([data-density="comfortable"]) .clm-clause-card { padding: var(--clause-pad-comfortable); }
:where([data-density="spacious"]) .clm-clause-card { padding: var(--clause-pad-spacious); }

@container style(--density: compact) {
  .clm-clause-card { padding: var(--clause-pad-compact); }
}
@container style(--density: spacious) {
  .clm-clause-card { padding: var(--clause-pad-spacious); }
}
```

### 2.3 Typography & Readability Rules (`typography`, `generative_ui`)
1. **Minimum Font Size Floor**: Never use sub-12px micro-text (`text-[10px]`, `text-[11px]`, or `font-size < 0.75rem`). Keep `0.75rem` (`12px` / `text-xs`) as the strict floor for badges and metadata.
2. **Contract Prose Measure & Wrapping**:
   - Cap contract clause prose at `max-inline-size: 75ch` (`<= 80ch` per `typography` guide) with unitless `line-height: 1.65` and `text-wrap: pretty`.
   - Use `text-wrap: balance` on standalone headings (`<h1>`–`<h3>`, `<th scope="col">`), never on bordered/shaded boxes where trailing space looks unbalanced.
3. **Financial & Precedent Numerals**: Always apply `font-variant-numeric: tabular-nums` (`tabular-nums`) and `--font-mono` to dollar caps (`$45,000,000` FFP, `$90,000,000` 2.0x PO Super-Cap, `$900,000` +2.0% Tariff Cap), percentages (`88%`, `69%`, `63%`, `94%`), and clause citations (`GP1 §12.2`, `SP3 §4.1`).

---

## 3. Core CLM Component Patterns

### 3.1 Visual Hierarchy for Contract Redline Diffs (`color`, `highlight-text-ranges`, `accessibility`)
Contract reviewers must distinguish three states at a glance—**without relying on color alone** (WCAG 1.4.1 / `color` guide):

1. **Rejected Vendor Markup (`<del class="clm-diff-del">`)**:
   - **Visuals**: Orange-red tinted pill (`var(--diff-del-bg)`), dark crimson text (`var(--diff-del-text)`), `2px` solid strikethrough (`text-decoration: line-through solid var(--diff-del-strike) 2px`).
   - **Non-Color Signifier**: Prefix with a visually hidden label `<span class="visually-hidden">[Deleted vendor markup: </span>` (or visible `−` badge in high-contrast mode) and suffix `<span class="visually-hidden">]</span>`.
2. **Proposed Counter-Position Insertion (`<ins class="clm-diff-ins">`)**:
   - **Visuals**: Warm coral/amber highlight (`var(--diff-ins-bg)`), high-contrast text (`var(--diff-ins-text)`), bottom accent border (`border-block-end: 2px solid var(--diff-ins-border)`), and `text-decoration: none`.
   - **Non-Color Signifier**: Prefix with `✦` or `+` glyph (`aria-hidden="true"`) and `<span class="visually-hidden">[Proposed counter-position: </span>`.
3. **Clean Accepted State (`.clm-clause-card:has(.accept-toggle:checked)` or `[data-status="ACCEPTED"]`)**:
   - When the reviewer clicks **`✓ Accept changes`**, smoothly collapse `<del>` spans (`inline-size: 0; opacity: 0`) and transition `<ins>` into clean contract prose with an emerald verification badge (`✓ Accepted by [Human Name]`).
4. **Transient Clause Search / Cross-Reference Highlighting (`highlight-text-ranges`)**:
   - For transient search or cross-clause term highlighting (e.g., highlighting `"Firm-Fixed-Price"` across `SP3 §4.1` and `GP1 §3.1`), use the **CSS Custom Highlight API** (`CSS.highlights.set('clause-search', new Highlight(...ranges))` via `TreeWalker` on text nodes—never `innerHTML` string replacement—with a `<mark>` DOM fallback when `!CSS.highlights`).

```css
.clm-diff-del {
  background-color: var(--diff-del-bg);
  color: var(--diff-del-text);
  text-decoration: line-through solid var(--diff-del-strike) 2px;
  padding-inline: 0.25rem;
  border-radius: 0.25rem;
  transition: opacity 0.25s ease, inline-size 0.25s ease;
}

.clm-diff-ins {
  background-color: var(--diff-ins-bg);
  color: var(--diff-ins-text);
  text-decoration: none;
  border-block-end: 2px solid var(--diff-ins-border);
  padding-inline: 0.3rem;
  border-radius: 0.25rem;
  font-weight: 500;
  transition: background-color 0.25s ease, border-color 0.25s ease;
}

/* Forced Colors Mode Fallback (modern-web-guidance: color) */
@media (forced-colors: active) {
  .clm-diff-del {
    outline: 1px dashed GrayText;
  }
  .clm-diff-ins {
    outline: 2px solid Highlight;
  }
}
```

### 3.2 Parent Clause Card Reactivity with `:has()` (`child-state-based-styling`)
Use `:has()` scoped directly to `.clm-clause-card` (never `body:has(...)`) so each clause card updates its border, elevation, and status badge automatically based on its child controls (`:checked`, `:focus-within`, `:user-invalid`), paired with an `@supports not selector(:has(*))` fallback:

```css
.clm-clause-card {
  --card-border: var(--border-subtle);
  --card-ring: transparent;
  border: 1px solid var(--card-border);
  box-shadow: 0 0 0 2px var(--card-ring);
  border-radius: 0.75rem;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
}

/* Elevate card when reviewer is actively editing or commenting inside it */
.clm-clause-card:has(:focus-visible, textarea:focus) {
  --card-border: #10b981;
  --card-ring: rgba(16, 185, 129, 0.25);
}

/* Automatically style card when "Accept changes" radio/checkbox is checked */
.clm-clause-card:has(.status-accept:checked) {
  --card-border: var(--diff-accepted-border);
}

.clm-clause-card:has(.status-accept:checked) .clm-diff-del {
  display: none;
}

.clm-clause-card:has(.status-accept:checked) .clm-diff-ins {
  background-color: var(--diff-accepted-bg);
  color: var(--diff-accepted-text);
  border-block-end-color: var(--diff-accepted-border);
}

@supports not selector(:has(*)) {
  .clm-clause-card.is-accepted {
    --card-border: var(--diff-accepted-border);
  }
}
```

### 3.3 Floating Context Menus & Declarative Overlays (`viewport-aware-dropdowns`, `declarative-dialog-popover-control`, `animate-to-from-top-layer`)
Inspired by the Word-native floating action card (`media_1792469698101_00b1ca98.png`), each redlined clause exposes a 4-action floating toolbar (`✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, `💬 Comment`):

- **Button Group Semantics (`viewport-aware-dropdowns`)**: Model the floating action bar as a **button group revealed inside a native popover** (`popover="auto"`), **not** `role="menu"` / `role="menuitem"`, and do **not** add `aria-haspopup` to the trigger unless full ARIA menu arrow-key semantics are implemented.
- **Logical Anchor Positioning**: Use `position-area: block-end span-inline-end` (never mix physical and logical keywords) with `position-try-fallbacks: flip-block, flip-inline, flip-block flip-inline`.
- **Top-Layer Entry/Exit Animation (`animate-to-from-top-layer`)**: Transition `opacity, transform, display, overlay` with `transition-behavior: allow-discrete` placed **after** any shorthand, and define entry styles inside `@starting-style`.

```css
.clm-floating-toolbar[popover] {
  position-area: block-end span-inline-end;
  position-try-fallbacks: flip-block, flip-inline, flip-block flip-inline;
  inset: auto;
  margin-block-start: 0.5rem;
  opacity: 0;
  transform: translateY(4px) scale(0.98);
  transition-property: opacity, transform, display, overlay;
  transition-duration: 0.2s;
  transition-timing-function: ease-out;
  transition-behavior: allow-discrete;
}

.clm-floating-toolbar[popover]:is(:popover-open, .\:popover-open):where(:not([data-closing])) {
  opacity: 1;
  transform: translateY(0) scale(1);

  @starting-style {
    opacity: 0;
    transform: translateY(4px) scale(0.98);
  }
}

@media (prefers-reduced-motion: reduce) {
  .clm-floating-toolbar[popover] {
    transform: none !important;
    transition-duration: 0.05s !important;
  }
}
```

### 3.4 Inline Comment Attribution & Auto-Sizing Inputs (`form-fields-automatically-fit-contents`, `animate-to-intrinsic-sizes`)
- **Mandatory Human Attribution (`w:author`)**: Every inline or margin comment card in the UI and exported `.docx` must display the **human reviewer's name, role badge, and avatar initials** (e.g., `Pradeep Gupta • VP Global Tax & Trade`, `Rahul Kasanagottu • Sr. Director Strategic Sourcing`, `Megan Bowen • Chief Quality & Airworthiness Engineer`, `Lee Gu • Deputy General Counsel`, `Alex Wilber • CISO & Defense Cyber Lead`)—**never** `"AI System"` or `"CLM Bot"`.
- **Auto-Growing Comment & Rewrite Textareas (`form-fields-automatically-fit-contents`)**:
  Use `field-sizing: content` with explicit `width: 100%` (preventing horizontal jitter when placeholder text is replaced) and bounded `min-block-size: 2.5lh` / `max-block-size: 8lh`:

```css
.clm-comment-textarea {
  field-sizing: content;
  height: auto;
  width: 100%;
  min-block-size: 2.5lh;
  max-block-size: 8lh;
  padding: 0.625rem 0.75rem;
  border-radius: 0.5rem;
  border: 1px solid var(--border-subtle);
}
```

### 3.5 BigQuery Precedent Distribution Visualizations (`accessibility`, `color`)
Every redlined position displays its empirical **BigQuery Tier-1 Avionics Precedent Distribution (`N = 16` deals per clause, `64` total)**:
- **`GP1-12` (Warranty & FAA Inspection)**: `88%` (`14/16`) Held Firm | `12%` (`2/16`) Tier-1 Compromise | `0%` (`0/16`) Vendor Ask
- **`GP1-19` (Liability & IP Indemnity)**: `25%` (`4/16`) Held Firm | `69%` (`11/16`) Tier-1 Compromise (`2.0x PO / $90M Super-Cap`) | `6%` (`1/16`) Vendor Ask
- **`SP3-04` (Customs & Section 232/301 Tariffs)**: `31%` (`5/16`) Held Firm | `63%` (`10/16`) Tier-1 Compromise (`50/50 split >5%, capped at +2.0% / $900K`) | `6%` (`1/16`) Vendor Ask
- **`SP5-03` (DFARS 252.204-7012 Cyber)**: `94%` (`15/16`) Held Firm (`72-Hr Reporting`) | `6%` (`1/16`) Tier-1 Compromise | `0%` (`0/16`) Vendor Ask

**Design & Accessibility Rules for Precedent Charts**:
1. Wrap every precedent chart in `<figure>` with a descriptive `<figcaption>` summarizing the dominant precedent and sample size (`N = 16`).
2. Differentiate segments using **both color and pattern/label** (`Held Firm: 88% (14/16)`, `Compromise: 12% (2/16)`), and provide a collapsible or screen-reader-accessible `<table>` (`<caption>`, `<th scope="col">`) for assistive technologies.

### 3.6 Responsive Container Queries, View Transitions & Spatial Navigation (`size-aware-styling`, `same-document-transitions`, `spatial-navigation`)
1. **Modular Clause & Sidebar Panels (`size-aware-styling`)**: Set `container: clause-panel / inline-size` on split-pane columns so clause cards automatically switch from stacked vertical layout (`< 520px`) to side-by-side redline + margin comment layout (`>= 520px`).
2. **Smooth Variation & View Switching (`same-document-transitions`)**: When switching between the 12 UI Lab variations or filtering clauses, wrap the DOM update in `document.startViewTransition(() => updateView())` (with a direct fallback when `!document.startViewTransition`) and **always shift focus** to the newly active variation heading (`tabindex="-1"`) inside `transition.finished.finally(...)`.
3. **2D Spatial Keyboard Navigation (`spatial-navigation`)**: In grid/Bento/Kanban views (Variations 3, 8, 11), use the **Roving Tabindex Pattern** (`tabindex="0"` on active card, `tabindex="-1"` on inactive cards), compute targets dynamically via `getBoundingClientRect()` and `checkVisibility()`, ignore events inside `:read-write, select, input[type="range"], [role="slider"]`, and **never call `preventDefault()` when no candidate exists** in the pressed arrow direction so native viewport scrolling continues.

---

## 4. Pre-Flight UX Verification Checklist
Before delivering any Cymbal Aerospace CLM HTML interface or variation lab:
- [ ] **No Sub-12px Fonts**: All text is `>= 12px` (`0.75rem`) and uses `tabular-nums` for financial/precedent metrics.
- [ ] **Non-Color Diff Signifiers**: `<del>` and `<ins>` include semantic tags, strikethrough/underline differentiation, and screen-reader labels.
- [ ] **Human Comment Attribution**: Every comment displays the human reviewer (`Rahul Kasanagottu`, `Pradeep Gupta`, `Megan Bowen`, `Lee Gu`, `Alex Wilber`), never a bot/system label.
- [ ] **Keyboard & Focus Integrity**: Visible `:focus-visible` outlines (`outline: 3px solid ...; outline-offset: 2px`), native `<dialog>` `.showModal()` focus management, and focus routing after `startViewTransition()`.
- [ ] **Reduced Motion & Forced Colors**: `@media (prefers-reduced-motion: reduce)` and `@media (forced-colors: active)` rules are present.
