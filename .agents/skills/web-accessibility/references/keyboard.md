---
title: Keyboard Navigation (GAR Web 1.2)
shortname: gar-web-keyboard
priority: MANDATORY_CRITICAL
---

# Keyboard Navigation: Logic & Constraints

All functionality MUST be operable via keyboard-only interface (No Mouse/Touch
dependency).

## 1. Interaction Rules (MANDATORY)

-   **Semantic Selection:** Use native interactive elements (`<button>`, `<a>`,
    `<input>`, `<select>`, `<textarea>`).
-   **Tab Order:** MUST match DOM order.
    -   **Prohibited:** Positive `tabindex` (>0).
    -   **Required:** Use `tabindex="0"` for custom components; `tabindex="-1"`
        to remove from tab order but keep programmatic focus.
-   **Focus Management:**
    -   **Modals:** Trap focus within the dialog. Return focus to the trigger
        element on close.
    -   **Esc Key:** MUST close modals, menus, and popovers.
    -   **Dynamic Content:** Do NOT move focus unexpectedly.

## 2. Interaction Patterns by Component

Component           | Key Requirement
:------------------ | :-----------------------------------------------------
**Buttons/Links**   | Activate on `Enter`. Buttons also activate on `Space`.
**Menu Triggers**   | `aria-haspopup="menu"`, `aria-expanded` on `<button>`.
**Menus/Lists**     | `Tab` enters the group; `Arrow Keys` navigate items.
**Disclosure/Tabs** | `Space/Enter` toggles; `Arrow Keys` switch tabs.
**Modals**          | `Esc` to exit; Focus wrap-around.

## 3. High-Priority Code Patterns

### Standard (The "Default Path")

```html
<button type="button" onclick="...">Submit</button>
<a href="/dest">Navigate</a>
```

### Menu & Popup Triggers

```html
<!-- GOOD: aria-haspopup and aria-expanded directly on <button> -->
<button type="button"
        aria-haspopup="menu"
        aria-expanded="false"
        aria-controls="options-menu">
  Options
</button>
```

#### The "Container Trap" Anti-Pattern (Composite Components)

Avoid applying menu trigger attributes (`aria-haspopup`, `aria-expanded`) to
composite container components (such as chips or card wrappers) that render an
outer `<span>` or `<div>` wrapping an inner `<button>`:

```html
<!-- BAD: Container receives popup attributes -->
<span class="chip-container" aria-haspopup="menu" aria-expanded="false">
  <button class="chip-action">Filter Options</button>
</span>
<!-- FAILS aria-allowed-attr: <span> disallows aria-haspopup/aria-expanded -->
<!-- FAILS nested-interactive if role="button" is added to outer <span> -->

<!-- GOOD: Use an outlined dropdown button styled to match appearance -->
<button class="dropdown-button-outlined"
        aria-haspopup="menu"
        aria-expanded="false">
  Filter Options
</button>
```

### Custom (Only if native is impossible)

```html
<div role="button" tabindex="0"
     onclick="act()"
     onkeydown="e => (e.key === 'Enter' || e.key === ' ') && act()">
  Custom Button
</div>
```

## 4. Blockers (Auto-Fail Criteria)

1.  **Non-interactive Tags:** `onclick` on `<div>`, `<span>`, `<li>`, or `<img>`
    without `role` and `tabindex`.
2.  **Hidden Focus:** `outline: none` without a high-contrast `:focus-visible`
    replacement.
3.  **Keyboard Traps:** Focus entering a widget but unable to exit via `Tab` or
    `Esc`.
4.  **Motion-Only:** Functionality triggered by "Shake" or "Tilt" without a
    keyboard alternative.
5.  **Disallowed ARIA on Containers (`aria-allowed-attr`):** Placing popup or
    state attributes (`aria-expanded`, `aria-haspopup`, `aria-controls`) on
    generic `<div>` or `<span>` containers instead of interactive `<button>`s.
