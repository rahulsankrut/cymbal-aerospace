---
name: Charter
slug: charter
register: classic
mode: light
---

# Charter

## Identity

**North Star: "Stewardship in Navy and Brass."** An institutional annual report
or executive charter: a full-bleed deep navy title band (`#14213d`) edged in
burnished brass over warm cream paper. Upright Caslon headlines over a
crisp sans body with tabular figures, numbers set with the quiet authority of a
signed statement. Trustworthy and expensive — never flashy, never corporate-bland.

-   **Mood**: assured, formal, discreet, precise.
-   **Inspired by**: private-bank annual reports, institutional investment
    letters, executive strategy briefings, and formal advisory memos.

## When to Use

-   **Best for**: reports, financial summaries, formal briefs, investment and
    portfolio reviews, legal or policy memos, board and strategy documents,
    KPI dashboards for an executive audience.
-   **Avoid for**: playful or children's content, consumer product launches,
    creative or cultural features, anything casual, loud, or experimental.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Inter:wght@100..900&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f7f4ec;               /* warm cream paper */
  --surface-container-low: #fffdf8;    /* bright leaf: figure cards, panels */
  --surface-container: #ece5d4;        /* deeper cream: secondary buttons, a rare filled band */
  --surface-container-high: #e3dac4;   /* table header band, hover fill */

  /* Ink */
  --on-surface: #1c1f26;               /* near-black ink */
  --on-surface-variant: #4f5360;       /* graphite: captions, secondary text */

  /* Rules */
  --outline: #b08d57;                  /* brass: rules and borders; text only on navy */
  --outline-variant: #d9cfb8;          /* pale brass: hairline dividers, never text */

  /* Accents */
  --primary: #14213d;                  /* deep navy: title band, primary action, links */
  --on-primary: #f7f4ec;               /* cream on navy */
  --primary-container: #e3e6ee;        /* pale navy wash: selected row, active state */
  --on-primary-container: #14213d;
  --secondary: #2d5a4a;                /* bottle green: favorable notes, second voice */
  --tertiary: #8a6a35;                 /* dark brass: small accent text on cream/leaf only */
  --error: #9b2c2c;
  --on-error: #f7f4ec;

  /* Data series, in order of use */
  --data-1: #14213d;                   /* navy */
  --data-2: #8a6a35;                   /* dark brass */
  --data-3: #2d5a4a;                   /* bottle green */
  --data-4: #5b7aa0;                   /* slate blue */
  --data-context: #c2bba9;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Libre Caslon Text', serif;
  --font-body: 'Inter', sans-serif;
  --font-label: 'Inter', sans-serif;

  /* Shape */
  --rounded: 0.125rem;
  --rounded-lg: 0.125rem;
  --rounded-full: 0.125rem;            /* even tags stay squared: no pills */

  /* Style effects */
  --brass-rule: 2px solid var(--outline);
  --hairline: 1px solid var(--outline-variant);
  --leaf-underline: 0 1px 0 var(--outline-variant);
}
```

## Color

-   **Proportions**: cream and ink carry the page — roughly 85%. Navy is the
    institution's voice (about 10%): the title band, the primary action, links,
    and the series that matters. Brass is the hallmark (under 5%): rules,
    borders, and the emphasized phrase of the title.
-   **Brass is never text on cream.** `--outline` is 2.8:1 on cream — rules and
    borders only. On navy it passes (5.2:1); the title band lightens it toward
    cream with `color-mix(in srgb, var(--outline) 75%, var(--on-primary))`
    (6.9:1). Small warm text on cream (deltas, tags) uses `--tertiary`, and
    only on `--background` or `--surface-container-low` — it falls below 4.5:1
    on `--surface-container`.
-   **Green is for meaning, not decoration**: favorable deltas, positive
    notes, the third data series. Losses use `--error`, sparingly.
-   **Fills are restrained.** The bright leaf (`--surface-container-low`) holds
    figures and panels; the deeper cream is for secondary buttons and table
    headers. The only dark fill is navy, reserved for the title band and
    primary buttons.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Libre Caslon Text | 400 roman | Regular weight, not bold — authority from size and the serif, not mass. Tracking −0.01em at display sizes. Line height 1.06–1.15. |
| Small headings | Libre Caslon Text | 700 | Subhead size; the only place bold Caslon appears. |
| Body | Inter | 400; 600 for inline emphasis | 16–17px narrative, 15px in tools. Line height 1.55–1.65. |
| Labels, kickers, nav | Inter | 500–600, uppercase | 0.75–0.8rem, tracking 0.06–0.08em. |
| Key figures | Libre Caslon Text | 400 | Large, `font-variant-numeric: tabular-nums lining-nums`. |
| Table and chart figures | Inter | 400–500 | `tabular-nums`, right-aligned in columns. |

Headlines are title case or sentence case, never all caps. The contrast is a
large, regular-weight classical serif over small, tracked, upright sans labels.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Navy title band

The opening title block sits on a full-width navy band: cream headline and muted
cream for the lede. Once per artifact — it is the cover of the report. In
dashboards and tools it shrinks to a compact header strip with the same colors.

```css
.title-band {
  background: var(--primary);
  color: var(--on-primary);
  padding: var(--space-2xl) var(--space-xl) var(--space-xl);
  border-bottom: 3px solid var(--outline);
}
.title-band .lede {
  color: color-mix(in srgb, var(--on-primary) 78%, var(--primary));
}
```

### 2. Upright Caslon title with a brass bottom rule

Set the opening title and section headlines in regular-weight `Libre Caslon Text`
(`400` roman) with a `1px` burnished-brass rule beneath the title block.

```css
.title-band h1 {
  font-family: var(--font-headline);
  font-weight: 400;
  color: var(--on-primary);
}
```

### 3. Brass top rule on figures

Key figures and summary cards are a bright leaf with a 2px brass rule across the
top and a pale hairline beneath — like a tab in a bound report. Applies to
key-figure rows, summary cards, and the primary panel of a tool.

```css
.figure-card {
  background: var(--surface-container-low);
  border-top: var(--brass-rule);
  box-shadow: var(--leaf-underline);
  border-radius: var(--rounded-lg);
  padding: var(--space-md) var(--space-lg);
}
```

### 4. Statement figures

Numbers are set like a signed statement: the value in regular-weight Caslon with
tabular lining figures, a small uppercase label above in graphite, and the
delta below in dark brass (or green when favorable). Applies wherever the
content has a headline number.

```css
.figure-value {
  font-family: var(--font-headline);
  font-weight: 400;
  font-variant-numeric: tabular-nums lining-nums;
  color: var(--on-surface);
}
.figure-delta { color: var(--tertiary); font-weight: 600; margin-top: var(--space-xs); }
```

### 5. Brass section rule

Section openings carry a brass rule above the heading and a pale hairline under
it, so the page reads as a sequence of ruled schedules. Applies to section
headings and chart titles.

```css
.section-head {
  border-top: var(--brass-rule);
  padding-top: var(--space-md);
  border-bottom: var(--hairline);
  padding-bottom: var(--space-sm);
}
```

## Composition

-   **Flush left on a firm grid.** Headings, figures, and text align to a left
    edge with consistent columns, like a printed annual report. This follows
    the skill's preference for asymmetry: a wide main column beside a narrower
    notes or figures column reads as the house layout.
-   **Measured density.** Moderately dense — more than a literary narrative,
    less than a trading terminal. Even, generous gutters; nothing crammed.
-   **Separation by rules and leaves.** Sections are divided by brass and pale
    hairlines; groupings that need an object use the bright leaf with its brass
    top rule. No heavy boxes and no containers inside containers.
-   **Dashboards and tools** keep the navy header strip and ruled sections;
    figure rows become a tight grid of leaf cards.

## Components

-   **Labels above headings** (when used): Inter caps, tracked 0.06–0.08em, in
    brass; on the title band, brass on navy.
-   **Buttons**: 2px corners. Primary is a navy fill with cream text; secondary
    is a 1px navy outline on transparent with navy text. Labels in Inter 500,
    tracked 0.04em, sentence case. Hover deepens the fill or tints the outline
    button with `--primary-container`; no shadows.
-   **Tags**: a 1px brass outline, transparent fill, dark-brass text, squared
    corners — a stamp, not a pill.
-   **Links**: navy, with a brass underline offset 3px; hover thickens the
    underline.
-   **Inputs**: leaf fill, 1px `--outline-variant` border, 2px corners; focus
    turns the border navy and adds the focus ring.
-   **Tables**: the style's natural habitat. No vertical lines; a
    `--surface-container-high` header band in the label voice; pale hairlines
    between rows; a brass rule above totals. Figures right-aligned, tabular.
-   **Navigation and contents**: uppercase tracked labels, the active item
    underlined in brass.

## Data Visualization

-   **Series**: `--data-1` (navy) for the series that matters, then dark brass,
    bottle green, slate blue. Everything that is context is `--data-context`.
-   **Lines and marks**: 2px lines, flat bars with 0–2px corners, small square
    or circular endpoints. No gradients, glows, or 3D.
-   **Axes and gridlines**: axis labels in Inter at label size, tabular
    figures; gridlines 1px in `--outline-variant`; a single brass baseline at
    zero; no chart border.
-   **Labels and annotations**: label series directly at line ends;
    annotations in small graphite Inter with a thin ink leader line.
-   **Chart titles**: Caslon, with the brass section rule above.

## Motion

Composed and brief: fade in with a slight upward drift over `--dur-short` with
`--ease-out`; key figures may count up once. No bounces, springs, parallax, or
scale effects.

## Don'ts

-   No bold Caslon at display sizes — the regular weight is the voice.
-   No pill shapes, large radii, or soft drop shadows; corners stay at 2px.
-   No brass text on cream, and no gold gradients or metallic sheen — brass is
    a flat hairline.
-   Don't spread navy fills beyond the title band and primary buttons; navy
    panels everywhere turn the report into a corporate template.
-   No proportional figures in tables or figure cards; columns of numbers must
    align.
-   Don't center the page like an invitation; Charter is flush-left.

## If the User Asks for Dark

Keep the same roles on a midnight-navy ground: `--background: #10172a`,
`--surface-container-low: #1a2338`, `--on-surface: #ece6d8`,
`--on-surface-variant: #a9afbd`, `--primary: #c2cbe0` (pale navy-silver,
10.9:1) with `--on-primary: #14213d`, `--outline: #c9ad7a`, `--tertiary:
#c9ad7a` (brass becomes readable text, 8.3:1), `--secondary: #8fb3a3`. The

title band uses `--surface-container-high` instead of navy, with labels and
italic emphasis in plain `--outline` (the cream mix no longer applies).
