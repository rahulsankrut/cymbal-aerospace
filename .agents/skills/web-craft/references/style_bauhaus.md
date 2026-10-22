---
name: Bauhaus
slug: bauhaus
register: expressive
mode: light
---

# Bauhaus

## Identity

**North Star: "Form Follows Function."** A modernist workshop primer or
Bauhaus poster: warm off-white stock, near-black ink, and flat blocks of
primary yellow, red, and blue. Oversized geometric grotesk, thick black borders, and
solid offset shadows in place of soft ones. Bold, raw, and unapologetic — high
contrast, strong geometry, deliberate imperfection; never cute or decorative.

-   **Mood**: bold, direct, constructive, confident.
-   **Inspired by**: Bauhaus posters and primers, brutalist architecture,
    Swiss-school signage, neo-brutalist web design.

## When to Use

-   **Best for**: design and architecture topics, manifestos and opinion
    pieces, explainers that should feel energetic, product and startup
    overviews, workshop and course material, bold data stories, tools that want
    a strong graphic voice.
-   **Avoid for**: grief, health, or other sensitive content; luxury or
    heritage brands; quiet literary reading; anything that should feel soft,
    calm, or intimate.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&family=Inter:wght@100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f5f0e8;               /* warm off-white, like aged paper */
  --surface-container-low: #f2ede5;    /* card and panel fill inside thick borders */
  --surface-container: #eee9e0;        /* a filled panel: forms, sidebars */
  --surface-container-high: #e8e3da;   /* table header band, pressed fills */

  /* Ink */
  --on-surface: #1a1a1a;               /* near-black: text */
  --on-surface-variant: #4a4a4a;       /* captions and secondary text */

  /* Lines */
  --outline: #1a1a1a;                  /* thick borders, rules, offset shadows */
  --outline-variant: #d0cbc3;          /* gridlines and light dividers, never text */

  /* Accents */
  --primary: #1a1a1a;                  /* near-black: primary elements, hover-invert fill */
  --on-primary: #ffffff;
  --primary-container: #ffcc00;        /* signal yellow: CTAs, active states, highlights; never text */
  --on-primary-container: #1a1a1a;
  --secondary: #e63b2e;                /* signal red: blocks, bars, rules; never text */
  --tertiary: #0055ff;                 /* signal blue: links, interactive elements, blocks */
  --error: #cc0000;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #e63b2e;                   /* red */
  --data-2: #0055ff;                   /* blue */
  --data-3: #1a1a1a;                   /* black */
  --data-4: #9a7300;                   /* deep ochre: yellow's stand-in in charts */
  --data-context: #b5afa5;             /* context series */

  /* Fonts */
  --font-headline: 'Space Grotesk', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-label: 'Space Grotesk', sans-serif;

  /* Shape */
  --rounded: 0.125rem;
  --rounded-lg: 0.25rem;
  --rounded-full: 0.75rem;             /* the largest radius; never a pill */

  /* Style effects */
  --border-thick: 3px solid var(--outline);
  --border-medium: 2px solid var(--outline);
  --offset-shadow: 5px 5px 0 var(--outline);
  --offset-shadow-sm: 3px 3px 0 var(--outline);
  --rule-heavy: 6px solid var(--outline);
}
```

## Color

-   **Proportions**: paper and ink carry the page — roughly 75%. Flat color
    blocks take the rest, and they are loud by design: a yellow highlight, a
    blue panel, a red bar. Black plus **one accent per section**; never all
    three primaries fighting in the same block.
-   **Flat and solid only.** Every fill is one solid color. No gradients, tints,
    or transparency on surfaces.
-   **Red is never text, and never sits behind text.** At 3.7:1 on paper and
    4.2:1 under white or black text it fails both as a text color and as a text
    ground. Use it for wordless blocks, chart bars, heavy rules, and the accent
    edge of a section. Errors that need words use `--error`.
-   **Yellow carries ink.** Yellow (`--primary-container`) is a fill with
    near-black text on it (11.5:1) — CTAs, active tabs, highlighted words, a
    featured card. Yellow is never text and never a chart series (1.3:1 on
    paper).
-   **Blue** is the interactive color: links as text on paper and on
    `--surface-container-low` or `--surface-container` (4.6–4.9:1; not on
    `--surface-container-high`), and solid blue blocks with white text (5.6:1).
-   **`--outline-variant` and `--data-context`** are never text.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display | Space Grotesk | 700 | Oversized: at least 3× body, pushed past the foundation scale (narrative up to about 6rem). Tracking −0.03 to −0.02em, line height 0.95–1.05. Uppercase for short titles; sentence case for long ones. |
| Headlines | Space Grotesk | 700 | Sentence case, tracking −0.02em, line height 1.05–1.1. At least 2× body in narrative. |
| Body | Inter | 400; 600 for emphasis | Narrative 17–18px, line height 1.55–1.65. Tools and dashboards 15–16px. |
| Labels, kickers, buttons, nav | Space Grotesk | 600–700, uppercase | 0.75–0.85rem, tracking 0.08–0.12em. |
| Key figures | Space Grotesk | 700 | Very large, tabular figures (`font-variant-numeric: tabular-nums`), tracking −0.03em. |
| Table figures | Inter | 400–500 | Tabular figures, right-aligned. |

Contrast lives in scale as much as weight: massive bold headlines over
regular-weight body. No italics — emphasis comes from weight or a yellow
highlight block.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Thick border with solid offset shadow

A 3px near-black border and a hard 5px block shadow down and to the right, with
no blur. On every container that needs to read as an object: the primary
container, cards, key figure blocks, buttons, form panels, chart frames. This
replaces all soft elevation.

```css
.block {
  border: var(--border-thick);
  border-radius: var(--rounded);
  box-shadow: var(--offset-shadow);
  background: var(--surface-container-low);
  padding: var(--space-lg);
}
```

### 2. Oversized grotesk title with a highlight block

The opening title is huge, bold, tightly tracked, and flush left. One word or
phrase already in it — the key term — sits on a solid yellow block. One
highlight per title; never in body paragraphs.

```css
.title {
  font-family: var(--font-headline);
  font-weight: 700;
  font-size: var(--display-size);
  line-height: 1;
  letter-spacing: -0.03em;
  color: var(--on-surface);
}
.title mark {
  background: var(--primary-container);
  color: var(--on-primary-container);
  padding-inline: var(--space-xs);
  box-decoration-break: clone;
}
```

### 3. One-accent section openings

Each section opening gets a heavy top edge in that section's single accent
(red, blue, yellow, or black), with its kicker label on a solid block. Kicker
blocks are yellow with ink, blue with white, or black with white — in a red
section the edge is red and the kicker block is black. Rotate accents from
section to section.

```css
.section-open {
  --accent: var(--tertiary);  /* or --secondary, --primary-container, --primary */
  border-top: var(--space-sm) solid var(--accent);
  padding-top: var(--space-lg);
}
.section-open .kicker {
  display: inline-block;
  font-family: var(--font-label);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  background: var(--primary);
  color: var(--on-primary);
  padding: var(--space-xs) var(--space-sm);
}
```

### 4. Heavy black rules

Where content is divided without a box — between sections of a long page, above
a row of key figures, under a table header, below a chart title — use a solid
black rule, never a hairline.

```css
.divider { border-top: var(--rule-heavy); margin-block: var(--space-2xl); }
.figure-row { border-top: var(--border-thick); padding-top: var(--space-md); }
```

## Composition

-   **Flush-left and asymmetric — pushed further than usual.** Titles, section
    openings, and grids align to a hard left edge. Pair unequal columns (2:1,
    3:1), let an oversized heading overhang a narrow text column, and let one
    block in a row break the rhythm with a color fill. Never a centered,
    symmetrical layout.
-   **Dense and blocky.** Cards are content-dense; gaps between blocks are
    tight (`--space-md` to `--space-lg`) so the thick borders read as a
    constructed grid. Save large spacing for between sections.
-   **Separation** comes from thick borders, heavy rules, and flat color
    blocks — not tonal shifts or soft shadows. Leave room for offset shadows:
    the gap to a neighbor must be wider than the shadow.
-   **Dashboards and tools** suit the style well: a rigid grid of bordered
    blocks, a yellow active state, figures in large grotesk.

## Components

-   **Buttons**: uppercase label voice, `--border-thick`, `--rounded`, and
    `--offset-shadow-sm`. Primary is a yellow fill with ink text; secondary is
    a paper fill with ink text. Hover inverts to a black fill with white text;
    pressed moves the button into its shadow (shifted 3px, shadow gone).
-   **Cards**: defining treatment 1. In a row of cards, one may be filled solid
    yellow (ink text) or blue (white text) to mark the one that matters.
-   **Key figures**: a bordered block with a small uppercase label, the value
    in very large bold grotesk, and a short caption in `--on-surface-variant`.
-   **Tags**: `--border-medium`, uppercase label, solid fill — blue with white
    text or yellow with ink text; `--rounded`, not pills.
-   **Links**: blue, underlined 2px with a small offset; hover puts the link on
    a yellow block with ink text.
-   **Inputs**: a thick bottom border only, square corners, transparent fill;
    focus turns the border blue and adds the focus ring.
-   **Tables**: header row in the uppercase label voice on
    `--surface-container-high`, a 3px black rule under it, light
    `--outline-variant` lines between rows, no vertical lines; tabular figures.
-   **Navigation and tabs**: uppercase labels in a row; the active one is a
    solid yellow block with a black border.

## Data Visualization

-   **Series**: `--data-1` (red) for the series that matters, then blue, black,
    and ochre. Everything that is context is `--data-context`. Yellow may fill
    a highlighted band behind the marks, never a series.
-   **Marks**: flat, solid bars with square ends, separated by 2px black
    outlines where bars touch; 3px lines with square caps; square point
    markers. No gradients, rounded bars, glows, or 3D.
-   **Axes and gridlines**: a 2px black baseline and left axis; gridlines solid
    1px in `--outline-variant`; axis labels in the uppercase label voice.
-   **Labels and annotations**: label series directly in bold label type rather
    than in a legend; annotations as a small black block with white text and a
    straight 2px leader.
-   **Chart frames**: a chart that stands alone takes defining treatment 1; its
    title sits above in bold grotesk over a heavy rule.

## Motion

Mechanical and snappy, like sliding a block into place: entries slide a short
distance in from the left over `--dur-short` with `--ease-out`, staggered.
Hover lifts a block 2px up and left as its shadow grows; press drops it into
its shadow over `--dur-micro`. No bounces, springs, rotations, blurs, or soft
scale effects.

## Don'ts

-   No soft, blurred, or colored-glow shadows; no glassmorphism or
    transparency. The offset shadow is solid black, down-right only.
-   No pills or large radii, and no 1px borders on cards — thin borders make it
    look like a generic template.
-   No gradients on surfaces, text, or charts.
-   Don't use all three primaries in one block, and never set red or yellow as
    text.
-   Don't center the layout or shrink the headlines — timid scale is the
    fastest way to lose the style.

## If the User Asks for Dark

Invert to ink paper: `--background: #1a1a1a`, `--surface-container-low:
#222222`, `--surface-container-high: #2c2c2c`, `--on-surface: #f5f0e8`,
`--on-surface-variant: #bdb8b0`, `--outline: #f5f0e8` (borders, rules, and
offset shadows go off-white), `--primary: #f5f0e8` with `--on-primary:
#1a1a1a`, `--tertiary: #6b9bff` (links keep 4.5:1; blue blocks now carry ink
text), `--secondary: #ff6a5c`, `--error: #ff6b6b` with `--on-error: #1a1a1a`.
Yellow stays `#ffcc00` with ink text. In charts, `--data-1` and `--data-2` follow red and
blue, `--data-3` becomes `#f5f0e8`, `--data-4` `#ffcc00`, and `--data-context`
`#5c5c5c`.
