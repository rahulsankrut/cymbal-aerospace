---
title: Angular (TypeScript) & Angular Material Accessibility Guidance
shortname: gar-web-framework-angular-ts
priority: MANDATORY_CRITICAL
---

# Angular (TypeScript) & Angular Material Framework Rules

When fixing accessibility issues in **Angular (`.ts` / `.ng.html`)** and
**Angular Material** codebases, follow these framework-specific rules.

## 1. Preventing Redundant Accessible Names (Double Announcements)

-   **MatFormField & MatLabel Association**: When an input or `<mat-chip-grid>`
    is placed inside a `<mat-form-field>` that already contains a `<mat-label>`,
    Angular Material automatically links the `<mat-label>` as the accessible
    name.
-   **When to Remove `aria-label`**: If a bug reports that a screen reader
    announces the label twice (double announcement), **DELETE** the redundant
    explicit `aria-label` from the `<mat-chip-grid>` or `<input>`. Do NOT add
    `role="grid"` or keep redundant `aria-label` attributes when `<mat-label>`
    is already present.

## 2. Custom Component Input Bindings

-   Angular Material components wrap internal shadow/template DOM nodes. Setting
    a raw HTML `aria-label="..."` attribute on `<mat-select>` or custom
    components is often ignored by screen readers.
-   Always bind to the component's dedicated accessibility inputs:
    -   Use `[ariaLabel]="..."` or `[optionsAriaLabel]="..."` on `<mat-select>`
        / custom dropdowns.

## 3. Focus Restoration After Animations (Controllers & Lifecycle)

-   **Do Not Focus During Closing Animations**: Calling `element.focus()` inside
    a click handler (e.g. `collapseButtonClicked()`) while a dropdown, dialog,
    or panel is starting a CSS closing animation will fail or lose focus when
    the animation finishes.
-   **Use Animation Cleanup / Completion Callbacks**: Always place focus
    restoration inside the animation completion hook or controller cleanup
    method (e.g., `cleanupCloseLensAnimation()`, `afterClosed().subscribe(...)`)
    and expose the `focus()` method through the component's Controller API
    interface.
