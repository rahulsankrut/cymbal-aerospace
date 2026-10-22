---
name: Figure
slug: figure
register: classic
mode: light
---

# Figure

## Identity

**North Star: "The Chart Does the Talking."** An annotated journalistic figure
or data essay: a clean
white page, a reading serif for the story, a heavy grotesk for headlines, and
monospace for every number. Context stays gray, the story gets one color, and
the prose highlights its words in the same color as the line it describes.
Precise, confident, open about sources — never decorated, never cute.

-   **Mood**: rigorous, clear, curious, matter-of-fact.
-   **Inspired by**: newsroom graphics desks, interactive visual-journalism
    essays, and public-research chart books.

## When to Use

-   **Best for**: data stories, explainers with charts, research summaries,
    elections, climate, economics, public-policy analysis, dashboards that
    need to explain as well as report.
-   **Avoid for**: content with no numbers to show, luxury or lifestyle
    brands, poetry and memoir, playful content for children.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:ital,wght@0,400..900;1,400..900&family=Newsreader:ital,opsz,wght@0,6..72,200..800;1,6..72,200..800&family=Roboto+Mono:wght@100..700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #ffffff;               /* clean white page */
  --surface-container-low: #f7f7f7;    /* faint panel: a methods box, a tool sidebar */
  --surface-container: #f2f2f2;        /* chips, secondary fills */
  --surface-container-high: #ececec;   /* bar tracks, hovered rows */

  /* Ink */
  --on-surface: #121212;               /* near-black: headlines, body, annotations */
  --on-surface-variant: #5f5f5f;       /* graphite: decks, axis ticks, source lines */

  /* Rules */
  --outline: #8a8a8a;                  /* input and button borders, never text */
  --outline-variant: #e3e3e3;          /* gridlines and hairlines, never text */

  /* Accents */
  --primary: #121212;                  /* ink: primary button, baselines, stat rules */
  --on-primary: #ffffff;
  --primary-container: #e8e8e8;        /* pressed or selected neutral fill */
  --on-primary-container: #121212;
  --secondary: #1f5fa8;                /* text-safe blue: links, comparison labels */
  --tertiary: #b43c0b;                 /* text-safe story orange: kickers, deltas, story labels */
  --error: #b42318;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #e8590c;                   /* story orange: the one line that matters */
  --data-2: #2f6db5;                   /* comparison blue */
  --data-3: #1b8a6b;                   /* green, only when a third series must be named */
  --data-4: #8e5bb5;                   /* violet, rarely */
  --data-context: #c4c4c4;             /* everything else: gray context lines and bars */

  /* Fonts */
  --font-headline: 'Schibsted Grotesk', sans-serif;
  --font-body: 'Newsreader', serif;
  --font-label: 'Roboto Mono', monospace;

  /* Shape */
  --rounded: 0.25rem;                  /* buttons, inputs: barely softened */
  --rounded-lg: 0;                     /* panels, stat blocks, charts: square */
  --rounded-full: 0.25rem;             /* chips stay tabs, not pills */

  /* Style effects */
  --ink-rule: 1px solid var(--on-surface);
  --hairline: 1px solid var(--outline-variant);
  --grid-dash: 2 3;                    /* stroke-dasharray for gridlines */
  --story-stroke: 3px;
  --compare-stroke: 2px;
  --context-stroke: 1.4px;
  --bar-height: 6px;
  --highlight-1: linear-gradient(transparent 60%, color-mix(in srgb, var(--data-1) 15%, var(--background)) 60%);
  --highlight-2: linear-gradient(transparent 60%, color-mix(in srgb, var(--data-2) 15%, var(--background)) 60%);
}
```

## Color

-   **Proportions**: white and ink are the page — well over 90%. Gray is the
    chart's majority: context series, gridlines, bar tracks. Orange is the
    story (under 5%): one line, one bar, one delta, and the words that name
    it. Blue appears only when there is a real comparison.
-   **One story color per view.** If everything is highlighted, nothing is.
    Series that do not carry the point are `--data-context`, not a rainbow.
-   **Chart orange is never text.** `--data-1` is 3.6:1 on white: fine for
    lines, bars, and dots, too light for words. Labels, deltas, and kickers
    in orange use `--tertiary`; blue labels use `--secondary`.
-   **Gray context never carries meaning alone.** `--data-context` (1.7:1) is
    for background series and tracks the reader is meant to look past;
    anything the reader must find gets a series color and a direct label.
    `--outline` and `--outline-variant` are never text.
-   **Fills are rare.** Separate with ink rules, hairlines, and space; use
    `--surface-container-low` only for a panel that is genuinely aside (a
    methodology note, a tool's controls).

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Schibsted Grotesk | 800 (600–700 for section heads) | Tracking −0.025em, line height 1.05. Sentence case or headline case, never all caps. |
| Deck / subtitle | Newsreader | 400 italic | 1.0–1.1× body, in `--on-surface-variant`. |
| Body | Newsreader | 400; 500 for highlighted phrases | At least 17px for narrative. Line height 1.55–1.65. |
| Chart titles, buttons | Schibsted Grotesk | 600 | Chart titles at subhead size or a step below. |
| Labels, kickers, axes, sources | Roboto Mono | 400–500 | Label size; kickers uppercase with 0.08em tracking; axis ticks and sources in sentence case. |
| Numbers | Roboto Mono | 500 for key values, 400 elsewhere | Key values large with −0.02em tracking; `font-variant-numeric: tabular-nums`. |

Three voices with fixed jobs: the grotesk announces, the serif explains, the
mono measures. A number in a figure, table, chart, or stat is always mono; in
running prose it stays in the serif.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Gray context, one story color

Every chart: the series that make the point get a color and a heavier stroke;
everything else is thin gray behind them. The story line ends in a dot and is
labeled directly at its end, in the matching text-safe color.

```css
.series-context { stroke: var(--data-context); stroke-width: var(--context-stroke); fill: none; }
.series-compare { stroke: var(--data-2); stroke-width: var(--compare-stroke); fill: none; }
.series-story   { stroke: var(--data-1); stroke-width: var(--story-stroke); fill: none; stroke-linejoin: round; }
.series-story-end { fill: var(--data-1); }
.label-story   { fill: var(--tertiary);  font-family: var(--font-label); font-weight: 500; }
.label-compare { fill: var(--secondary); font-family: var(--font-label); font-weight: 500; }
```

### 2. Color-keyed text highlights

Where the prose names a series that a nearby chart shows, the phrase gets a
marker-pen underlay in that series' tint and its text color — the sentence
doubles as the legend. Only for phrases that correspond to a plotted series.

```css
.hl-1 { background: var(--highlight-1); color: var(--tertiary);  font-weight: 500; }
.hl-2 { background: var(--highlight-2); color: var(--secondary); font-weight: 500; }
```

### 3. Mono for every measured value

Key figures, table cells, axis ticks, chart subtitles with units, and source
lines are all in the mono with tabular figures, so numbers line up and read as
data rather than prose.

```css
.figure-value { font-family: var(--font-label); font-weight: 500; font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
.chart-sub, .source { font-family: var(--font-label); font-size: var(--label-size); color: var(--on-surface-variant); }
```

### 4. Ink-ruled stat blocks

Key figures sit under a 1px ink rule rather than in a box: small label, large
mono value, delta in the series' text color. When the value is a share of a
real whole, a thin proportion bar beneath it encodes that share in the series
color.

```css
.stat { border-top: var(--ink-rule); padding-top: var(--space-sm); border-radius: var(--rounded-lg); }
.stat-delta { font-family: var(--font-label); color: var(--tertiary); }
.stat-bar { height: var(--bar-height); background: var(--surface-container-high); margin-top: var(--space-sm); }
.stat-bar > span { display: block; height: 100%; background: var(--data-1); }
```

### 5. Newsroom chart furniture

Every figure: grotesk title, mono subtitle carrying units and range, dashed
hairline gridlines, one solid ink baseline, no frame — and, when the data has
a source, the mono source line sits tight under the plot.

```css
.chart-title { font-family: var(--font-headline); font-weight: 600; }
.gridline { stroke: var(--outline-variant); stroke-width: 1; stroke-dasharray: var(--grid-dash); }
.baseline { stroke: var(--on-surface); stroke-width: 1; }
.chart .source { margin-top: var(--space-xs); }
```

## Composition

-   **Flush-left, article-first.** Title block, deck, and body sit on a
    left-aligned reading column of 60–68ch; charts break out wider than the
    text column, up to the full content width. This follows the skill's
    preference for asymmetry.
-   **Charts are the anchors.** The rhythm alternates prose and figure; key
    figures sit in a row of equal columns directly under the chart they
    summarize.
-   **Airy between, tight within.** Generous space above each section and
    each figure; tight spacing between a chart's title, subtitle, plot, and
    source so they read as one unit. Dashboards run denser on the same rules.
-   **Separation by rules and space**, not cards or shadows: ink rules over
    stats, hairlines between table rows and sections.
-   **Dashboards and tools** keep the flush-left header and ink-ruled stats on
    a tighter grid; the highlight underlay is for narrative prose only.

## Components

-   **Buttons**: `--rounded` corners. Primary is an ink fill with white text;
    secondary is white with an `--outline` border and ink text. Label in the
    grotesk at 600. Hover lightens the ink fill slightly or darkens the
    border; no shadows.
-   **Key figures**: the ink-ruled stat block — mono uppercase label in
    `--on-surface-variant`, value in large mono, delta in `--tertiary` or
    `--secondary` matching its series.
-   **Tags and chips**: `--surface-container` fill, `--on-surface-variant` mono
    text, `--rounded-full` (a squarish tab, not a pill).
-   **Links**: `--secondary`, with a 1px underline offset 2px.
-   **Inputs**: white field, 1px `--outline` border, `--rounded` corners; mono
    for numeric entry. Focus turns the border ink and adds the focus ring.
-   **Tables**: no vertical lines, no zebra fills. Ink rule under the header,
    hairlines between rows; header in mono uppercase; numeric columns
    right-aligned in tabular mono.
-   **Annotations**: short mono text in ink with a thin ink leader line to the
    point it describes.

## Data Visualization

-   **Series**: `--data-1` (orange) for the story, `--data-2` (blue) for a
    single comparison, `--data-3` and `--data-4` only when the content names
    more series. Everything else is `--data-context`.
-   **Lines and marks**: story 3px, comparison 2px, context 1.4px; round
    joins; a filled dot at the story's endpoint. Bars flat and square. No
    gradients, glows, shadows, or 3D.
-   **Axes and gridlines**: tick labels in mono at label size in
    `--on-surface-variant`; gridlines dashed in `--outline-variant`; a single
    solid ink baseline at zero; no y-axis line, no chart border.
-   **Labels and annotations**: label series directly at their ends rather
    than in a legend; gray series can share one "others" label. Annotations
    sit in open space with an ink leader line.
-   **Titles and sources**: grotesk title stating what is measured, mono
    subtitle with units and range, mono source line underneath.

## Motion

Quick and functional: gray context fades in, then the story line draws once
(`stroke-dashoffset` over `--dur-long` with `--ease-out`); stat bars grow from
zero. No bounces, parallax, or looping animation.

## Don'ts

-   No rainbow charts: never give every series its own color when only one or
    two carry the point.
-   No orange text in `--data-1`; use `--tertiary`. No highlight underlay on
    phrases that don't match a plotted series.
-   No numbers in a chart, table, or stat set in the grotesk or serif, and no
    proportional figures in columns.
-   No shadowed or rounded cards, gradients, or tinted page backgrounds; the
    page is white.
-   No boxed legends when direct labels fit, no chart frames, no solid dark
    gridlines.

## If the User Asks for Dark

Keep the same roles on a near-black desk: `--background: #121212`,
`--surface-container-low: #1a1a1a`, `--on-surface: #ececec`,
`--on-surface-variant: #a3a3a3`, `--primary: #ececec` with `--on-primary:
#121212`, `--tertiary: #ff8a4c`, `--secondary: #7fb0ea`, `--data-1: #ff7a33`,
`--data-2: #5b93d6`, `--data-context: #4a4a4a`, `--outline-variant: #2e2e2e`.
The ink rule turns light with `--on-surface`; the highlight underlays mix
toward the dark background on their own.
