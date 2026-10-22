---
title: Focus Management (GAR Web 1.3)
shortname: gar-web-focus
priority: MANDATORY_CRITICAL
---

# Focus: Flow & Visibility

All interactive elements MUST receive focus in a logical, sequential order
matching the visual flow.

## 1. Focus Flow Rules (MANDATORY)

-   **Logical Sequence:** Follow reading order (Left-to-Right, Top-to-Bottom).
-   **No Mystery Focus:** Focus must NEVER move to off-screen or invisible
    elements.
-   **No Auto-Submit:** Focusing an element must NOT trigger a context change
    (e.g., auto-submitting a form or opening a new window).
-   **Persistent Visibility:** `:focus-visible` MUST be high-contrast and never
    obscured by other elements.

## 2. Dynamic Focus Logic

Scenario         | Required Action
:--------------- | :--------------
**Open Modal**   | Move focus to the first interactive element or primary close button inside the modal.
**Close Modal**  | When dismissed (Close button / `Escape`), return focus to the most recent active element outside the dialog (or to a logical target if closed by an in-dialog action; never drop focus to `<body>`).
**Item Deleted** | Move focus to the next logical item in the list or the parent container.
**Form Error**   | Move focus to the error summary or the first invalid field.

## 3. High-Priority Code Patterns

### Complete Modal Focus Lifecycle & Focus Trap (`<dialog>` & `role="dialog"`)

When implementing modal dialogs or modal drawers (including inside Python or
backend HTML string templates):

> **Note on Non-Modal Popovers:** Elements using the native HTML Popover API
> (`popover` attribute) are non-modal by default. Do NOT apply
> `aria-modal="true"`, background `inert`, or a `Tab` focus trap to non-modal
> popovers (though `Escape` should still dismiss them).

1.  **Trigger Semantics:** Use `<button type="button" aria-haspopup="dialog">`.
2.  **Dialog Landmarks (`<dialog>` vs. Custom Container):** Prefer native
    `<dialog aria-labelledby="<title-id>">` opened via `.showModal()` (which
    provides `role="dialog"`, `aria-modal="true"`, background inertness, `Tab`
    focus trapping, and `Escape` dismissal natively). For custom modal
    containers (e.g., `<div id="helpModal">`), declare `role="dialog"`,
    `aria-modal="true"`, and `aria-labelledby="<title-id>"`.
3.  **Background Inertness:** When a custom modal dialog is open, make other
    elements on the page inert by setting `inert` (or `aria-hidden="true"`) on
    sibling page containers (e.g., `<main>`), and remove it when the modal
    closes.
4.  **Save & Move Focus on Open:** Save `lastActiveElement =
    document.activeElement` before opening, then focus either the first
    interactive element inside the modal or the primary close button.
5.  **Trap `Tab` / `Shift+Tab` & Close on `Escape`:** Wrap focus between the
    first and last focusable elements inside the open modal, and close on
    `Escape` or backdrop click.
6.  **Restore Focus on Close (with Fallback):** When the dialog is dismissed via
    the close button, `Escape`, or backdrop click, check
    `lastActiveElement.isConnected` and call `lastActiveElement.focus()`,
    falling back to the trigger button selector if `lastActiveElement` is null
    or detached from the DOM. When the dialog closes because the user took an
    action inside the dialog, move focus to the application's logical target for
    that action (never allowing focus to drop to `<body>`).

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

### CSS Focus Reset (The "Safe" Way)

```css
/* NEVER use outline: none without a replacement */
:focus-visible {
  outline: 3px solid #005a9c;
  outline-offset: 2px;
}
```

## 4. Blockers (Auto-Fail)

1.  **Non-Modal Keyboard Traps:** User can `Tab` into a standard page widget but
    cannot `Tab` out.
2.  **Unbounded Modal Focus:** Opening a `role="dialog" aria-modal="true"`
    overlay without trapping `Tab`/`Shift+Tab` inside the modal or failing to
    restore focus to `lastActiveElement` on close.
3.  **Hidden Focus:** `outline: none` or `outline: 0` in CSS without a
    high-contrast `:focus-visible` indicator.
4.  **Sequential Disruption:** Tab order that skips visual sections of the page.
