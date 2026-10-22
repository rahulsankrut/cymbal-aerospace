---
title: Lit, Polymer & Wiz Accessibility Guidance
shortname: gar-web-framework-lit-polymer-wiz
priority: MANDATORY_CRITICAL
---

# Lit, Polymer & Wiz Framework Rules

When resolving accessibility defects in **Lit**, **Polymer**, or **Wiz**
applications, follow these framework-specific rules for Shadow DOM, decorative
icons, and view transitions.

## 1. Decorative Icons vs. Interactive Parent Containers (Lit / Web Components)

-   **Do Not Label Decorative Inner SVGs**: When an icon button (e.g.,
    `<sized-icon-button>`, `<mwc-icon-button>`, or custom Lit button) contains
    an inner `<svg>` or icon element, do NOT place `aria-label` on the inner
    `<svg>`.
-   **Correct Pattern**:
    1.  Mark the decorative inner icon with `aria-hidden="true"`.
    2.  Set the accessible name (`aria-label` or `label` property) on the
        interactive **parent button or custom host element**.

## 2. Wiz View Transitions & Focus Management

-   **View Transition Focus**: When transitioning between views in Wiz
    controllers (e.g. from a list view to an item detail view), remove
    `tabindex="0"` from non-interactive containers and programmatically focus
    the new view's heading (`tabindex="-1"`) inside the Wiz render lifecycle
    hook after the DOM transition completes.
-   **Strict Variable Scope Verification**: Always verify that any DOM element
    reference or helper variable called inside lifecycle methods is defined in
    scope to avoid introducing a runtime `ReferenceError`.
