# Material 3 Typography Reference

An overview of typography in the Material 3 design system, including the typescale architecture, token values, styling conventions, capitalization guidelines, line length constraints, iconography integration, and script fallback stacks.

## Typography Overview

Material 3 typography uses `Google Sans Flex` (GSF) as its core variable font standard, complemented by `Google Sans` (brand) and `Google Sans Text` (plain) for static rendering fallback.

* **Typescale Hierarchy**: 5 core functional roles (`display`, `headline`, `title`, `body`, `label`) across 3 sizes (`large` / `lg`, `medium` / `md`, `small` / `sm`).
* **Dual Style Variants**: Provides 15 **Baseline** styles for general UI content and 15 **Emphasized** styles with increased weight and corner roundness (`ROND: 100`) for visual hierarchy and active states.
* **Token-Based Styling**: All typographic styling must use CSS custom property tokens (`--md-sys-typescale-*`) or `.typescale-*` utility classes rather than raw pixel sizes.

## Typescale Roles & Hierarchy

The baseline typescale defines 5 semantic roles designed for specific visual hierarchy requirements:

* **Display (`display`)**:
  * **Display Large** (`--md-sys-typescale-display-large`): `3.5625rem/4rem 'Google Sans'` (57px / 64px line height)
  * **Display Medium** (`--md-sys-typescale-display-medium`): `2.8125rem/3.25rem 'Google Sans'` (45px / 52px line height)
  * **Display Small** (`--md-sys-typescale-display-small`): `2.25rem/2.75rem 'Google Sans'` (36px / 44px line height)
  * *Purpose*: Short, prominent hero text, large numerals, and key quantitative metrics on expansive screens. Display text is reserved for brief content moments and must never be used for multi-line paragraph prose.

* **Headline (`headline`)**:
  * **Headline Large** (`--md-sys-typescale-headline-large`): `2rem/2.5rem 'Google Sans'` (32px / 40px line height)
  * **Headline Medium** (`--md-sys-typescale-headline-medium`): `1.75rem/2.25rem 'Google Sans'` (28px / 36px line height)
  * **Headline Small** (`--md-sys-typescale-headline-small`): `1.5rem/2rem 'Google Sans'` (24px / 32px line height)
  * *Purpose*: High-emphasis section headings, primary page titles on mobile viewports, and major region dividers.

* **Title (`title`)**:
  * **Title Large** (`--md-sys-typescale-title-large`): `1.375rem/1.75rem 'Google Sans'` (22px / 28px line height)
  * **Title Medium** (`--md-sys-typescale-title-medium`): `500 1rem/1.5rem 'Google Sans Text'` (16px / 24px line height)
  * **Title Small** (`--md-sys-typescale-title-small`): `500 0.875rem/1.25rem 'Google Sans Text'` (14px / 20px line height)
  * *Purpose*: Medium-emphasis subheadings, card titles, dialog header text, list item headers, and table section headings.

* **Body (`body`)**:
  * **Body Large** (`--md-sys-typescale-body-large`): `1rem/1.5rem 'Google Sans Text'` (16px / 24px line height)
  * **Body Medium** (`--md-sys-typescale-body-medium`): `0.875rem/1.25rem 'Google Sans Text'` (14px / 20px line height)
  * **Body Small** (`--md-sys-typescale-body-small`): `0.75rem/1rem 'Google Sans Text'` (12px / 16px line height)
  * *Purpose*: Multi-line passages of text, paragraph prose, long descriptions, dialog body copy, user-submitted content, and card body text.

* **Label (`label`)**:
  * **Label Large** (`--md-sys-typescale-label-large`): `500 0.875rem/1.25rem 'Google Sans Text'` (14px / 20px line height)
  * **Label Medium** (`--md-sys-typescale-label-medium`): `500 0.75rem/1rem 'Google Sans Text'` (12px / 16px line height)
  * **Label Small** (`--md-sys-typescale-label-small`): `500 0.6875rem/1rem 'Google Sans Text'` (11px / 16px line height)
  * *Purpose*: Utilitarian UI controls, button labels, tab headers, chip text, badges, form input floating labels, helper captions, and image credit text.

## Baseline vs Emphasized Typography

