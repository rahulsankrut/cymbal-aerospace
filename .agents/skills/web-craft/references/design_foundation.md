# Design Foundation

The building blocks every artifact shares, whatever its style: the full `:root`
template, the type scale for each experience form, spacing and motion, the base
reset, layout patterns, and a font reference. The style itself comes from
**references/design_style_menu.md**; the decisions behind all of this are in
SKILL.md Step 4.

--------------------------------------------------------------------------------

## The `:root` Template

Build `:root` in the same order as SKILL.md 4.2: the style's block first, then
any user-requested changes, then the shared tokens below. Every value in the
artifact references these tokens — no inline hex, oklch, or rgb values in the
body.

```css
:root {
  /* 1. The chosen style's :root block (its colors, fonts, radii, and effects). */

  /* 2. Changes the user asked for (a font, a color, light or dark). */

  /* 3. Shared tokens: */

  /* Semantic -- harmonize with the style's palette (errors use --error) */
  --positive: ;
  --warning:  ;

  /* Focus ring -- usually the style's --primary */
  --focus: ;

  /* Type scale -- the block for your experience form, below */

  /* Spacing scale (4pt base) */
  --space-xs: 0.25rem;  --space-sm: 0.5rem;
  --space-md: 1rem;     --space-lg: 1.5rem;
  --space-xl: 2.5rem;   --space-2xl: 4rem;
  --space-3xl: 6rem;

  /* Motion */
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --dur-micro: 120ms;  --dur-short: 220ms;  --dur-long: 420ms;
}
```

### Type Scale by Experience Form

Styles define font families, not sizes. The scales below are starting points for
each experience form, used with the style's `--font-headline`, `--font-body`,
and `--font-label`. Adjust them for the font and the content; the guardrails
after them are what to keep.

**Narrative** — larger ratio, with a display size for the opening title:

```css
:root {
  --display-size:  clamp(2.75rem, 1.5rem + 4.5vw, 5rem);
  --headline-size: clamp(1.875rem, 1.25rem + 2.2vw, 2.75rem);
  --subhead-size:  clamp(1.25rem, 1.1rem + 0.6vw, 1.5rem);
  --body-size:     clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem);
  --label-size:    clamp(0.75rem, 0.72rem + 0.15vw, 0.8125rem);
}
```

**Dashboard / Data Explorer and Focused Tool** — tighter ratio for dense
layouts:

```css
:root {
  --display-size:  clamp(1.75rem, 1.4rem + 1.2vw, 2.25rem);
  --headline-size: clamp(1.25rem, 1.1rem + 0.5vw, 1.5rem);
  --subhead-size:  clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem);
  --body-size:     clamp(0.9375rem, 0.9rem + 0.15vw, 1rem);
    --label-size:    0.75rem;
}
```

**Guardrails** — keep these when adjusting:

-   **Body**: at least 16px (1rem) for narrative and at least 15px (0.9375rem)
    for dashboards and tools.
-   **Labels**: at least 12px (0.75rem).
-   **Section headings**: at least about 1.5× the body size for narrative and
    1.25× for dashboards and tools, so the hierarchy reads at a glance.
-   **Display**: sized so the opening title fits a narrow preview pane without
    taking it over.

**Reasons to adjust**:

-   **The style**: a style may push the scale further (for example Bauhaus's
    oversized headlines) but not compress it.
-   **The font**: faces with a small x-height (short lowercase letters, like EB
    Garamond or Cormorant) read smaller at the same size; step them up.
-   **The content**: a long title can step the display size down; a short one
    can take more room.

--------------------------------------------------------------------------------

## Base Reset

Follow the token block immediately with the base reset:

```css
/* Base reset -- required on every artifact */
*, *::before, *::after { box-sizing: border-box; }
html, body { overflow-x: clip; margin: 0; padding: 0; }
header { position: static !important; }

.page-grid {
  display: grid;
  gap: var(--space-lg);
  padding: var(--space-lg);
  max-width: 1200px;
  margin: 0 auto;
  overflow: hidden;
}
.page-grid * { min-width: 0; }
```

And in `<head>`:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

--------------------------------------------------------------------------------

## Font Reference

Each style brings its own families (see **references/design_style_menu.md**).
Use this list when adding a monospace label voice, or when the content's feel
calls for a different display face within the style's character. A font the user
asks for is used as asked, even if it is not listed here. All are on Google
Fonts with the weight ranges shown. Request only weights a family has: asking
for a missing weight makes Google Fonts reject the whole `<link>`.

**Monospace (labels, figures, data)**: IBM Plex Mono (100–700) · JetBrains Mono
(100–800) · Geist Mono (100–900) · Space Mono (400, 700)

**Serif display** — editorial, narrative, historical, literary, academic: Bitter
(100–900) · Source Serif 4 (200–900) · Newsreader (200–800) · Instrument Serif
(400 only) · EB Garamond (400–800) · Cormorant Garamond (300–700) · Shippori
Mincho (400–800)

**Geometric sans display** — technical, modern, data-forward: Space Grotesk
(300–700) · Geist (100–900) · Bricolage Grotesque (200–800) · Anton (400 only)

**Humanist sans display** — warm, approachable, educational: Bricolage Grotesque
(200–800)

--------------------------------------------------------------------------------

## Adaptive Card Grid

Use CSS Grid for any two-dimensional card layout:

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr));
  gap: var(--space-lg);
}
```

For component-level responsive behavior, use container queries on card wrappers:

```css
.card-wrapper { container-type: inline-size; }

@container (min-width: 400px) {
  .card-inner { grid-template-columns: 1fr 1fr; }
}
@container (max-width: 399px) {
  .card-inner { grid-template-columns: 1fr; }
}
```

Include a mobile breakpoint for page-level layout:

```css
@media (max-width: 640px) {
  .page-grid { grid-template-columns: 1fr; }
  aside { display: none; }
  body { padding: var(--space-sm); }
}
```

--------------------------------------------------------------------------------

## Reduced Motion

Include this on every artifact that uses animation or transitions:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration:  0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior:     auto !important;
  }
}
```
