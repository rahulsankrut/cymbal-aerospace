---
name: Neon Noir
slug: neon_noir
register: expressive
mode: dark
---

# Neon Noir

## Identity

**North Star: "Electric Nightscape."** A rain-slicked metropolis after
midnight: blue-black sky, signage in hot pink and cyan bleeding light into the
dark, a terminal readout in the corner. Geometric headlines, monospaced labels,
thin lit borders, and glows that stay soft and diffused. Futuristic, immersive,
high-energy — never a rave flyer, never a wall of rainbow.

-   **Mood**: electric, nocturnal, immersive, retro-futurist.
-   **Inspired by**: cyberpunk film and anime, neon-lit nightscapes, synthwave
    album art, sci-fi heads-up displays.

## When to Use

-   **Best for**: gaming, music and nightlife, esports and streaming stats,
    tech launches and developer tools, sci-fi and cyberpunk topics, hackathons,
    dense dark dashboards and monitoring views.
-   **Avoid for**: formal, institutional, medical, or financial reporting;
    grief or quiet personal stories; content for young children; anything
    that should feel calm, warm, or traditional.

## Setup

Font link:

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

`:root` block — start from this, then complete it with the shared tokens in
**references/design_foundation.md**:

```css
:root {
  color-scheme: dark;

  /* Page and surfaces: hierarchy by lightness, darkest at the base */
  --background: #0a0a12;               /* near-black with a blue undertone */
  --surface-container-low: #111118;    /* inset panels, table bands */
  --surface-container: #141422;        /* cards and the primary container */
  --surface-container-high: #1e1e30;   /* raised: menus, active rows, tooltips */

  /* Text */
  --on-surface: #e8e0f0;               /* cool lavender-white: body and headlines */
  --on-surface-variant: #a098b0;       /* muted lavender: captions, secondary text */

  /* Lines */
  --outline: #5a5068;                  /* borders and axes, never text */
  --outline-variant: #302840;          /* hairline dividers, gridlines */

  /* Neon accents */
  --primary: #ff2d78;                  /* hot pink: primary action, focus, active, key figure */
  --on-primary: #1a0010;               /* text on a rare pink fill */
  --primary-container: #b3004e;        /* deep magenta: selected fills, badges */
  --on-primary-container: #ffe0ec;
  --secondary: #00ffcc;                /* cyan: links, secondary actions, highlights */
  --tertiary: #ffe04a;                 /* neon yellow: badges, warnings, emphasis */
  --error: #ff4444;
  --on-error: #1a0000;

  /* Data series, in order of use */
  --data-1: #ff2d78;                   /* hot pink */
  --data-2: #00ffcc;                   /* cyan */
  --data-3: #ffe04a;                   /* neon yellow */
  --data-4: #b388ff;                   /* ultraviolet */
  --data-context: #6e6680;             /* context series */

  /* Fonts */
  --font-headline: 'Sora', sans-serif;
  --font-body: 'Inter', sans-serif;
  --font-label: 'Space Mono', monospace;

  /* Shape: barely softened, like machined panels */
  --rounded: 0.125rem;
  --rounded-lg: 0.25rem;
  --rounded-full: 0.75rem;             /* the style's softest corner; not a pill */

  /* Style effects */
  --glow-text: 0 0 8px currentColor;
  --glow-primary: 0 0 16px color-mix(in srgb, var(--primary) 40%, transparent);
  --glow-secondary: 0 0 16px color-mix(in srgb, var(--secondary) 35%, transparent);
  --neon-border: 1px solid color-mix(in srgb, var(--primary) 30%, transparent);
  --neon-border-lit: 1px solid color-mix(in srgb, var(--primary) 50%, transparent);
  --neon-inset: inset 0 0 12px color-mix(in srgb, var(--primary) 10%, transparent);
  --glow-line: drop-shadow(0 0 4px currentColor);
  --scanlines: repeating-linear-gradient(to bottom, transparent 0 3px, color-mix(in srgb, var(--on-surface) 3%, transparent) 3px 4px);
}
```

## Color

-   **Proportions**: the night carries the page — dark surfaces and lavender
    text are roughly 90% of what the reader sees. Neon is the light source,
    under 10%: borders, labels, the key figure, the primary action, the
    series that matters.
