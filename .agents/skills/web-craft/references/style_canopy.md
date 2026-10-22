---
name: Canopy
slug: canopy
register: classic
mode: light
---

# Canopy

## Identity

**North Star: "Under the Garden Canopy."** A kitchen-garden and
permaculture almanac in late afternoon: warm topsoil and loam cream layers,
canopy green, harvest ochre, and a single pale-leaf highlight card. Anchored by
a compact 12-month phenology / seasonal window strip (`J F M A M J J A S O N D`)
or step rhythm bar in monospace, soft 16px organic card corners, and a warm
editorial serif over a friendly rounded sans. Calm, grounded, and knowledgeable —
never rustic kitsch.

-   **Mood**: grounded, seasonal, approachable, quietly knowledgeable.
-   **Inspired by**: permaculture and kitchen-garden almanacs, heirloom seed
    catalogs, seasonal food and sustainability journals, natural-materials craft.

## When to Use

-   **Best for**: gardening, agriculture, and botany; food, cooking, and
    seasonal recipes; nature, ecology, and sustainability; health, nutrition,
    and wellbeing; community and family guides; personal trackers, planners, and
    gentle how-to tools.
-   **Avoid for**: high-frequency financial trading consoles, urgent incident
    dashboards, nightlife, anything meant to feel sharp, metallic, or neon.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..600&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces (earth strata) */
  --background: #faf6ef;               /* topsoil cream, never sterile white */
  --surface-container-low: #f0eae0;    /* warm loam: cards, seasonal strips */
  --surface-container: #e8e0d2;        /* deeper clay-loam: section bands, secondary buttons */
  --surface-container-high: #ddd3c2;   /* wells, hover fills, inactive timeline cells */

  /* Ink */
  --on-surface: #2a302b;               /* deep forest charcoal: headings, body */
  --on-surface-variant: #4a524b;       /* moss-slate: captions, secondary text */

  /* Lines */
  --outline: #737872;                  /* lichen gray: input borders, axes, never text */
  --outline-variant: #cbc5b8;          /* soft straw: subtle dividers, gridlines */

  /* Accents */
  --primary: #366948;                  /* canopy green: primary actions, active harvest cells, key series */
  --on-primary: #ffffff;
  --primary-container: #d8efe0;        /* pale leaf: the one highlighted recommendation card */
  --on-primary-container: #1f4d30;     /* deep leaf ink on the pale leaf card */
  --secondary: #5c635c;                /* stone-moss: monospace labels, metadata */
  --tertiary: #8f5822;                 /* harvest ochre: kickers, sowing badges, secondary figures */
  --tertiary-container: #f2d4a7;       /* warm seed-ochre fill: sowing/prep cells, warm tags */
  --on-tertiary-container: #6e3f0c;
  --error: #b83230;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #366948;                   /* canopy green */
  --data-2: #8f5822;                   /* harvest ochre */
  --data-3: #a85438;                   /* terracotta clay */
  --data-4: #4b6b78;                   /* rain-cistern slate */
  --data-context: #b5b0a3;             /* context series and baselines */

  /* Fonts */
  --font-headline: 'Literata', serif;
  --font-body: 'Nunito Sans', sans-serif;
  --font-label: 'Geist Mono', monospace;

  /* Shape */
  --rounded: 0.625rem;                 /* 10px buttons and inputs */
  --rounded-lg: 1rem;                  /* 16px organic cream-layer cards */
  --rounded-full: 9999px;

  /* Style effects */
  --shadow-soft: 0 4px 20px rgb(42 48 43 / 0.06);
  --shadow-soft-hover: 0 8px 28px rgb(42 48 43 / 0.09);
  --border-soft: 1px solid rgb(203 197 184 / 0.65);
  --focus-glow: 0 0 0 4px rgb(54 105 72 / 0.18);
}
```

## Color

-   **Proportions**: topsoil cream (`--background`) and warm loam
    (`--surface-container-low`) carry ~85% of the page. Canopy green (`--primary`,
    ~10%) + pale leaf (`--primary-container`) anchor the primary action, active
    cycle states, and the single featured card. Harvest ochre (`--tertiary` /
    `--tertiary-container`, ~5%) highlights kickers, prep/sowing phases, and
    secondary deltas.
-   **Every neutral is soil- or plant-shifted.** No sterile `#ffffff` page
    backgrounds, no cold blue-grays, no neon greens.
-   **Separate with earth-stratum tone steps, not hard borders.** Cards step
    from `#faf6ef` onto `#f0eae0` without a border; reserve `--border-soft` for
    inputs and table rows.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Literata | 600 (500 at display size); optical size auto | Tracking −0.01em at display size. Line height 1.1–1.2. |
