---
title: Forms, Inputs, Instructions & Error Recovery (gar-web-autofill, gar-web-efficient-entry, gar-web-user-instructions, gar-web-recaptcha, gar-web-undo)
shortname: gar-web-user-instructions
priority: HIGH
---

# Forms: Input Efficiency, Instructions & Error Recovery

Forms must minimize redundant typing, communicate format requirements clearly,
provide programmatic error recovery, and allow users to review or undo critical
submissions. This file covers [Autofill](http://go/gar-web-autofill),
[Efficient Entry](http://go/gar-web-efficient-entry),
[User Instructions](http://go/gar-web-user-instructions),
[reCAPTCHA](http://go/gar-web-recaptcha), and [Undo](http://go/gar-web-undo).

## 1. GAR Checkpoints & Core Rules

-   **Autofill & Efficient Entry (`gar-web-autofill`,
    `gar-web-efficient-entry`):**
    -   **Standard Autocomplete Tokens:** Personal, contact, and payment fields
        must declare valid HTML `autocomplete` tokens (e.g., `name`, `email`,
        `street-address`, `postal-code`, `cc-exp`).
    -   **No Redundant Data Entry:** Never force users to re-type information
        already entered in the same session; auto-populate or provide a "Same as
        shipping address" checkbox.
-   **User Instructions & Error Recovery (`gar-web-user-instructions`):**
    -   **Persistent Labels & Format Hints:** Every `<input>`, `<select>`, and
        `<textarea>` must have a persistent visible `<label for="ID">` (never
        rely on `placeholder` alone). Link format instructions (e.g.,
        `"MM/DD/YYYY"`) via `aria-describedby`.
    -   **No Sensory-Only Instructions:** Never identify required or invalid
        fields by color, shape, or position alone (e.g., pair red borders with
        an asterisk `*` and explicit error text).
    -   **Programmatic Error Association:** Invalid fields must set
        `aria-invalid="true"`, reference specific text instructions via
        `aria-describedby`, and announce errors via `role="alert"` or moving
        focus to an error summary.
-   **Reversible Submissions & Security (`gar-web-undo`, `gar-web-recaptcha`):**
    -   **Undo / Confirmation:** Destructive, financial, or legal actions must
        provide an undo window, a confirmation step, or pre-submission review.
    -   **Accessible Verification:** Prefer invisible reCAPTCHA v3; if a
        challenge is shown, provide both visual and audio alternatives.

## 2. Decision Matrix

Form Requirement               | Required HTML / ARIA Pattern                                                                                                                             | GAR 2027 Criterion
:----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------
**Personal / Address Input**   | `<label for="zip">Postal Code</label><input id="zip" autocomplete="postal-code">`                                                                        | `gar-web-autofill`
**Input with Format Hint**     | `<input id="exp" aria-describedby="exp-hint"><div id="exp-hint">Format: MM/YY</div>`                                                                     | `gar-web-user-instructions`
**Field Validation Failure**   | `<input id="email" aria-invalid="true" aria-describedby="email-err"><div id="email-err" role="alert">Enter a valid email (e.g. name@example.com).</div>` | `gar-web-user-instructions`
**Repeated Session Data**      | `<input type="checkbox" id="same-addr"><label for="same-addr">Billing address same as shipping</label>`                                                  | `gar-web-efficient-entry`
**Destructive / Final Action** | Confirmation `<dialog>` or post-action toast with `<button type="button">Undo</button>`                                                                  | `gar-web-undo`

## 3. Implementation Patterns

### Accessible Form Field with Format Hint & Autocomplete

```html
<!-- GOOD: Persistent <label for>, autocomplete token, and linked format hint -->
<div class="form-group">
  <label for="expiry">Expiry Date (MM/YY) <span aria-hidden="true">*</span></label>
  <input id="expiry"
         name="expiry"
         type="text"
         required
         autocomplete="cc-exp"
         aria-describedby="exp-hint">
  <div id="exp-hint">Enter the 2-digit month and 2-digit year.</div>
</div>

<!-- BAD: Relying only on placeholder text with no <label> or autocomplete -->
<input type="text" placeholder="Expiry Date (MM/YY)">
```

### Accessible Validation & Error Recovery

```html
<!-- GOOD: aria-invalid="true" + aria-describedby linking to specific recovery text -->
<div class="form-group">
  <label for="user-email">Work Email</label>
  <input id="user-email"
         type="email"
         autocomplete="email"
         aria-invalid="true"
         aria-describedby="email-error">
  <div id="email-error" role="alert" class="error-msg">
    Error: Please include an '@' in the email address.
  </div>
</div>
```

## 4. Blockers (Auto-Fail)

1.  **Placeholder-Only Inputs (`label`):** Using `placeholder` without a
    persistent `<label for="...">` or programmatic label.
2.  **Color-Only Error / Required State:** Indicating invalid or required inputs
    solely by turning the border red without `aria-invalid="true"` and visible
    error text.
3.  **Silent or Generic Validation Failures:** Failing form submission without
    announcing the error or failing to explain how to fix the input.
4.  **Missing Autocomplete on Personal Fields (`autocomplete-valid`):** Omitting
    `autocomplete` attributes (or using invalid tokens) on standard user name,
    email, phone, address, or payment inputs.
5.  **Irreversible Destructive Action:** Executing permanent data deletion or
    financial transactions on a single click without confirmation or undo.
