# Design tokens

Tokens are named values (colors, sizes, radii, durations) that every component
uses. This file covers how to structure them, a method to build a palette from
any brand color, one complete example, and how to check contrast.

## Structure

-   **Scales and roles**: scales hold raw steps (`--neutral-100`,
    `--accent-700`); roles say what a value is for (`--text`, `--surface`,
    `--border`). Components use only roles, so a new palette or a dark theme
    only reassigns roles.
-   **Roles to define**: page background, surface, and sunken surface; text,
    muted text, subtle text, and links; border, strong border, and control
    border; accent, strong accent, and soft accent; a strong and a soft color
    per status; hover, pressed, and selected; the focus ring; font families;
    type, spacing, and radius scales; shadows; motion durations and easing.
-   **Where**: on `:root`, so overlays attached to `body` (dialogs, menus,
    tooltips) get them too. Set durations to 0 under `prefers-reduced-motion`.

## Build a palette from any brand color

Build each hue (the accent, the grays, each status) as a 10-step scale with a
fixed OKLCH lightness per step. OKLCH lightness looks the same across hues, so a
step can play the same role whatever the color:

```python
import math

LIGHTNESS = {50: 0.98, 100: 0.95, 200: 0.89, 300: 0.81, 400: 0.71,
             500: 0.60, 600: 0.50, 700: 0.42, 800: 0.34, 900: 0.26}


def contrast(fg: str, bg: str) -> float:
  """Returns the WCAG contrast ratio of two '#rrggbb' colors."""

  def luminance(color: str) -> float:
    rgb = [int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = [
        c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
        for c in rgb
    ]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

  hi, lo = sorted((luminance(fg), luminance(bg)), reverse=True)
  return (hi + 0.05) / (lo + 0.05)


def hex_to_oklch(color: str) -> tuple[float, float, float]:
  """Returns (lightness 0-1, chroma, hue in degrees) of a '#rrggbb' color."""
  rgb = [int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
  r, g, b = [
      c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb
  ]
  l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
  m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
  s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
  lab_a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
  lab_b = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
  lightness = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
  hue = math.degrees(math.atan2(lab_b, lab_a)) % 360
  return lightness, math.hypot(lab_a, lab_b), hue


def oklch_to_hex(lightness: float, chroma: float, hue: float) -> str:
  """Returns the '#rrggbb' color for OKLCH values, clipped to sRGB."""
  a = chroma * math.cos(math.radians(hue))
  b = chroma * math.sin(math.radians(hue))
  l = (lightness + 0.3963377774 * a + 0.2158037573 * b) ** 3
  m = (lightness - 0.1055613458 * a - 0.0638541728 * b) ** 3
  s = (lightness - 0.0894841775 * a - 1.2914855480 * b) ** 3
  rgb = (
      4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
      -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
      -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
  )
  out = []
  for c in rgb:
    c = min(max(c, 0.0), 1.0)
    c = 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    out.append(round(c * 255))
  return '#' + ''.join(f'{c:02x}' for c in out)


def build_scale(chroma: float, hue: float) -> dict[int, str]:
  """Returns {step: '#rrggbb'}, with less chroma at the light and dark ends."""
  return {
      step: oklch_to_hex(l, chroma * min(1, (1 - l) / 0.3, l / 0.5), hue)
      for step, l in LIGHTNESS.items()
  }


_, brand_chroma, brand_hue = hex_to_oklch('#2563eb')  # The brand color.
print('accent', build_scale(brand_chroma, brand_hue))
print('grays', build_scale(0.01, brand_hue))
```

-   **Grays**: chroma 0.005–0.02. Use the accent's hue for a related palette, or
    a warm (about 60–90) or cool (about 230–270) hue to set the temperature.
-   **Status colors**: hues near 150 (green), 65 (amber), 25 (red), and 250
    (blue), with chroma about 0.15.

Which step serves which role. These hold for every hue with chroma up to 0.25
and gray chroma up to 0.02 (checked at 5 degree steps), on white and on the 50
and 100 steps:

