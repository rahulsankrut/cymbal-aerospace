---
name: Handbook
slug: handbook
register: classic
mode: light
---

# Handbook

## Identity

**North Star: "Plain, Direct, and Built for Everyone."** A high-contrast,
plain-language reference handbook or step-by-step guide: black on white, deep
navy and link blue, grounded action buttons, and a bright yellow focus state. A
single sturdy sans in heavy headlines and large body text, square corners, a
heavy top index rule with square numbered step badges, and a thick blue inset
callout rule that says "read this". Trustworthy, calm, and unmistakably clear —
nothing decorative, nothing ambiguous, never cold or bureaucratic.

-   **Mood**: plain, trustworthy, practical, accessible.
-   **Inspired by**: plain-language reference handbooks, high-legibility public
    guides, transit and utility systems, and step-by-step checklists.

## When to Use

-   **Best for**: step-by-step guides, checklists, eligibility checkers, civic
    and policy information, public notices, forms and calculators, explainers of
    rules, rights, procedures, or deadlines.
-   **Avoid for**: brand storytelling, luxury or fashion, literary or
    emotional narratives, playful or children's content, anything that wants
    atmosphere over clarity.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #ffffff;               /* plain white page */
  --surface-container-low: #f3f2f1;    /* light grey: inset panels, key figures */
  --surface-container: #e8e7e5;        /* a rare filled panel; no link text on it */
  --surface-container-high: #dbdad9;   /* pressed state of grey buttons */

  /* Ink */
  --on-surface: #0b0c0c;               /* near-black: all body text and headings */
  --on-surface-variant: #505a5f;       /* grey: captions, hints, metadata */

  /* Rules */
  --outline: #0b0c0c;                  /* form field borders, 2px */
  --outline-variant: #b1b4b6;          /* hairline dividers; never text */

  /* Accents */
  --primary: #162e51;                  /* standard navy: top index rule, step badges, primary buttons */
  --on-primary: #ffffff;
  --primary-container: #d2e2f1;        /* pale blue: status tags, notices */
  --on-primary-container: #0c2d4a;     /* dark blue text on pale blue */
  --secondary: #4c2c92;                /* visited-link purple */
  --tertiary: #1a569e;                 /* link blue: links, inset rules, header rule */
  --error: #d4351c;                    /* error red: text on white only */
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #1a569e;                   /* blue */
  --data-2: #c75a0a;                   /* deep orange */
  --data-3: #28a197;                   /* turquoise */
  --data-4: #4c2c92;                   /* purple */
  --data-context: #b1b4b6;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Public Sans', sans-serif;
  --font-body: 'Public Sans', sans-serif;
  --font-label: 'Public Sans', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;                   /* even tags are square */

  /* Style effects */
  --top-index-rule: 6px solid var(--primary);
  --inset-rule: 5px solid var(--tertiary);
  --button-ground: 0 2px 0 #091526;            /* dark navy ledge under primary */
  --button-ground-secondary: 0 2px 0 #858686;  /* grey ledge under secondary */
  --focus-yellow: #ffdd00;                     /* focus highlight; never text */
  --focus-ring: 3px solid var(--focus-yellow);
  --focus-bar: inset 0 0 0 2px var(--on-surface);
  --focus-underline: 0 -2px var(--focus-yellow), 0 4px var(--on-surface);
}
```

## Color

-   **Proportions**: white and near-black are almost everything — well over
    90%. Link blue (`--tertiary`) is the working accent (links, inset rules, the
    lead data series). Standard navy (`--primary`) appears on the top index rule,
    step badges, and the primary action button. Yellow appears only when
    something has focus.
-   **Standard navy means "do this".** Reserve `--primary` fills for step
    markers and the primary action button so the next step is unmistakable.
-   **Yellow is never text and never decoration.** At 1.35:1 on white it only
    works paired with the near-black bar or underline in the focus treatment,
    which carries the contrast.
-   **Grey is for structure.** `--outline-variant` (2.1:1) is for dividers and
    table rules only. `--surface-container-low` is the one fill in regular
    use; link blue drops below 4.5:1 on `--surface-container`, so keep links
    off it. Error red is text on white only (4.3:1 on grey fails).
-   **Pale blue** (`--primary-container`) is for status tags and notice
    panels, always with `--on-primary-container` text.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Public Sans | 800 (700 for small headings) | Large and tight: tracking −0.01em, line height 1.1. |
| Body | Public Sans | 400; 700 for emphasis | Large: about 19px (1.1875rem) for narrative. Line height 1.5. |
| Captions, hints, lead-ins | Public Sans | 400 | Body size or one step down, in `--on-surface-variant`. Sentence case, no tracking. |
| Labels, field names | Public Sans | 700 | Body size, sentence case, `--on-surface`. |
| Status tags | Public Sans | 700, uppercase | Label size, tracking 0.04em — the only uppercase in the style. |
| Figures | Public Sans | 800 for key figures; 400 in tables | `font-variant-numeric: tabular-nums` in tables and charts. |

One family does everything; hierarchy comes from the jump between 800
headlines and 400 body, and from size. Headlines read as plain words, never
stylized: no all caps, no italics (italics only for titles of works).

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Heavy top index rule & square step badges

Crown the page or main container with a `6px solid var(--primary)` top border
and a bold uppercase category/step header row (`STEP-BY-STEP GUIDE` or topic
label) above a `1px` black rule. Where the content has numbered steps, set each
step number inside a solid square `--primary` badge.

```css
.index-header {
  border-top: var(--top-index-rule);
  border-bottom: 1px solid var(--on-surface);
  padding: var(--space-sm) 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-label);
  font-weight: 700;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.step-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  background: var(--primary);
  color: var(--on-primary);
  font-weight: 800;
  font-size: 0.8125rem;
}
```

### 2. Inset blue rule

A 5px blue rule on the left edge of key figures, callouts, and the one
notice the reader must not miss. The panel is light grey or plain white; the
rule does the emphasizing, so there is no border on the other sides.

```css
.inset {
  border-left: var(--inset-rule);
  background: var(--surface-container-low);
  padding: var(--space-md) var(--space-lg);
}
```

### 3. Grounded action button

The primary action is a flat civic-navy slab with square corners and a 2px dark
ledge beneath it, as if it sits on the page. Secondary actions are grey with a
grey ledge. Applies to every button; navy only for the main one.

```css
.button {
  font: 600 1rem/1.2 var(--font-label);
  background: var(--primary);
  color: var(--on-primary);
  border: 0;
  border-radius: var(--rounded);
  padding: var(--space-sm) var(--space-md);
  box-shadow: var(--button-ground);
}
.button--secondary {
  background: var(--surface-container-low);
  color: var(--on-surface);
  box-shadow: var(--button-ground-secondary);
}
.button:active { transform: translateY(2px); box-shadow: none; }
```

### 4. Yellow focus

Focus is loud on purpose: a yellow outline with a near-black inner bar on
buttons and fields, and a yellow highlight with a black underline on links.
Applies to every focusable element and is how this style draws the focus ring.

```css
.button:focus-visible, input:focus-visible {
  outline: var(--focus-ring);
  outline-offset: 0;
  box-shadow: var(--focus-bar);
}
a:focus-visible {
  outline: none;
  background: var(--focus-yellow);
  color: var(--on-surface);
  text-decoration: none;
  box-shadow: var(--focus-underline);
}
```

## Composition

-   **Flush left.** Everything aligns to one left edge: title, caption, body,
    buttons. Narratives and guides read as one column of about 60–70ch,
    optionally beside a narrow side column (two-thirds / one-third). This
    follows the skill's preference for asymmetry.
-   **Medium density, generous type.** Text is big, but spacing is practical
    rather than airy: clear gaps between sections, tight gaps within a step.
-   **Separate with space and headings.** Sections are divided by heavy
    headings and whitespace; rows of facts by grey hairlines. Fills are
    reserved for inset panels. No floating card grids, no shadows.
-   **Dashboards and tools** keep the service bar and flush-left headings;
    key figures sit in a row of inset-rule panels, and tables are ruled, not
    boxed.

## Components

-   **Buttons**: square, weight 600, grounded ledge (treatment 3).
    Standard navy for the main action only; the rest grey.
-   **Key figures**: an inset-rule panel — a small grey label, the value in
    800 at headline size, a one-line description in near-black 400.
-   **Status tags**: pale blue fill, dark blue uppercase 700 label, square.
-   **Links**: blue, always underlined (1px, offset 3px; thickens to 3px on
    hover); visited links turn `--secondary`.
-   **Inputs**: white, 2px `--outline` border, square; label above in bold,
    hint below it in grey. Errors add a 5px red left rule to the field group
    and the message in red bold.
-   **Tables**: no vertical lines or zebra stripes; grey hairline under every
    row, bold header row with a near-black hairline beneath, tabular figures
    right-aligned.
-   **Summary lists**: key in bold on the left, value on the right, grey
    hairline between rows.
-   **Numbered steps**: numerals in bold at headline weight, flush left with
    the step's heading.

## Data Visualization

-   **Series**: `--data-1` (blue) for the series that matters, then orange,
    turquoise, purple. Context series and gridlines are `--data-context`.
    Never use focus yellow in charts.
-   **Marks**: flat fills, 2–3px lines, square ends; bars with square corners.
    No gradients, glows, or 3D.
-   **Axes and gridlines**: a near-black baseline; light grey horizontal
    gridlines only; axis labels at label size in `--on-surface-variant`; no
    chart border.
-   **Labels**: values and line labels set directly on the chart in bold body
    type rather than in a legend.
-   **Chart titles**: headline weight, flush left, no rule or box.

## Motion

Almost none. Short fades or state changes over `--dur-short`; no entrance
animation on scroll, no parallax, no bounce. A pressed button drops 2px.

## Don'ts

-   No rounded corners, pills, drop shadows, or gradients — the button ledge is
    the only shadow.
-   No light or thin weights for headlines, and no grey body text.
-   No more than one primary navy button per view.
-   No yellow outside focus states, and no blue that isn't a link, a rule, or
    data.
-   Don't center text blocks, titles, or button rows.
-   No decorative icons, hero imagery, or ornamental dividers.

## If the User Asks for Dark

Keep the roles on a near-black ground: `--background: #0b0c0c`,
`--surface-container-low: #1d1f20`, `--on-surface: #f3f2f1`,
`--on-surface-variant: #b1b4b6`, `--tertiary: #6fa8dc` (link blue lightened to
keep 4.5:1), `--primary: #2b548f` with white text, `--outline: #f3f2f1`. The
service bar becomes `#11223b` with the same blue rule; the yellow focus keeps a
near-black inner bar on light elements and a white one on dark.
