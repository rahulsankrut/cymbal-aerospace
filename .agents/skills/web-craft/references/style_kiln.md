---
name: Kiln
slug: kiln
register: classic
mode: light
---

# Kiln

## Identity

**North Star: "Quiet Craft, Fired in Stone."** A craft monograph or
ceramic studio catalogue: warm unbleached linen paper, deep sumi-charcoal ink,
quiet lichen-moss green, and a single vertical cinnabar-red seal stamp (`hanko`
mark). Crisp mincho-serif headlines set in calm roman weight, washi-stone
panels anchored by a `2px` vertical sumi left rule, and monospace catalog
metadata. Organic, contemplative, and tactile.

-   **Mood**: contemplative, artisanal, grounded, composed.
-   **Inspired by**: ceramic and craft monographs, woodblock and letterpress
    exhibition catalogues, architectural folios, and quiet studio journals.

## When to Use

-   **Best for**: culinary craft, tea/coffee and food stories, architecture and
    interiors, travel and place guides, nature and gardens, mindfulness and
    wellbeing, cultural history, and calm personal tools or planners.
-   **Avoid for**: high-frequency trading or incident consoles, loud promotional
    campaigns, children's arcade games, anything that wants neon or glossy chrome.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@400;500;600&family=Shippori+Mincho:wght@400;500;600;700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces: unbleached linen and river clay */
  --background: #f4f1ea;               /* warm unbleached linen paper */
  --surface-container-low: #ebe6db;    /* pale washi stone: specimen cards, panels */
  --surface-container: #e3ddd0;        /* warm clay: banded sections, secondary fills */
  --surface-container-high: #d9d1c2;   /* deeper clay: hover fills, selected rows */

  /* Ink */
  --on-surface: #1c1b18;               /* sumi charcoal ink: headlines, lede, and body */
  --on-surface-variant: #5e5a51;       /* weathered stone: captions, secondary text */

  /* Rules */
  --outline: #1c1b18;                  /* sumi rule: primary structural stroke */
  --outline-variant: #d2cbbd;          /* linen hairline: quiet dividers, never text */

  /* Accents */
  --primary: #1c1b18;                  /* sumi ink is the primary action fill */
  --on-primary: #f4f1ea;
  --primary-container: #ebe6db;        /* washi fill behind ink */
  --on-primary-container: #1c1b18;
  --secondary: #4a5d46;                /* lichen moss: kickers, figure notes, secondary series */
  --tertiary: #9e3b2b;                 /* cinnabar seal red: catalog stamp, focal callout */
  --error: #9e2a22;
  --on-error: #f4f1ea;

  /* Data series, in order of use */
  --data-1: #4a5d46;                   /* lichen moss */
  --data-2: #9e3b2b;                   /* cinnabar red */
  --data-3: #1c1b18;                   /* sumi charcoal */
  --data-4: #8a6f48;                   /* bamboo ochre */
  --data-context: #c7bfb0;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Shippori Mincho', serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-label: 'Geist Mono', monospace;

  /* Shape */
  --rounded: 0.125rem;                 /* 2px hand-trimmed paper corners */
  --rounded-lg: 0.125rem;
  --rounded-full: 0.125rem;

  /* Style effects */
  --rule-sumi-left: 2px solid var(--outline);
  --rule-sumi: 1px solid var(--outline);
  --rule-linen: 1px solid var(--outline-variant);
  --label-tracking: 0.14em;
}
```

## Color

-   **Proportions**: unbleached linen (`#f4f1ea`), pale washi stone (`#ebe6db`),
    and sumi charcoal (`#1c1b18`) carry about 90% of the page. Lichen moss
    (`#4a5d46`, 6.2:1 on linen) provides quiet organic warmth for kickers,
    subheads, and figure notes. Cinnabar (`#9e3b2b`, 5.8:1 on linen) is reserved
    for a single vertical catalog stamp or focal data point (under 2%).
-   **Washi panels with a vertical sumi spine.** Unlike borderless gallery pages,
    `Kiln` groups key figures and specimens on pale washi-stone panels
    (`--surface-container-low`) anchored by a `2px` sumi left border
    (`--rule-sumi-left`).

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Shippori Mincho | 500–600, upright roman | Large scale; tracking `-0.01em`; line height 1.1–1.18. Calm, upright mincho authority without italic flourishes. |
| Subheads / north-star line | Shippori Mincho | 500 | In `--secondary` (lichen moss), line height 1.35. |
| Body | Plus Jakarta Sans | 400; 500 for emphasis | 16–17px for narrative; line height 1.65. |
| Labels, kickers, catalog indices | Geist Mono | 500, uppercase | `0.75rem`, tracking `var(--label-tracking)`. Kickers in `--secondary`; seal stamp in `--tertiary`. |
| Key figures | Shippori Mincho | 600 | Large (1.875rem–2.5rem), `lining-nums tabular-nums`. |

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies;
use it wherever the artifact has that place.