| Body | Nunito Sans | 400; 700 for emphasis | 16–17px, line height 1.62–1.7. |
| Kickers | Nunito Sans | 700, uppercase | 0.75rem, tracking 0.1em, in `--tertiary` (harvest ochre). |
| Labels, phenology cells, metadata | Geist Mono | 500–600, uppercase | 0.6875–0.75rem, tracking 0.06em. Gives almanac tables, zones, and cycle bars crisp precision. |
| Key figures | Literata | 600 | Large (1.75rem–2.5rem), `lining-nums tabular-nums`. |

## Defining Treatments

Ranked by how much each defines the style. Use each wherever the artifact has
that place.

### 1. Pale-leaf highlight card paired with loam cards

Cards sit on warm loam (`--surface-container-low`) with `16px` (`--rounded-lg`)
corners and no border. The single most important card in a view (the primary
recommendation, headline metric, or featured guild/recipe) takes the pale-leaf
fill (`--primary-container: #d8efe0`) with deep-leaf ink
(`--on-primary-container: #1f4d30`).

```css
.card {
  background: var(--surface-container-low);
  border-radius: var(--rounded-lg);
  padding: var(--space-lg);
  border: 0;
}
.card.is-leaf-highlight {
  background: var(--primary-container);
  color: var(--on-primary-container);
}
```

### 2. Almanac phenology / cycle strip

Where the content involves months, seasons, phases, steps, or schedules, render
a compact horizontal almanac bar on `--surface-container-low` with a monospace
label on the left and compact `22px` cells on the right — using
`--tertiary-container` (seed ochre) for prep/early phases and `--primary`
(canopy green) for peak/harvest/target phases.

```css
.season-strip {
  background: var(--surface-container-low);
  border-radius: 12px;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.season-cells { display: flex; gap: 4px; }
.season-cell {
  font-family: var(--font-label);
  font-size: 0.6875rem;
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  background: var(--surface-container-high);
  color: var(--secondary);
}
.season-cell.is-prep {
  background: var(--tertiary-container);
  color: var(--on-tertiary-container);
  font-weight: 700;
}
.season-cell.is-peak {
  background: var(--primary);
  color: var(--on-primary);
  font-weight: 700;
}
```

### 3. Soft lift on interactive panels

Interactive calculators, planners, and clickable cards take `--shadow-soft` (and
`--shadow-soft-hover` on hover), while static cards stay flat so tone does the
work.

## Composition

-   **Flush-left almanac rhythm.** Title block on the left, followed by a
    seasonal/cycle strip or summary row, then asymmetric 2-column content cards.
-   **Breathable measure.** Body text at 60–70ch with generous padding inside
    every loam card.

## Components

-   **Labels above headings** (when used): uppercase, tracked 0.1em, 0.75rem, in
    harvest ochre (`--tertiary`).
-   **Buttons**: `10px` (`--rounded`) corners. Primary is solid `--primary`
    (canopy green) with white text in `Nunito Sans` 700; secondary is
    `--surface-container` (`#e8e0d2`) with `--on-surface` text and no border.
-   **Key figures**: uppercase label, large `Literata` 600 value, and a short
    caption in `--tertiary` (or `--on-primary-container` inside the pale-leaf
    card).
-   **Tags and badges**: `--tertiary-container` with `--on-tertiary-container`
    text, or `--primary-container` with `--on-primary-container` text.
-   **Tables**: `--surface-container-low` header row, `Geist Mono` uppercase
    column headers, `--border-soft` horizontal dividers, no vertical lines.

## Data Visualization

-   **Series**: `--data-1` (canopy green `#366948`), `--data-2` (harvest ochre
    `#8f5822`), `--data-3` (terracotta clay `#a85438`), `--data-4` (cistern
    slate `#4b6b78`), `--data-context` (`#b5b0a3`).
-   **Marks**: 2px rounded lines, bars with `6px` rounded tops, direct series
    labels, horizontal `--outline-variant` gridlines.

## Motion

Gentle and organic: fade in with a small upward drift over `--dur-long` with
`--ease-out`; interactive cards lift 2px on hover.

## Don'ts

-   No pure white page backgrounds, cold blue-grays, or neon greens.
-   No sharp `0px` corners or heavy black borders.
-   At most one `.is-leaf-highlight` card per view so the pale-leaf accent keeps
    its hierarchy.

## If the User Asks for Dark

Keep the same roles on a forest-floor night ground: `--background: #181d19`,
`--surface-container-low: #202722`, `--surface-container: #28312a`,
`--surface-container-high: #323d35`, `--on-surface: #ece8df`,
`--on-surface-variant: #c2c7be`, `--primary: #82c995` (`--on-primary: #0d2615`),
`--primary-container: #234730` (`--on-primary-container: #d8efe0`),
`--tertiary: #e0b472`.
