---
name: Aurora
slug: aurora
register: classic
mode: dark
---

# Aurora

## Identity

**North Star: "Calm Under Northern Skies."** A calm, fatigue-free
dark interface: soothing mineral-slate surfaces, mist-white typography, glacier
cyan for actions and primary series, and soft aurora sage for positive deltas
and secondary signals. Clean sans headings paired with readable geometric body
copy and tabular monospace readouts. Approachable, composed, and modern — never
harsh neon, never sterile black-and-purple.

-   **Mood**: calm, composed, modern, reassuring.
-   **Inspired by**: Scandinavian dark-mode interfaces, climate and energy
    monitors, personal finance and wellness dashboards, and ambient nocturnal
    tools.

## When to Use

-   **Best for**: monitoring and live-status dashboards, market and trading
    screens, sleep and night-time tracking, energy and climate monitoring, and
    developer or technical tools.
-   **Avoid for**: formal historical or literary manuscripts, loud arcade games,
    ceremonial luxury invitations, anything meant to feel antique or paper-bound.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: dark;

  /* Page and surfaces: deep oceanic slate steps */
  --background: #0c1214;               /* deep oceanic slate; also the recessed code/chart well */
  --surface-container-low: #111a1e;    /* barely lifted band or sidebar */
  --surface-container: #152024;        /* cards, panels, inputs */
  --surface-container-high: #1c2a30;   /* hover / active tier, raised menus */

  /* Text */
  --on-surface: #edf3f5;               /* soft mist white: headlines and body */
  --on-surface-variant: #94a8b0;       /* sea-glass grey: captions, secondary text */

  /* Borders */
  --outline: #38515c;                  /* stronger border: secondary buttons; never text */
  --outline-variant: #213138;          /* hairline dividers and card borders */

  /* Accents */
  --primary: #63c7d6;                  /* glacier cyan: primary action, active states, focus */
  --on-primary: #081214;
  --primary-container: #163840;        /* deep cyan-slate container */
  --on-primary-container: #c7f0f7;
  --secondary: #5d7882;                /* muted slate: icons, baselines; never body text */
  --tertiary: #87d69b;                 /* aurora sage: positive deltas, healthy status, second accent */
  --error: #f27474;                    /* errors only */
  --on-error: #1a0606;

  /* Data series, in order of use */
  --data-1: #63c7d6;                   /* glacier cyan */
  --data-2: #87d69b;                   /* aurora sage */
  --data-3: #e8b954;                   /* warm amber */
  --data-4: #f08c70;                   /* coral clay */
  --data-context: #415861;             /* context series and baselines */

  /* Fonts */
  --font-headline: 'Instrument Sans', sans-serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-label: 'Geist Mono', monospace;

  /* Shape */
  --rounded: 0.5rem;                   /* 8px buttons and inputs */
  --rounded-lg: 0.75rem;               /* 12px cards and panels */
  --rounded-full: 9999px;

  /* Style effects */
  --hairline: 1px solid var(--outline-variant);
  --hairline-strong: 1px solid var(--outline);
  --panel-gradient: linear-gradient(180deg, #162226 0%, #111a1e 100%);
  --heading-tracking: -0.025em;
  --label-tracking: 0.06em;
  --sage-tint: color-mix(in srgb, var(--tertiary) 13%, transparent);
  --cyan-tint: color-mix(in srgb, var(--primary) 13%, transparent);
}
```

## Color

-   **Proportions**: oceanic slate (`#0c1214` to `#1c2a30`) and mist-white text
    (`#edf3f5`) carry roughly 90% of the view. Glacier cyan (`#63c7d6`) is the
    primary signal (under 6%): primary buttons, active tabs, focus rings, and
    the primary data series. Aurora sage (`#87d69b`) marks positive trends,
    healthy states, and the secondary series.
-   **Mineral warmth, zero glare.** Because every dark surface has a subtle
    blue-green mineral undertone rather than stark `#000000`, high-density data
    and long sessions remain easy on the eyes.
-   **Never-text colors**: `--outline` (2.6:1) and `--secondary` (3.9:1) are for
    borders, icons, and chart context only. Secondary text uses
    `--on-surface-variant` (`#94a8b0`, 7.2:1 on `--background`).

## Typography

Role                              | Family                                                                     | Weight / style                        | Size and spacing
--------------------------------- | -------------------------------------------------------------------------- | ------------------------------------- | ----------------
Display, headlines                | Instrument Sans                                                            | 600 (700 for compact subheads)        | Tracking `--heading-tracking`. Line height 1.08–1.16.
Body                              | Plus Jakarta Sans                                                          | 400; 600 for inline emphasis          | Standard tracking. Line height 1.6 for narrative, 1.5 in dashboards and tools.
Data labels, table headers, units | Geist Mono                                                                 | 500, uppercase                        | Label size, tracking `--label-tracking`, in `--on-surface-variant`.
Figures, values, code             | Instrument Sans 600 for hero metrics; Geist Mono 500 for tables and deltas | `font-variant-numeric: tabular-nums`. |

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies;
use it wherever the artifact has that place.

