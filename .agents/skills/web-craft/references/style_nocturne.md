---
name: Nocturne
slug: nocturne
register: classic
mode: dark
---

# Nocturne

## Identity

**North Star: "The Midnight Observatory."** An astronomical logbook or nocturnal
reading room: deep Prussian-midnight surfaces, warm parchment-ivory type,
burnished celestial brass for actions and focal series, and pale horizon-sky
blue for coordinates and secondary signals. Classical old-style serif headlines
(`EB Garamond`) over a brass deck line meet a clean geometric sans and a crisp
monospace for every number, coordinate, and timestamp. Scholarly, luminous, and
composed — never cold neon, never generic SaaS purple.

-   **Mood**: composed, luminous, scholarly, nocturnal.
-   **Inspired by**: astronomical star charts, observatory logbooks, nocturnal
    scientific atlases, and evening research briefings.

## When to Use

-   **Best for**: science, space, physics, and astronomy; deep-dive technical
    explainers; thoughtful analytics and metrics dashboards.
-   **Avoid for**: loud promotional launches, playful children's content,
    daylight-first civic or clinical forms, anything that wants bright pastel
    cheer.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..700;1,400..600&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: dark;

  /* Page and surfaces: Prussian midnight steps */
  --background: #0a101d;               /* deep midnight slate; also the recessed code/chart well */
  --surface-container-low: #0e1626;    /* barely lifted band or sidebar */
  --surface-container: #111b2e;        /* cards, panels, inputs */
  --surface-container-high: #17243c;   /* hover / active tier, raised menus */

  /* Text */
  --on-surface: #f2ece1;               /* warm parchment ivory: headlines and body */
  --on-surface-variant: #9ba8bf;       /* cool starlight slate: captions, secondary text */

  /* Borders */
  --outline: #384d73;                  /* stronger border: secondary buttons, active frames; never text */
  --outline-variant: #21304d;          /* hairline dividers and card borders */

  /* Accents */
  --primary: #dfaa5b;                  /* celestial brass: primary actions, focal emphasis */
  --on-primary: #0a101d;
  --primary-container: #2b261c;        /* warm brass-tinted dark container */
  --on-primary-container: #f5dcb0;
  --secondary: #687a99;                /* muted slate: icons, baselines; never body text */
  --tertiary: #7cc4e8;                 /* horizon sky: coordinates, secondary signals, links */
  --error: #f27474;                    /* errors only */
  --on-error: #1a0606;

  /* Data series, in order of use */
  --data-1: #dfaa5b;                   /* celestial brass */
  --data-2: #7cc4e8;                   /* horizon sky */
  --data-3: #52d19c;                   /* aurora mint */
  --data-4: #e07a5f;                   /* solar coral */
  --data-context: #4a5d80;             /* context series and baselines */

  /* Fonts */
  --font-headline: 'EB Garamond', serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-label: 'JetBrains Mono', monospace;

  /* Shape */
  --rounded: 0.25rem;
  --rounded-lg: 0.375rem;
  --rounded-full: 9999px;

  /* Style effects */
  --hairline: 1px solid var(--outline-variant);
  --hairline-strong: 1px solid var(--outline);
  --panel-highlight: inset 0 1px 0 rgba(242, 236, 225, 0.05);
  --brass-glow: radial-gradient(circle at 88% 12%, rgba(223, 170, 91, 0.08), transparent 45%);
  --heading-tracking: -0.015em;
  --label-tracking: 0.06em;
  --sky-tint: color-mix(in srgb, var(--tertiary) 12%, transparent);
  --brass-tint: color-mix(in srgb, var(--primary) 14%, transparent);
}
```

## Color

-   **Proportions**: Prussian midnight (`#0a101d` to `#17243c`) and warm
    parchment-ivory text (`#f2ece1`) carry roughly 90% of the view. Celestial
    brass (`#dfaa5b`) is the primary signal (under 6%): the primary button, a
    single italic word in the display title, the focal data series. Horizon sky
    (`#7cc4e8`) marks coordinates, timestamps, and secondary series.