-   **Neon never fills large areas.** No pink hero bands, no cyan panels. A
    neon fill is only ever as large as a badge or a selected chip; buttons
    stay dark with a neon border.
-   **Two neons per view.** Pink leads and cyan answers; yellow stands in for
    one of them when the view needs a badge or warning. Body text is always
    neutral lavender, never neon.
-   **Depth from lightness, not shadow.** Each step up the surface scale is a
    little lighter and bluer; the background is always the darkest thing.
-   **`--outline` and `--outline-variant` are never text** (2.6:1 and 1.4:1);
    they are borders, axes, and gridlines.

## Typography

| Role | Family | Weight / style | Size and spacing |
|---|---|---|---|
| Display, headlines | Sora | 700–800 | Tracking −0.02 to −0.03em at display size; line height 1.05–1.15. |
| Section headings | Sora | 600–700 | −0.01em; sentence case. |
| Body | Inter | 400; 500 for emphasis | Line height 1.6. Lavender, never neon. |
| Labels, kickers, nav | Space Mono | 400 or 700, uppercase | 0.75–0.8rem, tracking 0.08–0.12em — a terminal readout. |
| Figures | Space Mono / Sora | 700 | Key figures in Sora 700; table and axis figures in Space Mono, which is tabular by nature. |

Weight contrast comes from heavy geometric headlines over regular Inter body,
with small uppercase monospace labels as a third, mechanical voice. Headlines
are solid `--on-surface` or a single neon color — never a gradient.

## Defining Treatments

Ranked by how much each defines the style. Each treatment says where it applies; use
it wherever the artifact has that place. When there is room for only a few, keep
the higher-ranked ones.

### 1. Neon-edged panel

A dark container with a thin pink border at 30% and a faint inner glow, as if
lit from its edge. Use it on cards, key-figure tiles, and the primary
container. A second panel in the same row may take cyan instead; never more
than two colors of edge in a view.

```css
.neon-panel {
  background: var(--surface-container);
  border: var(--neon-border);
  box-shadow: var(--neon-inset);
  border-radius: var(--rounded-lg);
  padding: var(--space-lg);
}
.neon-panel.is-cyan {
  border-color: color-mix(in srgb, var(--secondary) 30%, transparent);
  box-shadow: inset 0 0 12px color-mix(in srgb, var(--secondary) 10%, transparent);
}
```

### 2. Glowing accent text

A soft `currentColor` glow on the few words set in neon: the title's kicker,
the key figure's value, an active nav label. Never on body text, headings in
lavender, or anything longer than a short line.

```css
.neon-text { color: var(--primary); text-shadow: var(--glow-text); }
.kicker {
  font-family: var(--font-label);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--secondary);
  text-shadow: var(--glow-text);
}
```

### 3. Lights on interaction

Interactive elements are dark at rest and light up when engaged: the border
brightens and an outer glow blooms. Applies to buttons, cards that open, chips,
and inputs on focus.

```css
.btn-neon {
  background: var(--surface-container);
  color: var(--primary);
  border: var(--neon-border-lit);
  border-radius: var(--rounded);
  padding: var(--space-sm) var(--space-lg);
  transition: box-shadow var(--dur-short) var(--ease-out),
              border-color var(--dur-short) var(--ease-out);
}
.btn-neon:hover { border-color: var(--primary); box-shadow: var(--glow-primary); text-shadow: var(--glow-text); }
```

### 4. Lit data line

The series that matters glows faintly, like a tube of neon drawn across the
chart. Only on the highlighted series (line or bar); context stays matte.

```css
.chart .series-key { stroke: var(--data-1); color: var(--data-1); filter: var(--glow-line); }
.chart .series-context { stroke: var(--data-context); }
```

### 5. Scan-line texture

Faint horizontal scan lines across the page background or the opening title
block, at the edge of visibility. Never on cards, tables, or behind body text
in panels.

```css
.page { background-color: var(--background); background-image: var(--scanlines); }
```

## Composition

-   **Flush-left, asymmetric grid.** Titles, kickers, and body align to a
    strong left edge; dashboards use uneven columns (a wide main panel beside
    a narrow readout column) like a heads-up display. This follows the
    skill's general preference for asymmetry.