### 1. Tonal mineral panels with a soft vertical gradient

Cards, metric tiles, and chart containers sit on `--panel-gradient` (`#162226`
to `#111a1e`) inside a `1px` `--outline-variant` border at `12px` radius
(`--rounded-lg`). No heavy drop shadows; the gentle vertical luminance shift
gives panels a tactile, calm presence.

```css
.panel {
  background: var(--panel-gradient);
  border: var(--hairline);
  border-radius: var(--rounded-lg);
  padding: var(--space-lg);
}
```

### 2. Crisp grotesk headlines and monospace data labels

Lead directly with a tightly tracked `Instrument Sans` 600 headline and a calm
sea-glass grey (`--on-surface-variant`) subtitle or lede. Use `Geist Mono` for
card labels, table column headers, units, and axis ticks.

```css
.title {
  font-family: var(--font-headline);
  font-weight: 600;
  letter-spacing: var(--heading-tracking);
  line-height: 1.1;
  color: var(--on-surface);
}
.data-label {
  font-family: var(--font-label);
  font-size: var(--label-size);
  letter-spacing: var(--label-tracking);
  text-transform: uppercase;
  color: var(--on-surface-variant);
}
```

### 3. Aurora sage deltas and inline status indicators

Positive deltas, on-track indicators, and table status cells use aurora sage
(`--tertiary`) or a compact sage tint (`--sage-tint`) inside the metric card or
table row they describe — never as a decorative header pill.

```css
.status-chip {
  background: var(--sage-tint);
  color: var(--tertiary);
  border: 1px solid color-mix(in srgb, var(--tertiary) 35%, transparent);
  border-radius: var(--rounded);
  padding: 2px var(--space-sm);
  font-family: var(--font-label);
  font-size: var(--label-size);
}
```

### 4. Tabular metric tiles

Key figures pair a `Geist Mono` uppercase label above a large `Instrument Sans`
600 tabular number, with a `Geist Mono` delta line in `--tertiary` beneath.

```css
.metric-value {
  font-family: var(--font-headline);
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  letter-spacing: var(--heading-tracking);
  color: var(--on-surface);
}
.metric-delta {
  font-family: var(--font-label);
  font-size: var(--label-size);
  color: var(--tertiary);
}
```

### 5. Recessed slate wells for inputs, code, and interactive tracks

Inputs, sliders, and code blocks step down to `--background` (`#0c1214`) with a
`1px` `--outline-variant` border so interactive controls feel cleanly recessed.

```css
.well {
  background: var(--background);
  border: var(--hairline);
  border-radius: var(--rounded);
  padding: var(--space-md);
}
```

## Composition

-   **Flush-left, modular grid.** Built for multi-panel dashboards, trackers,
    and tools as well as clean technical explainers.
-   **Softly rounded (`8px`–`12px`), never sharp or bubbly.** Gives tools and
    dashboards a human, approachable feel while keeping tabular discipline.

## Components

-   **Buttons**: `8px` radius (`--rounded`), `Geist Mono` or `Instrument Sans`
    600. Primary is a glacier cyan fill (`--primary`) with dark slate text
    (`--on-primary`). Secondary is transparent with `--hairline-strong` and
    mist-white text.
-   **Cards and key figures**: mineral gradient panels (treatment 1).
-   **Links**: glacier cyan (`--primary`), underlined on hover.
-   **Tables**: no vertical rules; `--hairline` between rows; header cells in
    `Geist Mono` uppercase; numbers right-aligned and tabular.

## Data Visualization

-   **Series**: `--data-1` (glacier cyan `#63c7d6`) for the primary series,
    `--data-2` (aurora sage `#87d69b`) for the secondary series, `--data-3`
    (warm amber `#e8b954`), and `--data-4` (coral clay `#f08c70`). Context
    series in `--data-context`.
-   **Lines and marks**: 2px smooth strokes, subtle 12% area fill under primary
    trend lines, and bars with `3px` top radius.
-   **Axes and gridlines**: `Geist Mono` tick labels; `1px` `--outline-variant`
    horizontal gridlines.

## Motion

Smooth and unhurried: fades and short slides over `--dur-short` with
`--ease-out`.

## Don'ts

-   No neon purple, hot pink, or harsh `#000000` backgrounds.
-   No heavy drop shadows; rely on `--panel-gradient` and `1px`
    `--outline-variant` borders.
-   Don't add a logo badge next to the page title or place decorative category
    kickers and simulated "Live / Active" status pills in the page header.

## If the User Asks for Light

Keep the cool Nordic mineral palette on pale sea-mist paper:
`--background: #f3f7f8`, `--surface-container-low: #ffffff`,
`--surface-container: #e8eff1`, `--surface-container-high: #dce6e9`,
`--on-surface: #0f1c20`, `--on-surface-variant: #485e66`,
`--outline-variant: #cfdde2`, `--outline: #7b949e`, `--primary: #0e6f80` with
`--on-primary: #ffffff`, `--tertiary: #1f7a4c`.