-   **50–100**: page, sunken, and selected backgrounds, and soft status
    backgrounds.
-   **200–300**: dividers and decorative borders.
-   **Gray 500**: control borders and meaningful icons (3:1 or more).
-   **Gray 600**: subtle text (4.5:1 or more).
-   **Accent 600**: focus rings and indicators such as the active tab (3:1 or
    more).
-   **Gray 700**: muted text. **Accent or status 700**: colored text, links, and
    fills behind white text (4.5:1 or more).
-   **Gray 900**: main text.

Lighter steps pass for some hues; check them with `contrast()` before use. Dark
steps of yellow and orange turn brown, which is expected: use the brand shade
for fills and the 700 step for text.

## Example: brief A, a calm dashboard

One complete token set, built with the method above from a brand blue
(`#2563eb`), grays tinted toward it (chroma 0.01), and the status hues above.
Only the steps in use are listed. It shows the structure filled in; replace the
values for any other brief.

```css
:root {
  /* Scales. */
  --neutral-50: #f8f8f9;
  --neutral-100: #eeeeef;
  --neutral-200: #d9dbdd;
  --neutral-300: #bfc1c5;
  --neutral-500: #7d8086;
  --neutral-600: #606369;
  --neutral-700: #4b4d52;
  --neutral-800: #36383c;
  --neutral-900: #232427;
  --accent-100: #e2efff;
  --accent-600: #1754db;
  --accent-700: #1041ad;

  /* Surfaces. */
  --bg: var(--neutral-50);
  --surface: #fff;
  --surface-sunken: var(--neutral-100);

  /* Text. */
  --text: var(--neutral-900);
  --text-muted: var(--neutral-700);
  --text-subtle: var(--neutral-600);
  --text-link: var(--accent-700);

  /* Lines. */
  --border: var(--neutral-200);
  --border-strong: var(--neutral-300);
  --border-control: var(--neutral-500);

  /* Accent and states. */
  --accent: var(--accent-600); /* indicators, focus ring */
  --accent-strong: var(--accent-700); /* colored text, filled buttons */
  --accent-soft: var(--accent-100); /* selected backgrounds */
  --hover: color-mix(in srgb, var(--text) 4%, transparent);
  --pressed: color-mix(in srgb, var(--text) 8%, transparent);
  --selected: var(--accent-soft);
  --ink: var(--neutral-900); /* this brief's primary buttons */
  --ink-hover: var(--neutral-800);
  --focus-ring: 2px solid var(--accent);

  /* Status: the 700 step for text and icons, the 100 step behind them. */
  --success: #005f23;
  --success-soft: #e3f4e6;
  --warning: #7a3900;
  --warning-soft: #fbecde;
  --danger: #842927;
  --danger-soft: #ffe8e6;
  --info: #004e8e;
  --info-soft: #e2f0ff;

  /* Type. */
  --font-sans: Inter, system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-display: var(--font-sans);
  --font-mono: 'Roboto Mono', ui-monospace, Menlo, monospace;
  --text-xs: 12px;
  --text-sm: 13px;
  --text-md: 14px;
  --text-lg: 16px;
  --text-xl: 20px;
  --text-2xl: 24px;

  /* Space: 4 px grid. */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;

  /* Shape. */
  --radius-sm: 6px; /* chips, menu items, tooltips */
  --radius-md: 8px; /* buttons, inputs, rich tooltips */
  --radius-lg: 12px; /* cards, menus */
  --radius-xl: 16px; /* dialogs */
  --radius-pill: 999px;

  /* Depth: floating layers only, tinted with the gray hue. */
  --shadow-xs: 0 1px 2px rgb(35 36 39 / 0.04);
  --shadow-sm: 0 1px 2px rgb(35 36 39 / 0.05), 0 1px 3px rgb(35 36 39 / 0.06);
  --shadow-md:
    0 4px 12px -2px rgb(35 36 39 / 0.08), 0 2px 4px -2px rgb(35 36 39 / 0.05);
  --shadow-lg:
    0 16px 40px -8px rgb(35 36 39 / 0.16), 0 4px 12px -4px rgb(35 36 39 / 0.08);
  --scrim: rgb(35 36 39 / 0.4);

  /* Motion. */
  --ease: cubic-bezier(0.2, 0, 0, 1);
  --duration-fast: 120ms; /* hover, press */
  --duration: 180ms; /* menus, tooltips */
  --duration-slow: 260ms; /* dialogs, panels */
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration: 0ms;
    --duration-slow: 0ms;
  }
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: var(--text-md) / 1.5 var(--font-sans);
}

:focus-visible {
  outline: var(--focus-ring);
  outline-offset: 2px;
}
```

