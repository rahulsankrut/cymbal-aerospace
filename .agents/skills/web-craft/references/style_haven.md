---
name: Haven
slug: haven
register: classic
mode: light
---

# Haven

## Identity

**North Star: "Quiet Sufficiency."** A calm, uncluttered domestic and everyday
refuge: cool pale mist-gray, soft black, muted slate and sage. Light geometric
headlines, hairline borders, small radii, and no shadows. Calm, functional,
and quietly considered. Nothing is loud, but everything is deliberate. It
should never feel sterile or clinical.

-   **Mood**: calm, functional, warm-minimal, unhurried.
-   **Inspired by**: warm-minimal architectural interiors, natural linen and
    pale timber craft, tactile planners and stationery, and sunlit domestic
    spaces.

## When to Use

-   **Best for**: lifestyle, wellbeing, home and interiors, how-to guides,
    calm planners and trackers, everyday utility tools, gentle explainers.
-   **Avoid for**: urgent or high-drama content, luxury or ceremonial
    occasions, loud marketing, content that needs a strong historical or
    literary voice.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&family=Hanken+Grotesk:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
```

`:root` block: start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: light;

  /* Page and surfaces */
  --background: #f5f6f5;               /* cool pale gray, like limewashed walls */
  --surface-container-low: #ffffff;    /* white panels: cards, inputs, the main tool */
  --surface-container: #e3ebe2;        /* sage mist: tags, a rare tinted panel */
  --surface-container-high: #dbe2dd;   /* hover and selected rows */

  /* Ink */
  --on-surface: #23272a;               /* soft black */
  --on-surface-variant: #5c6468;       /* stone gray: captions, secondary text */

  /* Rules */
  --outline: #c9d0cc;                  /* control borders: inputs, secondary buttons; never text */
  --outline-variant: #dde2df;          /* hairline: card borders, dividers; never text */

  /* Accents */
  --primary: #3c5a6e;                  /* muted slate blue */
  --on-primary: #ffffff;
  --primary-container: #e2e9ee;        /* pale slate: selected states, a highlighted panel */
  --on-primary-container: #2a4152;
  --secondary: #4f6b53;                /* deep sage: captions that need warmth, tags */
  --tertiary: #5f7c63;                 /* sage: fills, marks, data; never text */
  --error: #a63d32;                    /* muted brick */
  --on-error: #ffffff;

  /* Data series, in order of use */
  --data-1: #3c5a6e;                   /* slate */
  --data-2: #5f7c63;                   /* sage */
  --data-3: #a8694a;                   /* clay */
  --data-4: #8a7a68;                   /* oak */
  --data-context: #c3cac6;             /* context series and gridlines */

  /* Fonts */
  --font-headline: 'Outfit', sans-serif;
  --font-body: 'Hanken Grotesk', sans-serif;
  --font-label: 'Outfit', sans-serif;

  /* Shape */
  --rounded: 0.375rem;
  --rounded-lg: 0.5rem;
  --rounded-full: 9999px;

  /* Style effects */
  --hairline: 1px solid var(--outline-variant);
  --hairline-control: 1px solid var(--outline);
  --elevation: none;                   /* Haven has no shadows */
}
```

## Color

-   **Proportions**: pale gray, white, and soft black carry the page, roughly
    90% of what the reader sees. Slate is the signal (under 5%): the primary
    action, links, the active state, the data series that matters. Sage is
    the quiet second voice: captions, tags, the second series.
-   **Light sage is never text.** `--tertiary` is 4.3:1 on the page, so it is
    for fills, chart marks, and small icons only. Sage text uses
    `--secondary`.
-   **`--outline` and `--outline-variant` are never text.** They are borders
    and hairlines.
-   **Layer by value, not color.** White panels sit on the pale gray page; the
    difference is small and that is the point. Use sage mist
    (`--surface-container`) for tags and at most one tinted panel per view.
-   **Everything is muted.** No saturated hues, no gradients, no pure black.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Outfit | 300–400; 600 for the emphasized phrase | Tracking −0.02em. Line height 1.05–1.15. |
| Subheads | Outfit | 500 | Tracking −0.01em. |
| Body | Hanken Grotesk | 400; 400 italic for emphasis | Line height 1.6. |
| Labels, kickers, nav | Outfit | 500, sentence case | Label size, tracking 0.01–0.02em. Not uppercase. |
| Key figures | Outfit | 500 | Large, tracking −0.02em; `font-variant-numeric: tabular-nums` in tables and charts. |
| Captions | Hanken Grotesk | 500 | Small, in `--on-surface-variant` or `--secondary`. |

Headlines are sentence case or title case, never all caps. Weight contrast
comes from a light, large geometric display over medium-weight labels and
figures. Labels stay sentence case, which overrides the skill's general
uppercase-label default: in Haven the label voice comes from family and
weight, not capitals.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Light headline, one weighted phrase

The opening title and section headings are set light in Outfit, with the
phrase that carries the meaning raised to 600. Use it on the title block and on
major section headings, one weighted phrase per heading at most, and only on
words already in the heading.

```css
.headline {
  font-family: var(--font-headline);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.08;
  color: var(--on-surface);
}
.headline b, .headline strong { font-weight: 600; }
```

