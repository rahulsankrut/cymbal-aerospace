# UI Skills & Modern Web Guidance Research Report (`researcher_ui_skills`)

## 1. Executive Summary
To support the **Cymbal Aerospace CLM (`BA-2026-AV-8921`)** UX Architecture Plan and the **12-Variation CLM UI Mockup Lab (`cymbal_clm_ui_lab_12_variations.html`)**, we conducted a comprehensive audit of:
1. **`modern-web-guidance` (`npx -y modern-web-guidance@latest`)**: Searched the full catalog (`970` lines of indexed capabilities) and retrieved **16 canonical guides** covering intrinsic sizing animations, `:has()` parent-state reactivity, top-layer Popover/Dialog orchestration, CSS Anchor Positioning, Container Size & Style Queries, Same-Document View Transitions, CSS Custom Highlight API, auto-growing form controls (`field-sizing: content`), 2D spatial keyboard navigation, and WCAG 2.2 AA accessibility/color-scheme rules.
2. **Local Antigravity UI Skills**: Audited `generative_ui` (CSP-compliant Tailwind script, `>= 12px` minimum font floor, semantic surface variables), `building-data-apps` (`DM Sans` + `JetBrains Mono` typography pairing, Zinc/Slate card hierarchy, `relative z-30` stacking), and `a11y-debugging` (accessibility tree inspection, keyboard focus trapping, `>= 24x24px` / `48x48px` tap targets).
3. **Public Enterprise Legal & Financial Design Systems**: Synthesized best practices from **J.P. Morgan Salt Design System** (multi-density tokens for institutional trading/financial workbenches), **IBM Carbon Design System for AI** (AI explainability slugs and confidence/precedent telemetry), **GitHub Primer** (accessible split/unified diff polarity tokens with non-color indicators), and **Microsoft Fluent 2** (Word-native floating action bars and `w:author` margin comment threading).
4. **Reusable Skill Installation**: Authored and installed **`clm-ux-design-system`** at both:
   - `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/skills/clm-ux-design-system/SKILL.md`
   - `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/skills/clm-ux-design-system/SKILL.md`

---

## 2. Inventory of Searched & Retrieved `modern-web-guidance` Guides

