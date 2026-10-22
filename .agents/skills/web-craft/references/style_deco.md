---
name: Deco
slug: deco
register: expressive
mode: dark
---

# Deco

## Identity

**North Star: "The Grand Salon After Dark."** A jazz-age poster or the lobby of
a 1930s grand hotel or ocean liner: deep emerald-black lacquer, burnished gold,
and cream. Geometric all-caps headlines with wide tracking, double gold frames,
fine vertical pinstripes, and strict mirror symmetry. Glamorous, ceremonial,
confident — never kitsch, costume-party, or gaudy.

-   **Mood**: glamorous, ceremonial, poised, nocturnal.
-   **Inspired by**: 1920s–30s decorative arts, transatlantic ocean-liner
    salons, jazz-age theatre programs, and geometric poster art.

## When to Use

-   **Best for**: history (especially 1900–1940), storytelling, events,
    invitations and galas, food and drink, hospitality, travel and transport
    history, architecture.
-   **Avoid for**: dense operational dashboards, technical or product
    documentation, health and safety content, anything somber, urgent, or
    aimed at young children.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Lora:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: dark;

  /* Page and surfaces */
  --background: #0e1714;               /* emerald-black lacquer */
  --surface-container-low: #13211c;    /* a step up, for inset panels */
  --surface-container: #182c25;        /* green marble, for a rare filled panel */
  --surface-container-high: #1f3a31;   /* deep emerald: hover, selected rows */

  /* Ink */
  --on-surface: #f3ead7;               /* cream */
  --on-surface-variant: #c8bfa9;       /* warm stone: captions, secondary text */

  /* Rules */
  --outline: #c9a14a;                  /* burnished gold: frames and rules */
  --outline-variant: #5d4e2b;          /* dim bronze: hairlines, never text */

  /* Accents */
  --primary: #c9a14a;                  /* burnished gold */
  --on-primary: #0e1714;
  --primary-container: #2a2414;        /* smoked gold, for a selected state */
  --on-primary-container: #e8cf8f;
  --secondary: #86bfa5;                /* jade: quotations, secondary marks */
  --tertiary: #d8b866;                 /* bright gilt: tags, hover on gold */
  --error: #e8836f;                    /* coral lacquer */
  --on-error: #0e1714;

  /* Data series, in order of use */
  --data-1: #c9a14a;                   /* gold */
  --data-2: #5fae8c;                   /* jade */
  --data-3: #e8836f;                   /* coral */
  --data-4: #8aa9d6;                   /* liner blue */
  --data-context: #6b7a72;             /* context series; gridlines use outline-variant */

  /* Fonts */
  --font-headline: 'Josefin Sans', sans-serif;
  --font-body: 'Lora', serif;
  --font-label: 'Josefin Sans', sans-serif;

  /* Shape */
  --rounded: 0;
  --rounded-lg: 0;
  --rounded-full: 0;

  /* Style effects */
  --gold-rule: 1px solid var(--outline);
  --gold-frame-inset: 6px;
  --pinstripe: repeating-linear-gradient(90deg, rgb(201 161 74 / 0.05) 0 1px, transparent 1px 28px);
  --flank-rule-width: 40px;
}
```

## Color

-   **Proportions**: emerald-black and cream carry the page — roughly 85–90%
    of what the reader sees. Gold is the signature (around 10%): frames,
    rules, the emphasized headline words, labels, the primary action, the
    first data series. Jade and coral are rare second voices.
-   **Gold is a text color here.** At 7.5:1 on the background it may set
    labels, kickers, links, and headline emphasis — much of the style's
    glamour. Keep body paragraphs cream; a page of gold prose looks cheap.
-   **Bronze (`--outline-variant`) is never text.** At about 2:1 it is only
    for hairlines, tag borders, and gridlines.
-   **Depth comes from green, not grey.** Panels step up through the emerald
    surfaces; never introduce neutral greys or pure black.
-   **Fills are rare.** Separate with gold frames, rules, and space; use
    `--surface-container` only for a panel that must read as its own object.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Josefin Sans | 300 uppercase; emphasized words 600 in `--primary` | Tracking 0.12–0.14em, line height 1.15–1.2. Wide tracking makes lines long: step the display size down rather than let a title wrap to four lines. |
| Section headings | Josefin Sans | 400 uppercase | Tracking 0.12em. |
| Body | Lora | 400; 400 italic for emphasis | At least 17px for narrative. Line height 1.6–1.7. |
| Labels, kickers, nav, buttons | Josefin Sans | 600 uppercase | 0.75–0.8rem, tracking 0.2–0.25em, usually in `--primary`. |
| Ledes, captions, key-figure notes | Lora | 400 italic | Ledes at 1.1× body; captions in `--on-surface-variant`. |
| Key figures | Josefin Sans | 300 | Large, tracking 0.06em, lining tabular figures. |

Weight contrast is the voice: a light, airy, widely tracked geometric capital
with one or two heavy gold words. Josefin's lowercase is never used for
headlines; Lora never appears in caps.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Double gold frame

A gold rule with a second rule inset 6px. Frames key figures, the opening
title block, or the primary container of a tool. Unlike quieter styles, Deco
may repeat it across a row of peers (a set of key figures) — but frames never
nest, and body sections are never framed.

```css
.deco-frame {
  border: var(--gold-rule);
  outline: var(--gold-rule);
  outline-offset: calc(-1 * var(--gold-frame-inset));
  padding: var(--space-lg);
  text-align: center;
}
```

### 2. Tracked capital headline with gold emphasis

The opening title and section headings in light, widely tracked capitals; the
title's key phrase (words already in it) switches to heavy gold.

```css
.deco-title {
  font-family: var(--font-headline);
  font-weight: 300;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  line-height: 1.2;
  color: var(--on-surface);
}
.deco-title b { font-weight: 600; color: var(--primary); }
```

### 3. Flanking gold rules

Short gold rules on both sides of a centered label: the kicker or subtitle by
the title, section labels, chart titles. Rules, never glyphs.

```css
.flanked {
  font-family: var(--font-label);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: var(--primary);
}
.flanked::before, .flanked::after {
  content: "";
  display: inline-block;
  width: var(--flank-rule-width);
  height: 1px;
  background: var(--outline);
  vertical-align: middle;
  margin-inline: var(--space-sm);
}
```

### 4. Vertical pinstripes

Faint gold vertical lines every 28px across the page background, like
lacquered wall panelling. Barely visible; on the page only, never on cards,
charts, or inputs.

```css
body { background-color: var(--background); background-image: var(--pinstripe); }
```

### 5. Gold hairline dividers

Section openings and rows of entries are separated by a single gold rule, or a
bronze hairline where gold would be too loud (list entries, table rows).

```css
.section-head { border-bottom: var(--gold-rule); padding-bottom: var(--space-sm); }
.entry + .entry { border-top: 1px solid var(--outline-variant); padding-top: var(--space-md); }
```

## Composition

-   **Mirror symmetry is the point.** Title blocks, kickers, section openings,
    key-figure rows, and button groups are centered on the page's axis, like a
    poster or a hotel façade. This overrides the general preference for
    asymmetry.
-   **Body text is not centered.** Paragraphs sit left-aligned in a centered
    measure of 60–66ch.
-   **Rows come in balanced sets.** Key figures and cards sit in equal-width
    columns that mirror around the center; avoid lopsided spans.
-   **Airy but formal.** Generous space between sections; separation comes
    from gold rules, frames, and space — not fills or shadows.
-   **Dashboards and tools** keep a centered header and gold rules, but their
    grids are left-aligned and denser; frame only the primary container.

## Components

-   **Buttons**: square corners. Primary is a gold fill with emerald-black
    text; secondary is a gold outline with gold text on transparent. Label in
    `--font-label`, 600, uppercase, tracking 0.2em, generous horizontal
    padding. Hover brightens to `--tertiary` or fills the outline; no shadows.
-   **Key figures**: in a double gold frame, centered — a tracked gold label,
    the value in light Josefin, an italic Lora note in warm stone.
-   **Tags**: a 1px bronze border, square corners, gilt (`--tertiary`) tracked
    uppercase label at label size.
-   **Links**: gold, with a 1px bronze underline offset 3px that turns gold on
    hover.
-   **Inputs**: a transparent field with a gold hairline underneath; focus
    brightens the line and adds the focus ring.
-   **Tables**: no vertical lines. A gold rule under the header, bronze
    hairlines between rows; header cells in the label voice; lining tabular
    figures.
-   **Navigation and contents**: centered tracked labels separated by generous
    space or a short vertical bronze rule.

## Data Visualization

-   **Series**: `--data-1` (gold) for the series that matters, then jade,
    coral, liner blue. Everything that is context is `--data-context`.
-   **Lines and marks**: 1.5–2px lines with square caps; bars flat with square
    tops and slim gaps, like columns on a façade. No gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in `--font-label`, uppercase, tracked,
    in `--on-surface-variant`; gridlines solid 1px in `--outline-variant`; a
    gold baseline; no chart border.
-   **Labels and annotations**: label series directly at their ends in the
    label voice; annotations in italic Lora with a thin gold leader line.
-   **Chart titles**: centered tracked capitals with flanking gold rules.

## Motion

Poised and theatrical, like a curtain rising: fade in with a small upward
drift over `--dur-long` with `--ease-out`; gold rules may draw outward from the
center (`transform: scaleX`). No bounces, springs, or shimmer effects.

## Don'ts

-   No diamonds, sunbursts, fans, chevron borders, or other Deco clip-art; the
    style lives in rules, frames, and type.
-   No metallic gradients or shine on gold; gold is a flat color.
-   No rounded corners, drop shadows, or glows.
-   Don't set headlines in sentence case or Josefin lowercase, and don't set
    body text in Josefin or in gold.
-   Don't nest double frames, frame every section, or add a novelty Deco
    display face.
-   No neutral greys or pure black; every dark is green-tinted.

## If the User Asks for Light

Keep the same roles on a cream ground: `--background: #f5efe1`,
`--on-surface: #14201b`, `--on-surface-variant: #4a4536`, `--primary: #7a5c18`
(a darker gold that keeps 4.5:1 for labels and links), `--on-primary:
#f5efe1`, `--outline: #b08a3a` (rules only, never text), `--secondary:
#1f5a44`. Raise the pinstripe opacity to about 0.08 so it still reads, and use
emerald `#1f3a31` only as a dark band behind the title block if it needs weight.