### 2. Hairline panel

Containers are white panels on the pale gray page with a 1px hairline border,
an 8px radius, and no shadow. Use it for cards, key-figure tiles, the primary
tool container, and form groups. This is the only container treatment.

```css
.panel {
  background: var(--surface-container-low);
  border: var(--hairline);
  border-radius: var(--rounded-lg);
  box-shadow: var(--elevation);
  padding: var(--space-md) var(--space-lg);
}
```

### 3. Quiet sentence-case label

Kickers, card labels, table headers, and axis labels are small Outfit at 500 in
sentence case with barely-open tracking, in stone gray. Use it wherever the
artifact has a label.

```css
.label {
  font-family: var(--font-label);
  font-size: var(--label-size);
  font-weight: 500;
  letter-spacing: 0.015em;
  text-transform: none;
  color: var(--on-surface-variant);
}
```

### 4. Sage caption

The short line under a key figure, or the subtitle under the title, is set in
deep sage. It gives a little warmth beside slate and soft black. Use it only
for text the content already has.

```css
.caption-sage {
  font-family: var(--font-body);
  font-weight: 500;
  color: var(--secondary);
  margin-top: var(--space-xs);
}
```

### 5. Hairline section divide

Sections are separated by a full-width hairline and generous space, not by
fills or bands. Use it between major sections and above a footer.

```css
.section + .section {
  border-top: var(--hairline);
  padding-top: var(--space-2xl);
  margin-top: var(--space-2xl);
}
```

## Composition

-   **Flush-left grid.** Titles, labels, panels, and buttons align to a
    common left edge, with generous, even side margins. This follows the
    skill's preference for asymmetry: a wide main column beside a narrower
    one, or key-figure tiles of unequal width.
-   **Airy but orderly.** Narrative pages are spacious, with wide margins and
    large gaps between sections. Dashboards and tools are moderately dense,
    but panels always keep comfortable inner padding.
-   **Separation by value and hairlines.** Content separates with white
    hairline panels on the gray page, hairline dividers, and space. Never use
    shadows, and never nest a panel inside a panel.
-   **Body text** sits left-aligned in a measure of 60–68ch.

## Components

-   **Buttons**: 6px radius. Primary is a slate fill with white text; secondary
    is transparent with a `--outline` border and soft-black text. Label in
    Outfit 500, sentence case. Hover darkens the fill or adds a
    `--surface-container-high` background. No shadows.
-   **Key figures**: in a hairline panel. A quiet sentence-case label, the
    value in large Outfit 500, and a short sage caption.
-   **Tags**: sage-mist fill (`--surface-container`), deep-sage text in Outfit
    500, fully rounded, no border.
-   **Links**: slate, with a 1px underline offset 3px. The underline thickens
    on hover.
-   **Inputs**: white field, `--outline` border, 6px radius. Focus turns the
    border slate and adds the focus ring.
-   **Tables**: no vertical lines and no zebra stripes. Hairlines between rows,
    header cells in the label voice, tabular figures, and hover rows in
    `--surface-container-high`.
-   **Navigation**: sentence-case labels in Outfit. The active item is slate
    with a 2px slate underline.

## Data Visualization

-   **Series**: `--data-1` (slate) for the series that matters, then sage,
    clay, and oak. Everything that is context is `--data-context`.
-   **Lines and marks**: 2px lines with round caps and joins. Bars have a
    2px radius on the top corners. Use flat fills only: no gradients, glows,
    or 3D.
-   **Axes and gridlines**: axis labels in the label voice. Gridlines are
    solid hairlines in `--outline-variant`, horizontal only. No chart
    border.
-   **Labels and annotations**: label series directly at their ends in Outfit
    500 (slate, or deep sage `--secondary` for the sage series). Annotations
    use body text in stone gray.
-   **Chart container**: charts sit inside a hairline panel, with the title in
    Outfit 500 at the top left.

## Motion

Calm and brief: fade in with a short upward drift over `--dur-short` to
`--dur-long` with `--ease-out`. Hovers are quick color shifts over
`--dur-micro`. No bounces, springs, parallax, or scale effects.

## Don'ts

-   No drop shadows, glows, or elevated cards. The hairline does the work.
-   No uppercase, widely tracked labels. That voice belongs to other styles.
-   No heavy (700+) headlines across a whole title. Only one phrase gets 600.
-   No saturated accents, pure black, gradients, or colored page backgrounds.
-   No large radii or pill-shaped cards. Corners stay 6–8px, and only tags
    and avatars are fully round.
-   Don't set light sage (`--tertiary`) as text, and don't fill several panels
    with sage mist.

## If the User Asks for Dark

Keep the same roles on a winter-evening ground: `--background: #1c2023`,
`--surface-container-low: #24292d`, `--on-surface: #e6e9e7`,
`--on-surface-variant: #a9b2b6`, `--primary: #9db8cc` (a lighter slate that
keeps 4.5:1, with `--on-primary: #1c2023`), `--secondary: #a6c2aa`,
`--outline-variant: #343b40`. Keep hairlines, with no shadows or glows.
