---
title: Dynamic Updates & Screen Reader Announcements (gar-web-updates-with-screen-reader)
shortname: gar-web-updates-with-screen-reader
priority: HIGH
---

# Dynamic Updates: ARIA Live Regions & Announcements

Communicate asynchronous state changes, search/filter counts, Toast
notifications, and validation alerts to screen readers without unexpectedly
stealing keyboard focus
([go/gar-web-updates-with-screen-reader](http://go/gar-web-updates-with-screen-reader)).

## 1. GAR Checkpoints & Core Rules

-   **Updates With Screen Reader (`gar-web-updates-with-screen-reader`):**
    -   **Announce Without Moving Focus:** Asynchronous status changes (e.g.,
        `"3 results found"`, `"File uploaded"`, `"Draft saved"`) must be
        announced via an ARIA live region while keeping keyboard focus on the
        user's active control.
    -   **Pre-Mount Live Containers:** The live region element (`aria-live` or
        `role="status"` / `role="alert"`) must exist in the DOM **before** text
        is injected into it; dynamically inserting a new element together with
        its text often fails to trigger an announcement.
    -   **Polite vs. Assertive Priority:** Use `aria-live="polite"` (or
        `role="status"`) for routine updates and progress milestones, and
        reserve `role="alert"` (`aria-live="assertive"`) strictly for critical,
        time-sensitive errors.
    -   **Prevent Concurrent Focus/Click Swallowing (Android TalkBack):** On
        Android TalkBack, synchronous announcements fired on the exact same tick
        as a button click or layout shift can be swallowed; defer programmatic
        announcer calls by ~500ms when needed (see
        `references/frameworks/lit-polymer-wiz.md` for Closure/Wiz
        `Timer.callOnce`).

## 2. Decision Matrix

Update Scenario                               | Required ARIA Pattern                                                                                | Screen Reader Behavior
:-------------------------------------------- | :--------------------------------------------------------------------------------------------------- | :---------------------
**Search / Filter Results Count, Toast Info** | `<div role="status" aria-live="polite" aria-atomic="true">`                                          | Waits until current speech finishes, then announces full updated text.
**Critical Form / Network Error**             | `<div role="alert" aria-live="assertive">`                                                           | Interrupts current speech immediately to announce the error.
**Background Upload / Job Progress**          | `<div role="status" aria-live="polite">` *(throttled to key milestones, e.g., Start, 50%, Complete)* | Announces milestone updates without continuous per-percent chatter.

## 3. Implementation Patterns

### Polite Status & Milestone Updates (`aria-live="polite"`)

```html
<!-- GOOD: Live container is present in initial DOM; JS updates textContent at key milestones -->
<div id="upload-status" role="status" aria-live="polite" aria-atomic="true" class="sr-only"></div>

<script>
  function updateUploadStatus(message) {
    const statusEl = document.getElementById('upload-status');
    if (statusEl) statusEl.textContent = message;
  }
</script>
```

### Immediate Error Alert (`role="alert"`)

```html
<!-- GOOD: Assertive alert for critical failure -->
<div id="network-alert" role="alert" aria-live="assertive">
  Connection lost. Changes could not be saved.
</div>
```

## 4. Blockers (Auto-Fail)

1.  **Silent Visual Status Changes:** Updating filter results, saving state, or
    displaying visual toast/error banners without an `aria-live` region or
    programmatic announcer call.
2.  **Live Region Chatter:** Placing `aria-live` on rapidly mutating elements
    (countdown timers ticking every second, continuous byte-progress counters,
    or live stock tickers), which floods the screen reader queue.
3.  **Unrequested Focus Stealing on Status Updates:** Calling `.focus()` on a
    toast or status banner while the user is actively typing in an input field.
