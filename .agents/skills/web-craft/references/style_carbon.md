---
name: Carbon
slug: carbon
register: classic
mode: light
---

# Carbon

## Identity

**North Star: "Productive Clarity."** A systematic enterprise design system:
pure white, a disciplined gray ramp, one decisive blue, and a single sans with a
monospace label voice. Square corners, flat gray layers, and 1px rules. Every
element is functional; nothing is decorative. Calm, exact, and trustworthy —
never cold, flashy, or ornamental.

-   **Mood**: systematic, precise, accessible, quietly confident.
-   **Inspired by**: industrial enterprise design systems, cloud operations
    consoles, technical documentation, and high-density analytics tools.

## When to Use

-   **Best for**: dashboards and analytics, admin and operations tools,
    technical reports, product and engineering documentation, data-dense
    tables, calculators and configurators, anything that must read as
    reliable.
-   **Avoid for**: personal or emotional stories, celebrations, lifestyle and
    hospitality, children's content, anything meant to feel warm, crafted, or
    playful.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,100..700;1,100..700&family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #ffffff;               /* pure white, maximum contrast */
  --surface-container-low: #f4f4f4;    /* gray 10: inputs, zebra rows */
  --surface-container: #f4f4f4;        /* gray 10: the standard layer (cards) */
  --surface-container-high: #e0e0e0;   /* gray 20: a layer on a layer, hover */

  /* Ink */
  --on-surface: #161616;               /* gray 100: headings and body */
  --on-surface-variant: #525252;       /* gray 70: helper text, captions */

  /* Rules */
  --outline: #8d8d8d;                  /* gray 50: input underlines, never text */
  --outline-variant: #e0e0e0;          /* gray 20: section and row dividers */

  /* Accents */
  --primary: #0f62fe;                  /* signal blue: actions, links, active */
  --on-primary: #ffffff;
  --primary-container: #d0e2ff;        /* blue 20: selected rows, tags */
  --on-primary-container: #161616;
  --secondary: #6f6f6f;                /* gray 60: tertiary text, icons */
  --tertiary: #198038;                 /* green 60: success and validation */
  --error: #da1e28;                    /* red 60: danger and errors */
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #0f62fe;                   /* blue 60 */
  --data-2: #6929c4;                   /* purple 70 */
  --data-3: #005d5d;                   /* teal 70 */
  --data-4: #9f1853;                   /* magenta 70 */
  --data-context: #8d8d8d;             /* gray 50: context series */

  /* Fonts */
  --font-headline: 'IBM Plex Sans', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-label: 'IBM Plex Mono', monospace;

  /* Shape */
  --rounded: 0.125rem;                 /* inputs, checkboxes: barely softened */
  --rounded-lg: 0.25rem;
  --rounded-full: 0.75rem;             /* tags only: a 24px pill */

  /* Style effects */
  --shadow-1: 0 2px 6px rgb(0 0 0 / 0.1);    /* menus, popovers, tooltips */
  --shadow-2: 0 4px 12px rgb(0 0 0 / 0.12);  /* raised menus, floating panels */
  --rule: 1px solid var(--outline-variant);  /* section and row separation */
  --field-rule: 1px solid var(--outline);    /* bottom border on inputs */
  --indicator: 2px solid var(--primary);     /* active / key-item marker */
}
```

## Color

-   **Proportions**: white and the gray ramp carry the page — 90% or more.
    Blue is the signal (under 5%): the primary action, links, the active tab,
    the selected row, the series that matters. Green and red appear only as
    states.
-   **Semantic roles strictly.** Blue means "interactive or selected," green
    means "valid or positive," red means "error or destructive." Never use
    any of them as decoration.
-   **Accent text sits on white or gray 10 only.** Blue, gray 60, green, and
    red all pass 4.5:1 on `--background` and `--surface-container`, but fall to
    about 3.8:1 on `--surface-container-high` — on gray 20 use `--on-surface`
    or `--on-surface-variant`. On `--primary-container`, text is always
    `--on-primary-container`, never blue.
-   **`--outline` is never text.** At 3.3:1 it is for input underlines,
    unchecked controls, and icon strokes only.
-   **Layer with gray, not shadow.** Each nested level steps one shade:
    white → gray 10 → gray 20.

## Typography

Role                                 | Family        | Weight / style                                               | Size and spacing
------------------------------------ | ------------- | ------------------------------------------------------------ | ----------------
Display, headlines                   | IBM Plex Sans | 300 for display; 600 for emphasized words and small headings | Tracking 0 at display size — Plex is already tight. Line height 1.15–1.25.
Body                                 | IBM Plex Sans | 400; 600 for inline emphasis                                 | 14–16px in tools and dashboards, 16–18px in narrative. Line height 1.5.
Metric labels, column headers, units | IBM Plex Mono | 400–500, uppercase                                           | 0.75rem, tracking 0.08–0.12em.
Figures, key values                  | IBM Plex Mono | 300–400                                                      | Fixed-width, so columns align; key values large and light.
Helper text, captions                | IBM Plex Sans | 400                                                          | 0.75–0.875rem in `--on-surface-variant`.

Headlines are sentence case. Hierarchy comes from weight (300 / 400 / 600)
working with size, not from color — a light display line over semibold small
headings and mono labels.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Flat gray layers

Containers are gray 10 rectangles on white with square corners and no border or
shadow; a container inside a container steps to gray 20. Applies to cards,
key-figure tiles, panels, and the primary container of a tool.

```css
.layer {
  background: var(--surface-container);
  border-radius: 0;
  padding: var(--space-md);
}
.layer .layer { background: var(--surface-container-high); }
```

### 2. Light/semibold headline split

Display headlines set in Plex Sans 300, with the key phrase in 600. Applies to
the title block and major section headings; small headings are plain 600.

```css
.headline {
  font-family: var(--font-headline);
  font-weight: 300;
  letter-spacing: 0;
  line-height: 1.2;
}
.headline strong { font-weight: 600; }
```

### 3. Mono label voice

Uppercase, tracked Plex Mono for metric labels, column headers, axis labels,
units, and dates; key values in large, light mono. Applies wherever the content
has a data label, a date, a code, or a figure.

```css
.label {
  font-family: var(--font-label);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--on-surface-variant);
}
.key-value { font-family: var(--font-label); font-weight: 300; font-size: 2rem; }
```

### 4. Blue indicator bar

A 2px blue bar marks what is active or most important: the selected tab, the
current nav item, the headline key-figure tile. Bottom edge for horizontal
items, left edge for vertical lists. One indicated item per group.

```css
.is-active, .key-tile { border-bottom: var(--indicator); }
.side-nav .is-active { border-bottom: 0; border-left: var(--indicator); }
```

### 5. Hairline section separation

Sections and rows are divided by a single 1px gray 20 rule, not by boxes or
space alone. Applies under section headings, between list entries, and between
table rows.

```css
.section-head { border-bottom: var(--rule); padding-bottom: var(--space-sm); }
.list > * + * { border-top: var(--rule); padding-top: var(--space-sm); }
```

## Composition

-   **Flush-left grid.** Everything hangs from a strict left edge on a
    column grid; headings, labels, and button rows are left-aligned. This
    agrees with the skill's preference for asymmetry — vary column spans
    (e.g. 8 + 4, 3 + 9) rather than centering.
-   **Dense and gridded.** Tight, regular spacing on the 8px rhythm of the
    shared scale (`--space-sm`, `--space-md`), compact table rows, small gaps
    between tiles. Larger steps (`--space-xl`) only between major sections.
-   **Separation by tone and rule.** Gray layer shifts first, 1px rules second,
    shadows only for things that float (menus, popovers, tooltips).
-   **Narratives** keep the left edge and a 65ch measure, with more space
    between sections; the mono labels and gray layers stay.

## Components

-   **Buttons**: square corners, 48px tall (40px when sharing a row with inputs,
    so the row lines up), label left-aligned with extra room on the right
    (padding roughly `var(--space-sm) var(--space-2xl) var(--space-sm)
    var(--space-md)`), Plex Sans 400. Primary is a solid blue fill with white
    text; secondary is a 1px blue outline; ghost is blue text only. Hover
    darkens the fill (`color-mix(in srgb, var(--primary), var(--on-surface)
    25%)`); no shadows.
-   **Cards and tiles**: gray 10, no radius, 16px padding (`--space-md`), mono
    label on top, light mono value below, helper text in gray 70.
-   **Inputs**: 40px tall, gray 10 fill, no side or top border, a `--field-rule`
    underline, `0 var(--space-md)` inner padding (selects add room on the right
    for the arrow); label above in 0.75rem gray 70. Focus adds the ring; error
    turns the underline red with red helper text.
-   **Tags**: blue 20 fill, gray 100 text, `--rounded-full`, 24px tall, Plex
    Sans 400 at 0.75rem.
-   **Tables**: zebra striping with gray 10 on alternating rows, gray 20 header
    row with mono uppercase headers, no vertical lines, compact row height;
    numbers right-aligned in mono. Selected row uses blue 20.
-   **Tabs**: plain text labels over a gray 20 baseline; the active tab gets
    the blue indicator bar and 600 weight.
-   **Links**: blue, no underline at rest, underlined on hover.
-   **Notifications**: a gray 10 strip with a 3px left bar in the state color
    (blue, green, red) and an icon in the same color.

## Data Visualization

-   **Series**: `--data-1` (blue) for the series that matters, then purple,
    teal, magenta. Everything that is context is `--data-context`.
-   **Lines and marks**: 1.5–2px lines, flat-topped square bars with 1px gaps,
    no rounded bar ends. No gradients, glows, shadows, or 3D.
-   **Axes and gridlines**: axis and tick labels in `--font-label` at label
    size in gray 70; solid gridlines in `--outline-variant`; a solid gray 50
    baseline at zero; no chart border.
-   **Labels and annotations**: legend in a single row above the plot with
    small square swatches; direct labels in mono where they fit. Tooltips are
    white with `--shadow-1`, square corners, mono values.
-   **Chart titles**: Plex Sans 600 at small-heading size, left-aligned, with
    a mono label for units beneath.

## Motion

Quick and functional: state changes over `--dur-micro`, panels and reveals
over `--dur-short` with `--ease-out`, short fades or a few pixels of slide. No
bounces, springs, parallax, or decorative entrance choreography.

## Don'ts

-   No rounded cards or pill buttons; only tags use `--rounded-full`.
-   No drop shadows on cards; shadows are for floating layers only.
-   No blue, green, or red used as decoration, background washes, or
    gradients.
-   Don't center headings or button rows, and don't set body text in mono.
-   Don't mix in a second sans or a serif; Plex Sans and Plex Mono only.
-   No ornamental icons or illustrations; icons only where they carry meaning.

## If the User Asks for Dark

Keep the same roles on Carbon's gray 100 theme: `--background: #161616`,
`--surface-container: #262626`, `--surface-container-high: #393939`,
`--on-surface: #f4f4f4`, `--on-surface-variant: #c6c6c6`, `--primary: #78a9ff`
(blue 40, with `--on-primary: #161616`), `--outline-variant: #393939`,
`--tertiary: #42be65`, `--error: #ff8389`. Layers step lighter, not darker;
shadows become stronger and are still reserved for floating layers.
