---
name: Riso
slug: riso
register: expressive
mode: light
---

# Riso

## Identity

**North Star: "Two Inks, Slightly Off."** A risograph print from an indie
studio: fluoro pink and riso blue on warm uncoated paper, a navy third drum for
the words, a flood of yellow now and then. Heavy uppercase grotesque headlines
with the second ink printed a few pixels off, hard offset blocks instead of soft
shadows, a faint halftone dot in the paper. Handmade but deliberate. Never
childish, never messy.

-   **Mood**: curious, upbeat, crafty, confident.
-   **Inspired by**: risograph zines, indie publishers, museum shop posters.

## When to Use

-   **Best for**: science for curious minds, arts and culture, community
    projects and events, education and explainers, small-press or studio
    content.
-   **Avoid for**: formal finance, legal, or medical content, grief or somber
    subjects, luxury brands, dense operational dashboards that need a neutral
    ground.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Work+Sans:ital,wght@0,100..900;1,100..900&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f7f3ea;               /* warm uncoated paper */
  --surface-container-low: #ffffff;    /* bright white stock, for cards */
  --surface-container: #efe8d8;        /* darker paper, for a recessed panel */
  --surface-container-high: #fff8b3;   /* pale yellow stock, the alternate card */

  /* Ink */
  --on-surface: #1d2a5a;               /* navy drum: all body text */
  --on-surface-variant: #3d4775;       /* lighter navy: captions, secondary text */

  /* Rules */
  --outline: #1d2a5a;                  /* navy: 2px block borders and rules */
  --outline-variant: #c3c6d9;          /* pale navy: hairline dividers, never text */

  /* Accents */
  --primary: #006aa8;                  /* riso blue: headlines, links, fills */
  --on-primary: #ffffff;
  --primary-container: #ffe800;        /* yellow flood: highlights, secondary button */
  --on-primary-container: #1d2a5a;
  --secondary: #ff52b4;                /* fluoro pink: fills, offsets, misregistration; never text */
  --tertiary: #d00074;                 /* magenta: kickers, deltas, small emphasis text */
  --error: #c0262d;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #0078bf;                   /* pure riso blue */
  --data-2: #d00074;                   /* magenta */
  --data-3: #1d2a5a;                   /* navy */
  --data-4: #d9531e;                   /* riso orange */
  --data-context: #b4b8cc;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Archivo', sans-serif;
  --font-body: 'Work Sans', sans-serif;
  --font-label: 'Space Mono', monospace;

  /* Shape */
  --rounded: 0.25rem;
  --rounded-lg: 0.5rem;
  --rounded-full: 9999px;

  /* Style effects */
  --misregister: 3px 2px 0 rgb(255 82 180 / 0.85);  /* pink drum printed off-register */
  --ink-border: 2px solid var(--outline);
  --offset-pink: 5px 5px 0 var(--secondary);
  --offset-blue: 5px 5px 0 var(--primary);
  --offset-sm: 3px 3px 0 var(--primary);
  --halftone: radial-gradient(rgb(29 42 90 / 0.07) 1px, transparent 1.2px);
  --halftone-size: 6px 6px;
}
```

## Color

-   **Proportions**: paper and navy carry the page, about 80% of it. Blue is the
    loud voice: headlines, chips, the lead data series. Pink is the second
    ink, seen as offsets, misregistration, and the primary button. Yellow is a
    flood used once or twice per view. Magenta is for small text only.
-   **Pink is never text.** At 2.7:1 on paper it is a fill and shadow color
    only. Text on a pink fill is navy, never white.
-   **Two inks per element.** Each object pairs navy with one accent (a pink
    offset or a blue offset, a yellow fill or a blue fill), never three.
-   **Flat ink.** Colors are solid ink or the paper. No gradients, and no
    transparency except the misregistration and the halftone.
-   Magenta (`--tertiary`) passes 4.5:1 on paper, white, and the pale yellow
    card, but not on `--surface-container` or the yellow flood. Keep it off
    those.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Archivo | 900, uppercase | Push the scale up; tracking −0.02em; line height 1.0–1.05. In `--primary`. |
| Subheads | Archivo | 800, sentence case | Navy, tracking −0.01em. |
| Body | Work Sans | 400; 600 for emphasis | At least 17px for narrative. Line height 1.6. |
| Labels, kickers, tags, nav | Space Mono | 400–700, uppercase | Label size, tracking 0.06–0.08em. Reads like a rubber stamp or a printer's slug. |
| Key figures | Archivo | 900 | Very large, navy, tabular figures. |
| Data, axis labels | Space Mono | 400 | Label size, tabular. |

Headlines shout in uppercase; everything else is calm sentence case. The
contrast comes from a heavy grotesque over small monospaced labels, with Work
Sans as the plain-spoken middle.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Misregistered headline

The display title and section headings print in blue with a pink copy a few
pixels off, as if the second drum slipped. Headlines only: never body, labels,
or figures.

```css
.misregister {
  font-family: var(--font-headline);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: -0.02em;
  color: var(--primary);
  text-shadow: var(--misregister);
}
```

### 2. Offset ink block

Cards, key-figure tiles, the primary container, and the primary button sit on a
hard, unblurred offset of the second ink with a 2px navy border, like a print
pulled slightly out of line. Alternate the offset color between neighbors; the
alternate tile also takes the pale yellow stock.

```css
.ink-block {
  background: var(--surface-container-low);
  border: var(--ink-border);
  border-radius: var(--rounded-lg);
  box-shadow: var(--offset-pink);
  padding: var(--space-lg);
}
.ink-block:nth-child(even) {
  background: var(--surface-container-high);
  box-shadow: var(--offset-blue);
}
```

### 3. Overprint charts

Chart fills (bars, areas, overlapping marks) print like riso inks laid over
each other: flat solid fills that multiply where they overlap, so blue over
magenta turns deep violet. Applies to every chart with filled marks.

```css
.chart .mark {
  fill: var(--data-1);
  mix-blend-mode: multiply;
  stroke: none;
}
.chart .mark.series-2 { fill: var(--data-2); }
```

### 4. Halftone paper

A faint navy dot screen on the page ground, the grain of the drum. Only on the
page background; cards and panels are clean flat stock on top of it.

```css
body {
  background-color: var(--background);
  background-image: var(--halftone);
  background-size: var(--halftone-size);
}
```

### 5. Stamp labels

Kickers, tags, and status chips set in uppercase Space Mono on a solid blue
fill, like an issue number stamped on a cover. Use it for labels the content
already has, not as decoration.

```css
.stamp {
  font-family: var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  background: var(--primary);
  color: var(--on-primary);
  border-radius: var(--rounded-full);
  padding: var(--space-xs) var(--space-sm);
}
```

## Composition

-   **Flush-left poster grid.** Titles, body, and blocks align to a strong left
    edge; key figures sit in a row of equal-height blocks. This follows the
    skill's general preference for asymmetry.
-   **Medium density.** Blocks sit close (gaps of `--space-lg`) but each has
    generous inner padding. Leave room around blocks for their offsets so
    shadows never collide with neighbors.
-   **Separation by objects, not lines.** Content groups are bordered ink
    blocks with offsets. Between sections, use space or a single 2px navy rule.
    Hairlines (`--outline-variant`) appear only inside tables and lists.
-   **Dashboards and tools** keep the misregistered title, ink blocks, and stamp
    labels, but drop the misregistration from small panel headings and use
    the smaller `--offset-sm`.

## Components

-   **Buttons**: small radius, Space Mono label. Primary is a pink fill with a
    navy label and a 3px blue offset; secondary is a yellow fill, or
    transparent with a 2px navy border. Hover shifts the button toward its
    offset (`translate(1px, 1px)`) and shrinks the shadow, as if pressed onto
    the page.
-   **Key figures**: an ink block with a small Space Mono label, a huge Archivo
    900 value in navy, and a short magenta note beneath.
-   **Tags and chips**: blue fill, white `Space Mono` label, fully rounded.
-   **Links**: blue, 600 weight, with a 2px pink underline offset 3px.
-   **Inputs**: white field, 2px navy border, small radius; focus adds the
    focus ring and a small blue offset.
-   **Tables**: a 2px navy rule under the header, hairlines between rows,
    header cells in Space Mono uppercase, and a yellow-flood row for the one
    that matters.
-   **Highlights**: an important phrase in body text can sit on the yellow
    flood (`--primary-container`) in navy, once or twice per view.

## Data Visualization

-   **Series**: `--data-1` (riso blue) for the series that matters, then
    magenta, navy, orange. Context is `--data-context`.
-   **Marks**: flat solid fills that overprint (treatment 3); bars with square tops
    or a small radius; lines 2.5–3px with round caps, thick like a marker. No
    gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in Space Mono, a 2px navy baseline,
    gridlines dashed in `--outline-variant`, and no chart border. The chart
    sits in an ink block if it needs a frame.
-   **Labels and annotations**: label series directly in Space Mono in the
    series color (an orange series takes a navy label); annotations in Work
    Sans with a short navy leader.
-   **Chart titles**: Archivo 800, navy, sentence case, not misregistered.

## Motion

Snappy and physical, like sheets coming off the drum: blocks slide in from a
small offset over `--dur-short` with `--ease-out`, and offsets appear a beat
after their block. Buttons press into their shadow. No bounces, wobbles, or
spinning.

## Don'ts

-   No blurred or soft shadows; every shadow is a hard, solid offset.
-   No pink text, and no white text on pink.
-   No gradients, glassmorphism, or neon glows. Riso is flat ink.
-   Don't misregister body text, labels, numbers, or every heading in a dense
    tool; it reads as a rendering bug.
-   Don't let the halftone run inside cards or behind long text, and don't
    darken it past a faint grain.
-   No rotated or tilted blocks, sticker clutter, or hand-drawn doodles. It is
    handmade but deliberate.
-   Don't stack a third accent on one element (pink offset, blue fill, and
    yellow stock at once).

## If the User Asks for Dark

Print on black stock: `--background: #171c33`, `--surface-container-low:
#20274a`, `--on-surface: #f7f3ea`, `--on-surface-variant: #c6c9de`,
`--outline: #f7f3ea`, `--primary: #5cb8f0` (with `--on-primary: #171c33`),
`--tertiary: #ff6fc0`. Pink and yellow stay as they are. Switch overprint
charts to `mix-blend-mode: screen`, and turn the halftone dot paper-colored at
0.06 opacity.