### 1. Vertical cinnabar catalog stamp (`hanko` mark)

When the content has its own catalog, issue, or part identifier, set it
vertically in the upper-right corner of the title block inside a `1px` cinnabar
border (`--tertiary`). At most one per page.

```css
.seal-stamp {
  border: 1px solid var(--tertiary);
  color: var(--tertiary);
  font-family: var(--font-label);
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  padding: 0.375rem 0.3125rem;
  writing-mode: vertical-rl;
  text-transform: uppercase;
}
```

### 2. Washi-stone panels with a 2px sumi left spine

Key figures, specimen entries, and callout blocks sit on pale washi stone
(`--surface-container-low`) with a `2px` solid sumi left border
(`--rule-sumi-left`) and `2px` corners — evoking a bound Japanese monograph or
folded studio sheet.

```css
.washi-card {
  background: var(--surface-container-low);
  border-left: var(--rule-sumi-left);
  border-radius: var(--rounded);
  padding: 16px 18px;
}
.washi-card .value {
  font-family: var(--font-headline);
  font-weight: 600;
  font-size: var(--headline-size);
  color: var(--on-surface);
}
.washi-card .note {
  color: var(--secondary);
  font-size: 0.8125rem;
  font-weight: 500;
}
```

### 3. Upright Shippori Mincho headline with a lichen-moss subhead

Set the opening title and section headings in upright `Shippori Mincho` (`500`
or `600`) in sumi ink, paired with a quiet subhead or north-star line in lichen
moss (`--secondary`) directly beneath.

```css
.display {
  font-family: var(--font-headline);
  font-weight: 500;
  font-size: var(--display-size);
  line-height: 1.1;
  letter-spacing: -0.01em;
  color: var(--on-surface);
}
.subhead-moss {
  font-family: var(--font-headline);
  font-weight: 500;
  color: var(--secondary);
  margin-top: var(--space-xs);
}
```

### 4. Monospace catalog labels and tags

Set figure labels, table headers, and square tags in uppercase `Geist Mono`
(`0.14em` tracking) so technical measurements (temperatures, weights, durations,
years) feel like studio kiln logs.

```css
.label {
  font-family: var(--font-label);
  font-weight: 500;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: var(--label-tracking);
}
```

### 5. Generous paper margins and horizontal linen hairlines

Give the title block and primary column wide breathing room so the unbleached
linen paper reads as a physical sheet, divided between major sections by `1px`
linen hairlines (`--rule-linen`).

## Composition

-   **Flush-left, asymmetric, and calm.** Align headings, kickers, and text to a
    clean left axis while letting the vertical cinnabar seal balance the upper
    right.
-   **Washi spine cards for metrics and specimens; bare linen for prose.**

## Components

-   **Buttons**: `2px` radius (`--rounded`), uppercase `Geist Mono` (`0.12em`
    tracking). Primary is sumi ink (`--primary`) with linen text; secondary is a
    `1px` sumi outline on `--surface-container-low`.
-   **Key figures**: inside `.washi-card` — monospace label, large `Shippori
    Mincho` 600 value, and a short note in lichen moss (`--secondary`).
-   **Tags**: `2px` radius, `1px` `--outline-variant` border, `--surface-container-low`
    fill, monospace label in `--secondary`.
-   **Tables**: `1px` sumi rule above and below the header, `--rule-linen`
    between rows, no vertical rules or zebra striping.

## Data Visualization

-   **Series**: `--data-1` (lichen moss `#4a5d46`) for the primary series,
    `--data-2` (cinnabar `#9e3b2b`) for the focal comparison or threshold, then
    sumi (`#1c1b18`) and bamboo ochre (`#8a6f48`).
-   **Lines and marks**: fine `1.5px` strokes, square bar ends, `1px` sumi
    baseline, and horizontal `--outline-variant` gridlines only.

## Motion

Slow, quiet fades over `--dur-long` with `--ease-out`. No bounces or scale pops.

## Don'ts

-   No pill buttons, large rounded corners, or drop shadows.
-   No italic words inside `Shippori Mincho` headlines — keep the mincho serif
    upright and calm.
-   Don't overuse cinnabar (`--tertiary`) — it is a seal stamp and focal point,
    never a section background.

## If the User Asks for Dark

Use sumi-lacquer dark: `--background: #141412`, `--surface-container-low: #1d1c19`,
`--surface-container: #252420`, `--on-surface: #ece7dc`,
`--on-surface-variant: #a69f91`, `--outline: #ece7dc`,
`--outline-variant: #33312b`, `--primary: #ece7dc`, `--on-primary: #141412`,
`--secondary: #8fb088` (moss), `--tertiary: #e06d58` (cinnabar).
