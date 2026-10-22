---
name: Terracotta
slug: terracotta
register: classic
mode: light
---

# Terracotta

## Identity

**North Star: "Sunlit Plaster and Courtyard Shade."** A sunlit
riad courtyard in late afternoon: warm tadelakt lime-plaster surfaces, burnt
terracotta clay, burnished brass hairlines, and a cool zellige emerald accent.
Key figure cards take a restrained architectural arch silhouette at their top
corners (`28px 28px 6px 6px`), separated from the title block by a fine brass
diamond rule. Calm, tactile, and architectural — never kitsch, never cold.

-   **Mood**: warm, architectural, sun-washed, quietly luxurious.
-   **Inspired by**: Moroccan riad courtyards and tadelakt plaster architecture,
    zellige tilework and brass craft, Mediterranean and North African travel
    and design monographs.

## When to Use

-   **Best for**: travel and place guides, food, wine, and hospitality,
    architecture and interiors, culture and craft stories, itinerary planners,
    lifestyle and reading-friendly explainers.
-   **Avoid for**: dense operational or cloud-monitoring consoles, urgent alerts
    or incident tools, highly technical developer specs, anything meant to feel
    clinical, cold, or childlike.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f9f3eb;               /* warm tadelakt plaster, never cold white */
  --surface-container-low: #f3e9dc;    /* courtyard sand: arched cards, panels */
  --surface-container: #ede0d0;        /* deeper plaster: section bands, secondary fills */
  --surface-container-high: #e4d4c0;   /* table headers, wells, active states */

  /* Ink */
  --on-surface: #261b15;               /* cedarwood espresso: headings, body */
  --on-surface-variant: #57483f;       /* warm clay-taupe: captions, secondary text */

  /* Borders */
  --outline: #9e8a78;                  /* warm brass-taupe: input borders, axes, never text */
  --outline-variant: #dfd0be;          /* pale plaster rule: hairlines, card borders */

  /* Accents */
  --primary: #b84a24;                  /* burnt terracotta: primary actions, links, italic focal word */
  --on-primary: #ffffff;
  --primary-container: #f7ebe0;        /* sunlit terracotta wash: featured arch card, highlights */
  --on-primary-container: #7d2e12;     /* deep kiln terracotta on the wash */
  --secondary: #8f6524;                /* burnished brass: kickers, ornamental rules, metadata */
  --tertiary: #1d6356;                 /* zellige courtyard emerald: badges, deltas, secondary signal */
  --tertiary-container: #e1efe9;       /* pale zellige wash: status pills, callout tags */
  --on-tertiary-container: #13473d;
  --error: #b82929;
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #b84a24;                   /* burnt terracotta */
  --data-2: #1d6356;                   /* zellige emerald */
  --data-3: #b5893e;                   /* burnished brass / ochre */
  --data-4: #8c3838;                   /* desert rose */
  --data-context: #a39384;             /* context series */

  /* Fonts */
  --font-headline: 'Cormorant Garamond', serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
  --font-label: 'Plus Jakarta Sans', sans-serif;

  /* Shape */
  --rounded: 0.375rem;                 /* 6px standard corners */
  --rounded-lg: 0.75rem;               /* 12px large panels */
  --rounded-arch: 28px 28px 6px 6px;   /* signature riad arch top for metric/feature cards */
  --rounded-full: 9999px;

  /* Style effects */
  --soft-shadow: 0 4px 18px rgb(38 27 21 / 0.04);
  --soft-shadow-raised: 0 8px 28px rgb(38 27 21 / 0.07);
  --warm-hairline: 1px solid var(--outline-variant);
  --brass-gradient: linear-gradient(90deg, #d8c3b0, #b5893e, #d8c3b0);
}
```

## Color

-   **Proportions**: tadelakt plaster (`--background` and `--surface-container-low`)
    and cedarwood espresso ink carry 85–90% of the page. Burnt terracotta
    (`--primary`, ~6%) is the warm primary signal: the main button, the italic
    focal word in a headline, and the primary data series. Zellige emerald
    (`--tertiary`, ~4%) provides the cool courtyard counterpoint on badges,
    positive deltas, and the second data series.
-   **Every neutral is sun-warmed.** No pure whites, no blue-grays, no pure
     `#000000` black.
-   **Contrast guardrails**: `--primary` (`#b84a24`), `--secondary` (`#8f6524`),
    and `--tertiary` (`#1d6356`) all clear 4.5:1 on `--background` and
    `--surface-container-low`. `--outline` and `--outline-variant` are for
    rules, borders, and brass dividers only — never text.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Cormorant Garamond | 600; 600 italic for one focal word | Step up the scale (`clamp(2.25rem, 4vw, 3.5rem)`): Cormorant's small x-height blooms at larger sizes. Leading 1.04–1.12, tracking −0.01em. |
| Subheads | Cormorant Garamond | 600 | Sentence or title case, leading 1.2. |
| Body | Plus Jakarta Sans | 400; 600 for inline emphasis | 16–17px, line height 1.65. |
| Labels, kickers, badges | Plus Jakarta Sans | 700, uppercase | 0.6875–0.75rem, tracking 0.14–0.16em. |
| Key figures | Cormorant Garamond | 600, lining figures | Large (2rem–2.75rem); pairs architectural serif numerals with tracked sans labels. |
| Table and chart numbers | Plus Jakarta Sans | 500, `tabular-nums` | Body or label size. |