| Guide ID | Category | Key Web Platform Features | Application in Cymbal Aerospace CLM Workbench & 12-Variation Lab |
| :--- | :--- | :--- | :--- |
| `accessibility` | `accessibility` | Landmarks, `<dialog>`, `inert`, `.visually-hidden`, `:focus-visible`, `aria-live` | Screen-reader diff announcements, native modal focus locking without brittle JS traps, keyboard-only clause review, and accessible data tables backing BigQuery precedent charts. |
| `animate-to-intrinsic-sizes` | `css` | `interpolate-size: allow-keywords`, `calc-size()` | Smoothly expanding/collapsing clause rationale accordions, BigQuery SQL drawers, and rewrite input panels to `block-size: auto` without `max-height` hacks. |
| `child-state-based-styling` | `css` | `:has()`, `@supports not selector(:has(*))` | Reactive `.clm-clause-card` styling that elevates borders and swaps diff badges automatically when child radio/checkboxes (`:checked`) or comment textareas (`:focus`) change state. |
| `viewport-aware-dropdowns` | `ui-atoms` | `popover="auto"`, `position-area`, `position-try-fallbacks` | Word-native floating action toolbars (`✦ Rewrite with Input`, `✓ Accept`, `✕ Reject`, `💬 Comment`) tethered to redlined clauses that automatically flip axes at viewport edges. |
| `declarative-dialog-popover-control` | `ui-behaviors` | `commandfor`, `command="toggle-popover"`, `command="show-modal"` | Zero-JS declarative invocation of clause precedent popovers, SME routing preview modals, and UX Evaluation Matrix drawers. |
| `animate-to-from-top-layer` | `ui-behaviors` | `@starting-style`, `transition-behavior: allow-discrete`, `overlay` | Smooth entry/exit animations for floating redline action cards, modals, and toast notifications entering/leaving the browser top layer. |
| `size-aware-styling` | `css` | `container-type: inline-size`, `@container` | Modular clause cards and precedent widgets that adapt seamlessly whether placed in a narrow sidebar (Variation 2), a 3-column diff (Variation 5), or a wide Bento cell (Variation 11). |
| `design-token-reactivity` | `css` | `@container style(--density: ...)`, `:where([data-density])` | Reactive switching between `compact` (Bloomberg/Institutional terminal), `comfortable` (Standard CLM), and `spacious` (Executive Brief) density modes. |
| `same-document-transitions` | `ui-behaviors` | `document.startViewTransition()`, `view-transition-name` | Smooth visual morphing when switching across the 12 UI variations or toggling between Unified Diff, 3-Column Diff, and Clean Preview modes, with mandatory post-transition focus routing. |
| `highlight-text-ranges` | `ui-behaviors` | `CSS.highlights`, `Highlight`, `Range`, `::highlight()`, `<mark>` | High-performance, DOM-preserving highlighting for live clause search and cross-clause term matching (`"Firm-Fixed-Price"` across `SP3 §4.1` and `GP1 §3.1`), while reserving `<del>`/`<ins>`/`<mark>` for semantic diffs. |
| `form-fields-automatically-fit-contents` | `forms` | `field-sizing: content`, `min-block-size: 2.5lh`, `max-block-size: 8lh` | Auto-growing inline comment (`w:comment`) and counter-position rewrite `<textarea>` controls that expand vertically as SMEs type without horizontal jitter. |
| `color` | `visual-design` | WCAG 4.5:1 / 3:1 contrast, `@media (forced-colors: active)`, `color-mix(in oklab, ...)` | Non-color redline diff indicators (strikethrough + icons + visually hidden labels) and Windows High Contrast (`forced-colors`) outlines for `<del>` and `<ins>`. |
| `dark-mode` | `visual-design` | `<meta name="color-scheme" content="light dark">`, `light-dark()`, `scrollbar-color` | Seamless multi-theme support across **Emerald Stage**, **Institutional Dark Terminal**, and **Daylight Legal Paper** without FOUC. |
| `spatial-navigation` | `ui-behaviors` | Roving `tabindex`, `getBoundingClientRect()`, `checkVisibility()` | 2D arrow-key navigation across Bento Deal Room cards (Variation 11), Risk Heatmap cells (Variation 3), and SME Kanban columns (Variation 8). |
| `css-layout` | `css` | CSS Grid, `subgrid`, logical properties, `scrollbar-gutter: stable` | Aligning clause headers, baseline text, vendor redlines, and counter-proposals across rows in 3-column synchronized diff views (Variation 5) without ragged edges. |
| `typography` | `visual-design` | `max-width: 75ch`, `text-wrap: balance`, `text-wrap: pretty`, `rem` units | Optimal legal prose legibility (`65ch–75ch` measure, `1.65` unitless line-height) and balanced table/card headings. |

---

## 3. Enterprise Legal & Financial Design System Synthesis

1. **Word-Native Legal Review Paradigm (Spellbook / Ivo / Robin AI / Microsoft Fluent 2)**:
   - **Stage vs. Sheet Contrast**: Surrounding a crisp white/slate legal document sheet (`--paper-surface`) with a deep emerald stage (`#064e3b` / `#022c22`) immediately signals an active AI-assisted review session while keeping the contract typography familiar to legal counsel.
   - **Tethered Action Bar**: Placing `✦ Rewrite with Input`, `✓ Accept changes`, `✕ Reject changes`, and `💬 Comment` in a compact floating card directly below the active redline eliminates eye-travel between the document and distant toolbars.
   - **Strict Human Comment Attribution (`w:author`)**: In enterprise aerospace procurement, legal auditability requires that every margin comment saved to `BA-2026-AV-8921_Working_Review.docx` and `BA-2026-AV-8921_Cymbal_Counter_Proposal.docx` be attributed to the accountable human decision-maker (`Rahul Kasanagottu`, `Pradeep Gupta`, `Megan Bowen`, `Lee Gu`, `Alex Wilber`), never an unattributed AI system label.

2. **Institutional Financial Workbench Paradigm (J.P. Morgan Salt / Bloomberg / Cymbal Capital)**:
   - **High-Density Telemetry & Tabular Numerals**: Financial exposure caps (`$45,000,000` FFP ceiling, `$90,000,000` 2.0x PO Super-Cap, `$900,000` +2.0% Tariff Cap) and BigQuery precedent distributions (`88%`, `69%`, `63%`, `94%`) require `font-variant-numeric: tabular-nums` in `JetBrains Mono` so figures align vertically across tables and tickers.
   - **Live Data Provenance**: Pairing every AI recommendation with an expandable BigQuery SQL & Vector Search drawer (`vertex-ai-demos-468803.boeing_clm.historical_clause_exceptions`, `N = 16` deals per position) builds immediate institutional trust.