For another brief, keep this structure and change the values. Brief B in
[SKILL.md](/quality/scout/_agents/skills/ui_design/SKILL.md#example-defaults),
for example, would use warm grays from `build_scale(0.012, 75)`, the brand's
green or brown as the accent, a type scale that starts at 17–18 px, larger radii
and control heights, and `--ink` set to `--accent-strong` so primary buttons
carry the brand.

### Component sizes for brief A

-   **Buttons**: 36 px tall (32 px in dense toolbars), `--radius-md`, 14 px/500,
    16 px side padding, 18 px icons with an 8 px gap, no shadow. Primary:
    `--ink` fill, white text, `--ink-hover` on hover. Secondary: `--surface`
    with a 1 px `--border-strong` border. Tertiary: text only.
-   **Inputs and selects**: 36 px tall, `--radius-md`, 1 px `--border-control`,
    `--surface` fill, 12 px side padding, `--text-subtle` placeholder. On focus:
    `--accent` border plus the focus ring.
-   **Checkboxes, radios, and switches**: `--ink` when on, a `--border-control`
    outline when off.
-   **Tabs**: 40 px tall, transparent, 14 px/500, `--text-muted` when inactive
    and `--text` when active, a 2 px `--accent` indicator, `--hover` on hover.
-   **Segmented controls**: a `--surface-sunken` track with 2 px padding; the
    selected segment is `--surface` with `--shadow-xs`.
-   **Cards**: `--surface`, 1 px `--border`, `--radius-lg`, 16–24 px padding.
-   **Tables**: 40 px rows (36 px dense), 1 px `--border` between rows, header
    cells 12 px/500 `--text-muted`, `--hover` on row hover.
-   **Menus**: `--surface`, 1 px `--border`, `--radius-lg`, `--shadow-md`, 6 px
    padding, 32–36 px items with `--radius-sm`.
-   **Dialogs**: `--radius-xl`, `--shadow-lg`, 24 px padding, 18 px/600 title,
    `--scrim` behind, actions at the bottom right with the primary last.
-   **Tooltips**: plain labels are white 12 px text on `--neutral-900`,
    `--radius-sm`, 4 px × 8 px padding. Rich tooltips (charts, previews) are
    `--surface` with 1 px `--border`, `--radius-md`, and `--shadow-md`.
-   **Chips and badges**: `--radius-pill` or `--radius-sm`, 12 px/500, a status
    soft background with the matching strong color for text.
-   **Skeletons**: `--neutral-100` blocks with `--radius-sm`, the size of the
    content they stand in for.

### Charts for brief A

```js
// Tailwind 600 shades: 3:1 or more on white, and distinct from each other and
// from the blue accent, which marks the aggregate line.
const SERIES_COLORS = [
  '#059669', '#7c3aed', '#ea580c', '#0891b2',
  '#db2777', '#65a30d', '#c026d3', '#d97706',
];

// The same name gets the same color on every page and reload.
function seriesColor(name) {
  let hash = 0;
  for (const ch of name) hash = (hash * 31 + ch.charCodeAt(0)) | 0;
  return SERIES_COLORS[Math.abs(hash) % SERIES_COLORS.length];
}
```

-   To make your own list, take the builder's 600 step for 8–10 hues spread
    around the color wheel, leaving out hues near the accent. The 600 step
    passes 3:1 on white for any hue.
-   Lines: context series 1 px `--neutral-300` at 40% opacity, selected series
    1.75 px in their color, the aggregate 2.25 px in `--accent`.
-   Axes: 1 px `--neutral-200` grid lines, a `--neutral-300` baseline, and 11–12
    px `--text-subtle` labels with tabular figures.
-   Hover: a 1 px `--neutral-500` crosshair dashed `3 3`, and a rich tooltip
    with 12 px text, an 8 px color swatch per row, and values in weight 600.
-   Legend: 12 px `--text-muted` with a 14 px × 2 px line sample per series.

## Fonts and icons

Load text fonts in one request, with only the weights in use. For example, with
Inter and Roboto Mono:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Roboto+Mono:wght@400;500&display=swap">
```

-   **Google products and internal tools**: the Google Sans family matches other
    Google apps. Request
    `family=Google+Sans:wght@400;500;600&family=Google+Sans+Text:wght@400;500;600&family=Google+Sans+Code:wght@400;500`,
    then put `'Google Sans Text'` first in `--font-sans`, `'Google Sans'` in
    `--font-display`, and `'Google Sans Code'` in `--font-mono`.
-   **Icon fonts**: a variable icon font with every axis is large; Material
    Symbols Outlined is 4 MB. Pin the axes you don't animate
    (`opsz,wght,FILL,GRAD@20,400,0..1,0` keeps only the fill axis: 480 KB), or
    also add `&icon_names=home,search,settings` with the icons in use (a few
    KB). Use `display=block` for icon fonts so icon names never flash as text.
    Google products can load Google Symbols the same way.

## Mapping a component library

Point the library's theme variables at the tokens instead of restyling each
component. Material Web example:

```css
:root {
  --md-sys-color-primary: var(--accent);
  --md-sys-color-on-primary: #fff;
  --md-sys-color-surface: var(--surface);
  --md-sys-color-surface-container: var(--surface); /* menus */
  --md-sys-color-surface-container-high: var(--surface); /* dialogs */
  --md-sys-color-on-surface: var(--text);
  --md-sys-color-on-surface-variant: var(--text-muted);
  --md-sys-color-outline: var(--border-control);
  --md-sys-color-outline-variant: var(--border);
  --md-ref-typeface-brand: var(--font-display);
  --md-ref-typeface-plain: var(--font-sans);
  --md-sys-shape-corner-small: var(--radius-sm);
  --md-sys-shape-corner-medium: var(--radius-lg);
  --md-dialog-container-shape: var(--radius-xl);
  /* Brief A's near-black primary buttons. */
  --md-filled-button-container-color: var(--ink);
  --md-filled-button-container-shape: var(--radius-md);
  --md-filled-button-container-height: 36px;
  /* Tabs: a thin indicator and a neutral hover, not a primary tint. */
  --md-primary-tab-container-color: transparent;
  --md-primary-tab-active-indicator-height: 2px;
  --md-primary-tab-hover-state-layer-color: var(--text);
  --md-primary-tab-hover-state-layer-opacity: 0.04;
}
```

Other libraries have equivalent theme variables in their theming docs; map the
same roles. Then check each component's hover, focus, and selected states:
library defaults often tint them with the primary color.

## Checking contrast

Compute ratios with `contrast()` above instead of judging by eye, for each
text/background and control/background pair you add or change.

-   Targets are in the accessibility floor in
    [SKILL.md](/quality/scout/_agents/skills/ui_design/SKILL.md#accessibility-floor).
    Large text, which needs only 3:1, is 24 px or more, or 18.66 px bold.
-   For a `color-mix(in srgb, A p%, B)` token, mix each 0–255 channel first:
    `A*p + B*(1-p)`. Mix a translucent layer with the color underneath.
-   Common failures: light gray text on tinted surfaces, accent text on a pale
    accent background, white text on a light accent, and brand colors used for
    text without a check.
