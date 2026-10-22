---
name: Atelier
slug: atelier
register: classic
mode: light
---

# Atelier

## Identity

**North Star: "Restraint Is the Luxury."** A culture magazine or gallery
catalogue: near-monochrome ink on warm white stone, one muted taupe, thin black
rules, and a great deal of air. High-contrast Didone headlines with a single
italic word, a light geometric sans, and widely tracked small caps. Hushed,
expensive, curated — never showy, never glossy.

-   **Mood**: refined, hushed, curated, modern-classic.
-   **Inspired by**: independent culture and design quarterlies, exhibition
    catalogues, monograph books, and minimalist editorial layouts.

## When to Use

-   **Best for**: culture and art, design and architecture, fashion, travel
    features, biographies and profiles, exhibition or collection guides,
    premium brand and product stories.
-   **Avoid for**: dense operational dashboards, urgent or safety content,
    playful or children's material, anything that needs loud color coding.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Jost:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #fafaf8;               /* warm gallery white */
  --surface-container-low: #ece8e1;    /* pale stone, for a rare inset panel */
  --surface-container: #e5e0d8;        /* stone, for a panel that must read as an object */
  --surface-container-high: #ddd7cd;   /* deeper stone: hover fills, selected rows */

  /* Ink */
  --on-surface: #111111;               /* ink: headlines, lede, and body */
  --on-surface-variant: #5b5752;       /* warm graphite: captions, secondary text */

  /* Rules */
  --outline: #111111;                  /* ink hairline: the defining rule */
  --outline-variant: #d8d3cb;          /* stone hairline: quiet dividers, never text */

  /* Accents */
  --primary: #111111;                  /* ink is the accent: actions, emphasis */
  --on-primary: #fafaf8;
  --primary-container: #ece8e1;        /* stone fill behind ink */
  --on-primary-container: #111111;
  --secondary: #7a5c48;                /* muted taupe: kickers, notes, tags */
  --tertiary: #a89c8c;                 /* pale clay: ornament and fills only, never text */
  --error: #9a2b22;
  --on-error: #fafaf8;

  /* Data series, in order of use */
  --data-1: #111111;                   /* ink */
  --data-2: #7a5c48;                   /* taupe */
  --data-3: #948a7d;                   /* stone grey */
  --data-4: #55657a;                   /* dusk slate */
  --data-context: #cfc9bf;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Bodoni Moda', serif;
  --font-body: 'Jost', sans-serif;
  --font-label: 'Jost', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;                   /* even tags stay square */

  /* Style effects */
  --rule-ink: 1px solid var(--outline);
  --rule-stone: 1px solid var(--outline-variant);
  --label-tracking: 0.22em;
}
```

## Color

-   **Proportions**: gallery white and ink are nearly everything — about 95% of
    what the reader sees. Taupe is the only warmth (under 5%): the kicker under
    the title, the note beneath a key figure, a tag. Stone fills are rare.
-   **Ink is the accent.** Emphasis comes from black — a black button, a black
    rule, a larger Didone — not from a bright color. Never introduce a hue to
    make something "pop".
-   **Taupe as text** passes on the background, `--surface-container-low`, and
    `--surface-container`; it fails on `--surface-container-high`, so use ink
    there.
-   **Clay (`--tertiary`) and stone hairlines are never text** (2.6:1 and
    1.4:1). They are for fills, rules, and chart context only.
-   **Fills are rare.** Separate with black top rules and space; use a stone
    panel only for something that must read as a separate object (a form, a
    caption plate beside a figure).

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Bodoni Moda | 400; one italic word for emphasis | Push the display size up — the face is at its best large. Tracking −0.01em. Line height 1.05–1.1. |
| Lede | Jost | 300 | Only at 1.15–1.3× body size, never smaller; in `--on-surface`. Line height 1.6. |
| Body | Jost | 400; 400 italic for emphasis | At least 17px for narrative. Line height 1.6–1.7. |
| Labels, kickers, nav, buttons | Jost | 400, uppercase | At label size (0.75rem minimum); tracking `var(--label-tracking)`. Kicker in `--secondary`. |
| Key figures | Bodoni Moda | 400 | Large, lining figures; tabular in tables (`font-variant-numeric: lining-nums tabular-nums`). |

Headlines are sentence or title case, never all caps; all caps belong to the
small tracked labels only. Contrast comes from scale and stroke — a large,
hairline-and-thick Didone over tiny, airy, regular-weight capitals — not from
bold weights. Avoid Jost above 500 and Bodoni above 600.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Didone title with one italic word

The opening title and section headlines are set in large Bodoni Moda at regular
weight, with a single word from the content's own title set in italic. One
italic word per headline at most; if no word earns it, set the whole line roman.

```css
.display {
  font-family: var(--font-headline);
  font-weight: 400;
  font-size: var(--display-size);
  line-height: 1.06;
  letter-spacing: -0.01em;
  font-optical-sizing: auto;
}
.display em { font-style: italic; }
```

### 2. Tracked small-caps labels

Every label voice — the kicker under the title, key-figure labels, table
headers, buttons, tags, navigation — is small uppercase Jost with very wide
tracking. The kicker sits below the title in taupe, like a gallery wall label.

```css
.label {
  font-family: var(--font-label);
  font-weight: 400;
  font-size: var(--label-size);
  text-transform: uppercase;
  letter-spacing: var(--label-tracking);
}
.kicker { color: var(--secondary); margin-top: var(--space-sm); }
```

### 3. Ink top rule instead of a card

Key figures, list entries, and section openings carry a single 1px black rule
on top and no fill, border, or shadow — the value hangs beneath the line. Use
the stone hairline for quieter dividers inside a section.

```css
.ruled-top {
  border-top: var(--rule-ink);
  padding-top: var(--space-sm);
  background: transparent;
}
.ruled-top .value { font-family: var(--font-headline); font-weight: 400; font-size: var(--headline-size); }
.ruled-top .note { color: var(--secondary); }
.divider { border-top: var(--rule-stone); }
```

### 4. Gallery margins

The title block and the primary container get unusually wide inner margins —
noticeably more than the content needs — so the page reads as a white wall with
works displayed on it.

```css
.title-block { padding: var(--space-2xl) var(--space-xl) var(--space-xl); }
.main-column { padding-inline: var(--space-xl); }
```

### 5. Exhibition-label captions

Figures and charts are captioned like museum labels: a tracked small-caps
title, then a short line of graphite body text, set flush-left beneath an ink
rule.

```css
figcaption {
  border-top: var(--rule-ink);
  padding-top: var(--space-sm);
  margin-top: var(--space-md);
  color: var(--on-surface-variant);
}
figcaption .label { display: block; color: var(--on-surface); margin-bottom: var(--space-xs); }
```

## Composition

-   **Flush-left, editorial.** Title, kicker, lede, and figures align to a
    strong left edge, like a magazine opener; nothing is centered except an
    occasional single pull figure. This agrees with the skill's preference for
    asymmetry — lean into it: a narrow text column beside a wide image or
    chart, or an offset key-figure row.
-   **Airy.** Low density, generous margins and large gaps between sections;
    whitespace is the main separator, black top rules the second.
-   **No boxes.** Content is held by rules and space, not fills or shadows.
-   **Dashboards and tools** keep the Didone header, tracked labels, and ink
    rules, but tighten to the denser scale and drop the gallery margins.

## Components

-   **Buttons**: square. Primary is an ink fill with white text; secondary is a
    1px ink outline on transparent. Labels in the tracked uppercase voice,
    generous horizontal padding. Hover inverts (the outline fills with ink);
    no shadows.
-   **Key figures**: an ink top rule, a tracked label, the value in large
    regular Bodoni, a short note in taupe.
-   **Tags**: square, no fill, no border — just taupe tracked small caps.
-   **Links**: ink, with a 1px underline offset 4px; hover swaps the underline
    to taupe.
-   **Inputs**: transparent, a 1px ink line beneath, label in the tracked
    voice above.
-   **Tables**: no vertical lines or zebra fills. An ink rule above and below
    the header, stone hairlines between rows; header cells in the label voice.
-   **Navigation and contents**: a row of tracked small caps with wide gaps,
    the active item underlined in ink.

## Data Visualization

-   **Series**: `--data-1` (ink) for the series that matters, then taupe,
    stone, slate. Everything that is context is `--data-context`.
-   **Lines and marks**: 1–1.5px lines, thin bars with square ends, small
    filled squares at endpoints. No gradients, glows, heavy area fills, or 3D.
-   **Axes and gridlines**: a single ink baseline; horizontal gridlines only,
    in `--outline-variant`; no chart border. Axis labels in the tracked label
    voice.
-   **Labels and annotations**: label series directly at their ends in Jost;
    annotations in Jost italic with a hairline leader.
-   **Chart titles**: Bodoni at subhead size, captioned beneath as an
    exhibition label (treatment 5).

## Motion

Slow, composed, almost imperceptible: a fade with a small upward drift over
`--dur-long` with `--ease-out`, staggered gently. No bounces, springs, scale, or
parallax.

## Don'ts

-   No bold Didone or bold Jost headlines — heavy weights make it look like a
    sale flyer.
-   No color beyond ink, stone, and taupe; no bright accents, gradients, or
    tinted backgrounds.
-   No rounded corners, pill tags, drop shadows, or filled cards.
-   Don't tighten the label tracking, and don't track headlines wide.
-   Don't italicize whole headlines or more than one word per headline.
-   Don't crowd the page — cramped margins are what make this style look cheap.

## If the User Asks for Dark

Keep the same roles on an espresso ground: `--background: #15110e`,
`--on-surface: #f1ebe1`, `--on-surface-variant: #b3a693`, `--primary: #f1ebe1`
with `--on-primary: #15110e`, `--outline: #f1ebe1`, `--outline-variant:
#3a322b`, `--secondary: #c9b083` (champagne, for kickers and notes; 9:1). Rules
stay 1px; keep everything else.
