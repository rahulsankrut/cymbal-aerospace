# Typography Reference

This document provides a comprehensive guide to typography, typescale roles, token bindings, capitalization conventions, iconography styling, and text-formatting rules in the Workspace Design System (`workspace-design-system`).

## Overview

Typography in the Workspace Design System is driven by two primary brand font families and an icon font family:

- **Google Sans**: Used for display, headline, and large title roles.
- **Google Sans Text**: Used for body passages, medium/small titles, labels, captions, and standard form controls.
- **Google Symbols**: Used for vector font iconography (`--md-icon-font: 'Google Symbols'`).

Typography tokens are defined as CSS `font` shorthand declarations that combine font size, line height, and font family. In gBreeze, Workspace tokens (`--ws-sys-typescale-*`) are bound directly to gBreeze tokens (`--md-sys-typescale-*`).

All typescale roles are structured across three size suffixes: `-sm` (small), `-md` (medium), and `-lg` (large).

> **CRITICAL RULE**: ALWAYS use abbreviated size suffixes (`-sm`, `-md`, `-lg`). Full-word suffixes such as `-small`, `-medium`, or `-large` DO NOT exist in the design system and fail silently.

## Typescale Roles and Hierarchy

The typescale is organized into five semantic roles, each serving a specific structural purpose in the UI:

### 1. Display (`display`)

Display typography is reserved for short, prominent hero text, large display numbers, splash headers, and impactful dashboard callouts.

- **`display-lg`**: `3.5625rem` / `4rem` (57px / 64px), `Google Sans`
- **`display-md`**: `2.8125rem` / `3.25rem` (45px / 52px), `Google Sans`
- **`display-sm`**: `2.25rem` / `2.75rem` (36px / 44px), `Google Sans`

### 2. Headline (`headline`)

Headlines mark major screen transitions, primary page titles, and top-level section headers.

- **`headline-lg`**: `2rem` / `2.5rem` (32px / 40px), `Google Sans`
- **`headline-md`**: `1.75rem` / `2.25rem` (28px / 36px), `Google Sans`
- **`headline-sm`**: `1.5rem` / `2rem` (24px / 32px), `Google Sans`

### 3. Title (`title`)

Titles provide medium emphasis for subheaders, card titles, section dividers, dialog headers, list headers, and navigation drawers.

- **`title-lg`**: `1.375rem` / `1.75rem` (22px / 28px), `Google Sans`
- **`title-md`**: `1rem` / `1.5rem` (16px / 24px), `Google Sans Text` (weight `500`)
- **`title-sm`**: `0.875rem` / `1.25rem` (14px / 20px), `Google Sans Text` (weight `500`)

### 4. Body (`body`)

Body typography is designed for readable passages of text, paragraph prose, descriptions, list item details, and table data.

- **`body-lg`**: `1rem` / `1.5rem` (16px / 24px), `Google Sans Text`
- **`body-md`**: `0.875rem` / `1.25rem` (14px / 20px), `Google Sans Text`
- **`body-sm`**: `0.75rem` / `1rem` (12px / 16px), `Google Sans Text` (tracking `0.00625rem`)

### 5. Label (`label`)

Labels are utilitarian styles for action buttons, chips, form field headers, badge counters, table headers, metadata tags, and captions.

- **`label-lg`**: `0.875rem` / `1.25rem` (14px / 20px), `Google Sans Text` (weight `500`)
- **`label-md`**: `0.75rem` / `1rem` (12px / 16px), `Google Sans Text` (weight `500`, tracking `0.00625rem`)
- **`label-sm`**: `0.6875rem` / `1rem` (11px / 16px), `Google Sans Text` (weight `500`, tracking `0.00625rem`)

## Default UI Role Mapping

When building layout screens, apply typescale roles according to content hierarchy:

- **Primary Page Titles & Screen Banners**: Use `headline-lg` or `headline-md`.
- **Card Titles & Section Headers**: Use `title-lg`, `title-md`, or `title-sm`.
- **KPI Metrics & Stat Cards**: Use `display-lg`, `display-md`, or `headline-lg` paired with `font-variant-numeric: tabular-nums`.
- **Paragraphs & Multi-Line Prose**: Use `body-lg` or `body-md`.
- **Captions, Timestamps & Footnotes**: Use `body-sm` or `label-sm`.
- **Table Headers & Utilitarian Controls**: Use `label-md` or `label-sm`.
- **Component Internal Text**: gBreeze custom elements (`<md-gb-button>`, `<md-gb-chip>`, `<md-gb-tabs>`) encapsulate their own internal typography scales automatically. Refer to [Components](components.md) for individual component details.

## Token Reference Table

The table below maps all 15 base typescale roles from Workspace Design System tokens to gBreeze tokens and CSS values.

