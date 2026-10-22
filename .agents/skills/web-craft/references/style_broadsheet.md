---
name: Broadsheet
slug: broadsheet
register: classic
mode: light
---

# Broadsheet

## Identity

**North Star: "All the News, Weighed."** The newspaper of record: warm ivory
newsprint, near-black ink, claret accents, and bare teal tags. Heavy slab-serif
headlines (`Bitter`) over a sober reading serif (`Source Serif 4`), hairline
column rules, and the 3px double rule under the masthead. Authority comes from
typographic hierarchy and ruled columns, not decoration. Measured and serious,
never sensational or tabloid.

-   **Mood**: authoritative, measured, dense, trustworthy.
-   **Inspired by**: broadsheet newspapers of record, weekend review sections,
    financial and policy dailies, and multi-column print briefings.

## When to Use

-   **Best for**: news explainers, history and historical explainers (timelines,
    wars, dynasties, genealogies), finance and markets, policy and economics,
    current events, briefings and analysis, reports that weigh evidence.
-   **Avoid for**: playful or children's content, lifestyle and wellness,
    product marketing, anything meant to feel soft, romantic, or futuristic.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,500..800;1,400..700&family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f7f3eb;               /* warm ivory newsprint */
  --surface-container-low: #efe8da;    /* deeper newsprint: secondary buttons, a boxed aside */
  --surface-container: #e6ddcc;        /* a rare filled panel (a form, a data box) */
  --surface-container-high: #ddd2be;   /* hover on filled panels, selected rows */

  /* Ink */
  --on-surface: #1a1817;               /* newsprint black: headlines and body */
  --on-surface-variant: #4d4845;       /* grey ink: ledes, captions, bylines */

  /* Rules */
  --outline: #33302e;                  /* ink rules: section tops, input borders */
  --outline-variant: #cdc3b2;          /* column hairlines and gridlines, never text */

  /* Accents */
  --primary: #990f3d;                  /* claret: section labels, links, primary action */
  --on-primary: #ffffff;
  --primary-container: #f4dce2;        /* pale claret wash: a highlighted row */
  --on-primary-container: #6b0a2a;
  --secondary: #0d7680;                /* teal: tags, deltas; text on --background only */
  --tertiary: #0f5499;                 /* oxford blue: third data voice, rare */
  --error: #b3261e;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #990f3d;                   /* claret */
  --data-2: #0d7680;                   /* teal */
  --data-3: #0f5499;                 /* oxford blue */
  --data-4: #9a6312;                   /* ochre */
  --data-context: #bfb5a4;             /* context series and gridlines, never text */

  /* Fonts */
  --font-headline: 'Bitter', serif;
  --font-body: 'Source Serif 4', serif;
  --font-label: 'Source Sans 3', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;                   /* even tags are square */

  /* Style effects */
  --rule-masthead: 3px double var(--on-surface);
  --rule-ink: 1px solid var(--on-surface);
  --rule-section: 2px solid var(--outline);
  --rule-column: 1px solid var(--outline-variant);
}
```

## Color

-   **Proportions**: warm newsprint and black ink are the paper — well over 90%
    of the page. Claret is the signal (under 5%): links, the primary action,
    section labels, and the series that matters. Teal is the second, smaller
    voice: tags, deltas, the comparison series.
-   **Teal is text only on `--background`** (5.0:1). On the darker newsprint
    surfaces it drops under 4.5:1, so tags and deltas inside a filled panel
    switch to ink or claret.
-   **`--outline-variant` and `--data-context` are never text.** They are
    hairlines, gridlines, and context marks only.
-   **Fills are rare.** Columns are separated by rules, not boxes. A filled
    newsprint panel is reserved for one aside or form that must read as an
    object.
-   **Error** text sits on `--background` or `--surface-container-low` only.

## Typography

Role                       | Family         | Weight / style                                 | Size and spacing
-------------------------- | -------------- | ---------------------------------------------- | ----------------
Display, headlines         | Bitter         | 800 for the title, 700 for section heads       | Line height 1.06–1.14, tracking −0.015em. Sturdy slab-serif press authority without fragile hairlines.
Standfirst / lede          | Source Serif 4 | 400, in `--on-surface-variant`                 | 1.15–1.25× body, line height 1.5, measure under 58ch.
Body                       | Source Serif 4 | 400; italic for emphasis; 600 for run-in heads | Line height 1.55–1.65. Let the optical-size axis work (`font-optical-sizing: auto`).
Labels, table headers, nav | Source Sans 3  | 700, uppercase                                 | Label size, tracking 0.06em — compact, crisp newsroom sans contrast against the serifs.
Key figures                | Bitter         | 700                                            | Lining figures (`font-variant-numeric: lining-nums tabular-nums`).
Pull quotes                | Bitter         | 400–600 italic                                 | 1.4–1.6× body, ink, between ink rules.

Headlines are sentence case or headline case, never all caps; only the small
labels are uppercase. Contrast comes from a heavy slab-serif display face
(`Bitter`) against a light, even reading serif (`Source Serif 4`).

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Masthead rules

The opening title block sits under a 3px double ink rule across the top and
closes with a single 1px ink rule under the lede. Once per view, on the opening
title block only.

```css
.masthead-line {
  border-bottom: var(--rule-masthead);
  padding-bottom: var(--space-sm);
  font-family: var(--font-label);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.masthead { border-bottom: var(--rule-ink); padding-block: var(--space-lg); }
```

### 2. Heavy slab-serif headline

Every headline is `Bitter` at heavy weight, tightly leaded, slightly tightened —
the newspaper's voice. Main title at 800, section heads at 700.

```css
h1 { font-family: var(--font-headline); font-weight: 800; line-height: 1.06; letter-spacing: -0.015em; }
h2, h3 { font-family: var(--font-headline); font-weight: 700; line-height: 1.12; }
```

### 3. Column hairlines

Side-by-side items — a row of key figures, a multi-column grid, dashboard
panels — sit on the bare page separated by vertical hairlines, with no gaps
or fills. The first column has no rule and no left padding.

```css
.columns { display: flex; gap: 0; }
.columns > * { border-left: var(--rule-column); padding: var(--space-xs) var(--space-lg); background: transparent; }
.columns > :first-child { border-left: 0; padding-left: 0; }
```

### 4. Section top rule and claret label

Section openings carry a 2px ink rule across the top of the column. When a
section has a real date, part number, or source desk label, set it as a small,
bold, uppercase claret line; don't invent generic category kickers above every
heading.

```css
.section-open { border-top: var(--rule-section); padding-top: var(--space-sm); }
.section-label {
  font-family: var(--font-label);
  font-weight: 700;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--primary);
}
```

### 5. Bare teal tags

Tags, topics, and change indicators (deltas) are plain uppercase teal text with
no chip, outline, or left padding — a newspaper topic tag, not a pill.

```css
.tag {
  font-family: var(--font-label);
  font-weight: 700;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--secondary);
  background: transparent;
  padding: 0;
}
```

## Composition

-   **Flush-left on a column grid.** Headlines, ledes, and figures align to the
    left edge of their column, in line with the skill's general preference for
    asymmetry. Nothing is centered.
-   **Dense.** Tighter than a magazine: modest gaps between sections, small
    gutters, several columns where the content allows. Separation comes from
    ink rules (section tops), hairlines (between columns), and the masthead
    double rule — never shadows or rounded boxes.
-   **Narratives** run body text in one column of 60–68ch, with figures and
    asides able to break wider; the lede sits directly under the headline.
-   **Dashboards and tools** read like a markets page: ruled columns of
    figures, a ruled header, tables doing much of the work.

## Components

-   **Buttons**: square. Primary is a claret fill with white text; secondary is
    a `--surface-container-low` fill with ink text. Label at weight 600–700 in
    the label font. Hover darkens the fill; no shadows.
-   **Key figures**: in a hairline-ruled row — a small uppercase grey label, the
    value in `Bitter` 700, a teal or ink delta line beneath.
-   **Tags**: bare teal uppercase text (treatment 5).
-   **Links**: claret, underlined 1px with a 2px offset; the underline thickens
    on hover.
-   **Inputs**: square, a 1px `--outline` border on `--background`; focus turns
    the border claret and adds the focus ring.
-   **Tables**: an ink rule over the header and under the last row, hairlines
    between rows, no vertical lines and no zebra fills. Header in the label
    voice; numbers right-aligned in tabular lining figures.
-   **Navigation and contents**: a row of uppercase labels on the masthead
    line, separated by space or hairlines; the current item in claret.

## Data Visualization

-   **Series**: `--data-1` (claret) for the series that matters, then teal,
    oxford blue, ochre. Everything that is context is `--data-context`.
-   **Lines and marks**: 2px lines, square caps, flat bars with no rounding;
    no gradients, shadows, or 3D.
-   **Axes and gridlines**: horizontal gridlines only, in `--outline-variant`;
    a 1px ink baseline at zero; axis labels in the label font at label size,
    in `--on-surface-variant`. No chart border or background fill.
-   **Labels and annotations**: label series directly at line ends in bold
    label type in the series color (ochre's label in ink); annotations in
    italic body serif with a thin ink leader.
-   **Chart titles**: a `Bitter` 700 headline over a one-line standfirst in grey
    ink, with the source line beneath the chart in small grey type.

## Motion

Minimal, like news that does not perform: a short fade over `--dur-short` with
`--ease-out`, and charts that draw in once. No drifts, bounces, or parallax.

## Don'ts

-   No rounded corners, pills, drop shadows, or glows; `--rounded-full` is 0
    on purpose.
-   No filled cards for key figures or columns — rules separate, fills don't.
-   Don't use the masthead double rule more than once per view, or swap it for
    a thick single bar.
-   Don't set headlines in a light weight or body text in `Bitter`, and don't
    put headlines in all caps.
-   No sans-serif voice, no tabloid red banners, no bright saturated accents
    beyond claret and teal.
-   Don't put teal text on a filled newsprint surface.

## If the User Asks for Dark

Keep the same roles on a night-edition ground: `--background: #1d1a18`,
`--surface-container-low: #26221f`, `--on-surface: #f2e8de`,
`--on-surface-variant: #c2b8ae`, `--primary: #f08aa3` (a lighter claret that
keeps 4.5:1, with `--on-primary: #1d1a18`), `--secondary: #5cbcc4`,
`--tertiary: #7fb0e8`, `--outline: #e8ded4`, `--outline-variant: #4d4845`. The
rules keep their weights; the double rule becomes light ink.
