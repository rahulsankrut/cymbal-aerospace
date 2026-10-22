---
title: Angular (TypeScript) & Angular Material Accessibility Guidance
shortname: gar-web-framework-angular-ts
priority: MANDATORY_CRITICAL
---

# Angular (TypeScript) & Angular Material Framework Rules

Follow these rules when authoring or fixing accessibility in **Angular
(`.ng.html`, `.component.ts`)** and **Angular Material** components.

## 1. Target File Extensions & Scope

-   Applies to `.ng.html` templates and `.ts` Angular components/directives
    using `@angular/core`, `@angular/material`, or Google3 Angular wrappers.

## 2. Attribute Binding & Localization (`i18n`)

-   **Native HTML Elements vs. Angular Component Inputs:**
    -   On native HTML elements (`<button>`, `<a>`, `<input>`, `<div>`), bind
        dynamic ARIA attributes with the `attr.` prefix:
        `[attr.aria-label]="labelExpr"`, `[attr.aria-expanded]="isOpen"`,
        `[attr.aria-describedby]="descId"`.
    -   On Angular Material / custom components (`<mat-select>`,
        `<mat-checkbox>`, `<mat-radio-group>`), bind the component's dedicated
        `@Input()` property (`[ariaLabel]="labelExpr"`,
        `[optionsAriaLabel]="..."`) because raw host `aria-label` attributes are
        not forwarded into the inner interactive shadow/template node.
-   **Mandatory Template Localization (`i18n-aria-label`):**
    -   Whenever adding a static user-facing `aria-label="..."` or `title="..."`
        in an `.ng.html` template, **always pair it with `i18n-aria-label="..."`
        (or `i18n-title="..."`)** containing a translator description
        (`go/pan-i18n-angular#angular-templates`).
    -   When a visible localized element (`<span>`, `<label>`, `<h3>`) already
        exists in the template, prefer `aria-labelledby="<id>"` or
        `aria-describedby="<id>"` so the existing translated string is reused
        without introducing duplicate translation messages
        (`DuplicateUIStrings`).

```html
<!-- GOOD: Static aria-label paired with i18n-aria-label -->
<button mat-icon-button
        type="button"
        aria-label="Close settings dialog"
        i18n-aria-label="Accessible label for the button that closes the settings dialog.">
  <mat-icon aria-hidden="true">close</mat-icon>
</button>
```

## 3. Component Library Gotchas & Container Traps

-   **Preventing Redundant Accessible Names (`<mat-form-field>` &
    `<mat-label>`):**
    -   When an `<input>` or `<mat-chip-grid>` is placed inside a
        `<mat-form-field>` that already contains a `<mat-label>`, Angular
        Material automatically associates `<mat-label>` as the accessible name.
    -   If a bug reports that a screen reader announces the label twice (double
        announcement), **delete** the redundant explicit `aria-label` from the
        `<mat-chip-grid>` or `<input>`. Do not add `role="grid"` or keep
        duplicate `aria-label` attributes when `<mat-label>` is present.
-   **Dynamically Injected Decorative Icon `<span>` Wrappers in Directives:**
    -   When an Angular directive (e.g., `docLinkButton`) dynamically appends a
        `<span>` wrapping a decorative trailing icon (such as an `"open_in_new"`
        icon) inside a button or link whose accessible name already conveys that
        context, mark the injected `<span>` as decorative
        (`span.setAttribute('aria-hidden', 'true')` or give it `role="img"` only
        when `aria-label` is intentionally required on the `<span>`) rather than
        placing `aria-label` on a plain `<span>` with no role (which triggers
        `aria-prohibited-attr`). Keep the fix scoped strictly within the target
        directive without adding upstream `tagName` checks in shared directives.

```html
<!-- GOOD: <mat-label> provides the accessible name; redundant aria-label removed from <mat-chip-grid> -->
<mat-form-field>
  <mat-label i18n="Label for admin emails field">Enter admin emails</mat-label>
  <mat-chip-grid #chipGrid>
    <mat-chip-row *ngFor="let email of emails">{{email}}</mat-chip-row>
    <input [matChipInputFor]="chipGrid" />
  </mat-chip-grid>
</mat-form-field>
```

## 4. Focus & Async Lifecycle Management

-   **Do Not Focus Synchronously During Closing Animations:** Calling
    `element.focus()` inside a click handler (e.g., `collapseButtonClicked()`)
    while a dropdown, drawer, or dialog is starting a CSS closing animation
    causes focus to be lost when the animation finishes.
-   **Restore Focus in Animation / Dialog Completion Hooks:** Place focus
    restoration inside the animation completion callback or dialog `afterClosed`
    subscription (e.g., `cleanupCloseLensAnimation()`,
    `dialogRef.afterClosed().subscribe(() => triggerButton.focus())`) and expose
    `focus()` on the component's Controller API interface when encapsulated.