-   **Medium-dense.** Tighter than an editorial page: panels sit close, with
    `--space-md` to `--space-lg` gaps inside a view and `--space-2xl` between
    narrative sections so the dark has room to breathe.
-   **Separation by surface step and edge light.** Content is separated by a
    lighter surface and a thin neon or `--outline-variant` border, not by drop
    shadows. Plain sections on the background separate with space and a
    hairline.
-   **Narratives** open with a large Sora title on the scan-lined background,
    a glowing monospace kicker above it; body text sits in a 60–68ch measure.

## Components

-   **Buttons**: dark fill, neon border, neon label in `--font-label` uppercase;
    hover adds the outer glow and text glow (treatment 3). Primary is pink,
    secondary is cyan. No solid neon fills, no pill shapes.
-   **Key figures**: a neon-edged panel; monospace uppercase label in
    `--on-surface-variant`, the value in Sora 700 in pink or cyan with the text
    glow, a short caption in muted lavender.
-   **Badges and tags**: transparent, 1px neon border, monospace uppercase label
    in the same neon, `--rounded`. Yellow for warnings and "new".
-   **Links**: cyan, underlined with a 1px offset underline; hover adds the
    text glow.
-   **Inputs**: `--surface-container-low` fill, a single neon bottom border;
    focus brightens the border and adds `--glow-primary` alongside the focus
    ring.
-   **Tables**: `--surface-container-low` banding, `--outline-variant`
    hairlines, header cells in the monospace label voice; the active or
    selected row lifts to `--surface-container-high` with a pink left edge.
-   **Navigation**: monospace uppercase labels; the active item in pink with
    the text glow and a 1px pink underline.

## Data Visualization

-   **Series**: `--data-1` (pink) for the series that matters, then cyan,
    yellow, ultraviolet. Most charts need only pink plus `--data-context`;
    use all four only for genuinely categorical data.
-   **Lines and marks**: 2px lines with round caps; bars with a 1px neon border
    and a translucent fill of the same color (20–30%). The key series glows
    (treatment 4); nothing else does. No 3D, no rainbow gradients.
-   **Axes and gridlines**: axis lines in `--outline`, gridlines in
    `--outline-variant` (solid hairlines, like a HUD grid); tick labels in
    Space Mono at label size in `--on-surface-variant`. No chart border.
-   **Labels and annotations**: label series directly at their ends in the
    series color, in monospace; annotations in `--on-surface-variant` with a
    thin `--outline` leader.
-   **Tooltips**: `--surface-container-high` with a neon border, monospace
    figures.

## Motion

Quick and electric: elements fade in with a short upward slide over
`--dur-short` with `--ease-out`, staggered. Glows rise over `--dur-micro` to
`--dur-short` on hover and focus. Glows animate on interaction only — nothing
pulses, flickers, or flashes at rest.

## Don'ts

-   No neon backgrounds, neon section bands, or large neon fills.
-   No more than two neon colors in a view's UI; no neon body text.
-   No gradient headlines or rainbow gradients anywhere.
-   No tight or harsh glows (keep 8–20px blur), and no glow on every element —
    when everything glows, nothing does.
-   No black drop shadows; depth comes from surface lightness and edge light.
-   No pill buttons or large radii; corners stay at 2–4px.
-   No flicker, glitch, or pulsing animations at rest.
-   Don't let the scan-line texture become visible enough to compete with text.

## If the User Asks for Light

Neon only glows on dark, so a light version becomes "daylight signage": crisp
color, no glow. Use `--background: #f6f3fa`, `--surface-container: #ece8f3`,
`--surface-container-high: #e2dcec`, `--on-surface: #16121f`,
`--on-surface-variant: #4e4760`, `--outline: #8a8299`, `--primary: #c2185b`
(with `--on-primary: #ffffff`), `--secondary: #00695c`, `--tertiary: #735a00`,
`--data-4: #6a3fd1`. All text colors keep 4.5:1 on every surface. Drop the text
glows, the lit data line, and the scan lines; panels keep a 1px accent border at
40% instead of the inner glow, and hover deepens the border rather than
blooming.