3. **Diff Polarity & Guardrail Playbook Paradigm (GitHub Primer / Litera Kira / Ironclad)**:
   - **Tri-State Redline Semantics**:
     - **Rejected Vendor Markup (`<del class="clm-diff-del">`)**: Crimson pill background + `2px` solid strikethrough + screen-reader prefix.
     - **Proposed Counter-Position (`<ins class="clm-diff-ins">`)**: Warm coral/amber highlight + `2px` solid bottom border + `✦` prefix.
     - **Accepted State**: Smooth transition to emerald confirmation badge and clean prose preview.

---

## 4. Installed Skill Summary (`clm-ux-design-system`)

The new skill has been installed at:
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/.agents/skills/clm-ux-design-system/SKILL.md`
- `/Users/rahulsankrut/Desktop/code/Cymbal Aerospace/skills/clm-ux-design-system/SKILL.md`

It provides copy-paste-ready CSS/HTML/JS blueprints for:
1. **CSP-Safe Antigravity & Spark Canvas Setup** (`tailwindcss.min.js` + `<meta name="color-scheme" content="light dark">`).
2. **3 Built-In Theme Presets** (`emerald-stage`, `institutional-dark`, `daylight-paper`) + **3 Density Modes** (`compact`, `comfortable`, `spacious`).
3. **Semantic Redline Diff Tokens & Forced-Colors Fallbacks** (`.clm-diff-del`, `.clm-diff-ins`, clean accepted state, and `CSS.highlights` search range highlighting).
4. **`:has()` Reactive Clause Cards** with `@supports not selector(:has(*))` fallback.
5. **Popover + Anchor Positioning Floating Action Toolbar** with `@starting-style` and `transition-behavior: allow-discrete`.
6. **Auto-Sizing Human-Attributed Comment & Rewrite Inputs** (`field-sizing: content` with `width: 100%` and `min-block-size`/`max-block-size` bounds).
7. **Accessible BigQuery Precedent Distribution Bars** (`<figure>`/`<figcaption>` + screen-reader `<table>` alternatives).
8. **Pre-Flight UX Verification Checklist** enforcing `>= 12px` font floor, `tabular-nums`, human `w:author` attribution, and keyboard/screen-reader accessibility.

---

### Modern Web Guidance

- **`accessibility`**: I enforced native `<dialog>` `.showModal()` focus management, `.visually-hidden` prefixes on `<del>`/`<ins>` diffs, semantic `<figure>`/`<table>` alternatives for BigQuery precedent charts, and strict focus-visibility rules to prevent screen-reader dead zones ("If an element can receive keyboard focus, it must not be hidden via `aria-hidden=\"true\"`.").
- **`animate-to-intrinsic-sizes`**: I enabled `interpolate-size: allow-keywords` on `:root` with a `block-size: auto` fallback before `calc-size()` so clause rationale drawers and Playbook accordions animate smoothly to their natural height without fragile `max-height` hacks ("Transitions to intrinsic keywords are disabled by default (`numeric-only`) to maintain backward compatibility. You must apply `interpolate-size: allow-keywords` to the element or an ancestor.").
- **`child-state-based-styling`**: I scoped `:has(:checked)` and `:has(:focus-visible)` directly to `.clm-clause-card` alongside an `@supports not selector(:has(*))` modifier-class fallback to avoid expensive page-wide layout recalculations ("When using `:has()`, scope the selector to the most specific container possible (like `.theme-card`). Avoid anchoring it to very high-level elements like `body:has(...)` if the styling changes are localized, as broad `:has()` queries can trigger more layout recalculations.").
- **`viewport-aware-dropdowns`**: I modeled the floating clause action bar (`✦ Rewrite with Input`, `✓ Accept`, `✕ Reject`, `💬 Comment`) as a `popover="auto"` button group using logical `position-area: block-end span-inline-end` and `position-try-fallbacks`, omitting `role="menu"` and `aria-haspopup` so assistive tech is not promised unimplemented menu arrow-key semantics ("This pattern explicitly models a **button group revealed inside a popover** rather than a true ARIA menu. Do not apply `role=\"menu\"` or `role=\"menuitem\"` unless you fully implement the corresponding keyboard navigation contract").
- **`declarative-dialog-popover-control`**: I codified declarative `commandfor` and `command="toggle-popover"` / `command="show-modal"` triggers with conditional polyfill detection on `HTMLButtonElement.prototype` to avoid brittle click listeners ("Feature detect support by checking for the `commandForElement` property on the `HTMLButtonElement` prototype. Do NOT check the window or document object.").
- **`animate-to-from-top-layer`**: I configured floating popovers and modal dialogs to transition `opacity, transform, display, overlay` with `@starting-style` and `transition-behavior: allow-discrete` placed after shorthands so overlays are not clipped prematurely on exit ("To animate the `display` property, you must set `transition-behavior: allow-discrete`. This allows the element to remain visible during its exit transition. If using transition shorthands, be sure to place the `transition-behavior: allow-discrete` afterwards to prevent the shorthand from negating it.").
- **`size-aware-styling`**: I established `container: clause-panel / inline-size` on workbench panes so clause cards adapt between vertical stacked and side-by-side layouts based on pane width rather than viewport breakpoints ("You must first tell the browser which element is the container to be measured.").
- **`design-token-reactivity`**: I combined low-specificity `:where([data-density="..."])` attribute selectors with progressive `@container style(--density: ...)` rules so compact, comfortable, and spacious density modes work across all browsers without specificity wars ("Make sure the fallback approach uses `:where()` when selecting the container elements to avoid increasing the specificity.").
- **`same-document-transitions`**: I wrapped variation-switching DOM updates in `document.startViewTransition()` and routed programmatic focus to the active variation heading (`tabindex="-1"`) inside `transition.finished.finally()` so keyboard users never lose focus context ("Shift focus programmatically to an updated page heading or view container (using `tabindex=\"-1\"`) immediately after the DOM updates or when the view transition's `finished` promise resolves.").
- **`highlight-text-ranges`**: I separated transient clause search highlighting—using `TreeWalker` and `CSS.highlights` with a `<mark>` fallback—from semantic contract redlines (`<del>`, `<ins>`) so critical legal markup remains in the accessibility tree ("Custom highlights are purely presentational and are not exposed to the accessibility tree. If the highlighted text is semantically relevant to the document (e.g., a user-selected passage), use `<mark>` instead.").
- **`form-fields-automatically-fit-contents`**: I applied `field-sizing: content` with `height: auto`, explicit `width: 100%`, and `min-block-size: 2.5lh` / `max-block-size: 8lh` to inline SME comment and rewrite textareas so they grow smoothly vertically without horizontal collapse ("To prevent this, apply an explicit width (like `width: 100%`) to the textarea. This forces the textarea to maintain a stable horizontal width while still auto-sizing vertically as content wraps.").
- **`color`**: I paired red/coral/emerald diff tokens with strikethroughs, bottom borders, icons, and `@media (forced-colors: active)` outlines so contract reviewers never rely on color alone ("Don't use color alone to indicate the presence of a user interface component or its state: Use iconography and/or shape to help differentiate.").
- **`dark-mode`**: I placed `<meta name="color-scheme" content="light dark">` in `<head>` and `color-scheme: light dark` on `:root` with `light-dark()` tokens and `@media (prefers-color-scheme: dark)` fallbacks so native scrollbars and form controls match the active workbench theme ("Apply the `color-scheme` property to the `html` element or the `:root` pseudo-class. Browsers specifically look to the root element to determine the theme for the entire viewport—including the root scrollbars and the initial \"canvas\" background.").
- **`spatial-navigation`**: I specified roving `tabindex` 2D arrow-key navigation using live `getBoundingClientRect()` and `checkVisibility()` checks for Bento and Kanban views while letting boundary arrow presses bubble natively ("If there is no focusable element in the pressed direction, **do not prevent default browser behavior**. Let the event bubble so the browser can scroll the viewport natively.").
- **`css-layout`**: I used CSS Grid with `subgrid` for 3-column synchronized clause comparison and `scrollbar-gutter: stable` with `overscroll-behavior: contain` on independent scroll panes while preserving DOM focus order ("Don't use `order` or `flex-direction: *-reverse` to reorder interactive content. They change visual order only; the DOM order still drives sequential focus, so keyboard tab flow won't match what the user sees.").
- **`typography`**: I capped contract clause line lengths at `75ch` (`<= 80ch`) with unitless `line-height: 1.65` and restricted `text-wrap: balance` to unboxed headings while applying `text-wrap: pretty` to clause prose ("Avoid `text-wrap: balance` on elements with a visible box (backgrounds, borders, shadows, etc) as it does not change the container's width, it only affects how text wraps *within* that width.").