Material 3 provides 15 **Emphasized** styles that mirror the 15 Baseline styles:

* **Visual Distinction**: Emphasized styles feature higher font weight (`500`–`700`) and increased corner roundness (`ROND: 100`) in Google Sans Flex.
* **Usage Contexts**:
  * Indicating selected or active states in menus, button groups, or navigation rails.
  * Drawing immediate attention to unread messages, notification badges, processing status messages, and extended FAB labels.
  * Accentuating key callout moments without changing font size.
* **Swapping Tokens**: To convert a baseline text element to an emphasized variant, swap the baseline variable token for the corresponding emphasized token:
  * Baseline: `font: var(--md-sys-typescale-title-medium);`
  * Emphasized: `font: var(--md-sys-typescale-emphasized-title-medium);`

## Default Typography Roles for Web Elements

When building web components and prototype layouts, apply these default typescale mapping rules:

* **Page Title / Hero Header**: `headline-large` or `display-small`
* **Section Heading**: `headline-medium` or `headline-small`
* **Card Title / Modal Header**: `title-large` or `title-medium`
* **Card / Dialog Body Prose**: `body-medium` or `body-large`
* **Quantitative Metrics & Numbers**: `display-large` or `display-medium` with `tabular-nums`
* **Captions & Image Credits**: `body-small` or `label-medium`
* **Standard Interactive Controls**: Defer to built-in component typography (e.g. `<md-gb-button>` natively uses `label-large`).

## Typescale Tokens Reference Table

The table below details all 30 runtime custom properties defined in `design-system-bindings.css`, including shorthand values, tracking, and variable axis settings.

