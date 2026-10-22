# Plain CSS / SASS / Less — Extraction Reference

## Key Files to Read First

| File                                | What It Reveals                      |
| :---------------------------------- | :----------------------------------- |
| `index.html` / `*.html`             | `<link>` stylesheet order, inline    |
:                                     : styles, Google Fonts, CDN links      :
| `styles.css` / `main.css` /         | Primary stylesheet — the main design |
: `app.css`                           : token source                         :
| `reset.css` / `normalize.css`       | CSS reset strategy (affects spacing  |
:                                     : and typography defaults)             :
| `variables.css` / `_variables.scss` | Explicit design token definitions    |
: / `variables.less`                  :                                      :
| `_mixins.scss` / `mixins.less`      | Reusable style patterns — reveal     |
:                                     : component conventions                :
| `_typography.scss` /                | Type system definition               |
: `typography.css`                    :                                      :
| `_colors.scss` / `colors.css`       | Color palette definition             |

## CSS Custom Properties (CSS Variables)

The most modern and portable form of design tokens:

```css
:root {
  /* Colors */
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-surface: #ffffff;
  --color-text: #1e293b;
  --color-text-muted: #64748b;
  --color-border: #e2e8f0;

  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-8: 2rem;

  /* Radii */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
}
```

### Grep Patterns

```bash
# Find all CSS custom property definitions
grep -rn '^\s*--[a-z]' . --include='*.css' --include='*.scss' --include='*.less'

# Find all CSS custom property usages
grep -rn 'var(--' . --include='*.css' --include='*.scss' --include='*.less' --include='*.html'

# Find :root blocks (primary token source)
grep -A 30 ':root' . -r --include='*.css' --include='*.scss'

# Find color values (hex, rgb, hsl)
grep -rohn '#[0-9a-fA-F]\{3,8\}\|rgb[a]\?([^)]*)\|hsl[a]\?([^)]*)' . --include='*.css' --include='*.scss' | sort | uniq -c | sort -rn | head -30

# Find font-family declarations
grep -rn 'font-family' . --include='*.css' --include='*.scss' --include='*.less'

# Find @font-face declarations
grep -A 5 '@font-face' . -r --include='*.css' --include='*.scss'

# Find Google Fonts imports
grep -rn 'fonts.googleapis.com\|fonts.gstatic.com' . --include='*.html' --include='*.css'
```

## SASS/SCSS Variables and Mixins

SASS variables are compile-time tokens:

```scss
// _variables.scss
$primary: #2563eb;
$font-size-base: 1rem;
$border-radius: 0.5rem;
$breakpoint-md: 768px;
$breakpoint-lg: 1024px;

// _mixins.scss
@mixin respond-to($breakpoint) {
  @media (min-width: $breakpoint) { @content; }
}

@mixin card-base {
  background: $white;
  border-radius: $border-radius;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
}
```

### Grep Patterns for SASS

```bash
# Find all SASS variable definitions
grep -rn '^\$[a-z]' . --include='*.scss' --include='*.sass'

# Find all SASS variable usages
grep -rohn '\$[a-z][a-z0-9-]*' . --include='*.scss' | sort | uniq -c | sort -rn | head -30

# Find mixin definitions
grep -rn '@mixin ' . --include='*.scss'

# Find @import chains (stylesheet load order)
grep -rn '@import\|@use\|@forward' . --include='*.scss'
```

## Less Variables

```less
// variables.less
@primary-color: #1890ff;
@font-size-base: 14px;
@border-radius-base: 4px;
```

```bash
# Find Less variable definitions
grep -rn '^@[a-z]' . --include='*.less'
```

## BEM Naming Conventions

BEM class names reveal the component structure:

```css
/* Block */
.card { ... }

/* Block__Element */
.card__header { ... }
.card__body { ... }
.card__footer { ... }

/* Block--Modifier (variants) */
.card--featured { ... }
.card--compact { ... }
.button--primary { ... }
.button--large { ... }
```

```bash
# Find BEM-style class definitions to discover components
grep -rohn '\.[a-z][a-z0-9]*__[a-z][a-z0-9-]*\|\.[a-z][a-z0-9]*--[a-z][a-z0-9-]*' . --include='*.css' --include='*.scss' | sort -u | head -50
```

**Modifiers (`--`) reveal component variants** — these are the design system's
component API.

## Media Queries and Breakpoints

```bash
# Find all media query breakpoints
grep -rohn '@media[^{]*' . --include='*.css' --include='*.scss' | sort -u

# Find min-width breakpoints (mobile-first)
grep -rn 'min-width' . --include='*.css' --include='*.scss'

# Find max-width breakpoints (desktop-first)
grep -rn 'max-width' . --include='*.css' --include='*.scss'
```

## CSS Reset / Normalize Patterns

Check what reset strategy is used — it affects the baseline:

-   **No reset**: browser defaults, inconsistent cross-browser
-   **normalize.css**: preserves useful defaults, fixes cross-browser bugs
-   **reset.css**: strips all defaults to zero
-   **Modern reset** (`*, *::before, *::after { box-sizing: border-box; margin:
    0; }`): minimal, common in modern projects

## @font-face Declarations

```bash
# Find local font files
find . -name '*.woff2' -o -name '*.woff' -o -name '*.ttf' -o -name '*.otf' | head -20

# Find @font-face blocks with full details
grep -B 1 -A 6 '@font-face' . -r --include='*.css' --include='*.scss'
```

## Interpreting Findings

-   **CSS custom properties on `:root`** are the highest-confidence design
    tokens — the author intentionally created them
-   **SASS/Less variables** serve the same purpose but are compile-time only —
    they represent the source-of-truth palette
-   **Repeated raw values** (e.g., `#1e293b` appearing 15 times) that aren't
    captured in variables are *implicit* tokens — extract and name them
-   **BEM modifiers** map directly to component variants — `--primary`,
    `--large`, `--outlined`
-   **@import / @use chains** reveal the stylesheet architecture — follow them
    to find all token sources
-   **The most-used color values** (from the `uniq -c` grep) are the core
    palette — rare one-off colors are usually accidental
