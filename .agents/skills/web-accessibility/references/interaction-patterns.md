---
title: Interaction & Gestures (GAR 1.15, 1.19, 3.5, 2.2, 2.5)
shortname: gar-web-interaction
priority: HIGH
---

# Interaction: Gestures, Shortcuts & Pointers

All complex interactions MUST have simple, single-pointer alternatives.

## 1. Gesture Alternatives (MANDATORY)

-   **Path-Based/Dragging:** Any drag-and-drop or swipe action MUST have a
    single-click alternative (e.g., a "Move" menu or "Next/Prev" buttons).
-   **Multi-Point:** Pinch-to-zoom MUST have `+/-` button alternatives.
-   **Simultaneous:** Actions requiring two hands/points MUST have a
    single-point alternative.

## 2. Keyboard Shortcuts

-   **Modifier Required:** Shortcuts MUST include a modifier key (e.g.,
    `Ctrl+S`, `Cmd+K`).
-   **Single-Key Exceptions:** Allowed ONLY if (1) focus is limited to a
    specific component or (2) the shortcut can be remapped/turned off.

## 3. Target Size & Input

-   **Touch Targets:** Minimum **44x44px** (or 48x48px on some platforms) for
    all interactive elements.
    -   **Exception:** Inline links within a block of text.
-   **Motion:** Moving/blinking content MUST be pausable by the user if it
    lasts >5 seconds.
-   **Timeouts:** If a session times out (e.g., 20 min), the user MUST be warned
    and given a way to extend it (e.g., "Press any key to stay logged in").
-   **Undo:** Critical actions (Delete, Submit) MUST be reversible or confirmed.

## 4. Implementation Patterns

### Drag-and-Drop Alternative

```html
<li data-id="1">
  Item Name
  <button aria-label="Move Item 1 Up">Up</button>
  <button aria-label="Move Item 1 Down">Down</button>
  <button aria-label="Move to Folder">Move</button>
</li>
```

### Slider with Single-Pointer Control

```html
<input type="range" id="vol" min="0" max="100">
<input type="number" aria-controls="vol" aria-label="Volume Value">
```

### Accessible Touch Target

```css
.icon-button {
  width: 24px;
  height: 24px;
  padding: 12px; /* Adds padding to reach 48x48px hit area */
  box-sizing: content-box;
}
```

## 5. Blockers (Auto-Fail)

1.  **Gesture-Locked:** A carousel that ONLY responds to swipes.
2.  **Tiny Buttons:** `icon` buttons with no padding that are impossible to tap.
3.  **Unstoppable Animation:** A background video or marquee that cannot be
    paused.
4.  **Instant Timeout:** Logging a user out without warning.
