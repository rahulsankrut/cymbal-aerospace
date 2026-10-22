---
title: Forms, Inputs & Errors (GAR 1.7, 1.13, 3.4, 3.8)
shortname: gar-web-forms
priority: HIGH
---

# Forms: Input Efficiency & Error Recovery

Ensure forms are easy to complete and errors are easy to fix.

## 1. Input Efficiency (MANDATORY)

-   **Autofill:** Use standard `autocomplete` attributes for common fields
    (name, email, address).
-   **Efficient Entry:** Don't ask for the same info twice in one session.
    Provide a "Same as shipping" checkbox or similar reuse mechanism.
-   **Labels:** Every input MUST have a programmatically associated `<label>`.

## 2. Instructions & Errors

-   **Format Hints:** Provide format instructions (e.g., "MM/DD/YYYY") in the
    label or `aria-describedby`.
-   **Text-Based Errors:** Errors MUST be shown in text and explain how to fix
    the issue.
-   **No Sensory dependency:** Don't say "Fields in red are required." Say
    "Required fields are marked with an asterisk (*)."

## 3. Security (reCAPTCHA)

-   **Invisible First:** Use reCAPTCHA v3 (Enterprise) to avoid user challenges.
-   **Fallbacks:** If challenges are used, provide multi-sensory alternatives
    (audio + visual).

## 4. Implementation Patterns

### Accessible Form Field

```html
<label for="expiry">Expiry Date (MM/YY)</label>
<input id="expiry" name="expiry" autocomplete="cc-exp" aria-describedby="exp-hint">
<div id="exp-hint">Enter the 2-digit month and year.</div>
```

### Error Alert

```html
<div role="alert" class="error-msg">
  <strong>Error:</strong> Please enter a valid email address.
</div>
```

## 5. Blockers (Auto-Fail)

1.  **Unlabeled Inputs:** Using only a `placeholder` as a label.
2.  **Silent Errors:** Form submission fails but no error message is announced
    or displayed.
3.  **Retyping Data:** Forcing a user to re-enter their billing address when
    they already gave a shipping address.