-   **Warmth against cool depth.** The magic of the palette is the temperature
    contrast between the cool midnight-blue ground and the warm parchment-and-brass
    foreground. Never use pure `#000000` or cold `#ffffff`.
-   **Never-text colors**: `--outline` (2.5:1) and `--secondary` (3.9:1) are for
    borders, icons, and chart context only. Secondary text uses
    `--on-surface-variant` (`#9ba8bf`, 7.1:1 on `--background`).
-   **Depth by midnight tiers and top-edge catchlight.** Panels step up from
    `--background` to `--surface-container` with a `1px` `--outline-variant`
    border and a subtle `inset 0 1px 0 rgba(242, 236, 225, 0.05)` top highlight,
    never heavy drop shadows.

## Typography

Role                                 | Family                                                                           | Weight / style                                                        | Size and spacing
------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ----------------
Display, headlines                   | EB Garamond                                                                      | 500 upright roman; 400 italic for a focal term                        | Tracking `--heading-tracking`. Line height 1.06–1.15.
Body                                 | Plus Jakarta Sans                                                                | 400; 600 for inline emphasis                                          | Standard tracking. Line height 1.62 for narrative, 1.5 in dashboards and tools.
Coordinates, timestamps, data labels | JetBrains Mono                                                                   | 500, uppercase                                                        | Label size, tracking `--label-tracking`, in `--on-surface-variant` or `--tertiary`.
Figures, values, code                | EB Garamond 500 for hero stats; JetBrains Mono 500 for dense tables and readouts | `font-variant-numeric: tabular-nums`; hero figures in `--on-surface`. |

Headlines are sentence or title case, never all caps. All caps belong to
monospace data labels, coordinates, and table headers.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies;
use it wherever the artifact has that place. When there is room for only a few,
keep the higher-ranked ones.

### 1. Midnight panels with a starlight top catchlight

Cards, metric tiles, and chart containers sit on `--surface-container` with a
`1px` `--outline-variant` border and a faint inner top-edge highlight so they
feel like precision glass plates against the midnight ground.

```css
.panel {
  background: var(--surface-container);
  border: var(--hairline);
  box-shadow: var(--panel-highlight);
  border-radius: var(--rounded-lg);
  padding: var(--space-lg);
}
```

### 2. Classical old-style serif headline with a celestial-brass deck line

Set the opening title and major section headers in `EB Garamond` (`500` roman,
with `400` italic for a single focal word when appropriate) in warm parchment
ivory, paired with a compact celestial-brass (`--primary`) deck line or epoch
subtitle immediately below.

```css
.title {
  font-family: var(--font-headline);
  font-weight: 500;
  letter-spacing: var(--heading-tracking);
  line-height: 1.08;
  color: var(--on-surface);
}
.deck-brass {
  font-family: var(--font-label);
  font-size: var(--label-size);
  letter-spacing: var(--label-tracking);
  text-transform: uppercase;
  color: var(--primary);
  margin-top: var(--space-xs);
}
```

### 3. Monospace coordinate labels, units, and timestamps

Coordinates, epochs, units, and table headers use `JetBrains Mono` in horizon
sky (`--tertiary`) or starlight slate (`--on-surface-variant`), giving the page
the feel of an observatory instrument or charted atlas. Lead directly with the
title and deck; add a top coordinate or epoch label only when the source carries
real metadata (a date, mission ID, or celestial coordinate).

```css
.coord-label {
  font-family: var(--font-label);
  font-size: var(--label-size);
  letter-spacing: var(--label-tracking);
  text-transform: uppercase;
  color: var(--tertiary);
}
.badge {
  background: var(--sky-tint);
  color: var(--tertiary);
  border: 1px solid color-mix(in srgb, var(--tertiary) 35%, transparent);
  border-radius: var(--rounded);
  padding: var(--space-xs) var(--space-sm);
  font-family: var(--font-label);
  font-size: var(--label-size);
}
```

### 4. Subtle celestial radial wash on the hero header

