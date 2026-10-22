---
title: Dynamic Updates (GAR Web 2.7)
shortname: gar-web-updates
priority: HIGH
---

# Dynamic Updates: Live Regions

Communicate essential state changes without stealing focus.

## 1. Live Region Rules (MANDATORY)

-   **Don't Move Focus:** Updates should be announced, but focus should stay
    where the user is typing/interacting.
-   **Relevance:** Only announce "Essential" changes (Errors, Success messages,
    Status updates).
-   **Atomic Updates:** Use `aria-atomic="true"` to ensure the whole message is
    read when only part of it changes.

## 2. Notification Types

| Type               | ARIA Pattern            | Behavior                 |
| :----------------- | :---------------------- | :----------------------- |
| **Status/Info**    | `aria-live="polite"`    | Waits for silence before |
:                    :                         : speaking.                :
| **Critical/Error** | `role="alert"` or       | Interrupts immediately.  |
:                    : `aria-live="assertive"` :                          :
| **Progress**       | `role="status"`         | Periodic updates on      |
:                    :                         : background tasks.        :

## 3. Code Patterns

### Polite Status Update

```html
<div id="status" aria-live="polite" aria-atomic="true"></div>
<script>
  function notify(msg) { document.getElementById('status').textContent = msg; }
</script>
```

### Assertion (Errors)

```html
<div role="alert" aria-live="assertive">
  Connection lost. Please check your internet.
</div>
```

## 4. Blockers (Auto-Fail)

1.  **Silent Failures:** Form errors appearing visually but not announced to
    screen readers.
2.  **Chatter:** `aria-live` on a frequently updating element (e.g., a clock or
    stock ticker).

## 5. Known Workarounds (Android Talkback)

### Synchronous Updates Being Swallowed

When making dynamic ARIA updates (via `AriaAnnouncer` or direct DOM mutations),
Android Talkback may swallow or cancel the announcement if a concurrent button
click, focus change, or rapid layout shift occurs.

**Workaround:** Defer the announcement by ~500ms using a timer and use
`assertive` priority to guarantee the announcement isn't skipped. In the
Wiz/Search Next codebase, use `Timer.callOnce` instead of `setTimeout` to comply
with linters (`gts-no-timers`).

```typescript
import {Timer} from 'google3/third_party/javascript/closure/timer/timer';

// Defer the announcement by 500ms to prevent Android Talkback from skipping it
Timer.callOnce(() => {
  announcer.say('The state has updated.', 'assertive');
}, 500);
```
