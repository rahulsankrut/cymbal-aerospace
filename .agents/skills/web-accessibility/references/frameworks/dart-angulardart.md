---
title: AngularDart & ACX Accessibility Guidance
shortname: gar-web-framework-angulardart
priority: MANDATORY_CRITICAL
---

# AngularDart & ACX Framework Rules

Follow these type-safety, localization, and lifecycle rules when fixing or
authoring accessibility in **AngularDart (`.dart`, `.acx.html`)** and **ACX**
components.

## 1. Target File Extensions & Scope

-   Applies to `.acx.html` (and AngularDart `.html`) templates and `.dart`
    component classes using `angular` / `angular_components` (ACX).

## 2. Attribute Binding & Localization (`i18n`)

-   **Mandatory `Intl.message` Backing Getter:** Never hardcode English strings
    directly into `aria-label` or `[ariaLabel]` in `.acx.html` templates. Always
    define a public getter in the `.dart` backing class using `Intl.message`:

```dart
String get learnMoreAriaLabel => Intl.message(
      'Learn more about auto-apply recommendations',
      name: 'learnMoreAriaLabel',
      desc: 'Accessible label for the learn more link in the dialog.',
    );
```

-   **Template Binding Syntax:**
    -   On **ACX components** (`<material-button>`, `<material-input>`,
        `<help-learn-more-link>`, `<material-select>`), bind the Dart property
        via `[ariaLabel]="learnMoreAriaLabel"`.
    -   On **native HTML elements** (`<button>`, `<a>`, `<input>`), bind via
        `[attr.aria-label]="learnMoreAriaLabel"`.

## 3. Component Library Gotchas & Container Traps

-   **ACX Composite Component Inputs (`<material-chip>`, `<material-select>`):**
    -   Placing raw `aria-label`, `aria-haspopup`, or `aria-expanded` on an ACX
        composite host element attaches the attribute to the outer
        non-interactive wrapper tag (`<material-chip>` / `<div>`), triggering
        `aria-allowed-attr` violations or leaving the inner `<button>`
        unlabeled.
    -   Delegate to the component's dedicated inner-button input property (such
        as `[buttonAriaLabel]="..."` on `<material-chip>`) or use an ACX
        `<dropdown-button>` for popup triggers.

```html
<!-- GOOD: Delegates accessible name to the inner interactive button of <material-chip> -->
<material-chip [buttonAriaLabel]="filterChipAriaLabel">
  {{chipText}}
</material-chip>

<!-- BAD (Container Trap): Raw aria-label or aria-haspopup on the outer ACX host element -->
<material-chip aria-haspopup="menu" aria-expanded="false">
  {{chipText}}
</material-chip>
```

-   **Table Selection Headers (`empty-table-header`):**
    -   Never leave a leading row-selection `<th>` empty (`<th></th>`) or add
        only `[attr.aria-label]` to an empty `<th></th>` tag (which still fails
        ATF's `empty-table-header` check). Place discernible text (such as a
        visually-hidden `<span>{{selectColumnHeaderLabel}}</span>` or visible
        header text backed by `Intl.message`) or a labeled "Select all"
        `<material-checkbox [ariaLabel]="selectAllLabel">` inside the `<th>`.

## 4. Focus & Async Lifecycle Management

-   **`@ViewChild` Strict Type Safety:**
    -   Native HTML elements (`<button>`, `<div>`, `<input>`) do **not**
        implement ACX's `Focusable` interface. Typing a native DOM element
        reference as `Focusable?` causes a compile or runtime `TypeError`; type
        it as `HtmlElement?` or `ButtonElement?` (`import 'dart:html';`).
    -   When querying a custom ACX component (e.g., `<callout #callout>`) to
        focus its underlying DOM node, specify `read: HtmlElement`:

```dart
@ViewChild('callout', read: HtmlElement)
HtmlElement? calloutElement;
```

-   **Asynchronous Focus Scheduling & Imports:**
    -   When restoring focus after a slidealog/modal closes or an async state
        change updates `*ngIf`, schedule `.focus()` via
        `NgZone.runAfterChangesObserved(() { ... })`,
        `DomService.scheduleWrite(() { ... })`, or `Timer.run(() { ... })`.
    -   Whenever using `Timer.run()` or `Future.microtask()`, verify that
        `import 'dart:async';` is present at the top of the `.dart` file.
-   **Minimal Diff Discipline:** Only modify the specific element and
    interaction reported in the bug. Never remove `*ngIf` directives or add
    unrequested focus handlers to surrounding form fields.
