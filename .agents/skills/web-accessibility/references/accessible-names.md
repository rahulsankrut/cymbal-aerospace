---
title: Accessible Names, Text Alternatives & Clear Purpose (gar-web-accessibility-labels, gar-web-text-alternatives, gar-web-clear-purpose)
shortname: gar-web-accessibility-labels
priority: MANDATORY_CRITICAL
---

# Names: Labels, Text Alternatives & Clear Purpose

Every interactive component and non-decorative visual element must expose a
programmatic name, role, state, and clear purpose that stays consistent with the
visual interface. This file consolidates three GAR 2027 criteria:
[Accessibility Labels & Relationships](http://go/gar-web-accessibility-labels),
[Text Alternatives](http://go/gar-web-text-alternatives), and
[Clear Purpose](http://go/gar-web-clear-purpose).

> **Framework Note:** For Angular (`i18n-aria-label`, `<mat-label>` redundancy
> removal), AngularDart (`Intl.message`, `[buttonAriaLabel]`), Soy (`{msg}`), or
> Lit/Wiz custom components, load the matching file in `references/frameworks/`
> first.

## 1. GAR Checkpoints & Core Rules

-   **Accessibility Labels & Relationships (`gar-web-accessibility-labels`):**
    -   **Label Provided:** Every interactive control (`<button>`, `<a>`,
        `<input>`, `<select>`, custom widget) must have a programmatic
        accessible name.
    -   **Label Matches Visible Text (WCAG 2.5.3 Label-in-Name):** When a
        control displays visible text, its accessible name must contain (and
        ideally start with) that exact visible text so speech-input and sighted
        screen-reader users do not experience a mismatch.
    -   **Relationships Communicated:** Associate visible labels and hints
        programmatically using `<label for="ID">`, `aria-labelledby`, or
        `aria-describedby`.
    -   **No Redundant Labels (Double Announcements):** When a visible
        `<label>`, `<mat-label>`, or inner text node already names the control,
        do not add a duplicate `aria-label`.
-   **Text Alternatives (`gar-web-text-alternatives`):**
    -   **Informative Images:** Every non-decorative `<img>`, `<svg>`, or
        `<canvas>` must provide an alternative (`alt="..."` or `role="img"
        aria-label="..."`) that describes user intent or data rather than pixel
        appearance (`alt="Close"` instead of `alt="X icon"`).
    -   **Decorative Images & Accompanying Icons:** Decorative images must use
        `alt=""`. Inline `<svg>` or font icons placed alongside visible button
        or link text must declare `aria-hidden="true"`.
-   **Clear Purpose (`gar-web-clear-purpose` / `google-link-purpose`):**
    -   **Meaningful Link & Control Text:** Link and button labels must clearly
        identify their destination or action using concise, action-oriented
        language.
    -   **Consistent Terminology:** Controls that perform the exact same action
        across a view or flow must use the same label (e.g., do not mix
        `"Delete"` and `"Erase"`, or `"Contact us"` and `"Get in touch"`).
    -   **No Role Repetition:** Never include the component role (`"button"`,
        `"link"`, `"icon"`) inside `aria-label`, `alt`, or link text, as screen
        readers announce the role automatically.

## 2. Decision Matrix

### Component Naming & Icon Methods (`gar-web-accessibility-labels`, `gar-web-text-alternatives`)

Component / Scenario                     | Required Pattern                                                                            | Rationale
:--------------------------------------- | :------------------------------------------------------------------------------------------ | :--------
**Button or Link with Visible Text**     | `<button type="button">Save Changes</button>`                                               | Native text node provides both visual and programmatic name.
**Icon Accompanying Visible Text**       | `<button type="button"><svg aria-hidden="true">...</svg>Help</button>`                      | Hides decorative icon from AT so only the visible text is announced.
**Standalone Icon-Only Button**          | `<button type="button" aria-label="Close modal"><svg aria-hidden="true">...</svg></button>` | Explicit `aria-label` on `<button>` names the action while hiding the raw `<svg>`.
**Form Input with Visible Label**        | `<label for="email">Email</label><input id="email" type="email">`                           | Explicit `for`/`id` binding links label and expands click target.
**Visually Obvious Input (e.g. Search)** | `<input type="search" aria-label="Search site content">`                                    | Provides programmatic name when a visible `<label>` is omitted by design.
**Informative vs. Decorative `<img>`**   | `<img src="chart.png" alt="Q3 revenue up 15%">` vs. `<img src="divider.png" alt="">`        | Conveys essential data or suppresses decorative noise.

### Link Purpose Preference Hierarchy (`gar-web-clear-purpose` / `google-link-purpose`)

When authoring links or fixing vague/stop-word link violations, apply this
ranked hierarchy in order:

Rank                     | Approach                                   | Pattern                                                                                                                 | When to Use & Why
:----------------------- | :----------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- | :----------------
**Rank 1 (Ideal)**       | **Descriptive Visible Link Text**          | `<a href="/docs/watch">Learn more about watch connectivity</a>`                                                         | **Default whenever layout space permits** (including cards, tables, and repeating template links like `"Billing review link 2"`). Benefits sighted, low-vision, voice-control, and screen-reader users alike.
**Rank 2 (Good Enough)** | **Connect Context via `aria-describedby`** | `<h3 id="watch-hdr">Smartwatch Connectivity</h3> ... <a href="/docs/watch" aria-describedby="watch-hdr">Learn more</a>` | **Use when visual layout space is strictly constrained** (narrow cells, compact cards, or standalone links inside modals with clear headers). Screen readers announce visible text first, then context—satisfying `google-link-purpose` (`b/275069974`) without a WCAG 2.5.3 Label-in-Name mismatch or new translation strings.
**Rank 3 (Not Ideal)**   | **Combine via `aria-labelledby`**          | `<a id="lnk" href="/docs/watch" aria-labelledby="lnk desc">Learn more</a>`                                              | Use only when a concatenated accessible name from multiple DOM IDs is strictly required.
**Rank 4 (Last Resort)** | **Overwrite with `aria-label`**            | `<a href="/docs/watch" aria-label="Learn more about watch connectivity">Learn more</a>`                                 | **Avoid unless no context element exists in the DOM.** Overwriting visible text creates a Label-in-Name mismatch for voice-input and sighted screen-reader users.

## 3. Implementation Patterns

### Icon-Only vs. Text-Plus-Icon Buttons

```html
<!-- GOOD: Standalone icon-only button has aria-label on <button> and aria-hidden="true" on <svg> -->
<button type="button" aria-label="Close modal">
  <svg aria-hidden="true" viewBox="0 0 24 24">...</svg>
</button>

<!-- GOOD: Icon accompanying visible text has aria-hidden="true" and NO redundant aria-label on <button> -->
<button type="button" class="btn-help" onclick="openModal()" aria-haspopup="dialog">
  <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">...</svg>
  Help &amp; Concepts
</button>

<!-- BAD: Unlabeled icon button, or aria-label placed on inner <svg> instead of <button> -->
<button type="button">
  <svg aria-label="Close">...</svg>
</button>
```

### Clear Link Purpose (Rank 1 Visible Text vs. Rank 2 `aria-describedby`)

```html
<!-- GOOD (Rank 1 - Ideal): Specific visible destination text -->
<a href="/docs/watch">Learn more about watch connectivity</a>

<!-- GOOD (Rank 1 - Dynamic/Repeating Links): Short topic prefix instead of bare "link 2" -->
<a href="/topics/billing/1">Billing review</a>
(<a href="/topics/billing/2">Billing review link 2</a>)

<!-- GOOD (Rank 2 - Space-Constrained Layout): Preserves concise visual text and links to context via aria-describedby -->
<div class="card">
  <h3 id="feature-watch">Smartwatch Connectivity</h3>
  <p>All plans include connectivity to select smartwatches.</p>
  <a href="/docs/watch" aria-describedby="feature-watch">Learn more</a>
</div>

<!-- BAD: Generic stop-word link with no distinguishing text or programmatic context -->
<a href="/docs/watch">Learn more</a>
```

## 4. Blockers (Auto-Fail)

1.  **Empty Interactive Controls (`button-name`, `link-name`):** `<button>` or
    `<a>` containing only an `<svg>` or icon font without `aria-label` or
    `aria-labelledby` on the interactive host element.
2.  **Missing or Generic Image Alt (`image-alt`, `image-redundant-alt`):**
    `<img>` missing `alt`, using filenames (`alt="logo.png"`), or repeating role
    words (`alt="Search icon"`, `aria-label="Submit button"`).
3.  **Stop-Word / Ambiguous Links (`google-link-purpose`,
    `identical-links-same-purpose`):** Links whose accessible name and context
    consist only of generic filler/stop words (`"here"`, `"click here"`, `"read
    more"`, `"learn more"`, `"see details"`, `"link"`, `"link 2"`, `"more
    details"`) or multiple links with identical text pointing to different
    destinations.
4.  **Label-in-Name Mismatch (`label-content-name-mismatch`):** Overwriting
    visible button or link text with an `aria-label` that does not contain the
    visible text string.
5.  **Broken ID References:** `<label for="...">`, `aria-labelledby`, or
    `aria-describedby` pointing to a non-existent or duplicate DOM `id`.
