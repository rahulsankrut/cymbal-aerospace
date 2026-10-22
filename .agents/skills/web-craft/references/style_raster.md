---
name: Raster
slug: raster
register: expressive
mode: light
---

# Raster

## Identity

**North Star: "Grid, Type, Signal."** An International Typographic Style poster
on off-white stock: one heavy grotesk set huge and tight, a strict column grid,
black rules, and a single red. Hierarchy comes from scale and position alone —
no boxes, no shadows, no ornament. Confident, objective, rhythmic — never cold
or corporate.

-   **Mood**: rational, bold, precise, graphic.
-   **Inspired by**: mid-century Swiss typographic posters, European rail
    signage and timetables, and modernist transit wayfinding systems.

## When to Use

-   **Best for**: data stories, urbanism and transit, architecture and design,
    timelines and histories of systems, explainers built around a few strong
    numbers, clean dashboards.
-   **Avoid for**: intimate or sentimental content (letters, memorials,
    weddings), children's content, anything that should feel soft, handmade,
    or luxurious.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f2f2ee;               /* off-white poster stock */
  --surface-container-low: #ffffff;    /* bright white, for an inset panel or input */
  --surface-container: #e6e6e1;        /* light grey, for a rare filled panel */
  --surface-container-high: #dadad4;   /* hover and selected rows */

  /* Ink */
  --on-surface: #111111;               /* near-black: headlines, body, rules */
  --on-surface-variant: #3a3a3a;       /* graphite: captions, secondary text */

  /* Rules */
  --outline: #111111;                  /* the 2px black rule */
  --outline-variant: #bdbdb8;          /* light grey hairlines and gridlines, never text */

  /* Accents */
  --primary: #d01f17;                  /* signal red: the one accent */
  --on-primary: #ffffff;
  --primary-container: #fbe3e1;        /* pale red wash, for a selected state */
  --on-primary-container: #8a120c;
  --secondary: #111111;                /* black: secondary actions, second series */
  --tertiary: #d01f17;                 /* the same red: there is no third accent */
  --error: #b0170f;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #d01f17;                   /* signal red */
  --data-2: #111111;                   /* black */
  --data-3: #1f5fa8;                   /* transit blue */
  --data-4: #00843d;                   /* transit green */
  --data-context: #8a8a85;             /* context series */

  /* Fonts */
  --font-headline: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-label: 'Inter', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;                   /* square everywhere, even tags */

  /* Style effects */
  --rule-heavy: 2px solid var(--outline);
  --rule-hair: 1px solid var(--outline-variant);
  --index-col: 120px;                  /* width of the red index column */
  --index-gap: 24px;                   /* gutter between index column and text */
  --tracking-display: -0.05em;
  --tracking-headline: -0.045em;
}
```

## Color

-   **Proportions**: off-white and black carry the page — over 90%. Red is the
    signal (about 5%): the index column, the primary action, a tag, the series
    that matters. It appears as one or two solid, confident blocks, never as a
    sprinkle of small red details everywhere.
-   **Red text sits only on the page or white.** It holds 4.8:1 on
    `--background` and 5.4:1 on white, but drops under 4.5:1 on the grey
    containers and the pale red wash; there, text is black or
    `--on-primary-container`.
-   **Light grey is never text.** `--outline-variant` is for hairlines and
    gridlines only.
-   **Blue and green appear only in charts and maps**, as transit-line colors,
    never as UI accents.
-   **Fills are rare.** Separate with rules and whitespace; a grey panel is
    only for something that truly must read as a separate object.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Inter | 800 | Push the scale up: display 1.3–1.6× the form's default. Line height 0.9–0.95. Tracking −0.045em (−0.05em at the largest sizes). Lowercase. |
| Subheads | Inter | 700 | Sentence case, tracking −0.02em, line height 1.1. |
| Body | Inter | 400; 600 for emphasis | Line height 1.5. Tracking 0. |
| Labels, kickers, nav | Inter | 600, sentence case | Label size, tracking 0 — plain and small, never uppercase-and-spaced. |
| Key figures | Inter | 800 | Very large, tracking −0.05em, line height 0.9; tabular lining figures (`font-variant-numeric: tabular-nums`). |

One family, many weights: contrast comes from the jump between 800 headlines and
400–600 text, and from size, never from a second typeface or italics. Headlines
are lowercase; labels are sentence case.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Red index column

The opening title block is a two-column grid: a solid red column on the left,
with the headline, kicker, and lede to its right. The red column holds an index
the content already has — the section number, a year, the headline figure — set
huge in white 800 and anchored to the bottom; without one, it stays a solid red
block. Once per view; section openings may repeat it at a smaller scale in
narratives.

```css
.title-block {
  display: grid;
  grid-template-columns: var(--index-col) 1fr;
  column-gap: var(--index-gap);
}
.title-block .index {
  grid-row: span 4;
  display: flex;
  align-items: flex-end;
  background: var(--primary);
  color: var(--on-primary);
  font: 800 4rem/0.9 var(--font-headline);
  letter-spacing: var(--tracking-display);
  padding: var(--space-lg) var(--space-md);
}
```

### 2. Oversized lowercase grotesk

Every headline — the page title, section titles, chart titles — is heavy,
tightly tracked, set close, and lowercase. The size jump to body text is
dramatic; this is the poster voice.

```css
h1, h2 {
  font-family: var(--font-headline);
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: var(--tracking-headline);
  text-transform: lowercase;
}
```

### 3. Hanging grid

Everything below the title hangs on the text column, aligned with the
headline's left edge; the strip under the red column stays empty or carries
small labels the content already has (section names, dates, figure numbers).
This indent is what makes the page read as one grid.

```css
.hang { padding-left: calc(var(--index-col) + var(--index-gap)); }
.hang-label {
  width: var(--index-col);
  margin-left: calc(-1 * (var(--index-col) + var(--index-gap)));
}
```

### 4. Heavy black top rules

A 2px black rule above each key figure, figure, card, and section opens it —
no box, no fill, just the rule and the content beneath. A card is a block of
type under a line.

```css
.ruled { border-top: var(--rule-heavy); padding-top: var(--space-sm); }
```

### 5. Display-weight figures

Key figures are set like headlines: 800, very large, tightly tracked, with a
small 600 label above and a 500 caption below in graphite.

```css
.figure-value {
  font: 800 2.75rem/0.9 var(--font-headline);
  letter-spacing: var(--tracking-display);
  font-variant-numeric: tabular-nums;
}
```

## Composition

-   **Flush-left, grid-locked.** Everything aligns to a strict column grid with
    a ragged right edge; nothing is centered, including titles and button rows.
    This follows — and hardens — the skill's preference for asymmetry.
-   **Big contrast of scale.** A huge headline next to small, plain text;
    generous empty space beside and under the headline is part of the design.
-   **Moderately dense below the title.** Rows of figures and charts pack
    tightly on the grid with even gutters; separation comes from 2px rules and
    space, not fills or shadows.
-   **Dashboards and tools** keep the hanging grid and rules, and narrow the
    red index column to a slim red bar beside the title.

## Components

-   **Buttons**: square. Primary is a red fill with white 700 text. Secondary
    is plain black 700 text with a 2px black underline and no side padding.
    No shadows; hover darkens the fill or thickens the underline.
-   **Key figures**: in a row on the hanging grid, each under a 2px black rule
    — small black label, huge value, graphite caption.
-   **Tags**: a 2px red outline, red 700 text, square corners.
-   **Links**: black text with a 2px red underline; hover turns the text red.
-   **Inputs**: white field, 2px black bottom rule, square; focus turns the
    rule red and adds the focus ring.
-   **Tables**: no vertical lines and no zebra fills. A 2px black rule above the
    header, light grey hairlines between rows, header in 600 sentence case,
    tabular figures right-aligned.
-   **Navigation**: plain 600 labels in a flush-left row; the current item is
    red.

## Data Visualization

-   **Series**: `--data-1` (red) for the series that matters, then black, blue,
    green — like transit lines. Everything that is context is
    `--data-context`.
-   **Lines and marks**: thick, flat lines (3–4px for the main series, 2px for
    others), butt caps, 45° and 90° angles where the data allows; solid bars
    with no rounding. Endpoints as solid squares or white-filled circles with a
    black stroke, like stations. No gradients, glows, or 3D.
-   **Axes and gridlines**: a 2px black baseline; horizontal gridlines only, in
    `--outline-variant`; axis labels in 600 at label size; no chart border.
-   **Labels and annotations**: label series directly at their ends in 700, in
    the series color; no legend boxes.
-   **Chart titles**: lowercase 800 headline voice, under a 2px black rule.

## Motion

Precise and fast: elements slide in a short distance along the grid (from the
left or from below) over `--dur-short` with `--ease-out`, staggered in reading
order. No bounces, springs, or scale effects.

## Don'ts

-   No rounded corners, drop shadows, gradients, or textures.
-   No second typeface, no italics, and no centered titles.
-   No uppercase, widely tracked labels — that is a different style.
-   No second accent color in the UI, and don't spread small red accents
    everywhere; red works as a few solid blocks.
-   Don't set headlines at timid sizes or with default tracking; a small,
    loose headline loses the poster.
-   Don't box content in bordered cards; a rule above is enough.

## If the User Asks for Dark

Keep the same roles on a black poster: `--background: #111111`,
`--on-surface: #f2f2ee`, `--on-surface-variant: #b8b8b2`, `--outline: #f2f2ee`
(the heavy rule turns off-white), `--outline-variant: #3a3a3a`, `--primary:
#ff4a3d` with `--on-primary: #111111` (white on this red falls short of 4.5:1),
`--data-3: #5a9be0`, `--data-4: #2fb36a`, `--data-context: #77776f`.
