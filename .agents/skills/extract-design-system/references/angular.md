# Angular — Extraction Reference

## Key Files to Read First

| File                                 | What It Reveals                      |
| :----------------------------------- | :----------------------------------- |
| `package.json`                       | Detect `@angular/core`,              |
:                                      : `@angular/material`, `@angular/cdk`, :
:                                      : `primeng`, `ng-zorro-antd`,          :
:                                      : `tailwindcss`                        :
| `angular.json`                       | Global styles array, style           |
:                                      : preprocessor options, project        :
:                                      : structure                            :
| `src/styles.scss` / `src/styles.css` | Global stylesheet — CSS custom       |
:                                      : properties, resets, font imports,    :
:                                      : theme setup                          :
| `src/theme.scss`                     | Angular Material custom theme        |
:                                      : definition                           :
| `src/index.html`                     | Font links, `<body>` classes, meta   |
:                                      : theme-color                          :
| `src/app/app.component.scss`         | Root component styles                |

## Angular Material Theme Extraction

Angular Material's theming system is the richest design token source in Angular
projects:

```scss
// src/theme.scss or src/styles.scss
@use '@angular/material' as mat;

$my-primary: mat.m2-define-palette(mat.$indigo-palette);
$my-accent: mat.m2-define-palette(mat.$pink-palette, A200, A100, A400);
$my-warn: mat.m2-define-palette(mat.$red-palette);

$my-theme: mat.m2-define-light-theme((
  color: (
    primary: $my-primary,
    accent: $my-accent,
    warn: $my-warn,
  ),
  typography: mat.m2-define-typography-config(
    $font-family: 'Inter, sans-serif',
    $headline-1: mat.m2-define-typography-level(96px, 96px, 300),
    $headline-5: mat.m2-define-typography-level(24px, 32px, 400),
    $body-1: mat.m2-define-typography-level(16px, 24px, 400),
  ),
  density: 0,
));

@include mat.all-component-themes($my-theme);
```

**For Material 3 (M3) / Angular 17+:**

```scss
$theme: mat.define-theme((
  color: (
    theme-type: light,
    primary: mat.$azure-palette,
    tertiary: mat.$violet-palette,
  ),
  typography: (
    brand-family: 'Inter',
    plain-family: 'Inter',
  ),
));
```

### Grep Patterns for Material

```bash
# Find Material theme definitions
grep -rn 'define-palette\|define-light-theme\|define-dark-theme\|define-theme' src/ --include='*.scss'

# Find Material typography config
grep -rn 'define-typography-config\|define-typography-level' src/ --include='*.scss'

# Find Material component theme includes
grep -rn '@include mat\.' src/ --include='*.scss'

# Find custom Material palette values
grep -rn '\$.*palette' src/ --include='*.scss'
```

## Component-Level Styles

Each Angular component can have its own stylesheet:

```
src/app/
  button/
    button.component.ts       ← @Component decorator with styleUrls
    button.component.scss     ← Component-scoped styles
    button.component.html     ← Template with class bindings
```

### Grep Patterns

```bash
# Find all component stylesheets
find src/ -name '*.component.scss' -o -name '*.component.css' | head -50

# Find color values in component styles
grep -rn '#[0-9a-fA-F]\{3,8\}\|rgb\|hsl\|var(--' src/ --include='*.component.scss' --include='*.component.css'

# Find CSS custom properties
grep -rn '\-\-[a-z]' src/ --include='*.scss' --include='*.css'

# Find ViewEncapsulation overrides (components that leak styles globally)
grep -rn 'ViewEncapsulation' src/ --include='*.component.ts'

# Find ::ng-deep usage (deprecated but common — pierces encapsulation)
grep -rn '::ng-deep\|/deep/\|>>>' src/ --include='*.scss' --include='*.css'

# Find host binding styles
grep -rn ':host' src/ --include='*.scss' --include='*.css'

# Find [ngClass] and [ngStyle] bindings
grep -rn 'ngClass\|ngStyle' src/ --include='*.html'
```

## ViewEncapsulation

Angular scopes component styles by default (Emulated encapsulation). Key
patterns:

-   `:host` — styles the component's host element
-   `:host-context(.dark-theme)` — conditional host styling based on ancestor
-   `::ng-deep` — pierces encapsulation (deprecated but reveals intentional
    global overrides)
-   `ViewEncapsulation.None` — component styles are global (look for these —
    they define shared tokens)

## Global Styles via angular.json

```json
// angular.json → projects.*.architect.build.options
{
  "styles": [
    "src/styles.scss",
    "node_modules/@angular/material/prebuilt-themes/deeppurple-amber.css"
  ],
  "stylePreprocessorOptions": {
    "includePaths": ["src/styles"]
  }
}
```

The `styles` array lists all global stylesheets in load order. The
`includePaths` reveals shared SCSS partials.

## Angular CDK

The CDK provides unstyled primitives. If used without Material, the design
system is fully custom:

-   Look for CDK overlay styles, a11y styles, and layout utilities
-   All visual styling will be in component-level or global CSS

## Interpreting Findings

-   **Angular Material projects** have a well-defined theme — the
    `define-palette` / `define-theme` calls are the canonical color source
-   **Non-Material projects** rely more on global SCSS variables and CSS custom
    properties — check `styles.scss` and any `_variables.scss` partials
-   `::ng-deep` usage indicates where the team needed to override encapsulated
    styles — these reveal friction points in the design system
-   Components with `ViewEncapsulation.None` are acting as global style
    providers — treat their styles as design tokens
-   The `angular.json` styles array shows the global style load order — earlier
    files set the foundation
