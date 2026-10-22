---
name: Sonnet
slug: sonnet
register: expressive
mode: light
---

# Sonnet

## Identity

**North Star: "Ink, Candlelight, and Gilt Edges."** A cloth-bound volume of the
Romantic poets: aged ivory paper, iron-gall ink, deep oxblood, and antique gold.
Italic old-style serifs, gilt hairlines, and the calm symmetry of a printed
book. Tender, literary, unhurried — never sentimental or saccharine.

-   **Mood**: literary, romantic, quiet, timeless.
-   **Inspired by**: cloth-bound Romantic poetry volumes, fine-press collector
    editions, and 19th-century letterpress books.

## When to Use

-   **Best for**: poetry and literature, letters and memoir, literary history,
    weddings and anniversaries, heartfelt personal stories, reading guides.
-   **Avoid for**: dense dashboards and data tools, technical or product
    content, anything urgent, playful, or aimed at young children.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Crimson+Pro:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f5efe0;               /* aged ivory paper */
  --surface-container-low: #f8f3e7;    /* a lighter leaf, for inset panels */
  --surface-container: #ece3cf;        /* parchment, for a rare filled panel */
  --surface-container-high: #e4d8bf;

  /* Ink */
  --on-surface: #1f1a17;               /* iron-gall black */
  --on-surface-variant: #4a3f38;       /* faded ink: captions, secondary text */

  /* Rules */
  --outline: #a8843f;                  /* gilt: rules and frames, never text */
  --outline-variant: #d8c7a3;          /* pale gilt: hairline dividers */

  /* Accents */
  --primary: #6b1424;                  /* oxblood */
  --on-primary: #f5efe0;
  --primary-container: #efe0dc;
  --on-primary-container: #4a0d18;
  --secondary: #2f4a3a;                /* hunter green: quotations, tags */
  --tertiary: #a8843f;                 /* antique gold: ornament only */
  --error: #9b2c1f;
  --on-error: #f5efe0;

  /* Data series, in order of use */
  --data-1: #6b1424;                   /* oxblood */
  --data-2: #2f4a3a;                   /* hunter green */
  --data-3: #a8843f;                   /* antique gold */
  --data-4: #3d5a73;                   /* slate blue */
  --data-context: #b9ad9c;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Cormorant Garamond', serif;
  --font-body: 'Crimson Pro', serif;
  --font-label: 'Cormorant Garamond', serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 9999px;

  /* Style effects */
  --gilt-rule: 1px solid var(--outline);
  --gilt-frame-inset: 5px;
  --paper-vignette: inset 0 0 90px rgb(120 90 40 / 0.16);
}
```

## Color

-   **Proportions**: ivory and ink carry the page — roughly 90% of what the
    reader sees. Oxblood is the signal (under 5%): the title's emphasis, drop
    caps, the primary action, the data series that matters. Gold is
    ornament only: rules, frames, the occasional small mark.
-   **Gold is never text.** At 3:1 on ivory it is fine for rules and chart
    lines but fails as text. Labels that need warmth use oxblood.
-   **Green** is the quiet second voice: quotations, epigraphs, tags, and the
    second data series.
-   **Fills are rare.** Separate with gilt rules and space; use
    `--surface-container` only for a panel that truly needs to read as a
    separate object (a form, a sidebar of notes).

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Cormorant Garamond | 500 italic (600 for small headings) | Step up the scale: Cormorant's small x-height reads small. Tracking 0 to −0.005em. |
| Body | Crimson Pro | 400; 400 italic for emphasis | At least 18px for narrative. Line height 1.65–1.75. |
| Labels, kickers, nav | Cormorant Garamond | 600 roman, uppercase | 0.75–0.85rem, tracking 0.14–0.16em — reads as small caps. |
| Quotations, epigraphs | Cormorant Garamond | 400–500 italic | 1.15–1.25× body, in `--secondary`. |
| Figures | Crimson Pro | 400 | Old-style figures in running text (`font-variant-numeric: oldstyle-nums`); lining tabular figures in tables and charts. |

Headlines are sentence case or title case, never all caps. Weight contrast
comes from a large italic display face over small, tracked, upright labels.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Gilt double frame

A thin gold rule with a second rule inset 5px. Frames the opening title block,
or the single most important container in a view. One per view — it marks the
place of honor, so it loses meaning when repeated.

```css
.gilt-frame {
  border: var(--gilt-rule);
  outline: var(--gilt-rule);
  outline-offset: calc(-1 * var(--gilt-frame-inset));
  padding: var(--space-xl);
}
```

### 2. Drop cap

An oxblood initial on the opening paragraph, and on the first paragraph of each
major section in a narrative. Not in dashboards or tools, and never on more than
one paragraph per section.

```css
.drop-cap::first-letter {
  float: left;
  font-family: var(--font-headline);
  font-weight: 600;
  font-size: 3.6em;
  line-height: 0.85;
  padding: 0.06em 0.08em 0 0;
  color: var(--primary);
}
```

### 3. Gilt hairline rules

Gold hairlines take the place of boxes: under a section title, above and below a
row of key figures, between entries in a list. A card is a value held between
two rules, not a filled rectangle.

```css
.ruled { border-block: var(--gilt-rule); padding-block: var(--space-md); }
.section-title { border-bottom: 1px solid var(--outline-variant); padding-bottom: var(--space-sm); }
```

### 4. Verse block

When the content has a quotation, epigraph, or a line worth lingering on: italic
display serif in green, with a gold rule on its left. Only for words the content
already contains — never invent a quote to fill one.

```css
.verse {
  font-family: var(--font-headline);
  font-style: italic;
  font-size: 1.2em;
  line-height: 1.5;
  color: var(--secondary);
  border-left: var(--gilt-rule);
  padding-left: var(--space-md);
  max-width: 36ch;
}
```

### 5. Aged-paper vignette

A faint warm darkening at the edges of the page or the opening panel, as if the
paper has aged at its margins. Barely visible; never on cards.

```css
.page { box-shadow: var(--paper-vignette); }
```

## Composition

-   **Symmetry is the point.** Title blocks, section openings, key-figure rows,
    and button groups are centered on the page's axis — the calm of a title
    page. This overrides the general preference for asymmetry.
-   **Body text is not centered.** Paragraphs sit left-aligned in a centered
    measure of 60–68ch.
-   **Airy.** Generous margins and space between sections. Separation comes from
    space and gilt rules, not fills or shadows.
-   **Dashboards and tools** keep a centered header and gilt rules, but their
    grids are left-aligned and denser; skip drop caps and the vignette.

## Components

-   **Buttons**: square corners. Primary is an oxblood fill with ivory text;
    secondary is an oxblood outline on transparent. Label in `--font-label`
    (uppercase, tracked). Hover darkens the fill or fills the outline; no
    shadows.
-   **Key figures**: centered, held between gilt rules — a small tracked label
    in oxblood, the value in large italic display serif, a short italic caption
    in faded ink.
-   **Tags**: a 1px green outline, green tracked label, fully rounded.
-   **Links**: oxblood, with a gold underline offset 3px.
-   **Inputs**: a transparent field with an ink hairline underneath; focus turns
    the line oxblood and adds the focus ring.
-   **Tables**: no vertical lines. Gold hairlines under the header and between
    row groups; header cells in the label voice; lining tabular figures.
-   **Navigation and contents**: centered labels separated by middots (·).

## Data Visualization

-   **Series**: `--data-1` (oxblood) for the series that matters, then green,
    gold, slate. Everything that is context is `--data-context`.
-   **Lines and marks**: 1.5–2px lines, square line caps, small filled circles
    at endpoints. No gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in `--font-label` at label size;
    gridlines dotted in `--outline-variant`; no chart border.
-   **Labels and annotations**: label lines directly at their ends in italic
    body serif rather than in a legend; annotations in italic with a thin ink
    leader line.
-   **Chart titles**: display serif, with a gilt hairline beneath.

## Motion

Slow and quiet, like turning a page: fade in with a small upward drift over
`--dur-long` with `--ease-out`. No bounces, springs, or scale effects.

## Don'ts

-   No script or handwriting fonts.
-   No rounded cards, drop shadows, or glows; the vignette is the only shadow.
-   No more than one gilt double frame per view, and no more than one drop cap
    per section.
-   Don't center long paragraphs, and don't set body text in Cormorant.

## If the User Asks for Dark

Keep the same roles on a candlelit ground: `--background: #1c1714`,
`--on-surface: #efe6d4`, `--on-surface-variant: #c4b8a4`, `--primary: #d98a95`
(a lighter oxblood that keeps 4.5:1), `--outline: #c9a35a`, `--secondary:
#8fb39b`. Drop the vignette.