| Role & Size | Workspace System Token | gBreeze Token | CSS Shorthand Value (`font`) | Tracking Token |
| --- | --- | --- | --- | --- |
| Display Large | `--ws-sys-typescale-display-large` | `--md-sys-typescale-display-lg` | `3.5625rem/4rem 'Google Sans'` | N/A |
| Display Medium | `--ws-sys-typescale-display-medium` | `--md-sys-typescale-display-md` | `2.8125rem/3.25rem 'Google Sans'` | N/A |
| Display Small | `--ws-sys-typescale-display-small` | `--md-sys-typescale-display-sm` | `2.25rem/2.75rem 'Google Sans'` | N/A |
| Headline Large | `--ws-sys-typescale-headline-large` | `--md-sys-typescale-headline-lg` | `2rem/2.5rem 'Google Sans'` | N/A |
| Headline Medium | `--ws-sys-typescale-headline-medium` | `--md-sys-typescale-headline-md` | `1.75rem/2.25rem 'Google Sans'` | N/A |
| Headline Small | `--ws-sys-typescale-headline-small` | `--md-sys-typescale-headline-sm` | `1.5rem/2rem 'Google Sans'` | N/A |
| Title Large | `--ws-sys-typescale-title-large` | `--md-sys-typescale-title-lg` | `1.375rem/1.75rem 'Google Sans'` | N/A |
| Title Medium | `--ws-sys-typescale-title-medium` | `--md-sys-typescale-title-md` | `500 1rem/1.5rem 'Google Sans Text'` | N/A |
| Title Small | `--ws-sys-typescale-title-small` | `--md-sys-typescale-title-sm` | `500 0.875rem/1.25rem 'Google Sans Text'` | N/A |
| Body Large | `--ws-sys-typescale-body-large` | `--md-sys-typescale-body-lg` | `1rem/1.5rem 'Google Sans Text'` | N/A |
| Body Medium | `--ws-sys-typescale-body-medium` | `--md-sys-typescale-body-md` | `0.875rem/1.25rem 'Google Sans Text'` | N/A |
| Body Small | `--ws-sys-typescale-body-small` | `--md-sys-typescale-body-sm` | `0.75rem/1rem 'Google Sans Text'` | `--ws-sys-typescale-body-small-tracking` (`0.00625rem`) |
| Label Large | `--ws-sys-typescale-label-large` | `--md-sys-typescale-label-lg` | `500 0.875rem/1.25rem 'Google Sans Text'` | N/A |
| Label Medium | `--ws-sys-typescale-label-medium` | `--md-sys-typescale-label-md` | `500 0.75rem/1rem 'Google Sans Text'` | `--ws-sys-typescale-label-medium-tracking` (`0.00625rem`) |
| Label Small | `--ws-sys-typescale-label-small` | `--md-sys-typescale-label-sm` | `500 0.6875rem/1rem 'Google Sans Text'` | `--ws-sys-typescale-label-small-tracking` (`0.00625rem`) |

## Applying Typography in Prototypes

There are two supported ways to apply typography in web prototypes:

### Method 1: Tailwind / CSS Utility Classes (Preferred)

When styling standard HTML elements in markup, apply `.typescale-<scale>-<size>` or `.typescale-emphasized-<scale>-<size>` utility classes directly:

```html
<h1 class="typescale-headline-lg text-on-surface">Main Dashboard</h1>

<p class="typescale-body-md text-on-surface">
  Standard body passage with <span class="typescale-emphasized-body-md">emphasized text</span>.
</p>
```

#### Emphasized Typescale Scale (`typescale-emphasized-*`)

Google Sans Flex utilizes variable font axes (`font-variation-settings: 'wght' 400`). Because the `'wght'` variation axis takes precedence over CSS `font-weight`, standard Tailwind weight utilities like `font-medium` or `font-bold` **HAVE NO EFFECT** when paired with `.typescale-*`.

To render text in medium (`500`) or bold (`600`) weight, ALWAYS use `.typescale-emphasized-<scale>-<size>`:

```html
<!-- ❌ DON'T: font-medium is ignored because typescale-title-md sets 'wght' 400 -->
<h3 class="typescale-title-md font-medium">Ignored Weight</h3>

<!-- ✅ DO: Use typescale-emphasized-* for medium/semibold weight -->
<h3 class="typescale-emphasized-title-md">Proper Emphasized Title</h3>
```

### Method 2: Custom CSS Declarations

When writing custom CSS rules in `<style>` blocks, bind all three custom property tokens together in order (`font`, `letter-spacing`, and `font-variation-settings`):

```css
.custom-card-title {
  font: var(--md-sys-typescale-title-lg);
  letter-spacing: var(--md-sys-typescale-title-lg-tracking);
  font-variation-settings: var(--md-sys-typescale-title-lg-axes);
}

.custom-emphasized-subtitle {
  font: var(--md-sys-typescale-emphasized-title-md);
  letter-spacing: var(--md-sys-typescale-title-md-tracking);
  font-variation-settings: var(--md-sys-typescale-emphasized-title-md-axes);
}
```

### Prohibited Typography Classes

The following Tailwind utilities are unmapped or reset to `initial` in the gBreeze theme stylesheet and MUST NOT be used:

