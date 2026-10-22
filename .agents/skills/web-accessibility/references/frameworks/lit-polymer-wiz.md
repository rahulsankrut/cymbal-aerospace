---
title: Lit, Polymer & Wiz Accessibility Guidance
shortname: gar-web-framework-lit-polymer-wiz
priority: MANDATORY_CRITICAL
---

# Lit, Polymer & Wiz Framework Rules

Follow these Shadow DOM, decorative icon, view-transition, and announcer rules
when resolving accessibility issues in **Lit**, **Polymer**, or **Wiz (`.ts`,
`.js`)** applications.

## 1. Target File Extensions & Scope

-   Applies to Lit (`LitElement`, `html` tagged templates), Polymer, and Wiz
    controllers/views (`.ts`, `.js`).

## 2. Attribute Binding & Localization (`i18n`)

-   **Lit Template Bindings (`gar-web-accessibility-labels`,
    `gar-web-clear-purpose`):**
    -   Bind ARIA attributes on standard or custom elements in Lit templates and
        connect space-constrained `"Learn more"` links to card headings via
        `aria-describedby`:

```typescript
html`
  <div class="card">
    <h3 id="feature-${item.id}">${item.title}</h3>
    <p>${item.summary}</p>
    <a href="${item.url}" aria-describedby="feature-${item.id}">${this.learnMoreText}</a>
  </div>
`;
```

-   **Localization:** Ensure all user-facing accessible labels come from
    `goog.getMsg(...)` or the component's localized message catalog rather than
    untranslated string literals.

## 3. Component Library Gotchas & Container Traps

-   **Decorative Inner SVGs vs. Interactive Host Buttons:**
    -   When an icon button (`<sized-icon-button>`, `<mwc-icon-button>`, or
        custom Lit button) wraps an inner `<svg>` or icon element, **never**
        place `aria-label` on the inner `<svg>`.
    -   Mark the inner `<svg>` with `aria-hidden="true"` and set the accessible
        name (`aria-label` or `label` property) on the interactive parent button
        or host component:

```typescript
// GOOD: Parent interactive button holds aria-label; inner <svg> is hidden from AT
html`
  <sized-icon-button aria-label=${this.closeButtonLabel} @click=${this.onClose}>
    <svg aria-hidden="true" viewBox="0 0 24 24">...</svg>
  </sized-icon-button>
`;
```

-   **Clickable Cards with Secondary Actions (`nested-interactive`):**
    -   When an outer card `<div role="button" tabindex="0" @click=${...}>`
        wraps inner action buttons or links, **never** fix `nested-interactive`
        by merely removing `role="button"` and `tabindex="0"` while leaving
        `@click` on the non-interactive outer `<div>`.
    -   Remove `@click`, `role="button"`, and `tabindex="0"` from the outer card
        `<div>` and place the primary card navigation/action on a semantic `<a
        href=${this.detailsUrl}>` (or `<button>`) inside the card heading
        (`<h3><a href=${this.detailsUrl}>${this.title}</a></h3>`), using a CSS
        stretched-link (`::after`) if full-card click area is desired.

## 4. Focus & Async Lifecycle Management

-   **Wiz View Transitions & Render Lifecycle Focus:**
    -   When transitioning between views in Wiz controllers (e.g., from a report
        list view to a report detail view), remove `tabindex="0"` from
        non-interactive containers and programmatically focus the new view's
        heading (`tabindex="-1"`) inside the Wiz post-render lifecycle hook
        after the DOM transition completes.
    -   Always verify that any DOM element reference or helper variable called
        inside lifecycle methods is defined in scope to avoid introducing a
        runtime `ReferenceError`.
-   **Centralized Closing-Animation Cleanup & Controller `.focus()` APIs:**
    -   When a dropdown, panel, or overlay plays a closing animation, restore
        focus inside the **shared animation-cleanup method** (e.g.,
        `cleanupCloseLensAnimation()`) so focus is restored across all dismissal
        paths (collapse button, `Escape`, outside click) rather than only inside
        a single button click handler.
    -   When restoring focus to an encapsulated child or sibling controller,
        call its public Controller `.focus()` API (e.g.,
        `this.lensThumbnailController.focus()`) instead of querying internal DOM
        nodes directly.
-   **Background Dialog Focus Stealing & Avoiding Private Polymer Internals:**
    -   When a background-mounted Polymer/Lit dialog steals focus on initial
        page load, fix the spurious close/autofocus event race condition **at
        the dialog source** (e.g., only emit close/restore-focus events when the
        dialog transitions from an open state) rather than adding defensive
        guards in downstream victim components (such as page search inputs).
    -   Rely exclusively on standard DOM and public component APIs; **never**
        access private Polymer framework properties such as `polymerController`.
-   **Deferred Live Announcements on Android TalkBack (`Timer.callOnce`):**
    -   When firing `AriaAnnouncer` updates alongside a button click, focus
        shift, or layout transition in Wiz/Closure, Android TalkBack may swallow
        synchronous announcements. Defer the announcement by ~500ms using
        `Timer.callOnce` (instead of raw `setTimeout`, which violates
        `gts-no-timers`):

```typescript
import {Timer} from 'google3/third_party/javascript/closure/timer/timer';

Timer.callOnce(() => {
  this.announcer.say(statusMessage, 'assertive');
}, 500);
```
