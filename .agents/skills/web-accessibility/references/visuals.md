---
title: Visuals, Contrast, Spacing & Forced Colors (gar-web-text-color, gar-web-non-text-contrast, gar-web-text-spacing, gar-web-responsive-design, gar-web-screen-orientation, gar-web-hover, gar-web-run-through-forced-colors, gar-web-dark-mode, gar-web-reduce-transparency)
shortname: gar-web-text-color
priority: HIGH
---

# Visuals: Contrast, Reflow, Hover & Forced Colors

User interfaces must remain perceivable and operable across contrast needs,
200%–400% zoom, custom text spacing, both screen orientations, and forced-colors
(Windows High Contrast) mode. This file covers
[Text Color](http://go/gar-web-text-color),
[Non-Text Contrast](http://go/gar-web-non-text-contrast),
[Text Spacing](http://go/gar-web-text-spacing),
[Responsive Design](http://go/gar-web-responsive-design),
[Screen Orientation](http://go/gar-web-screen-orientation),
[Hover](http://go/gar-web-hover),
[Forced Colors](http://go/gar-web-run-through-forced-colors),
[Dark Mode](http://go/gar-web-dark-mode), and
[Reduce Transparency](http://go/gar-web-reduce-transparency).

## 1. GAR Checkpoints & Core Rules

-   **Color Contrast & Color Independence (`gar-web-text-color`,
    `gar-web-non-text-contrast`):**
    -   **Contrast Ratios:** Standard text (`< 18pt` or `< 14pt bold`) requires
        at least **4.5:1** contrast against its background. Large text (`>=
        18pt` or `>= 14pt bold`), informative icons, and interactive UI
        boundaries (input borders, focus rings, checkboxes) require at least
        **3.0:1** contrast.
    -   **Material Design 3 (HCT Tone Delta):** In Material 3's HCT color space,
        contrast is determined by Tone (`T`, `0`–`100`) difference: `ΔT =
        |T_foreground - T_background|`. Maintain **`ΔT >= 50`** for normal text
        (`>= 4.5:1`) and **`ΔT >= 40`** for large text and UI components (`>=
        3.0:1`).
    -   **Never Rely on Color Alone:** Always pair color cues with a secondary
        visual/programmatic indicator (e.g., underlines on inline links, icons
        plus text labels for status badges and chart series).
-   **Text Spacing, Reflow & Orientation (`gar-web-text-spacing`,
    `gar-web-responsive-design`, `gar-web-screen-orientation`):**
    -   **Relative Units & Flexible Containers:** Use `rem`/`em` for typography
        and `min-height` instead of fixed `height` with `overflow: hidden` so
        text can expand (`1.5x` line-height, `0.12em` letter-spacing) and reflow
        at 320 CSS px width (400% zoom) without clipping or 2D scrolling.
    -   **No Orientation Lock:** Support both portrait and landscape layouts.
-   **Hover & Focus Popovers (`gar-web-hover`):**
    -   **Dismissible, Hoverable & Persistent:** Tooltips or popovers triggered
        by pointer hover or keyboard focus must stay visible when moving the
        pointer onto the tooltip itself (**Hoverable**), close on `Escape`
        without moving focus (**Dismissible**), and remain visible until the
        user moves hover/focus away or dismisses it (**Persistent**).
-   **Forced Colors, Dark Mode & Transparency
    (`gar-web-run-through-forced-colors`, `gar-web-dark-mode`,
    `gar-web-reduce-transparency`):**
    -   **Forced Colors (`@media (forced-colors: active)`):** Because
        `box-shadow` and background colors are stripped in Windows High Contrast
        mode, cards, modals, and buttons must define explicit borders (e.g.,
        `1px solid transparent` in default mode, or `CanvasText`/`ButtonBorder`
        in `forced-colors: active`) and use `currentColor` for SVG fills.

## 2. Decision Matrix

Visual Element / Mode                      | Minimum Threshold / CSS Rule                                                                         | GAR 2027 Criterion
:----------------------------------------- | :--------------------------------------------------------------------------------------------------- | :-----------------
**Normal Body Text (<18pt)**               | Contrast `>= 4.5:1` (or Material 3 HCT `ΔT >= 50`, e.g., Tone `40` on Tone `90`).                    | `gar-web-text-color`
**Large Text (>=18pt) & UI Borders/Icons** | Contrast `>= 3.0:1` (or Material 3 HCT `ΔT >= 40`, e.g., Tone `50` on Tone `90`).                    | `gar-web-non-text-contrast`
**Inline Links & Status Badges**           | Color + `text-decoration: underline` (links) or icon + text label (badges).                          | `gar-web-text-color`
**Text Containers & Cards**                | `min-height` (never fixed `height` + `overflow: hidden`), `rem`/`em` sizing, flex/grid wrap.         | `gar-web-text-spacing`, `gar-web-responsive-design`
**Forced Colors (High Contrast)**          | `border: 1px solid transparent` (or `@media (forced-colors: active) { border-color: CanvasText; }`). | `gar-web-run-through-forced-colors`

## 3. Implementation Patterns

### Contrast, Secondary Indicators & Flexible Reflow

```css
/* GOOD: High-contrast text, underlined inline links, and flexible container */
.status-badge-error {
  background-color: #fce8e6; /* M3 Tone 90 */
  color: #8c1d18;            /* M3 Tone 30 (ΔT = 60 >= 50 -> passes 4.5:1) */
  border: 1px solid #b3261e; /* M3 Tone 40 (ΔT = 50 >= 40 -> passes 3.0:1) */
  min-height: 2rem;          /* Expands with text zoom; no fixed px height */
  padding: 0.25rem 0.75rem;
}

p a {
  color: #0b57d0;
  text-decoration: underline;
}
```

### Forced Colors (High Contrast Mode) Support

```css
/* GOOD: Transparent border reserves space and becomes visible automatically in forced-colors mode */
.card,
.modal-dialog {
  min-height: 6rem;
  padding: 1rem;
  border: 1px solid transparent;
}

@media (forced-colors: active) {
  .card,
  .modal-dialog {
    border-color: CanvasText;
  }
  .custom-selected {
    outline: 2px solid Highlight;
  }
}
```

## 4. Blockers (Auto-Fail)

1.  **Insufficient Text or UI Contrast (`color-contrast`):** Text below `4.5:1`
    (M3 `ΔT < 50`) or interactive borders/icons below `3.0:1` (M3 `ΔT < 40`).
2.  **Color-Only Meaning (`link-in-text-block`):** Conveying error/success
    states or inline links by color alone without an icon, text label, or
    underline.
3.  **Fixed-Height Text Clipping & Disabled Zoom (`meta-viewport`):** Setting
    `user-scalable=no` or `maximum-scale < 2` on `<meta name="viewport">`, or
    applying fixed pixel `height` with `overflow: hidden` to text containers.
4.  **Unreachable / Unclosable Hover Tooltips:** Tooltips that disappear when
    the user moves the mouse pointer onto the tooltip or cannot be dismissed
    with `Escape`.
5.  **Invisible Boundaries in Forced Colors Mode:** Relying solely on
    `box-shadow` for modal/card/button boundaries without a fallback border in
    `@media (forced-colors: active)`.
