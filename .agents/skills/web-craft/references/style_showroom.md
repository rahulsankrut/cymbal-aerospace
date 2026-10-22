---
name: Showroom
slug: showroom
register: classic
mode: light
---

# Showroom

## Identity

**North Star: "Quietly Premium."** A sunlit industrial-design showroom or
product showcase: cool off-white, near-black text, one confident blue. Big,
tightly tracked headlines, centered compositions, large rounded tiles, and lots
of air. No borders, no ornament: the content is the hero and nothing competes
with it. Assured and polished, never flashy or salesy.

-   **Mood**: calm, precise, premium, confident.
-   **Inspired by**: industrial-design showrooms, flagship hardware launch
    pages, consumer-technology showcases, and interactive product feature tours.

## When to Use

-   **Best for**: product and how-it-works explainers, focused tools and
    calculators, onboarding and setup guides, feature overviews, launch or
    spec summaries.
-   **Avoid for**: literary, historical, or heritage content, dense
    multi-panel dashboards, anything that should feel handmade, raw, or
    playful.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@100..900&family=Inter:wght@100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #fbfbfd;               /* cool off-white page */
  --surface-container-low: #f5f5f7;    /* the tile: key figures, panels, bands */
  --surface-container: #e8e8ed;        /* quiet fills: tracks, secondary buttons; never under gray text */
  --surface-container-high: #dcdce1;   /* pressed and selected fills */

  /* Ink */
  --on-surface: #1d1d1f;               /* near-black: headlines and body */
  --on-surface-variant: #6e6e73;       /* gray: ledes, captions, labels */

  /* Rules */
  --outline: #d2d2d7;                  /* input and control edges, never text */
  --outline-variant: #e5e5ea;          /* hairline dividers and gridlines, never text */

  /* Accents */
  --primary: #006bd6;                  /* the one confident blue: actions, links */
  --on-primary: #ffffff;
  --primary-container: #e8f1fd;        /* pale blue: chips, selected rows */
  --on-primary-container: #0058b0;
  --secondary: #bf4800;                /* burnt orange: eyebrows ("New"), the second series */
  --tertiary: #1d1d1f;                 /* graphite fill: tooltips, selected segment */
  --error: #d70015;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #006bd6;                   /* blue */
  --data-2: #bf4800;                   /* burnt orange */
  --data-3: #248a3d;                   /* green */
  --data-4: #8944ab;                   /* purple */
  --data-context: #aeaeb2;             /* context series */

  /* Fonts */
  --font-headline: 'Inter Tight', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-label: 'Inter', sans-serif;

  /* Shape */
  --rounded: 9999px;                   /* buttons and controls are pills */
  --rounded-lg: 1.25rem;               /* 20px tiles */
  --rounded-full: 9999px;

  /* Style effects */
  --headline-tracking: -0.035em;       /* display headlines */
  --figure-tracking: -0.03em;          /* key-figure values */
  --tile-shadow-hover: 0 8px 28px rgb(0 0 0 / 0.08);  /* clickable tiles on hover only */
  --chevron: " \203A";                 /* the › after text links */
}
```

## Color

-   **Proportions**: off-white, tile gray, and near-black are about 95% of the
    page. Blue is the signal (under 5%): the primary action, links, the
    series that matters, the active state. Orange appears once or twice per
    view at most, as an eyebrow or the second series.
-   **One blue.** Never introduce a second blue or tint the page blue; the
    pale `--primary-container` is for chips and selection only.
-   **Gray text stays on light ground.** `--on-surface-variant` passes on
    `--background` and on tiles (`--surface-container-low`) but not on
    `--surface-container` or darker; put captions only on the first two.
    `--outline` and `--outline-variant` are never text.
-   **Text on graphite** (`--tertiary`) is `--background`.
-   **Separation is tonal.** Tiles and bands are a step of gray against the
    page; there are no borders on containers.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Inter Tight | 700 (600 for small headings) | Push the display size large. Tracking `--headline-tracking` (−0.035em) on display, −0.02em on section headings. Line height 1.05–1.1. |
| Body, ledes | Inter | 400; 500 for inline emphasis | Ledes one step above body in `--on-surface-variant`. Line height 1.5–1.6. |
| Labels, eyebrows, nav | Inter | 500, sentence case | Label size, tracking 0 — no uppercase, no letter-spacing. |
| Key figures | Inter Tight | 600–700 | Large, tracking `--figure-tracking`; units in the same face at about half size. |
| Figures in tables and charts | Inter | 400–500 | `font-variant-numeric: tabular-nums`. |

Headlines are sentence case. Weight contrast comes from a heavy, tightly tracked
headline over regular gray body text. Labels are quiet sentence-case text, not
tracked caps.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Centered headline stack

The opening title block and each major section opening: a heavy, tightly
tracked headline on the page's axis with a gray lede beneath it in a narrow
centered measure. The tight tracking at large size is the style's voice.

```css
.headline-stack { text-align: center; padding-block: var(--space-2xl) var(--space-xl); }
.headline-stack h1, .headline-stack h2 {
  font-family: var(--font-headline);
  font-weight: 700;
  letter-spacing: var(--headline-tracking);
  line-height: 1.05;
  color: var(--on-surface);
}
.headline-stack .lede {
  color: var(--on-surface-variant);
  max-width: 48ch;
  margin: var(--space-md) auto 0;
}
```

### 2. Borderless rounded tiles

Key figures, panels, chart containers, and the primary container of a tool
sit on 20px-radius tiles one gray step off the page, with no border and no
resting shadow. Key-figure tiles center their content: label, big figure,
caption.

```css
.tile {
  background: var(--surface-container-low);
  border-radius: var(--rounded-lg);
  padding: var(--space-xl) var(--space-lg);
  border: 0;
}
.tile.figure { text-align: center; }
.tile.figure .value {
  font-family: var(--font-headline);
  font-weight: 700;
  letter-spacing: var(--figure-tracking);
  line-height: 1.1;
}
.tile.figure .caption { color: var(--on-surface-variant); font-weight: 500; }
```

### 3. Pill action with chevron link

Wherever the content has actions: the primary is a blue pill; the secondary
is plain blue text with a trailing chevron, not a second button. Centered
under the headline stack or a tile.

```css
.btn-primary {
  background: var(--primary);
  color: var(--on-primary);
  border-radius: var(--rounded);
  font: 500 0.875rem/1 var(--font-label);
  padding: var(--space-sm) var(--space-lg);
  border: 0;
}
.link-more { color: var(--primary); font-weight: 500; text-decoration: none; }
.link-more::after { content: var(--chevron); }
```

### 4. Tonal section bands

In narratives, major sections alternate full-width between the page color
and the tile gray instead of being divided by rules. Tiles inside a gray band
switch to `--background` so they still read as a step.

```css
.band { padding-block: var(--space-2xl); }
.band.alt { background: var(--surface-container-low); }
.band.alt .tile { background: var(--background); }
```

## Composition

-   **Centered on the axis.** Title blocks, section openings, key-figure
    tiles, and button rows are centered — the poise of a product page. This
    overrides the general preference for asymmetry.
-   **Body text is not centered** beyond a short lede. Longer paragraphs sit
    left-aligned in a centered measure of 60–68ch.
-   **Airy.** Generous vertical space between sections (`--space-2xl`), roomy
    padding inside tiles, and wide gutters between them.
-   **Separation by tone and space**: tiles, bands, and whitespace — no
    borders, rules, or resting shadows around containers.
-   **Dashboards and tools** keep the centered header, but their tile grids
    are flush-left and denser (`--space-md` gaps); skip the bands. Tile sizes
    can vary within the grid — a wide tile beside two narrow ones.

## Components

-   **Labels above headings** (when used): one short sentence-case line in burnt
    orange (`--secondary`), no tracking.
-   **Buttons**: pills. Primary is a blue fill with white text; secondary is
    a chevron text link, or a `--surface-container` pill with near-black
    text when it must be a button. Hover darkens the fill slightly; no
    shadow on buttons.
-   **Key figures**: a centered tile — small gray label, big tight figure in
    near-black, a gray caption beneath. The figure is never blue.
-   **Chips**: pale blue (`--primary-container`) pill,
    `--on-primary-container` text, 500 weight, sentence case.
-   **Links**: blue, no underline at rest, underline on hover.
-   **Inputs**: pill-shaped (or 12px-radius for multi-line) field on
    `--background` with a 1px `--outline` edge; focus swaps the edge to blue
    with the focus ring.
-   **Segmented controls and toggles**: a `--surface-container` track with a
    `--background` thumb or selected segment; switches go blue when on.
-   **Tables**: no vertical lines, `--outline-variant` hairlines between rows,
    gray 500-weight header, tabular figures, generous row height.
-   **Clickable tiles** lift with `--tile-shadow-hover` on hover; static
    tiles never carry a shadow.

## Data Visualization

-   **Series**: `--data-1` (blue) for the series that matters, then orange,
    green, purple. Everything else is `--data-context`.
-   **Marks**: 2–3px lines with round caps; bars with rounded top corners
    (4–6px); a single large dot on the current or final value. A soft
    single-hue area fill under a line at low opacity is fine; no 3D or
    multi-color gradients.
-   **Axes and gridlines**: minimal. Gridlines in `--outline-variant`,
    horizontal only; axis labels in `--on-surface-variant` at label size; no
    axis lines or chart border.
-   **Labels**: label series directly at their ends in 500 weight; the
    headline number above the chart in the key-figure voice.
-   **Containers**: charts sit on a tile, with a sentence-case title in the
    headline face.

## Motion

Smooth and precise: fade in with a short upward rise over `--dur-long` with
`--ease-out`; tiles may scale from 0.98 to 1 as they enter. Hover lifts use
`--dur-short`. No bounces, springs, or parallax.

## Don'ts

-   No borders around tiles or cards, and no resting drop shadows; it should
    never look like a bordered template card.
-   No uppercase tracked labels — Showroom labels are sentence case.
-   No loose headline tracking or light headline weights; a 400-weight,
    default-tracked headline instantly looks generic.
-   No gradients on buttons or backgrounds, no second accent blue, no colored
    page tints.
-   No small radii on tiles (under 16px) and no square buttons.
-   Don't crowd tiles edge to edge or shrink the space between sections; the
    air is what makes it premium.

## If the User Asks for Dark

Keep the same roles on black: `--background: #000000`,
`--surface-container-low: #1c1c1e`, `--surface-container: #2c2c2e`,
`--on-surface: #f5f5f7`, `--on-surface-variant: #a1a1a6`, `--primary:
#2997ff` with `--on-primary: #000000`, `--secondary: #ff8a3d`,
`--outline-variant: #38383a`. Tiles become the `#1c1c1e` step; drop the
hover shadow in favor of a slightly lighter fill.
