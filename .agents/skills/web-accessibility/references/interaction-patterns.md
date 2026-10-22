---
title: Interaction, Gestures, Shortcuts & Pointers (gar-web-gesture-based-interaction, gar-web-single-pointer-operations, gar-web-dragging-movements, gar-web-single-key-shortcuts, gar-web-target-size, gar-web-motion-stoppable, gar-web-timeout)
shortname: gar-web-single-pointer-operations
priority: HIGH
---

# Interaction: Gestures, Pointers, Target Size & Timing

All complex pointer gestures must have simple single-pointer and keyboard
alternatives, interactive targets must be large enough to tap accurately, and
users must control time limits and motion. This file covers
[Gesture-Based Interaction](http://go/gar-web-gesture-based-interaction),
[Single-Pointer Operations](http://go/gar-web-single-pointer-operations),
[Dragging Movements](http://go/gar-web-dragging-movements),
[Single-Key Shortcuts](http://go/gar-web-single-key-shortcuts),
[Target Size](http://go/gar-web-target-size),
[Motion Stoppable](http://go/gar-web-motion-stoppable), and
[Timeout](http://go/gar-web-timeout).

## 1. GAR Checkpoints & Core Rules

-   **Pointer & Gesture Alternatives (`gar-web-gesture-based-interaction`,
    `gar-web-single-pointer-operations`, `gar-web-dragging-movements`):**
    -   **Single-Pointer & Keyboard Equivalents:** Every drag-and-drop,
        swipe/path gesture, multipoint pinch-to-zoom, or device-motion action
        must provide a single-click/tap and keyboard-operable alternative (e.g.,
        "Move Up / Move Down" buttons, a "Move to..." menu, or `+ / -` zoom
        buttons).
    -   **No Down-Event Lock:** Trigger actions on `click` / `pointerup` rather
        than `mousedown` / `touchstart` so users can slide off a control to
        cancel an accidental press.
-   **Keyboard Shortcuts (`gar-web-single-key-shortcuts`):**
    -   **Require Modifier Keys:** Global keyboard shortcuts must include a
        non-printable modifier key (`Ctrl`, `Alt`, `Meta`/`Cmd`) unless the
        shortcut is active only while focus is inside that specific widget or
        the user can disable/remap single-key shortcuts.
-   **Touch & Pointer Target Size (`gar-web-target-size`):**
    -   **Minimum Hit Area:** Interactive controls must provide a minimum target
        area of **44x44 CSS pixels** (48x48dp recommended for Material/mobile),
        or maintain equivalent non-overlapping spacing, except for inline links
        within sentences.
-   **Motion & Timeouts (`gar-web-motion-stoppable`, `gar-web-timeout`):**
    -   **Pausable Motion:** Auto-playing carousels, marquees, or animations
        lasting `> 5 seconds` must include a visible Pause/Stop button and
        respect `@media (prefers-reduced-motion: reduce)`.
    -   **Timeout Warning & Extension:** Before a session or auth timeout
        expires, warn the user and allow extending the time limit with a simple
        action (e.g., pressing `Space`/`Enter` on an "Extend Session" button).

## 2. Decision Matrix

Interaction Pattern                 | Required Accessible Alternative                                                                                                                                    | GAR 2027 Criterion
:---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------
**Drag-and-Drop Reordering**        | Dedicated `<button>` controls ("Move Up", "Move Down", or "Move to position") alongside drag handles.                                                              | `gar-web-dragging-movements`
**Swipe Carousel / Pinch Zoom**     | Visible `<button>` controls for "Previous / Next" and "Zoom In / Zoom Out".                                                                                        | `gar-web-single-pointer-operations`
**Small Icon Glyph (e.g. 24x24px)** | Expand hit area to `>= 44x44px` (48x48px) using `padding` or `min-width`/`min-height`.                                                                             | `gar-web-target-size`
**Custom Keyboard Shortcut**        | Require a modifier key (`e.ctrlKey`, `e.altKey`, or `e.metaKey`), ignore events when focus is inside text inputs, or provide a setting to disable/remap shortcuts. | `gar-web-single-key-shortcuts`
**Auto-Advancing Carousel (>5s)**   | Provide `<button type="button" aria-label="Pause carousel">` and pause on keyboard focus/hover.                                                                    | `gar-web-motion-stoppable`

## 3. Implementation Patterns

### Drag-and-Drop List with Single-Pointer & Keyboard Buttons

When fixing a drag-and-drop list where a drag handle is implemented as `<div
role="button" draggable>`, convert the drag handle itself to a `<button
type="button" aria-label="Reorder ...">` (with `aria-hidden="true"` on the inner
grip `<svg>`) or add `tabindex="0"` and keyboard handling alongside explicit
"Move Up" / "Move Down" `<button type="button">` controls:

```html
<!-- GOOD: Reorderable item uses semantic <button> controls and hides decorative grip SVG -->
<li class="task-item" data-id="1">
  <span>Prepare Q4 Launch Review</span>
  <div class="task-actions" role="group" aria-label="Reorder Prepare Q4 Launch Review">
    <button type="button" aria-label="Move Prepare Q4 Launch Review up">Move Up</button>
    <button type="button" aria-label="Move Prepare Q4 Launch Review down">Move Down</button>
  </div>
</li>
```

### Accessible Touch Target Size & Reduced Motion

```css
/* GOOD: 24px icon padded to a 48x48px interactive hit area */
.icon-button {
  min-width: 48px;
  min-height: 48px;
  padding: 12px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* GOOD: Respect user preference for reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 4. Blockers (Auto-Fail)

1.  **Drag-Only or Swipe-Only Controls:** Kanbans, sliders, or carousels that
    can only be operated by dragging or swiping without single-click/keyboard
    buttons.
2.  **Undersized Touch Targets (`target-size`):** Interactive buttons or icons
    smaller than `44x44px` (or tightly packed without spacing) outside inline
    prose.
3.  **Unmodified Single-Key Shortcuts:** Binding bare character keys (`'s'`,
    `'/'`, `'k'`) globally on `window`/`document` without checking that focus is
    outside text inputs or allowing users to disable them (breaks speech-input
    dictation).
4.  **Unstoppable Animation (>5s):** Auto-scrolling tickers, looping background
    videos, or carousels without a keyboard-accessible Pause/Stop control.
5.  **Unwarned Session Timeout:** Logging a user out or discarding form state on
    a timer without a prior warning dialog and extension button.
