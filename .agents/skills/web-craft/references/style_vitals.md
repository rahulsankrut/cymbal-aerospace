---
name: Vitals
slug: vitals
register: classic
mode: light
---

# Vitals

## Identity

**North Star: "Calm Confidence."** Clear human readings and reassuring
guidance: clean white, calm clinical teal, and healthy green set in a typeface
designed for legibility (`Atkinson Hyperlegible`), with `4px` status accent
bars, target reference-range bands, and soft corners. Reassuring and very readable — never clinical-cold, never
cutesy.

-   **Mood**: calm, trustworthy, plain-spoken, caring.
-   **Inspired by**: patient health portals, public-health reference guides,
    personal finance and benefits explainers, and accessible wellness tools.

## When to Use

-   **Best for**: health and wellness, test results and readings, benefits and
    insurance explainers, public-health information, care plans, personal
    finance or family guides, anything that needs to reassure and be very
    readable.
-   **Avoid for**: luxury, fashion, or nightlife; edgy or playful brands;
    literary or historical narratives; dense trading-style dashboards.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&family=Figtree:wght@300..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #ffffff;               /* clean white page and cards */
  --surface-container-low: #f1f7f8;    /* faint teal wash: page bands, inset panels */
  --surface-container: #e3f1f3;        /* pale teal: filled panels, hover fills */
  --surface-container-high: #d5e9ec;   /* selected rows, pressed states */

  /* Text */
  --on-surface: #1b2b33;               /* deep blue-slate: headlines and body */
  --on-surface-variant: #46585f;       /* slate: ledes, captions, labels */

  /* Rules */
  --outline: #7b9198;                  /* input borders, axis lines; never text */
  --outline-variant: #d5e3e5;          /* card hairlines and dividers; never text */

  /* Accents */
  --primary: #0f7c8a;                  /* calm teal: top bar, actions, links */
  --on-primary: #ffffff;
  --primary-container: #e3f1f3;        /* teal tint behind info notes and chips */
  --on-primary-container: #0a5560;     /* text on teal tints */
  --secondary: #1d5e3a;                /* deep green: text of reassurance chips */
  --tertiary: #2e7d4f;                 /* healthy green: status bars, in-range marks */
  --error: #b3261e;                    /* out of range, alerts */
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #0f7c8a;                   /* teal */
  --data-2: #2e7d4f;                   /* green */
  --data-3: #b86e00;                   /* amber: "worth watching" */
  --data-4: #5c5fb0;                   /* muted indigo */
  --data-context: #b8c7ca;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Figtree', sans-serif;
  --font-body: 'Atkinson Hyperlegible', sans-serif;
  --font-label: 'Figtree', sans-serif;

  /* Shape */
  --rounded: 0.625rem;                 /* buttons, inputs */
  --rounded-lg: 0.875rem;              /* cards and panels */
  --rounded-full: 9999px;              /* chips */

  /* Style effects */
  --top-bar: 6px solid var(--primary);
  --status-bar-width: 4px;
  --card-border: 1px solid var(--outline-variant);
  --card-lift: 0 1px 2px rgb(27 43 51 / 0.05), 0 6px 16px rgb(27 43 51 / 0.05);
}
```

## Color

-   **Proportions**: white and deep slate carry the page — roughly 85%. Pale
    teal washes and hairlines take another 10%. Teal is the signal (about 5%):
    the top bar, the primary action, links, the series that matters. Green
    appears only where something is healthy, on track, or confirmed.
-   **Color means status.** Teal is neutral and informational, green is
    healthy or in range, `--error` is out of range or needs action, amber
    (`--data-3`) is "worth watching". Never use green or red decoratively.
-   **Teal as text** only on `--background` and `--surface-container-low`
    (4.9:1 and 4.5:1). On `--surface-container` and other teal tints it drops
    to 4.25:1 — use `--on-primary-container` there.
-   **Never text**: `--outline`, `--outline-variant`, `--data-context`, and
    amber `--data-3` (4.0:1 — fine for marks and bars, not for words).
-   **Fills are soft and pale.** Separate with white cards on a faint teal
    wash, or hairline borders on white. No saturated panel backgrounds beyond
    the primary button.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Figtree | 800 (700 for small headings) | Tracking −0.015em; line height 1.05–1.15. Sentence case. |
| Body | Atkinson Hyperlegible | 400; 700 for emphasis | Step body up a notch: about 1.0625rem for narrative. Line height 1.6. |
| Ledes | Atkinson Hyperlegible | 400 | 1.05–1.15× body, `--on-surface-variant`, max 60ch. |
| Labels, kickers, nav | Figtree | 600; uppercase for small kickers | `--label-size`, tracking 0.06–0.08em. Buttons stay sentence case. |
| Key figures | Figtree | 800 | Large, lining tabular figures (`font-variant-numeric: tabular-nums`). |

Headlines are plain sentences, never all caps. Hierarchy comes from a heavy,
tight sans headline over open, generous body text — weight, not color, does
the work. Italic is for the rare emphasized term in body text only.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Status accent bar

Cards and key figures are white panels with a hairline border and a 4px bar on
the left whose color states meaning: teal for neutral or informational, green
for healthy or in range, error red for out of range. Applies to key-figure
cards, result cards, and callouts the content already has.

```css
.status-card {
  background: var(--background);
  border: var(--card-border);
  border-left: var(--status-bar-width) solid var(--primary);
  border-radius: var(--rounded-lg);
  padding: var(--space-md) var(--space-lg);
}
.status-card[data-status="ok"]    { border-left-color: var(--tertiary); }
.status-card[data-status="alert"] { border-left-color: var(--error); }
```

### 2. Teal top bar

A solid 6px teal band across the very top of the page, or of the primary
container in an embedded view. One per view: it is the style's header mark,
not a section divider.

```css
.page { border-top: var(--top-bar); }
```

### 3. Heavy plain-language headline

The title block pairs an 800-weight, tightly tracked Figtree headline with a
calm slate lede in the body face beneath it. Applies to the opening title and,
a step smaller, to section headings.

```css
.title {
  font-family: var(--font-headline);
  font-weight: 800;
  letter-spacing: -0.015em;
  line-height: 1.08;
  color: var(--on-surface);
}
.lede {
  font-size: 1.1em;
  line-height: 1.6;
  color: var(--on-surface-variant);
  max-width: 60ch;
  margin-top: var(--space-sm);
}
```

### 4. Reassurance chip

Status labels the content already has ("Verified", "In range", "Covered",
"Reviewed") become fully rounded chips: pale green fill, deep green semibold
text. Teal-tinted for informational labels, red-tinted for alerts.

```css
.chip {
  font-family: var(--font-label);
  font-weight: 600;
  font-size: var(--label-size);
  padding: var(--space-xs) var(--space-md);
  border-radius: var(--rounded-full);
  background: color-mix(in srgb, var(--tertiary) 14%, var(--background));
  color: var(--secondary);
}
.chip[data-status="info"]  { background: var(--primary-container); color: var(--on-primary-container); }
.chip[data-status="alert"] { background: color-mix(in srgb, var(--error) 10%, var(--background)); color: var(--error); }
```

### 5. Target / reference-range band

When a chart or meter shows a measure that has a target, benchmark, or recommended
range, shade that range as a pale green band behind the data so the reader sees
at once whether the value sits inside it.

```css
.range-band {
  fill: var(--tertiary);
  fill-opacity: 0.12;
  stroke: none;
}
```

## Composition

-   **Flush-left and orderly.** Title blocks, body, and grids share one left
    edge; this follows the skill's general preference for asymmetry. Key
    figures sit in an even row of equal cards.
-   **Comfortable density.** Generous line height and padding inside cards,
    moderate space between them — calm, never cramped, never so sparse it
    feels empty.
-   **Separation by cards and washes.** White cards with hairline borders, or
    a `--surface-container-low` band behind a group of white cards. Thin
    `--outline-variant` dividers between list entries; no heavy rules.
-   **Dashboards and tools** keep the top bar and status cards, tighten
    padding, and use the wash as the page background so white cards stand
    forward.

## Components

-   **Buttons**: `--rounded` corners, Figtree 600, sentence case, roomy
    padding. Primary is a teal fill with white text; secondary is a 1px teal
    outline with teal text on white. Hover darkens the fill, or gives the
    outline button a `--surface-container-low` fill.
-   **Key figures**: a status card (treatment 1) — small uppercase label in slate,
    the value large in Figtree 800, a one-line plain-language caption below in
    green or `--error` when it carries status, slate when neutral.
-   **Callouts**: `--primary-container` fill, `--rounded-lg`, teal status bar,
    text in `--on-primary-container`.
-   **Links**: teal, underlined with a 2px offset; the underline thickens on
    hover.
-   **Inputs**: white field, 1px `--outline` border, `--rounded` corners,
    Figtree 600 labels above; focus turns the border teal.
-   **Tables**: white, `--outline-variant` row dividers, header row on
    `--surface-container-low` in the label voice, tabular figures, status
    values as chips.
-   **Navigation and tabs**: Figtree 600 labels; the active item carries a 3px
    teal underline.

## Data Visualization

-   **Series**: `--data-1` (teal) for the series that matters, then green,
    amber, indigo. Context is `--data-context`. Status colors keep their
    meaning: green marks in range, `--error` marks out of range.
-   **Lines and marks**: 2–2.5px lines with round caps and joins; bars with
    small rounded top corners (about 3px); a filled circle on the latest
    value. No gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in `--font-label`,
    `--on-surface-variant`; horizontal gridlines only, solid 1px
    `--outline-variant`; no chart border.
-   **Labels and annotations**: label lines and values directly in Figtree
    600; thresholds and targets as dashed `--outline` lines with a
    plain-language label; normal ranges as a band (treatment 5).
-   **Chart titles**: Figtree 700, phrased as a plain sentence of what the
    chart shows.

## Motion

Gentle and functional: fade in with a small upward drift over `--dur-short`
with `--ease-out`; key figures and status bars may fill in once. No bounces,
pulses, or looping attention-grabbers — nothing that reads as alarm.

## Don'ts

-   No pure-black text and no harsh traffic-light dashboards; status colors
    stay calm and are used only for status.
-   No neon or saturated fills, gradients, or glassmorphism; no heavy shadows
    (`--card-lift` at most, for floating panels).
-   No sharp square corners and no pill-shaped cards; buttons and cards use
    the soft radii.
-   No cartoon illustration, emoji, or bubbly rounded display faces — it must
    reassure, not be cute.
-   Don't set body text in Figtree or headlines in Atkinson, and don't shrink
    body text to fit more in.
-   Don't repeat the top bar as a section divider.

## If the User Asks for Dark

Keep the same roles on a deep night-shift slate: `--background: #0f1a1f`,
`--surface-container-low: #15242a`, `--surface-container: #1c2e35`,
`--on-surface: #e6eff1`, `--on-surface-variant: #a9bcc2`, `--primary: #4fb8c6`
with `--on-primary: #0f1a1f`, `--on-primary-container: #bfe6eb`, `--tertiary:
#5cbf85`, `--secondary: #9fdcb7`, `--error: #f2867c`, `--outline-variant:
#2c4048`. Keep the top bar and status bars; drop `--card-lift`.
