---
title: Focus Management & DOM Order (gar-web-focus, gar-web-dom-order)
shortname: gar-web-focus
priority: MANDATORY_CRITICAL
---

# Focus: Logical Order, Visibility & Modal Lifecycle

All interactive elements must receive focus in a sequential order matching the
visual layout ([go/gar-web-dom-order](http://go/gar-web-dom-order)) with a
clearly visible focus indicator ([go/gar-web-focus](http://go/gar-web-focus)).

> **Framework Note:** For Angular closing animation hooks, AngularDart
> `@ViewChild(read: HtmlElement)` / `DomService.scheduleWrite`, Wiz view
> transitions, or Flutter `ReadingOrderTraversalPolicy()`, load the matching
> file in `references/frameworks/` first.

## 1. GAR Checkpoints & Core Rules

-   **DOM & Focus Order (`gar-web-dom-order`, `gar-web-focus`):**
    -   **Match Visual Reading Order:** Structure DOM nodes so native `Tab`
        order follows visual reading order (left-to-right, top-to-bottom in LTR;
        right-to-left in RTL). Avoid using `flex-direction: row-reverse` or CSS
        `order` on interactive elements.
    -   **No Hidden or Off-Screen Focus:** Hidden panels, closed menus, and
        off-screen drawers must use `hidden`, `display: none`, `visibility:
        hidden`, or `inert` so keyboard focus never disappears into invisible
        elements.
    -   **Visible Focus Indicator:** Every focusable control must display a
        high-contrast `:focus-visible` indicator (`>= 3:1` contrast) that is not
        clipped by `overflow: hidden` or obscured by sticky headers/footers.
-   **Modal Dialog & Overlay Focus Lifecycle (`gar-web-focus`):**
    -   **Trigger & Container Semantics:** Trigger buttons must set
        `aria-haspopup="dialog"`. Prefer native `<dialog
        aria-labelledby="<title-id>">` opened via `.showModal()`. For custom
        modal containers (`<div id="...">`), set `role="dialog"`,
        `aria-modal="true"`, and `aria-labelledby="<title-id>"`, and mark
        sibling background containers `inert` while open. (Note: non-modal HTML
        `popover` elements must **not** trap `Tab` or set background `inert`.)
    -   **Trap & Restore Focus:** Save `lastActiveElement =
        document.activeElement` before opening, move focus inside the dialog on
        open, cycle `Tab`/`Shift+Tab` strictly between the first and last
        focusable elements while open, close on `Escape`, and restore focus to
        `lastActiveElement` (with a trigger selector fallback) on close so focus
        never drops to `<body>`.
    -   **Centralized Close / Animation-Cleanup Hook & Controller `.focus()`
        API:** Always trigger focus restoration inside the **shared close or
        closing-animation cleanup method** (which runs for all dismissal paths:
        close button, `Escape` key, and backdrop/outside click), never inside a
        single collapse/close button click handler alone. When the target
        component exposes an encapsulated Controller `.focus()` method (e.g.,
        `this.thumbnailController.focus()`), call the Controller API instead of
        querying internal child DOM nodes directly.
    -   **Fix Focus-Stealing Race Conditions at the Overlay Source:** If a
        background-mounted dialog or overlay steals focus on initial page load
        (or fires a close/restore-focus event before ever being opened), prevent
        the spurious event/autofocus emission **at the dialog source** (guarding
        on whether the dialog was actually opened) rather than adding defensive
        focus-suppression checks to downstream search inputs or page controls.

## 2. Decision Matrix

Scenario                                        | Required Focus Action                                                                   | Target Element
:---------------------------------------------- | :-------------------------------------------------------------------------------------- | :-------------
**Open Modal Dialog**                           | Save `document.activeElement`, set background `inert`, move focus inward.               | First interactive control or primary close `<button>` inside dialog.
**Dismiss Modal (Close / `Escape` / Backdrop)** | Remove background `inert`, restore focus to trigger (or fallback selector if detached). | `lastActiveElement.focus()` (or `.btn-trigger` fallback).
**Close Modal via In-Dialog Action**            | Move focus to the logical destination created or revealed by that action.               | Newly added item, confirmation heading (`tabindex="-1"`), or parent container.
**Delete Item in List/Table**                   | Move focus to the next surviving item, previous item, or list heading.                  | Next/previous interactive row button or container (`tabindex="-1"`).
**SPA View / Route Transition**                 | Move focus to the new view's main heading after render completes.                       | `<h1 tabindex="-1">` of the newly rendered view.

## 3. Implementation Patterns

### Complete Modal Focus Lifecycle & Focus Trap (`<dialog>` & Custom `role="dialog"`)

```javascript
// Native <dialog> (preferred when supported by layout):
// dialogEl.showModal(); // Natively traps Tab, sets background inert, and closes on Escape.

// Custom modal container (<div id="helpModal" role="dialog" aria-modal="true" aria-labelledby="...">):
let lastActiveElement = null;

function openModal() {
  const modal = document.getElementById('helpModal');
  if (!modal) return;
  lastActiveElement = document.activeElement;
  const main = document.querySelector('main');
  if (main) main.inert = true;
  modal.classList.add('open');
  const initialFocus = modal.querySelector(
      '.modal-close, button:not([disabled]), [href], input:not([disabled])'
  );
  if (initialFocus) initialFocus.focus();
}

function closeModal() {
  const modal = document.getElementById('helpModal');
  if (modal) modal.classList.remove('open');
  const main = document.querySelector('main');
  if (main) main.inert = false;
  if (
      lastActiveElement &&
      lastActiveElement.isConnected &&
      typeof lastActiveElement.focus === 'function'
  ) {
    lastActiveElement.focus();
  } else {
    const trigger = document.querySelector('.btn-help');
    if (trigger) trigger.focus();
  }
  lastActiveElement = null;
}

document.addEventListener('keydown', function(e) {
  const modal = document.getElementById('helpModal');
  if (!modal || !modal.classList.contains('open')) return;
  if (e.key === 'Escape') {
    closeModal();
    return;
  }
  if (e.key === 'Tab') {
    const focusables = modal.querySelectorAll(
        'button:not([disabled]), [href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"]):not([disabled])'
    );
    if (focusables.length === 0) return;
    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      last.focus();
      e.preventDefault();
    } else if (!e.shiftKey && document.activeElement === last) {
      first.focus();
      e.preventDefault();
    }
  }
});
```

### Visible Focus Indicator (`:focus-visible`)

```css
/* GOOD: High-contrast focus ring with offset */
:focus-visible {
  outline: 3px solid #005a9c;
  outline-offset: 2px;
}

/* BAD: Removing focus outline without a high-contrast replacement */
button:focus {
  outline: none;
}
```

## 4. Blockers (Auto-Fail)

1.  **Suppressed Focus Outline:** Using `outline: none` or `outline: 0` without
    providing a `:focus-visible` indicator meeting `>= 3:1` contrast.
2.  **Unbounded Modal Focus:** Opening a `role="dialog" aria-modal="true"`
    overlay without trapping `Tab`/`Shift+Tab` inside the dialog or allowing
    background page elements to remain focusable.
3.  **Dropped Focus on Close (`document.body` Reset):** Closing a modal, menu,
    or deleted list item and letting focus reset to the top of `<body>` instead
    of restoring focus to the trigger or next logical element.
4.  **Ghost / Off-Screen Focus:** Allowing `Tab` to reach elements inside
    visually collapsed drawers or carousels (e.g., `opacity: 0` or `transform:
    translateX(-100%)` without `visibility: hidden` or `inert`).
5.  **Visual vs. DOM Order Mismatch:** Using CSS `order`, `flex-direction:
    row-reverse`, or absolute positioning in a way that causes `Tab` focus to
    jump erratically across the screen.
