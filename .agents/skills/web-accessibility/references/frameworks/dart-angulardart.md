---
title: AngularDart & ACX Accessibility Guidance
shortname: gar-web-framework-angulardart
priority: MANDATORY_CRITICAL
---

# AngularDart & ACX Framework Rules

When fixing accessibility bugs in **AngularDart (`.dart` / `.acx.html`)**
codebases, you MUST follow Google3 AngularDart type, internationalization, and
lifecycle rules. Do NOT apply generic HTML-only fixes.

## 1. Accessible Names & Localization (`Intl.message`)

-   **Mandatory Backing Property**: Never hardcode English strings directly into
    `aria-label` or `[ariaLabel]` in `.html` templates.
-   **Internationalization Rule**: Always define a localized getter in the Dart
    component class using `Intl.message`:

    ```dart
    String get learnMoreAriaLabel => Intl.message(
          'Learn more about auto-apply recommendations',
          name: 'learnMoreAriaLabel',
          desc: 'Accessible label for the learn more link in the dialog.',
        );
    ```
-   **Template Binding**: Bind the component property in the template using
    `[ariaLabel]="learnMoreAriaLabel"` (for ACX components) or
    `[attr.aria-label]="learnMoreAriaLabel"` (for native HTML elements).

## 2. Focus Management & Strict Type Rules

-   **`@ViewChild` Type Safety**:

    -   Native HTML elements (`<button>`, `<div>`, `<input>`) do **NOT**
        implement the ACX `Focusable` interface. Typing a native element
        reference as `Focusable?` will cause a runtime `TypeError` or compile
        error. Use `HtmlElement?` or `ButtonElement?`.
    -   When querying a custom ACX component (e.g. `<callout #callout>`) to
        focus its underlying DOM node, you MUST specify `read: HtmlElement`:

    ```dart
    @ViewChild('callout', read: HtmlElement)
    HtmlElement? calloutElement;
    ```
-   **Asynchronous Focus Timing**:

    -   When restoring focus after a dialog/slidealog closes or after an async
        state change, synchronous `.focus()` calls often fail because the DOM
        has not updated yet.
    -   Use `NgZone.runAfterChangesObserved(() { ... })`,
        `DomService.scheduleWrite(() { ... })`, or `Timer.run(() { ... })`.
    -   **Mandatory Import**: Whenever using `Timer.run()` or
        `Future.microtask()`, verify that `import 'dart:async';` is present at
        the top of the `.dart` file.

## 3. Scope & Minimal Diff Discipline

-   **No Unrequested Audits**: Only fix the specific element and interaction
    reported in the bug. Do NOT remove `*ngIf` directives or add focus handlers
    to unrelated form inputs in the same component.
