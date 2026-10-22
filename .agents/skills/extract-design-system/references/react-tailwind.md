# React / Next.js / Tailwind — Extraction Reference

## Key Files to Read First

| File                              | What It Reveals                         |
| :-------------------------------- | :-------------------------------------- |
| `tailwind.config.js` /            | Full color palette, font families,      |
: `tailwind.config.ts`              : spacing scale, breakpoints, custom      :
:                                   : shadows, border radii — the single      :
:                                   : richest source of design tokens         :
| `globals.css` / `app/globals.css` | CSS custom properties, `@tailwind`      |
:                                   : directives, base layer overrides, font  :
:                                   : imports                                 :
| `next.config.js`                  | Font optimization config, image domains |
:                                   : (hints at asset strategy)               :
| `package.json`                    | Detect `tailwindcss`,                   |
:                                   : `@headlessui/react`, `@radix-ui/*`,     :
:                                   : `shadcn`, `daisyui`,                    :
:                                   : `styled-components`, `@emotion/*`       :
| `components.json` (shadcn/ui)     | Theme and component alias config        |
| `theme.ts` / `theme.js`           | Custom theme objects for CSS-in-JS or   |
:                                   : component libraries                     :

## Tailwind Config Extraction

The `tailwind.config` is the most token-dense file. Parse it carefully:

```js
// Look for theme.extend — this is where custom tokens live
theme: {
  extend: {
    colors: { ... },        // ← Full color palette with semantic names
    fontFamily: { ... },    // ← Font stacks
    fontSize: { ... },      // ← Type scale (may include line-height tuples)
    spacing: { ... },       // ← Custom spacing beyond the default scale
    borderRadius: { ... },  // ← Corner radius tokens
    boxShadow: { ... },     // ← Shadow levels
    screens: { ... },       // ← Breakpoints
  }
}
```

**Also check for plugins**: `daisyui`, `@tailwindcss/typography`,
`@tailwindcss/forms` — these inject additional design tokens.

## Grep Patterns for Colors & Styles

```bash
# Find all Tailwind color classes used across components
grep -roh 'bg-[a-z0-9-]*\|text-[a-z0-9-]*\|border-[a-z0-9-]*' src/ | sort | uniq -c | sort -rn

# Find CSS custom properties
grep -rn '\-\-[a-z]' src/ --include='*.css' --include='*.tsx' --include='*.jsx'

# Find inline style objects (CSS-in-JS patterns)
grep -rn 'style={{' src/ --include='*.tsx' --include='*.jsx'

# Find styled-components definitions
grep -rn 'styled\.\|styled(' src/ --include='*.tsx' --include='*.ts'

# Find emotion css prop usage
grep -rn 'css={' src/ --include='*.tsx' --include='*.jsx'
```

## CSS Modules

If files like `Component.module.css` exist:

-   Each `.module.css` file is scoped to its component
-   Look for color values, spacing, and typography in these files
-   They often override or supplement Tailwind classes

## Component Variant Patterns

React components often encode design variants through props:

```tsx
// Look for variant props — these reveal the design system's component API
<Button variant="primary" size="lg" />
<Badge color="success" />
<Card elevation="md" />
```

Search for these patterns:

```bash
# Find variant/size/color props in component definitions
grep -rn 'variant.*=\|size.*=\|color.*=' src/ --include='*.tsx'

# Find cva() or class-variance-authority definitions (common in shadcn)
grep -rn 'cva(' src/ --include='*.tsx' --include='*.ts'

# Find clsx/cn/classnames utility usage
grep -rn 'clsx\|classnames\|cn(' src/ --include='*.tsx' --include='*.ts'
```

## Next.js Specifics

-   **`app/` directory** (App Router): check `app/layout.tsx` for global font
    setup, `app/globals.css` for base styles
-   **`pages/` directory** (Pages Router): check `pages/_app.tsx` for global
    providers and `styles/globals.css`
-   **Font optimization**: Next.js uses `next/font` — look for `const font =
    Inter({...})` patterns in layout files
-   **`public/`**: check for local font files (`.woff2`, `.ttf`)

## Interpreting Findings

-   If `tailwind.config` has extensive `extend.colors`, the team has a
    well-defined palette — use those names
-   If colors are mostly Tailwind defaults (`blue-500`, `gray-200`), the design
    system is lightweight — extract the *used subset*
-   If both Tailwind and CSS-in-JS are present, Tailwind likely handles
    layout/utility and CSS-in-JS handles component-specific theming
-   shadcn/ui projects define colors as CSS custom properties in `globals.css`
    and reference them in `tailwind.config` — check both