The page or hero header carries a barely perceptible radial wash of brass light
in the upper corner (`--brass-glow`) over `--background`, suggesting instrument
illumination without reducing text contrast.

```css
.hero-header {
  background-color: var(--background);
  background-image: var(--brass-glow);
}
```

### 5. Recessed midnight wells for code, logs, and canvas plots

Interactive simulations, star maps, and code blocks step back down to
`--background` (`#0a101d`) inside a `--hairline` frame so they read as recessed
observation windows.

```css
.observation-well {
  background: var(--background);
  border: var(--hairline);
  border-radius: var(--rounded);
  padding: var(--space-md);
  font-family: var(--font-label);
  color: var(--on-surface);
}
```

## Composition

-   **Flush-left, structured.** Titles, deck lines, and ledes align to a crisp
    left edge; multi-column views pair a wide primary canvas or narrative column
    with a narrower telemetry/annotation rail.
-   **Calm and uncrowded.** Let the deep Prussian ground breathe around panels
    and charts; use `1px` `--outline-variant` rules to organize dense sections.
-   **Works across narratives and dashboards.** In narratives, lean into `EB
    Garamond` headlines and annotated diagrams; in dashboards and tools, lean
    into `JetBrains Mono` tabular readouts and recessed chart wells.

## Components

-   **Buttons**: 4px radius (`--rounded`), `JetBrains Mono` 500. Primary is a
    celestial brass fill (`--primary`) with midnight text (`--on-primary`).
    Secondary is transparent with a `--hairline-strong` border and ivory text.
-   **Cards and key figures**: midnight panels (treatment 1); mono label on top,
    large `EB Garamond` 500 or `JetBrains Mono` 500 value, and a sky-blue or
    brass note beneath.
-   **Tags and badges**: 4px badge in `--sky-tint` or `--brass-tint` with a
    matching 35% border; reserve for real coordinates, epochs, or data units.
-   **Links**: horizon sky (`--tertiary`), underlined on hover.
-   **Inputs**: `--background` fill, `--hairline-strong` border, 4px radius;
    focus ring in `--primary` (`2px solid`, `2px` offset).
-   **Tables**: no vertical rules; `--hairline` between rows; header cells in
    the mono label voice; numbers right-aligned and tabular.

## Data Visualization

-   **Series**: `--data-1` (celestial brass `#dfaa5b`) for the focal series,
    then `--data-2` (horizon sky `#7cc4e8`), `--data-3` (aurora mint `#52d19c`),
    and `--data-4` (solar coral `#e07a5f`). Context series in `--data-context`.
-   **Lines and marks**: 1.5–2px crisp strokes, small circular markers at key
    events or endpoints, and a soft 10% area fill under a single primary trend
    line when helpful.
-   **Axes and gridlines**: axis labels in `JetBrains Mono`; gridlines in dashed
    or solid `1px` `--outline-variant`.
-   **Annotations**: direct callouts in `JetBrains Mono` with a `1px` brass or
    sky leader line pointing to the anomaly or milestone.

## Motion

Measured and smooth: fades and gentle 6px slides over `--dur-medium` with
`--ease-out`. Avoid bouncy springs or jarring flashes.

## Don'ts

-   No neon purple, hot magenta, or cyberpunk glow effects.
-   No heavy bold weights (`700`+) in `EB Garamond` for long headlines — medium
    (`500`) roman with at most one italic brass word gives the style its poise.
-   No pure `#000000` backgrounds or stark `#ffffff` text.
-   No heavy drop shadows; rely on surface steps and the 1px `--outline-variant`
    border.

## If the User Asks for Light

Keep the observatory-atlas character on warm parchment paper:
`--background: #f6f2e9`, `--surface-container: #efe9dc`,
`--surface-container-high: #e5decb`, `--on-surface: #101829`,
`--on-surface-variant: #4a5568`, `--outline-variant: #d5ccb8`,
`--outline: #8c826d`, `--primary: #9c6514` with `--on-primary: #f6f2e9`,
`--tertiary: #1b5e8a`.
