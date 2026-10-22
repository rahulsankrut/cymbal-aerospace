# Svelte / SvelteKit — Extraction Reference

## Key Files to Read First

| File                              | What It Reveals                         |
| :-------------------------------- | :-------------------------------------- |
| `package.json`                    | Detect `svelte`, `@sveltejs/kit`,       |
:                                   : `@skeletonlabs/skeleton`, `daisyui`,    :
:                                   : `tailwindcss`                           :
| `svelte.config.js`                | Preprocessor config (SCSS, PostCSS),    |
:                                   : adapter, alias paths                    :
| `tailwind.config.*`               | If Tailwind is used — full token source |
| `src/app.css` / `src/app.postcss` | Global styles, CSS custom properties,   |
:                                   : font imports                            :
| `src/app.html`                    | `<head>` content — Google Fonts links,  |
:                                   : meta theme-color                        :
| `src/routes/+layout.svelte`       | Root layout — global wrapper,           |
:                                   : navigation, style imports               :
| `src/lib/theme.ts` or             | Custom theme definitions, design tokens |
: `src/lib/styles/`                 :                                         :
| `skeleton.config.ts`              | Skeleton UI theme preset selection      |

## Svelte Component Style Extraction

Svelte components embed styles directly:

```svelte
<style>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  button {
    background: var(--color-primary);
    border-radius: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
  }
</style>
```

Styles in `<style>` blocks are **scoped by default** in Svelte — no `scoped`
attribute needed.

### Grep Patterns

```bash
# Extract style blocks from all .svelte files
grep -A 40 '<style' src/ -r --include='*.svelte' | head -500

# Find CSS custom property definitions
grep -rn '\-\-[a-z]' src/ --include='*.svelte' --include='*.css' --include='*.postcss'

# Find CSS custom property usage
grep -rn 'var(--' src/ --include='*.svelte' --include='*.css'

# Find inline style directives (Svelte syntax)
grep -rn 'style:' src/ --include='*.svelte'

# Find class directives (Svelte conditional classes)
grep -rn 'class:' src/ --include='*.svelte'

# Find Tailwind classes in Svelte templates
grep -roh 'class="[^"]*"' src/ --include='*.svelte' | head -100

# Find component prop-based styling
grep -rn 'export let.*variant\|export let.*size\|export let.*color' src/ --include='*.svelte'
```

## Svelte Style Directives

Svelte has unique style/class directives that encode design decisions:

```svelte
<!-- Style directive — inline but reactive -->
<div style:color={textColor} style:font-size="{size}px">

<!-- Class directive — conditional class application -->
<button class:active={isActive} class:large={size === 'lg'}>

<!-- Global styles (escape scoping) -->
<style>
  :global(body) {
    background: #0f0f23;
  }
</style>
```

Search for `style:` and `class:` directives — they reveal dynamic styling
patterns.

## Skeleton UI Integration

Skeleton UI is a popular Svelte component library with theming:

```ts
// skeleton.config.ts or tailwind.config.ts
import { skeleton } from '@skeletonlabs/tw-plugin';

plugins: [
  skeleton({
    themes: {
      preset: ['skeleton', 'wintry', 'crimson'],
      custom: [myCustomTheme],
    },
  }),
]
```

-   Skeleton themes define colors as CSS custom properties with `--color-*`
    naming
-   Check `data-theme` attribute on `<body>` in `app.html` for active theme
-   Custom themes are defined as objects with `surface`, `primary`, `secondary`,
    etc.

## DaisyUI Integration

If DaisyUI is present:

-   Check `tailwind.config` for `daisyui.themes` — this defines the full palette
-   DaisyUI uses semantic class names (`btn-primary`, `bg-base-100`) that map to
    CSS custom properties
-   Custom themes override these properties

## SvelteKit Layout Styles

```
src/routes/
  +layout.svelte     ← Root layout, imports global CSS, defines nav/shell
  +layout.ts          ← May load theme data
  +page.svelte        ← Individual pages
  (group)/
    +layout.svelte    ← Grouped layout, may have different styling
```

-   The root `+layout.svelte` often imports `../app.css` and wraps all pages
-   Check for layout groups `(marketing)/`, `(dashboard)/` — these may have
    distinct visual treatments

## Interpreting Findings

-   Svelte's scoped styles mean design tokens are often repeated across
    components — look for the *most common values* to identify the implicit
    system
-   If CSS custom properties are defined in `app.css` on `:root`, these are the
    intentional design tokens
-   Svelte projects without a UI library tend to have more "organic" design
    systems — the tokens emerge from repeated patterns rather than explicit
    config
-   `style:` directives indicate dynamic theming — the variable sources reveal
    the design token layer
-   If Tailwind is present, the `tailwind.config` is the canonical token source
    (see the react-tailwind reference)