## Defining Treatments

Ranked by how much each defines the style. Use each wherever the artifact has
that place.

### 1. Riad arch metric & feature cards

Key-figure tiles, itinerary day cards, and summary callouts sit on
`--surface-container-low` with a soft architectural arch at the top corners
(`border-radius: var(--rounded-arch)` — `28px 28px 6px 6px`) and a `1px` plaster
border. The featured card in a row takes `--primary-container` with a warm
terracotta-tinted border (`#c98a6b`).

```css
.arch-card {
  background: var(--surface-container-low);
  border: 1px solid var(--outline-variant);
  border-radius: var(--rounded-arch);
  padding: 20px 18px 16px;
  text-align: center;
  box-shadow: var(--soft-shadow);
}
.arch-card.is-featured {
  background: var(--primary-container);
  border-color: #c98a6b;
}
```

### 2. Cormorant title with a terracotta italic focal word

Set the primary title and major section headings in `Cormorant Garamond` 600
with tight leading, and set one key word (a place, a craft, the core concept) in
italic burnt terracotta (`--primary`).

```css
.title {
  font-family: var(--font-headline);
  font-weight: 600;
  font-size: var(--display-size);
  line-height: 1.05;
  letter-spacing: -0.01em;
  color: var(--on-surface);
}
.title i, .title em {
  font-style: italic;
  color: var(--primary);
}
```

### 3. Brass diamond ornamental divider

Beneath the hero headline (or between major narrative acts), place a centered
tracked label flanked by a 1px burnished-brass gradient rule and `◆` diamonds.
Use at most once or twice per page.

```css
.ornament-rule {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-block: var(--space-md);
  color: var(--secondary);
  font-family: var(--font-label);
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
}
.ornament-rule::before,
.ornament-rule::after {
  content: "";
  flex: 1;
  height: 1px;
  background: var(--brass-gradient);
}
```

### 4. Zellige emerald counterpoint badge & delta

Pair warm terracotta actions with cool zellige emerald (`--tertiary` /
`--tertiary-container`) on status pills, category tags, and secondary figure
captions so the page has the authentic warm-clay + cool-tile balance of a
courtyard.

```css
.badge-emerald {
  background: var(--tertiary-container);
  color: var(--on-tertiary-container);
  border: 1px solid #b5d6c9;
  padding: 4px 12px;
  border-radius: var(--rounded-full);
  font-family: var(--font-label);
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
```

## Composition

-   **Courtyard cadence.** Give the hero title block generous breathing room,
    followed by a 2- to 4-column row of `.arch-card` tiles for key metrics or
    chapters.
-   **Wide text panels and tables** use standard `--rounded-lg` (`12px`)
    corners rather than the arch silhouette; reserve `--rounded-arch` for compact
    cards in a row (metrics, days, places, specimens) where the arch reads
    cleanly.
-   **Tonal plaster bands** (`--surface-container`) separate major sections
    without heavy box shadows.

## Components

-   **Labels above headings** (when used): Plus Jakarta Sans 700 caps, 0.16em
    tracking, in `--primary`; a two-part row spaced apart when there are two
    items.
-   **Buttons**: pill-shaped (`--rounded-full`). Primary is solid `--primary`
    (burnt terracotta) with white text; secondary is transparent with a `1px`
    `#c4b29e` border and `--on-surface` text.
-   **Key figures**: inside `.arch-card` — tracked uppercase label in
    `--on-surface-variant`, large `Cormorant Garamond` 600 numeral, and a short
    caption in `--tertiary` (zellige emerald).
-   **Inputs & selects**: `--surface-container-low` fill, `1px solid
    var(--outline-variant)` border, `--rounded` (`6px`) corners; focus border in
    `--primary`.
-   **Tables**: header row in `--surface-container` with tracked uppercase labels;
    `1px solid var(--outline-variant)` row dividers; no vertical lines.

## Data Visualization

-   **Series**: `--data-1` (burnt terracotta `#b84a24`) for the primary series,
    `--data-2` (zellige emerald `#1d6356`) for the comparison series, `--data-3`
    (burnished brass `#b5893e`), `--data-4` (desert rose `#8c3838`), and
    `--data-context` (`#a39384`) for context.
-   **Marks**: 2px lines with round caps; bar tops slightly rounded (`4px 4px 0
    0`). Direct end-of-line labels in `Plus Jakarta Sans` 600.

## Motion

Unhurried and warm: fade in with a gentle 6px upward drift over `--dur-long`
with `--ease-out`; cards lift subtly to `--soft-shadow-raised` on hover.

## Don'ts

-   No cold whites (`#ffffff` page backgrounds), blue-grays, or neon accents.
-   Don't put `--rounded-arch` on wide full-bleed tables or multi-paragraph text
    containers — keep the arch silhouette on metric, step, or feature cards.
-   No heavy black borders or harsh drop shadows.

## If the User Asks for Dark

Shift to a lantern-lit courtyard night palette: `--background: #1a1310`,
`--surface-container-low: #241b16`, `--surface-container: #2e231d`,
`--on-surface: #f5ece0`, `--on-surface-variant: #c7b6a6`, `--primary: #e07a52`
(`--on-primary: #1a1310`), `--secondary: #d4a857`, `--tertiary: #5ec2b0`,
`--outline-variant: #3d2f27`.
