---
title: Flutter Web Accessibility Guidance
shortname: gar-web-framework-flutter
priority: MANDATORY_CRITICAL
---

# Flutter Web Accessibility & Focus Traversal Rules

Follow these semantics and traversal-policy rules when fixing or authoring
accessibility in **Flutter Web (`.dart`)** applications.

## 1. Target File Extensions & Scope

-   Applies to `.dart` files importing `package:flutter/material.dart`,
    `package:flutter/widgets.dart`, or `package:flutter/semantics.dart`.

## 2. Attribute Binding & Localization (`i18n`)

-   **Semantics Widget & Tooltip Properties:**
    -   Provide accessible names on icon controls using `IconButton(tooltip:
        ...)` or by wrapping custom interactive widgets in `Semantics(label:
        ..., button: true, child: ...)`.
    -   Localize all user-facing semantic labels using `Intl.message` or the
        application's generated `AppLocalizations` delegate.

## 3. Component Library Gotchas & Container Traps

-   **Merging vs. Excluding Decorative Semantics:**
    -   When a custom card or row combines a decorative icon with a text label,
        use `ExcludeSemantics` on decorative children or `MergeSemantics` on the
        interactive parent so screen readers do not announce separate, unlabeled
        child nodes.
    -   Avoid wrapping individual child widgets in redundant `Focus(...)`
        widgets or toggling `canRequestFocus` flags when a group traversal
        policy resolves the ordering issue.

## 4. Focus & Async Lifecycle Management

-   **Visual Reading Order (`ReadingOrderTraversalPolicy`):**
    -   `WidgetOrderTraversalPolicy()` traverses widgets in widget-tree
        insertion order, which frequently diverges from visual layout (e.g.,
        positioned action bars, rows, or responsive grids), causing VoiceOver
        and `Tab` focus to jump non-linearly.
    -   To align keyboard and screen-reader traversal with visual reading order,
        configure `FocusTraversalGroup` with `ReadingOrderTraversalPolicy()` and
        keep the diff minimal:

```dart
// GOOD: Uses ReadingOrderTraversalPolicy() so focus follows visual layout order
FocusTraversalGroup(
  policy: ReadingOrderTraversalPolicy(),
  child: CustomActionsBar(...),
)
```