- **No Default Text Sizes**: Do NOT use `.text-xs`, `.text-sm`, `.text-base`, `.text-lg`, `.text-xl`, `.text-2xl`, etc.
- **No Default Font Families**: Do NOT use `.font-sans`, `.font-serif`, `.font-mono`.
- **No Default Tracking or Leading**: Do NOT use `.tracking-*` or `.leading-*`.

## Capitalization Conventions

Adhere strictly to standard casing rules across all prototype copy:

- **Sentence Case Standard**: Use sentence case for ALL UI copy, including page titles, section headers, card titles, button labels, tab headers, table headers, menu items, chip tags, tooltips, and dialog headlines. Capitalize only the first letter of the first word and proper nouns (e.g., "Save changes", "Create new document", "Account settings").
- **Title Case Restrictions**: Title Case is strictly prohibited except when referencing proper nouns, trademarked product names, or official brand titles (e.g., "Google Workspace", "Gemini", "Google Drive").
- **No Uppercase Transformation**: NEVER apply `text-transform: uppercase` or Tailwind `uppercase` to buttons, tabs, chips, labels, form controls, or table headers. All UI elements must maintain natural sentence case.
- **Preserve Acronyms and Proper Nouns**: Retain standard capitalization for acronyms, technical initialisms, and brand names (e.g., "API", "AI", "URL", "ID", "PDF", "Google", "Workspace").

## Readability & Numeric Formatting Rules

### Multi-Line Body Copy Width Limit

To ensure optimal reading length, constrain multi-line body paragraphs and long prose passages to a `max-width` of **`60ch` to `75ch`** (e.g., `max-w-[65ch]` in Tailwind or `max-width: 65ch;` in CSS). Never specify a `min-width` on body copy containers.

```html
<article class="max-w-[65ch]">
  <p class="typescale-body-lg text-on-surface">
    This multi-line paragraph is constrained to 65 characters per line for optimal reading comfort.
  </p>
</article>
```

### Tabular Numerals (`tabular-nums`)

For data tables, KPI stat counters, financial totals, timers, and aligned metric cards, apply `font-variant-numeric: tabular-nums` (or the `.tabular-nums` utility) to ensure equal-width numeric alignment:

```html
<div class="typescale-display-lg tabular-nums text-primary">
  $1,248,500.00
</div>
```

## Iconography and Typography

Iconography in Workspace Design System is integrated using Google Symbols font glyphs or inline SVG icons.

### Icon Font Family Setup

Icons use the `Google Symbols` font family, configured globally via `--md-icon-font`:

```css
@import url("https://fonts.googleapis.com/css2?family=Google+Symbols&display=block");

:root {
  --md-icon-font: 'Google Symbols';
}
```

### Sizing Icons (`--md-icon-size`)

ALWAYS size `<md-gb-icon>` or `.md-icon` using the `--md-icon-size` CSS variable or inline utility:

```html
<!-- Custom element icon -->
<md-gb-icon style="--md-icon-size: 20px">search</md-gb-icon>

<!-- Utility class icon -->
<span class="md-icon [--md-icon-size:24px]" aria-hidden="true">settings</span>
```

### CRITICAL PROHIBITION: Never Apply `.typescale-*` to Icons

> **CRITICAL RULE**: NEVER place `.typescale-*` or `.font-*` classes directly on `<md-gb-icon>` or `.md-icon`.
>
> `.typescale-*` sets the CSS `font:` shorthand (`font-family: "Google Sans Flex"`), which overwrites `"Google Symbols"` and causes the icon glyph to render as plain text string (e.g. "search" or "settings").

```html
<!-- ❌ DON'T: Overwrites icon font family and breaks icon rendering -->
<md-gb-icon class="typescale-title-md">search</md-gb-icon>
<span class="md-icon typescale-headline-sm">favorite</span>

<!-- ✅ DO: Control icon size with --md-icon-size and color with text-* -->
<md-gb-icon style="--md-icon-size: 20px" class="text-primary">search</md-gb-icon>
<span class="md-icon [--md-icon-size:24px] text-on-surface" aria-hidden="true">favorite</span>
```

### Icon Component vs Utility Class

- **`<md-gb-icon>`**: Use inside gBreeze custom elements, Lit component templates, or shadow roots.
- **`.md-icon`**: Use for light DOM standalone HTML elements. Always set `aria-hidden="true"` when using `.md-icon`.

```html
<!-- Standard light DOM icon -->
<span class="md-icon [--md-icon-size:20px] text-on-surface-variant" aria-hidden="true">more_vert</span>
```

## Localization & Non-Latin Font Fallbacks

Workspace Design System provides comprehensive support for non-Latin scripts (Arabic, Japanese, Korean, Chinese, Devanagari, Thai, Hebrew) and RTL text layouts using Google Fonts `Noto Sans <Script>` families.

**Pull [LocalizedTypography](localized-typography.md)** when configuring multi-language, non-Latin, or RTL typography fallbacks.
