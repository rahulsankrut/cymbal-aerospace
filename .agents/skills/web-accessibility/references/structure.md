---
title: Structural Integrity, Navigation & Context Change (gar-web-headings, gar-web-page-title, gar-web-language-markup, gar-web-consistent-components, gar-web-consistent-help-order, gar-web-context-change, gar-web-accessible-navigation, gar-web-repeated-content)
shortname: gar-web-headings
priority: HIGH
---

# Structure: DOM Semantics, Landmarks & Predictability

The programmatic DOM structure must match the visual hierarchy, provide
navigable landmarks, and prevent unexpected context changes. This file covers
[Headings](http://go/gar-web-headings),
[Page Title](http://go/gar-web-page-title),
[Language Markup](http://go/gar-web-language-markup),
[Accessible Navigation](http://go/gar-web-accessible-navigation),
[Repeated Content](http://go/gar-web-repeated-content),
[Consistent Components](http://go/gar-web-consistent-components),
[Consistent Help Order](http://go/gar-web-consistent-help-order), and
[Context Change](http://go/gar-web-context-change).

> **Note:** For link and button naming clarity (`gar-web-clear-purpose` /
> `google-link-purpose`), see
> [Accessible Names & Clear Purpose](accessible-names.md).

## 1. GAR Checkpoints & Core Rules

-   **Headings & Page Titles (`gar-web-headings`, `gar-web-page-title`):**
    -   **Single `<h1>` & Logical Nesting:** Every page view must have a
        descriptive `<title>` and a logical heading hierarchy (`<h1>` followed
        by `<h2>`, `<h3>`) without skipping levels for visual styling.
-   **Data Tables & Column Headers (`empty-table-header`):**
    -   **Non-Empty `<th>` Content:** Every `<th>` (or `role="columnheader"` /
        `role="rowheader"`) must contain discernible text content or a labeled
        interactive child control (such as a visually-hidden `<span>Select
        row</span>` or a "Select all" checkbox inside `<th>`). Never leave a
        `<th>` tag empty (`<th></th>`) or put only an `aria-label` on an empty
        `<th aria-label="..."></th>` tag, as ATF's `empty-table-header` check
        requires inner text or a labeled child control inside the `<th>`.
-   **Language Markup (`gar-web-language-markup`):**
    -   **Document & Inline Language:** The root `<html>` element must declare a
        valid BCP-47 `lang` attribute (e.g., `<html lang="en">`), and passages
        in a different language must set `lang="..."` on their container so
        screen readers use the correct pronunciation rules.
-   **Landmarks & Bypassing Repeated Content (`gar-web-accessible-navigation`,
    `gar-web-repeated-content`):**
    -   **Semantic Regions:** Use `<header>`, `<nav>`, `<main>`, `<aside>`, and
        `<footer>` to define page regions. When multiple `<nav>` or `<section>`
        landmarks exist, give each a unique `aria-label` or `aria-labelledby`.
    -   **Skip Link:** Provide a keyboard-focusable "Skip to main content" link
        at the top of the page targeting `<main id="main-content">`.
-   **Consistency (`gar-web-consistent-components`,
    `gar-web-consistent-help-order`):**
    -   **Consistent Identification & Help Order:** Components with identical
        functionality and repeated help/support links ("Help", "Feedback") must
        maintain consistent labeling and relative DOM order across pages.
-   **Predictable Context Changes (`gar-web-context-change`):**
    -   **No Unannounced Auto-Navigation or Auto-Submit:** Moving focus to or
        changing the value of a form control (`<select>`, `<input
        type="radio">`, `<input type="checkbox">`) must not automatically reload
        the page, submit a form, or shift focus without an explicit submit
        button or prior warning.

## 2. Decision Matrix

Structural Need                  | Required Pattern                                                                                                                 | GAR 2027 Criterion
:------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :-----------------
**Document Identity & Language** | `<html lang="en">` + `<head><title>Page - App</title></head>`                                                                    | `gar-web-language-markup`, `gar-web-page-title`
**Bypass Repeated Header/Nav**   | `<a href="#main" class="skip-link">Skip to main content</a> ... <main id="main">`                                                | `gar-web-repeated-content`
**Multiple Navigation Regions**  | `<nav aria-label="Primary">` and `<nav aria-label="Breadcrumb">`                                                                 | `gar-web-accessible-navigation`
**Section Hierarchy**            | `<h1>Page Title</h1>` $\rightarrow$ `<h2>Section</h2>` $\rightarrow$ `<h3>Subsection</h3>`                                       | `gar-web-headings`
**Dropdown / Filter Selection**  | Pair `<select>` with an explicit `<button type="submit">Apply</button>` (or update results via live region without losing focus) | `gar-web-context-change`

## 3. Implementation Patterns

### Document Language, Title, Landmarks & Skip Link

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Billing Overview - Cloud Console</title>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <header>
    <nav aria-label="Primary">...</nav>
  </header>
  <main id="main-content" tabindex="-1">
    <h1>Billing Overview</h1>
    <section aria-labelledby="recent-heading">
      <h2 id="recent-heading">Recent Transactions</h2>
    </section>
  </main>
</body>
</html>
```

### Predictable Selection (No Unexpected Context Change)

```html
<!-- GOOD: Selecting an option does not unexpectedly navigate; user activates button -->
<label for="region-select">Data Region</label>
<select id="region-select" name="region">
  <option value="us">United States</option>
  <option value="eu">Europe</option>
</select>
<button type="button" onclick="applyRegion()">Switch Region</button>

<!-- BAD: Changing <select> immediately triggers full page navigation without warning -->
<select onchange="window.location.href = this.value">...</select>
```

## 4. Blockers (Auto-Fail)

1.  **Missing Document Language or Title (`html-has-lang`, `document-title`):**
    Omitting `<html lang="...">` or `<title>`.
2.  **Skipped or Visual-Only Headings (`heading-order`, `empty-heading`):**
    Jumping from `<h1>` directly to `<h4>` for font sizing, or rendering empty
    heading tags.
3.  **Unlabeled Duplicate Landmarks (`landmark-unique`):** Rendering multiple
    `<nav>`, `<aside>`, or `role="region"` containers without distinct
    `aria-label` or `aria-labelledby` names.
4.  **Unexpected Context Change on Input/Focus:** Auto-submitting a form or
    navigating to a new URL immediately on `onchange` or `onfocus` of a radio
    button, checkbox, or `<select>` without prior instructions.
