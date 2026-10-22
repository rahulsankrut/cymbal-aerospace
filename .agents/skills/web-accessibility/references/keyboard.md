---
title: Keyboard Operability (gar-web-keyboard)
shortname: gar-web-keyboard
priority: MANDATORY_CRITICAL
---

# Keyboard Navigation: Operability & Semantics

All interactive functionality must be operable through a keyboard-only interface
without requiring mouse hover, drag, or touch gestures
([go/gar-web-keyboard](http://go/gar-web-keyboard)).

> **Framework Note:** When authoring composite components or menu triggers in
> Angular, AngularDart/ACX, Soy/Closure, or Lit/Wiz, load the matching file in
> `references/frameworks/` to ensure ARIA state attributes are bound to the
> inner `<button>` rather than outer wrapper containers.

## 1. GAR Checkpoints & Core Rules

-   **Keyboard Functionality (`gar-web-keyboard`):**
    -   **Native Interactive Elements First:** Use `<button type="button">` for
        in-page actions/toggles and `<a href="...">` for navigation. Native
        elements provide built-in `Tab` focusability and `Enter`/`Space`
        activation.
    -   **TabIndex Discipline:** Never use positive `tabindex` (`tabindex="1"`
        or higher), which breaks natural DOM tab order. Use `tabindex="0"` only
        on custom interactive roles (`role="button"`), and `tabindex="-1"` for
        elements that receive programmatic `.focus()` only.
    -   **Popup & Menu Trigger State:** Menu and popup trigger buttons must
        declare `aria-haspopup="menu"` (or `"dialog"`, `"listbox"`) and toggle
        `aria-expanded="true|false"` directly on the interactive `<button>`.
    -   **Dismissal & Escape:** Pressing `Escape` must close open menus,
        popovers, and modal dialogs and return focus to the trigger.

## 2. Decision Matrix

Component Type               | Required Element & ARIA                                                   | Required Keyboard Behavior
:--------------------------- | :------------------------------------------------------------------------ | :-------------------------
**Action / Toggle Button**   | `<button type="button">` (with `aria-pressed` if toggle)                  | Reached via `Tab`; activates on `Enter` and `Space`.
**Navigation Link**          | `<a href="/destination">`                                                 | Reached via `Tab`; activates on `Enter`.
**Menu / Popup Trigger**     | `<button type="button" aria-haspopup="menu" aria-expanded="false">`       | `Enter`/`Space`/`Down Arrow` opens menu and sets `aria-expanded="true"`; `Escape` closes.
**Menu / Listbox Items**     | `role="menu"` / `role="listbox"` with `role="menuitem"` / `role="option"` | `Tab` enters group; `Arrow` keys move between items; `Escape` exits.
**Tabs / Disclosure**        | `<button role="tab" aria-selected="true">` / `<details><summary>`         | `Space`/`Enter` toggles disclosure; `Arrow` keys switch tabs.
**Custom Non-Native Button** | `<div role="button" tabindex="0">` *(only when `<button>` is impossible)* | Must implement explicit `keydown` handler for both `Enter` and `Space` (with `e.preventDefault()` on `Space`).

## 3. Implementation Patterns

### Buttons & Links (Native Default vs. Custom Fallback)

```html
<!-- GOOD (Default Path): Native <button> for actions and <a href> for navigation -->
<button type="button" onclick="submitForm()">Submit</button>
<a href="/settings">Account Settings</a>

<!-- GOOD (Custom Fallback -- ONLY if native <button> is impossible): Requires role, tabindex="0", and Enter/Space keydown -->
<div role="button"
     tabindex="0"
     onclick="act()"
     onkeydown="if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); act(); }">
  Custom Action
</div>

<!-- BAD: Clickable <div> or <span> without keyboard focusability or Enter/Space handling -->
<div class="btn" onclick="act()">Submit</div>
```

### Menu & Popup Triggers

```html
<!-- GOOD: aria-haspopup and aria-expanded placed directly on the interactive <button> -->
<button type="button"
        class="dropdown-button-outlined"
        aria-haspopup="menu"
        aria-expanded="false"
        aria-controls="options-menu">
  Filter Options
</button>

<!-- BAD (Container Trap): Applying menu trigger attributes to an outer wrapper <span> or <div> -->
<span class="chip-container" aria-haspopup="menu" aria-expanded="false">
  <button type="button" class="chip-action">Filter Options</button>
</span>
```

## 4. Blockers (Auto-Fail)

1.  **Non-Interactive Click Handlers:** Attaching `onclick` or click listeners
    to `<div>`, `<span>`, `<li>`, or `<img>` without `role`, `tabindex="0"`, and
    `Enter`/`Space` keyboard handlers.
2.  **Disallowed ARIA on Containers / "Container Trap" (`aria-allowed-attr`,
    `nested-interactive`):** Applying interactive state or popup attributes
    (`aria-haspopup`, `aria-expanded`, `aria-controls`, `aria-pressed`) to a
    generic outer wrapper (`<span>` or `<div>`, such as a chip or card host)
    instead of the inner `<button>`, or adding `role="button"` to an outer
    container that already wraps an inner `<button>` or `<a>`. When fixing
    `nested-interactive` on a clickable card, **never** merely strip
    `role="button"` and `tabindex="0"` while leaving `@click`/`onclick` on the
    outer `<div>` (which makes the card's primary action keyboard-inaccessible);
    always move the primary navigation/action onto a semantic `<a href="...">`
    or `<button>` inside the card heading (using CSS stretched-link `::after` if
    full-card click area is desired) and remove the click handler from the outer
    container.
3.  **Positive TabIndex (`tabindex` > 0):** Using `tabindex="1"` or higher to
    force tab order instead of fixing the underlying DOM order.
4.  **Keyboard Traps:** Focus enters a non-modal widget and cannot exit via
    standard `Tab`, `Shift+Tab`, or `Escape` keys.
5.  **Pointer/Motion-Only Actions:** Functionality triggered exclusively by
    mouse hover (`onmouseenter`), double-click, or device shake/tilt without a
    keyboard-accessible control.
