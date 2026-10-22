---
name: Moderne
slug: moderne
register: expressive
mode: light
---

# Moderne

## Identity

**North Star: "Optimism, Moulded."** Warm mid-century modern print: cream stock,
flat inks of mustard, teal, and burnt orange, a bold high-contrast display
serif, and a round, friendly geometric sans. Asymmetric leaf-shaped corners,
pill buttons, and overlapping circles that multiply where they meet, like offset
inks laid one on another. Cheerful, crafted, and grown-up — never kitsch, retro
pastiche, or cartoonish.

-   **Mood**: optimistic, warm, crafted, confident.
-   **Inspired by**: 1950s–60s modernist graphic design, screen-printed book
    jackets and title cards, and mid-century exhibition catalogues.

## When to Use

-   **Best for**: design and culture history, food and recipes, home and
    interiors, friendly explainers, product and object stories, light
    personal planners and trackers.
-   **Avoid for**: somber or sensitive subjects, dense financial or technical
    dashboards, legal or medical content, anything that must feel neutral or
    institutional.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Lexend:wght@100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f4ecdc;               /* warm cream stock */
  --surface-container-low: #fbf6ea;    /* lighter cream, for inset panels and inputs */
  --surface-container: #e9dcc0;        /* sand, for a filled panel or tertiary button */
  --surface-container-high: #e0cfaa;   /* toasted sand, for hover on sand */

  /* Ink */
  --on-surface: #2b2a26;               /* warm near-black ink */
  --on-surface-variant: #55524a;       /* soft ink: captions, labels, secondary text */

  /* Rules */
  --outline: #2b2a26;                  /* ink: the 2px borders on leaves and inputs */
  --outline-variant: #d9cdb3;          /* pale sand: hairline dividers, never text */

  /* Accents */
  --primary: #1f6f6b;                  /* deep teal: primary action, links */
  --on-primary: #ffffff;
  --primary-container: #bcd9d2;        /* sage: the second leaf's fill */
  --on-primary-container: #17504d;     /* deep teal text on sage */
  --secondary: #ad431b;                /* burnt orange, deepened for text: accent word, secondary button */
  --tertiary: #e0a526;                 /* mustard: fills and orbs only, never text */
  --error: #9a1f3a;                    /* raspberry, kept distinct from the orange */
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #1f6f6b;                   /* teal */
  --data-2: #d9572b;                   /* bright burnt orange: marks and orbs only */
  --data-3: #a87710;                   /* deep mustard, dark enough for marks */
  --data-4: #6b4a2e;                   /* walnut */
  --data-context: #a39880;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'DM Serif Display', serif;
  --font-body: 'Lexend', sans-serif;
  --font-label: 'Lexend', sans-serif;

  /* Shape */
  --rounded: 9999px;                              /* pills: buttons, inputs */
  --rounded-lg: 2.25rem 0.5rem 2.25rem 0.5rem;    /* the leaf */
  --rounded-full: 9999px;

  /* Style effects */
  --ink-border: 2px solid var(--outline);
  --leaf-mirror: 0.5rem 2.25rem 0.5rem 2.25rem;   /* the leaf, flipped */
  --orb-r: 2.25rem;
  --orb-r-small: 1.75rem;
  --orb-clearance: 10rem;                         /* keeps title text clear of the orbs */
  --orbs:
    radial-gradient(circle at calc(100% - 4.375rem) 4.5rem, color-mix(in srgb, var(--data-2) 90%, transparent) var(--orb-r-small), transparent calc(var(--orb-r-small) + 1px)),
    radial-gradient(circle at calc(100% - 6.25rem) 3.625rem, color-mix(in srgb, var(--primary) 85%, transparent) var(--orb-r), transparent calc(var(--orb-r) + 1px)),
    radial-gradient(circle at calc(100% - 8.75rem) 4.375rem, var(--tertiary) var(--orb-r), transparent calc(var(--orb-r) + 1px));
}
```

## Color

-   **Proportions**: cream and ink carry the page — roughly 75%. The inks
    share the rest as flat, confident blocks: teal for action and the lead
    data series, mustard wash and sage as leaf fills, burnt orange as the one
    hot accent (under 5%: a headline word, the secondary button).
-   **Flat spot inks.** Every color is solid, as if printed in spot colors.
    Where two colors overlap (the orbs, overlapping chart marks) they
    multiply rather than stack opaquely.
-   **Mustard is never text** (1.9:1 on cream); it fills leaves, orbs, and
    chart areas. The bright orange `--data-2` (3.3:1) is a mark color only;
    orange text and the orange button use `--secondary`.
-   **Teal and orange text sit only on cream** (`--background`,
    `--surface-container-low`). On sand, sage, or mustard fills, text is ink.
-   **Light fills tint, never shout.** The mustard leaf is mustard mixed 45%
    into cream; the sage is `--primary-container`. Full-strength mustard and
    orange cover small areas only.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | DM Serif Display | 400 (its only weight) | Large and tight: tracking −0.01em, line height 1.05–1.1, title measure about 15ch. |
| Body | Lexend | 400; 500 for emphasis | At least 17px for narrative. Line height 1.6. Lexend sets wide: keep the measure to 60–65ch. |
| Labels, kickers, nav | Lexend | 500, uppercase | 0.75rem, tracking 0.08em, in `--on-surface-variant`. |
| Sub-headline, north-star line | Lexend | 500 | 1–1.1× body, in `--primary`. |
| Quotations | DM Serif Display | 400 italic | 1.3–1.5× body, in ink. |
| Figures | DM Serif Display for key figures; Lexend in tables and charts | 400 | Tabular lining figures (`font-variant-numeric: tabular-nums`) in tables and charts. |

Headlines are title case or sentence case, never all caps, in solid warm
charcoal ink (`--on-surface`). Hierarchy comes from the jump between the
high-contrast serif and the light, round sans; the display face has one weight,
so never fake-bold it, and never set body in it.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Leaf cards with ink borders

The primary containers — key-figure cards, the main panel of a tool, a row of
feature cards — get a 2px ink border and the leaf shape: two opposite corners
large, two small. In a row, alternate the fill (mustard wash, then sage) and
flip every other leaf, so the row reads like a set of moulded shells.

```css
.leaf {
  border: var(--ink-border);
  border-radius: var(--rounded-lg);
  padding: var(--space-lg);
  background: color-mix(in srgb, var(--tertiary) 45%, var(--background));
  color: var(--on-surface);
}
.leaf:nth-child(even) {
  border-radius: var(--leaf-mirror);
  background: var(--primary-container);
}
```

### 2. Multiplied orbs on the title block

Three overlapping circles — mustard, teal, orange — painted into the top-right
corner of the opening title block's own background and blended with multiply,
so their overlaps darken like overprinted ink. Only on the title block, once
per artifact; the title text keeps clear of them.

```css
.title-block {
  background-color: var(--background);
  background-image: var(--orbs);
  background-blend-mode: multiply;
  background-repeat: no-repeat;
  padding: var(--space-xl);
}
.title-block > * { padding-inline-end: var(--orb-clearance); }
```

### 3. Pills and ink chips

Buttons and inputs are full pills: the primary a teal fill, the secondary a
burnt-orange fill, both with white text. Tags are small ink pills with cream
text — the dark counterweight to all the warm color.

```css
.btn { border-radius: var(--rounded); padding: var(--space-sm) var(--space-lg); font-family: var(--font-label); font-weight: 500; }
.btn-primary { background: var(--primary); color: var(--on-primary); }
.btn-secondary { background: var(--secondary); color: var(--on-primary); }
.chip { border-radius: var(--rounded-full); background: var(--on-surface); color: var(--background); padding: var(--space-xs) var(--space-md); }
```

## Composition

-   **Flush-left and offset.** Text aligns left on a loose grid; the title
    block is weighted left, with the orbs balancing it on the right. Leaves
    sit in rows of two or three, unequal in width where the content allows.
    This follows the skill's general preference for asymmetry.
-   **Medium density, generous gutters.** Roomy section spacing
    (`--space-2xl` and up in narratives), comfortable padding inside leaves.
-   **Separation by color blocks and ink lines.** Content is grouped in
    filled, ink-bordered leaves or divided by pale sand hairlines; no
    shadows. Running text sits directly on cream, not inside cards.
-   **Dashboards and tools** keep leaves for key figures and the main panel,
    tighten leaf padding to `--space-md`, and use the orbs only if the view
    has a real title block.

## Components

-   **Labels above headings** (when used): a compact burnt-orange
    (`--secondary`) stamp with cream uppercase Lexend.
-   **Buttons**: pills, Lexend 500, sentence case. Teal primary,
    burnt-orange secondary, and a tertiary in sand (`--surface-container`)
    with ink text. Hover deepens the fill a step; no shadows or lifts.
-   **Key figures**: in leaves — an uppercase label in soft ink, the value
    large in DM Serif Display, a short Lexend 500 caption in ink.
-   **Tags**: ink pills with cream text.
-   **Links**: teal, with a 2px underline offset 3px; on hover the underline
    turns burnt orange.
-   **Inputs**: pill-shaped fields on `--surface-container-low` with the 2px
    ink border; text areas take `--rounded-lg`.
-   **Tables**: no vertical lines; a 2px ink rule under the header, sand
    hairlines between rows, header cells in the label voice. A highlighted
    row takes the mustard wash.
-   **Navigation and tabs**: a row of pills; the active pill is ink with
    cream text.

## Data Visualization

-   **Series**: `--data-1` teal for the series that matters, then orange,
    deep mustard, walnut. Context is `--data-context`.
-   **Marks**: flat fills; bars with fully rounded ends or leaf-cornered tops;
    2.5px lines with round caps; generous dot markers. Overlapping areas and
    bubbles use `mix-blend-mode: multiply` at 85–90% opacity, echoing the
    orbs. No gradients, glows, or 3D.
-   **Axes and gridlines**: a 2px ink baseline; other gridlines in
    `--outline-variant`; axis labels in Lexend at label size, soft ink.
-   **Labels and annotations**: direct labels in Lexend 500 beside the marks;
    a callout value in DM Serif Display.
-   **Chart titles**: DM Serif Display in ink, left-aligned above the plot.

## Motion

Buoyant but brief: entries fade in and rise a short distance over
`--dur-long` with `--ease-out`, staggered across a row of leaves like cards
being dealt. No bounces, wobbles, or spinning orbs.

## Don'ts

-   Don't round every corner equally: the leaf (two big, two small) is the
    shape. Uniform rounded rectangles look like a generic app.
-   No gradients, drop shadows, or glows; colors are flat spot inks.
-   No circles, boomerangs, or atomic starbursts anywhere but the title
    block's orbs — no extra shapes to "add retro".
-   Don't use full-strength mustard or orange as large backgrounds, and never
    set text in mustard.
-   No script, slab, or novelty "retro" fonts, and don't bold or all-caps DM
    Serif Display.
-   Don't color more than one word orange per headline.

## If the User Asks for Dark

Keep the same roles on a walnut-espresso ground: `--background: #221d18`,
`--surface-container-low: #2b251f`, `--on-surface: #f4ecdc`,
`--on-surface-variant: #c9bea8`, `--outline: #f4ecdc`, `--primary: #6cc1b8`
with `--on-primary: #10302d` (also the secondary button's text),
`--secondary: #f08a5d`, `--primary-container: #1f4a47`. Leaves become deep
teal and dark mustard (`color-mix(in srgb, var(--tertiary) 30%,
var(--background))`) with cream text; the orbs and chart overlaps switch to
`screen` blending.
