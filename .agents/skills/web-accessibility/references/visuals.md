---
title: Visuals, Contrast & Spacing (GAR 1.14, 2.11, 1.16, 2.13)
shortname: gar-web-visuals
priority: HIGH
---

# Visuals: Contrast, Spacing & Layout

UI MUST be perceivable in high-contrast modes, lighting variations, and custom
user styles.

## 1. Color Contrast (MANDATORY)

-   **Standard Text:** Minimum **4.5:1** ratio against background.
-   **Large Text/UI Components:** Minimum **3.0:1** (Includes icons, input
    borders, and checkboxes).
-   **Material Design 3 (HCT Color Space) Contrast:**
    -   Material 3 uses the **HCT (Hue, Chroma, Tone)** color space. Contrast is
        determined solely by the difference in **Tone (T)** (perceived lightness
        from `0` to `100`). Hue and Chroma do not affect contrast calculations.
    -   **Contrast Formula:** `ΔT = |T_foreground - T_background|`
    -   **Accessibility Thresholds (Delta Tone):**
        -   **`ΔT >= 40`**: Guarantees a contrast ratio of at least **3.0:1**.
            This passes WCAG AA requirements for **large text and UI
            components** (e.g., buttons, icons, input borders, text fields).
        -   **`ΔT >= 50`**: Guarantees a contrast ratio of at least **4.5:1**.
            This passes WCAG AA requirements for **normal/small text**.
    -   *Example:* If the background color has a Tone of `90` (very light), any
        normal text placed on it MUST have a Tone of `40` or lower (`90 - 50 =
        40`) to be accessible.
-   **Color as Information:** Color MUST NOT be the only way to convey info.
    -   **Requirement:** Add secondary markers (e.g., underline for links, icons
        for status).

## 2. Text Spacing & Reflow

-   **Flexible Layouts:** Content MUST NOT clip or overlap when spacing is
    increased.
-   **Avoid Fixed Heights:** Use `min-height` instead of `height` on containers.
-   **Relative Units:** ALWAYS use `rem` or `em` for font-size, line-height, and
    padding. `px` is prohibited for text containers.

## 3. Responsive Design & Orientation

-   **One-Dimensional Scrolling:** At 320px width (mobile), users MUST NOT need
    to scroll horizontally to read text.
-   **Orientation:** Support both Portrait and Landscape. NEVER lock orientation
    unless essential (e.g., a piano app).
-   **Hover Content:** Content triggered by hover (tooltips) MUST:
    -   **Persist:** Stay visible while the mouse is over it.
    -   **Dismissible:** Be closable via `Esc` or moving the mouse.
    -   **Hoverable:** User can move the mouse *onto* the tooltip without it
        disappearing.

## 4. Forced Colors (High Contrast Mode)

-   **Standard:** Support `forced-colors: active` (Windows High Contrast).
-   **Visibility:** Pop-ups and cards MUST have a visible `border` (1px solid
    ButtonBorder) as box-shadows are removed.
-   **System Colors:** Use system color keywords (e.g., `CanvasText`,
    `Highlight`) for custom components.

## 5. Implementation Patterns

### Accessible Link

```css
/* Color + Underline (Secondary Indicator) */
a {
  color: #1a73e8;
  text-decoration: underline;
}
```

### Flexible Container

```css
.card {
  min-height: 100px; /* Adapts to text growth */
  padding: 1em;
  border: 1px solid transparent;
}

@media (forced-colors: active) {
  .card { border-color: CanvasText; } /* Ensure visibility in HCM */
}
```

## 6. Blockers (Auto-Fail)

1.  **Low Contrast:** Light gray text on white background (e.g., `#ccc` on
    `#fff`).
2.  **Insufficient Tone Difference (Material 3):** Under-threshold delta Tone
    (e.g., `ΔT < 50` for normal text, or `ΔT < 40` for UI components/large text
    in an HCT/Material 3 color system).
3.  **Fixed Pixel Containers:** `div { height: 20px; overflow: hidden; }`
    containing text.
4.  **Color-Only Status:** A red dot for "Error" without an "Error" icon or
    label.
5.  **Orientation Lock:** CSS `orientation: portrait` media queries that hide
    content in landscape.
