---
title: Flutter Accessibility Guidance (Reading Order & Traversal)
shortname: gar-web-framework-flutter
priority: MANDATORY_CRITICAL
---

# Flutter Accessibility & Focus Traversal Rules

When resolving accessibility focus or VoiceOver reading order issues in
**Flutter (`.dart`)** applications, use Flutter's built-in traversal policies
rather than manual focus nodes.

## 1. Visual Reading Order (`ReadingOrderTraversalPolicy`)

-   **Do Not Use `WidgetOrderTraversalPolicy` for Visual Layouts**:
    `WidgetOrderTraversalPolicy()` traverses widgets in the order they appear in
    the widget tree, which frequently diverges from visual layout (e.g. rows,
    columns, action bars).
-   **Use `ReadingOrderTraversalPolicy()`**: To fix non-linear VoiceOver or
    keyboard focus order, configure the `FocusTraversalGroup` with
    `ReadingOrderTraversalPolicy()`:

    ```dart
    FocusTraversalGroup(
    policy: ReadingOrderTraversalPolicy(),
    child: CustomActionsBar(...),
    )
    ```
-   **Avoid Extra Focus Wrappers**: Do NOT wrap individual child widgets in
    redundant `Focus(...)` widgets or toggle `canRequestFocus` flags when a
    traversal policy change resolves the issue. Keep the diff minimal.
