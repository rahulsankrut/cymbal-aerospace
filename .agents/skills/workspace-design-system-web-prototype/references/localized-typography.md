# Localized Typography Reference

This document provides detailed guidelines for handling non-Latin scripts, Right-to-Left (RTL) languages, and Google Fonts script fallbacks within the Workspace Design System (`workspace-design-system`).

## Script Font Families

When rendering content in non-Latin scripts, use official Google Fonts `Noto Sans <Script>` font families. Do NOT invent non-public `Google Sans` script font names (such as `Google Sans Arabic` or `Google Sans Japanese`), as they are not available on public CDNs and will fail to load.

- **Arabic**: `Noto Sans Arabic`
- **Japanese**: `Noto Sans JP`
- **Korean**: `Noto Sans KR`
- **Simplified Chinese**: `Noto Sans SC`
- **Traditional Chinese**: `Noto Sans TC`
- **Devanagari (Hindi, Marathi)**: `Noto Sans Devanagari`
- **Thai**: `Noto Sans Thai`
- **Hebrew**: `Noto Sans Hebrew`

## Google Fonts Import Declarations

Import required script families from Google Fonts in your stylesheet header alongside `Google Sans` and `Google Symbols`:

```css
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Google+Sans+Text:wght@400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Arabic:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+KR:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Sans+Devanagari:wght@400;500;700&family=Noto+Sans+Thai:wght@400;500;700&family=Noto+Sans+Hebrew:wght@400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Google+Symbols&display=block');
```

## Language Scoping and Font Stack Binding

Scope localized font stacks to the `<body>` tag using `:lang(...)` selectors rather than `<html>`. Target both the body element itself and all descendant elements inside it:

```css
/* Arabic */
body:lang(ar), body :lang(ar) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans Arabic', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans Arabic', sans-serif;
}

/* Japanese */
body:lang(ja), body :lang(ja) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans JP', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans JP', sans-serif;
}

/* Korean */
body:lang(ko), body :lang(ko) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans KR', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans KR', sans-serif;
}

/* Simplified Chinese */
body:lang(zh-CN), body :lang(zh-CN) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans SC', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans SC', sans-serif;
}

/* Traditional Chinese */
body:lang(zh-TW), body :lang(zh-TW) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans TC', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans TC', sans-serif;
}

/* Devanagari */
body:lang(hi), body :lang(hi) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans Devanagari', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans Devanagari', sans-serif;
}

/* Thai */
body:lang(th), body :lang(th) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans Thai', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans Thai', sans-serif;
}

/* Hebrew */
body:lang(he), body :lang(he) {
  --md-ref-typeface-brand: 'Google Sans Flex', 'Google Sans', 'Noto Sans Hebrew', sans-serif;
  --md-ref-typeface-plain: 'Google Sans Text', 'Noto Sans Hebrew', sans-serif;
}
```

## CSS `font:` Shorthand Preservation Rule

Because CSS custom property tokens like `font: var(--md-sys-typescale-body-md)` use the CSS `font` shorthand syntax, assigning `font:` resets `font-family` back to the default specified in the token (`Google Sans` or `Google Sans Text`).

To prevent the `font` shorthand from overwriting non-Latin script font families in localized subtrees, ALWAYS declare `font-family: inherit;` immediately AFTER applying `font: var(--md-sys-typescale-...)`:

```css
/* ✅ DO: Preserve script typeface after font shorthand */
.localized-title {
  font: var(--md-sys-typescale-title-lg);
  font-family: inherit;
  letter-spacing: var(--md-sys-typescale-title-lg-tracking);
  font-variation-settings: var(--md-sys-typescale-title-lg-axes);
}
```

```css
/* ❌ DON'T: Shorthand resets font-family to Google Sans, breaking non-Latin scripts */
.localized-title {
  font: var(--md-sys-typescale-title-lg);
}
```

## Right-to-Left (RTL) Layout Considerations

When working with RTL languages (such as Arabic or Hebrew):

- Set `dir="rtl"` on the element containing localized content (e.g., `<body lang="ar" dir="rtl">`).
- Use logical CSS properties (`margin-inline-start`, `padding-inline-end`, `inset-inline-start`) instead of physical directional properties (`margin-left`, `padding-right`, `left`).
- In Tailwind layout utilities, use logical spacing classes like `ps-s100` (padding-inline-start) and `pe-s100` (padding-inline-end) rather than `pl-*` or `pr-*`.
