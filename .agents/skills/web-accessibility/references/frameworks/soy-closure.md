---
title: Closure Templates (Soy) & Closure UI Accessibility Guidance
shortname: gar-web-framework-soy-closure
priority: MANDATORY_CRITICAL
---

# Closure Templates (Soy) & Closure Library Rules

When fixing accessibility bugs in **Closure Templates (`.soy`)** or **Closure
Library / Guts** components, adhere strictly to Google3 template localization
and component layer boundaries.

## 1. Mandatory Localization in Soy Templates (`{msg}`)

-   Never hardcode raw English strings into `aria-label` or component parameters
    inside `.soy` files.
-   Wrap every accessible name string in a `{msg desc="..."}...{/msg}` block:

    ```soy
    {let $filterAriaLabel kind="text"}
      {msg desc="Accessible label for the network filter dropdown button."}
        Filter network items
      {/msg}
    {/let}
    <button aria-label="{$filterAriaLabel}">...</button>
    ```

## 2. Target Layer Discipline (Wrapper vs. Base Library)

-   **Modify Application Wrappers, Not Core Base Libraries**: When a bug occurs
    in a product component that wraps Closure UI (e.g.,
    `guts.components.ClosureDropdown` wrapping `goog.ui.Select`), modify the
    wrapper component or its opt-in configuration flags (such as
    `add_aria_pos_size = true`) rather than editing shared third-party/base
    Closure Library classes.
-   Calculate dynamic ARIA positional attributes (`aria-posinset`,
    `aria-setsize`) inside the wrapper's rendering loop where the filtered item
    count is known.
