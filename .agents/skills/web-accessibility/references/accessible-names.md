---
title: Accessible Names & Labels (GAR Web 1.1)
shortname: gar-web-accessible-names
priority: MANDATORY_CRITICAL
---

# Names: Labelling & Text Alternatives

Every interactive element and non-text content MUST have a programmatic name.

## 1. Labelling Rules (MANDATORY)

-   **Visible Text Match:** If a button has text, its `aria-label` MUST include
    that text.
-   **Form Labels:** Every `<input>` MUST have a `<label for="ID">`.
-   **Icon Buttons:** MUST have an `aria-label` or `aria-labelledby`.
-   **Alt Text:** Every `<img>` MUST have an `alt` attribute.
    -   Use `alt=""` for decorative images.
    -   Describe the *intent*, not the pixels (e.g., `alt="Close"` not `alt="X
        icon"`).

## 2. Naming Methods

| Method              | When to Use                                           |
| :------------------ | :---------------------------------------------------- |
| **Native Text**     | `<button>Submit</button>` (Best Path).                |
| **Label Element**   | `<label for="email">Email</label><input id="email">`. |
| **aria-label**      | For icon-only buttons or when visible text is         |
:                     : insufficient.                                         :
| **aria-labelledby** | To link a component to an existing heading or text    |
:                     : block.                                                :

## 3. High-Priority Code Patterns

### Correct Icon-Only Button

```html
<button type="button" aria-label="Close modal">
  <svg aria-hidden="true">...</svg>
</button>
```

### Decorative Icon Accompanying Visible Text (`aria-hidden="true"`)

When an inline `<svg>`, Material icon, or glyph accompanies visible text inside
a `<button>` or `<a>`, the icon is decorative and MUST declare
`aria-hidden="true"` so screen readers do not announce unlabelled SVG paths or
duplicate icon names alongside the visible label:

```html
<button type="button" class="btn-help" onclick="openModal()" aria-haspopup="dialog">
  <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">...</svg>
  Help &amp; Concepts
</button>
```

### Descriptive Search

```html
<input type="text" aria-label="Search site content">
```

## 4. Link Purpose & Stop Words (`google-link-purpose`)

Automated accessibility checkers (Fixie/Gimli) enforce the `google-link-purpose`
check (WCAG 2.4.4 & 2.4.9). Links must have text that clearly describes their
purpose without relying solely on ambiguous context.

### The Stop Words Problem

Link text that consists only of generic filler/stop words fails automated
checks. Common failing patterns include:

-   "here", "click here", "read more", "learn more", "link", "link 2", "more
    details".

### Hierarchy of Approaches (Ranked by Best Practice)

1.  **Rank 1: Ideal — Descriptive Visible Link Text**

    -   Whenever layout space permits (including free-flowing text in templates,
        email schedules, event descriptions, and cards), write specific, concise
        visual link text.
    -   For repeating or dynamic links, compose short, crisp visible
        descriptions (e.g., `"Billing review link 2"`) rather than generic
        placeholders (`"here"`, `"link 2"`).
    -   Sighted, low-vision, and screen reader users all benefit from clear
        destinations without Label-in-Name (WCAG 2.5.3) disconnects.

    ```html
    <!-- Static link: clear destination visible to all users -->
    <a href="/docs/watch">Learn more about watch connectivity</a>

    <!-- Dynamic/repeating links: short topic prefix instead of bare "link 2" -->
    <a href="/topics/billing/1">Billing review</a>
    (<a href="/topics/billing/2">Billing review link 2</a>)
    ```

2.  **Rank 2: Good Enough — Connect to Context via `aria-describedby`**

    -   When visual layout space is strictly constrained (e.g., narrow table
        cells, tight badge counters, or compact cards where extra text cannot
        fit), keep the concise visual text (e.g., `"Learn more"` or `"link 2"`)
        and connect the link to the nearby heading, topic, or descriptive text
        using `aria-describedby`.
    -   **Why this is preferred over `aria-label`:** Screen readers announce the
        visible link text first, then announce the description. This avoids the
        **Label-in-Name (WCAG 2.5.3)** disconnect where voice-control or sighted
        screen reader users see one word but hear something completely
        different.
    -   Per `b/275069974`, `google-link-purpose` officially recognizes
        `aria-describedby` as satisfying the check.

    ```html
    <!-- Preserves concise layout while providing programmatic context -->
    <div class="card">
      <h3 id="feature-watch">Smartwatch Connectivity</h3>
      <p>All plans include connectivity to select smartwatches.</p>
      <a href="/docs/watch" aria-describedby="feature-watch">Learn more</a>
    </div>
    ```

3.  **Rank 3: Not Ideal — Connect Link and Context with `aria-labelledby`**

    -   References both the link itself and the context element:

    ```html
    <span id="watch-desc">Connectivity to select smartwatches.</span>
    <a id="watch-link"
       href="/docs/watch"
       aria-labelledby="watch-link watch-desc">
      Learn more
    </a>
    ```

4.  **Rank 4: Not Ideal — Overwrite the Link Name using `aria-label`**

    -   Silences the checker, but completely replaces the accessible name. This
        creates a confusing mismatch for speech-input users (who speak what they
        see) and sighted screen reader users.
    -   Avoid unless no other option exists.

    ```html
    <!-- NOT IDEAL: Overwrites visible text completely -->
    <a href="/docs/watch"
       aria-label="Learn more about watch connectivity">
      Learn more
    </a>
    ```

## 5. Blockers (Auto-Fail)

1.  **Empty Buttons:** `<button><svg>...</svg></button>` with no text or label.
2.  **Generic Alt:** `alt="image"`, `alt="icon"`, or using filenames like
    `alt="logo.png"`.
3.  **Broken Labels:** Label `for` attribute that doesn't match an input `id`.
4.  **Stop-Word Links (`google-link-purpose`):** Standalone or repeated links
    reading only generic filler words (`"Learn more"`, `"Click here"`, `"here"`,
    `"link 2"`) with no programmatic context (`aria-describedby`) or
    distinguishing visible text.
