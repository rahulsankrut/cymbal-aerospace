---
title: Structural Integrity & Semantics (GAR 1.6, 1.8, 1.11, 1.12, 1.20)
shortname: gar-web-structure
priority: HIGH
---

# Structure: DOM, Headings, & Semantics

The programmatic structure MUST match the visual intent and hierarchy of the
page.

## 1. Heading Hierarchy & Titles

-   **One H1:** Every page MUST have exactly one `<h1>`.
-   **No Skipping:** Levels must follow `h1 > h2 > h3`.
-   **Descriptive Purpose:** Link and button text MUST be clear without
    surrounding context (Avoid "Click here", "Read more").

## 2. Global Semantics

-   **Language:** The `<html>` element MUST have a `lang` attribute (e.g.,
    `<html lang="en">`).
-   **Consistent UI:** Components with the same functionality MUST be identified
    consistently across the site (e.g., don't use a "Search" icon on one page
    and a "Find" button on another).
-   **Landmarks:** Use `<header>`, `<nav>`, `<main>`, `<footer>` to define
    regions.
-   **Consistent Help:** If "Help" or "Contact Us" links appear on multiple
    pages, they MUST be in the same relative order (e.g., always last in the
    footer).

## 3. Predictability (Context Change)

-   **No Surprises:** Changing a setting (e.g., a dropdown select) MUST NOT
    unexpectedly submit a form or open a new window.
-   **Warning:** If a context change is unavoidable (e.g., a "Delete Account"
    button), warn the user *before* the action occurs.

## 4. Implementation Patterns

### Language & Title

```html
<!DOCTYPE html>
<html lang="en">
<head><title>Dashboard - My App</title></head>
...
```

### Descriptive Buttons

```html
<!-- GOOD -->
<a href="/settings">Edit Profile Settings</a>
<button type="submit">Save Changes</button>

<!-- BAD -->
<a href="/settings">Click here</a>
```

### Predictable Select

```javascript
// GOOD: User changes select, then clicks a button to navigate
<select id="lang">...</select>
<button onclick="changeLang()">Go</button>

// BAD: User changes select, page immediately reloads
<select onchange="window.location = this.value">...</select>
```

## 5. Blockers (Auto-Fail)

1.  **Missing Lang:** `<html lang="">` or missing attribute entirely.
2.  **Vague Links:** Multiple "Learn more" links that point to different
    destinations without distinguishing accessible names.
3.  **Semantic styling:** Using `<h3>` just to get small bold text in a place
    that isn't a heading.
4.  **Auto-Submit:** A form that submits as soon as a radio button is clicked
    (without warning).
5.  **Container vs Action Attribute Leaks:** In composite component libraries
    (e.g., chips, cards), applying interactive ARIA attributes (`aria-expanded`,
    `aria-haspopup`) to an outer container element (`<span>`, `<div>`) instead
    of delegating to the inner actionable control (`<button>`).
