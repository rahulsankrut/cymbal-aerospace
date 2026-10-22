# Vue / Nuxt — Extraction Reference

## Key Files to Read First

| File                                | What It Reveals                       |
| :---------------------------------- | :------------------------------------ |
| `package.json`                      | Detect `vue`, `nuxt`, `vuetify`,      |
:                                     : `quasar`, `primevue`, `element-plus`, :
:                                     : `@vueuse/*`                           :
| `nuxt.config.ts` / `nuxt.config.js` | CSS config, module list,              |
:                                     : Vuetify/PrimeVue plugin options,      :
:                                     : global CSS imports                    :
| `vite.config.ts`                    | CSS preprocessor config, plugin list  |
| `src/assets/main.css` or            | Global styles, CSS custom properties  |
: `src/style.css`                     : on `\:root`                           :
| `src/plugins/vuetify.ts`            | Vuetify theme definition — colors,    |
:                                     : dark mode, typography                 :
| `quasar.config.js`                  | Quasar framework config — brand       |
:                                     : colors, icon set, CSS addons          :
| `tailwind.config.*`                 | If Tailwind is also used (common in   |
:                                     : Nuxt projects)                        :

## Single-File Component (SFC) Style Extraction

Vue SFCs contain `<style>` blocks co-located with templates:

```vue
<style scoped>
.card {
  background: var(--surface-card);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}
</style>
```

### Grep Patterns

```bash
# Extract all <style> blocks from .vue files
grep -A 50 '<style' src/ -r --include='*.vue' | head -500

# Find CSS custom property definitions
grep -rn '\-\-[a-z]' src/ --include='*.vue' --include='*.css' --include='*.scss'

# Find CSS custom property usage
grep -rn 'var(--' src/ --include='*.vue' --include='*.css'

# Find scoped vs global styles
grep -rn '<style' src/ --include='*.vue'

# Find dynamic :style bindings
grep -rn ':style=' src/ --include='*.vue'

# Find :class bindings (conditional classes)
grep -rn ':class=' src/ --include='*.vue'
```

## Vuetify Theme Extraction

Vuetify stores its entire design system in a theme config:

```ts
// src/plugins/vuetify.ts
createVuetify({
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#1867C0',
          secondary: '#5CBBF6',
          background: '#FFFFFF',
          surface: '#F5F5F5',
          error: '#B00020',
        },
      },
    },
  },
})
```

Also check for:

-   `$vuetify.theme` usage in components
-   SASS variable overrides in `variables.scss` (Vuetify auto-imports this)
-   `v-theme-provider` components for nested themes

## Quasar Framework

Quasar defines brand colors in `quasar.config.js`:

```js
framework: {
  config: {
    brand: {
      primary: '#1976D2',
      secondary: '#26A69A',
      accent: '#9C27B0',
      dark: '#1D1D1D',
      positive: '#21BA45',
      negative: '#C10015',
      info: '#31CCEC',
      warning: '#F2C037',
    }
  }
}
```

Also check `src/css/quasar.variables.scss` for SASS variable overrides.

## PrimeVue / Element Plus

-   PrimeVue: look for theme imports in `main.ts` (e.g., `import
    'primevue/resources/themes/lara-light-blue/theme.css'`) and check for custom
    `presets` in PrimeVue 4+ Styled mode
-   Element Plus: look for SCSS variable overrides and `ElConfigProvider` for
    size/locale settings

## Nuxt-Specific Conventions

-   **`app.vue`**: root layout, check for global wrappers and style imports
-   **`layouts/default.vue`**: primary layout structure — navigation, footer,
    content area
-   **`assets/css/`**: global stylesheets imported via `nuxt.config.ts` → `css:
    [...]`
-   **`app.config.ts`**: runtime config that may include theme/UI settings
-   **Nuxt Modules**: `@nuxtjs/tailwindcss`, `@nuxtjs/color-mode`, `nuxt-icon` —
    each may inject styles

## Interpreting Findings

-   Vue projects using a UI framework (Vuetify, Quasar, PrimeVue) have their
    palette defined in the framework config — prioritize that over scattered CSS
-   Scoped styles (`<style scoped>`) are component-local — look for repeated
    patterns across multiple components to identify the implicit design system
-   If CSS custom properties appear on `:root` in a global stylesheet, these are
    intentional design tokens
-   `:class` bindings with objects reveal the component's visual states — these
    map to component variants