| Typescale Role | CSS Variable Token | Font Shorthand Value | Letter Spacing (Tracking) | Variable Axes (`font-variation-settings`) |
| :--- | :--- | :--- | :--- | :--- |
| **Display Large** | `--md-sys-typescale-display-large` | `3.5625rem/4rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Display Medium** | `--md-sys-typescale-display-medium` | `2.8125rem/3.25rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Display Small** | `--md-sys-typescale-display-small` | `2.25rem/2.75rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Headline Large** | `--md-sys-typescale-headline-large` | `2rem/2.5rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Headline Medium** | `--md-sys-typescale-headline-medium` | `1.75rem/2.25rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Headline Small** | `--md-sys-typescale-headline-small` | `1.5rem/2rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Title Large** | `--md-sys-typescale-title-large` | `1.375rem/1.75rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Title Medium** | `--md-sys-typescale-title-medium` | `500 1rem/1.5rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Title Small** | `--md-sys-typescale-title-small` | `500 0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Body Large** | `--md-sys-typescale-body-large` | `1rem/1.5rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Body Medium** | `--md-sys-typescale-body-medium` | `0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Body Small** | `--md-sys-typescale-body-small` | `0.75rem/1rem 'Google Sans Text'` | `0.00625rem` | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 400` |
| **Label Large** | `--md-sys-typescale-label-large` | `500 0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Label Medium** | `--md-sys-typescale-label-medium` | `500 0.75rem/1rem 'Google Sans Text'` | `0.00625rem` | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Label Small** | `--md-sys-typescale-label-small` | `500 0.6875rem/1rem 'Google Sans Text'` | `0.00625rem` | `'CRSV' 0, 'GRAD' 0, 'ROND' 0, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Display Large** | `--md-sys-typescale-emphasized-display-large` | `500 3.5625rem/4rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Display Medium** | `--md-sys-typescale-emphasized-display-medium` | `500 2.8125rem/3.25rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Display Small** | `--md-sys-typescale-emphasized-display-small` | `500 2.25rem/2.75rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Headline Large** | `--md-sys-typescale-emphasized-headline-large` | `500 2rem/2.5rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Headline Medium** | `--md-sys-typescale-emphasized-headline-medium` | `500 1.75rem/2.25rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Headline Small** | `--md-sys-typescale-emphasized-headline-small` | `500 1.5rem/2rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Title Large** | `--md-sys-typescale-emphasized-title-large` | `500 1.375rem/1.75rem 'Google Sans'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Title Medium** | `--md-sys-typescale-emphasized-title-medium` | `700 1rem/1.5rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 600` |
| **Emphasized Title Small** | `--md-sys-typescale-emphasized-title-small` | `700 0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 600` |
| **Emphasized Body Large** | `--md-sys-typescale-emphasized-body-large` | `500 1rem/1.5rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Body Medium** | `--md-sys-typescale-emphasized-body-medium` | `500 0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Body Small** | `--md-sys-typescale-emphasized-body-small` | `500 0.75rem/1rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 500` |
| **Emphasized Label Large** | `--md-sys-typescale-emphasized-label-large` | `700 0.875rem/1.25rem 'Google Sans Text'` | Default (`0`) | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 600` |
| **Emphasized Label Medium** | `--md-sys-typescale-emphasized-label-medium` | `700 0.75rem/1rem 'Google Sans Text'` | `0.00625rem` | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 600` |
| **Emphasized Label Small** | `--md-sys-typescale-emphasized-label-small` | `700 0.6875rem/1rem 'Google Sans Text'` | `0.00625rem` | `'CRSV' 0, 'GRAD' 0, 'ROND' 100, 'slnt' 0, 'wdth' 100, 'wght' 600` |

## Application Methods in HTML & CSS

When applying typography in web prototypes, follow these two supported patterns:

### 1. Utility Classes in HTML DOM (Preferred)

Apply `.typescale-<scale>-<size>` or `.typescale-emphasized-<scale>-<size>` directly to DOM elements. Utility classes automatically bind all three required properties (`font`, `letter-spacing`, and `font-variation-settings`).

* Size abbreviations in CSS utility classes MUST use `sm`, `md`, or `lg` (e.g. `.typescale-title-md`, `.typescale-body-lg`, `.typescale-label-sm`).
* **NEVER** use `small`, `medium`, or `large` in utility class names (e.g., `.typescale-body-medium` is INVALID).

### 2. Custom CSS Binding Rules

When writing custom CSS classes, ALWAYS bind all three custom properties together in strict sequence:

```css
.custom-card-title {
  font: var(--md-sys-typescale-title-medium);
  letter-spacing: var(--md-sys-typescale-title-medium-tracking);
  font-variation-settings: var(--md-sys-typescale-title-medium-axes);
}
```

* **CRITICAL Declaration Order**: Always declare `letter-spacing` and `font-variation-settings` AFTER `font: var(--md-sys-typescale-...)`. Because the CSS `font` shorthand resets all font sub-properties (including `letter-spacing` and `font-variation-settings`), placing tracking or axes tokens before `font` causes them to be overwritten and disabled.

### 3. Tabular Numerals for Quantitative Data

Apply `font-variant-numeric: tabular-nums;` (or the Tailwind utility class `tabular-nums`) to all numeric figures, KPI metrics, data table columns, live counters, and timers. Monospaced tabular digits ensure optical alignment across changing numerical values without layout jitter.

## Capitalization & Text Formatting Conventions

Follow strict Material 3 English text capitalization rules across all prototype UI copy:

* **Sentence Case Standard**: Use sentence-style capitalization (`sentence case`) for ALL UI elements—only the first letter of the first word is capitalized. This applies to page titles, card headers, form labels, menu items, navigation links, top app bar titles, and button labels (e.g. "Create new project", "Save draft", "Settings and privacy").
* **Preserving Proper Nouns & Brands**: Capitalize proper nouns, brand names, and product names according to their official branding (e.g., "Google Cloud", "Android", "Material Design", "YouTube").
* **Preserving Acronyms**: Keep standard capitalization for established acronyms (e.g., "API", "URL", "HTML", "UI", "CSS", "FAB", "AI").
* **Strict Prohibition on Uppercase Text**:
  * **DO NOT** use `text-transform: uppercase` or ALL CAPS blocks on buttons, tab items, column headers, or badges.
  * Uppercase text blocks reduce reading speed, cause screen reader issues, and violate Material 3 accessibility guidelines.
* **Punctuation Rules**:
  * Skip trailing periods on single-sentence button labels, tooltip messages, bullet list items, dialog titles, and card headers.
  * Omit colons in section headings and list headers.
  * Use Oxford commas in lists containing 3 or more items.
  * Use natural contractions ("don't", "can't", "it's") to maintain a friendly, conversational tone.

## Prose Layout & Line Length Rules

* **Multi-line Body Copy Range**: Multi-line paragraph prose and content body text MUST be constrained to a `max-width` between `60ch` and `75ch` (recommended `max-width: 65ch`). This line length range prevents eye strain when moving from line endings to line beginnings.
* **No Minimum Width**: **NEVER** set a `min-width` on text containers or body blocks, allowing layouts to adapt dynamically to narrow viewports.
* **Text Wrapping & Truncation**: Allow text containers to grow vertically and wrap naturally (`overflow-wrap: break-word`). Avoid forced line breaks (`<br>`) in dynamic text strings. When truncating text with ellipses, ensure full content remains accessible via tooltips or expanded cards.

## Iconography & Relationship to Typography and Color

Material 3 aligns iconography directly with typography through Google Symbols icon fonts and semantic color roles:

* **Icon Font Setup**: Icons use the Google Symbols icon font (`--md-icon-font: 'Google Symbols'`). Render icons using the `<md-gb-icon>` custom element or `.md-icon` utility class (e.g. `<md-gb-icon>search</md-gb-icon>`).
* **Icon Sizing (`--md-icon-size`)**:
  * **ALWAYS** size icons using the `--md-icon-size` custom property (e.g., `<md-gb-icon style="--md-icon-size: 24px;">settings</md-gb-icon>`).
* **CRITICAL RESTRICTION — Never Apply Typescale Classes to Icons**:
  * **DO NOT** apply `.typescale-*` utility classes or custom `font-family` CSS properties to `<md-gb-icon>` or `.md-icon` elements.
  * Setting a typescale class applies `font: var(--md-sys-typescale-...)`, which overrides `font-family: "Google Symbols"` with `Google Sans Flex` or `Google Sans Text`. This destroys the symbol font binding and renders the icon as plain text ligatures (e.g. displaying the literal text word "settings" instead of a gear symbol).
* **Icon Color Alignment**: Match icon color to surrounding text roles using semantic tokens (e.g., `color: var(--md-sys-color-on-surface)` for primary icons, `color: var(--md-sys-color-on-surface-variant)` for secondary icons, `color: var(--md-sys-color-primary)` for active icons).

## Script Fallback & Internationalization (I18N)

Material 3 supports global language scripts through a structured fallback stack and CSS language scoping:

* **Non-Latin Script Support**:
  * `Google Sans Flex` supports Extended Latin characters. Non-Latin scripts require public `Noto Sans <Script>` fonts from Google Fonts (`Noto Sans Arabic`, `Noto Sans JP`, `Noto Sans KR`, `Noto Sans SC`, `Noto Sans TC`, `Noto Sans Devanagari`, `Noto Sans Thai`, `Noto Sans Hebrew`).
  * Do **NOT** invent non-public typeface names (e.g. "Google Sans Arabic" is INVALID).
* **Language Scoping with `:lang(...)`**:
  * Apply font family overrides scoped to language selectors on `body:lang(<code>)` and `body :lang(<code>)` rather than `html`:

```css
body:lang(ja), body :lang(ja) {
  font-family: 'Google Sans Flex', 'Google Sans', 'Noto Sans JP', var(--md-ref-typeface-plain), sans-serif;
}
body:lang(ar), body :lang(ar) {
  font-family: 'Google Sans Flex', 'Google Sans', 'Noto Sans Arabic', var(--md-ref-typeface-plain), sans-serif;
}
```

* **Preserving Script Fonts after CSS `font` Shorthand**:
  * When using CSS `font: var(--md-sys-typescale-...)` shorthands in localized subtrees, explicitly declare `font-family: inherit;` AFTER `font:` so the shorthand declaration does not reset the script typeface:

```css
.localized-title {
  font: var(--md-sys-typescale-title-medium);
  font-family: inherit; /* Preserves language-scoped Noto Sans typeface */
}
```

## Reference Breadcrumbs

**Pull [TypographyEditorial](typography_editorial.md)** when configuring custom font variation axes (`Google Sans Flex`), setting up editorial hero moments, or implementing bespoke font personalization.
