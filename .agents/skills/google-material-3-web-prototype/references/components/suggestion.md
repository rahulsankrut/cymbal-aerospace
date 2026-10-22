# AI Suggestion Controls (`<md-gb-suggestion>`, `<md-gb-suggestion-group>`)

The `<md-gb-suggestion>` and `<md-gb-suggestion-group>` pair provides post-generation AI reply buttons, prompt completions, and responsive choice layouts for conversational AI interfaces.

> **CARVE-OUT RULE**: For conversational AI follow-up prompts and suggested replies, ALWAYS use `<md-gb-suggestion>` inside `<md-gb-suggestion-group>` instead of buttons or chips. This carve-out is limited strictly to AI follow-up suggestions.

## Import & Script Bundle Requirement

Google-internal components ship as a self-registering bundle rather than an importmap module. Load the bundle via a `<script src>` tag:

```html
<script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
```

To include icons inside suggestions, import `<md-gb-icon>`:

```html
<script type="module">
  import '@material/web/labs/gb/styles/icon/md-gb-icon.js';
</script>
```

---

## `<md-gb-suggestion>` API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `variant` / `.variant` | `'single' \| 'binary' \| 'multiple-choice'` | `'single'` | Visual layout form of the suggestion pill. |
| `density` / `.density` | `0 \| -1 \| -2 \| -3 \| -4` | `0` | Density scale adjusting height (-4px/step) and padding. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction and removes element from keyboard tab order. |
| `soft-disabled` / `.softDisabled` | `boolean` | `false` | Disables activation while keeping keyboard focusability with `aria-disabled="true"`. |
| `value` / `.value` | `string` | `''` | Value payload string associated with the suggestion choice. |
| `aria-label` / `.ariaLabel` | `string` | `''` | Accessible label delegated to inner button (required for ambiguous text like 'Yes'/'No'). |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Visible label text of the suggestion button. |
| `icon` | Slotted leading icon element (e.g. `<md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>`). |

---

## `<md-gb-suggestion-group>` API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `layout` / `.layout` | `'auto' \| 'row' \| 'stack'` | `'auto'` | Layout mode. `'auto'` chooses layout based on option count and inline width. `'row'` forces horizontal binary row; `'stack'` forces vertical column. |
| `density` / `.density` | `0 \| -1 \| -2 \| -3 \| -4` | `0` | Density scale propagated to child suggestions. |
| `heading-level` / `.headingLevel` | `number` | `2` | Heading level (1–6) applied to internal accessible heading wrapper. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `(default)` | Slotted 1–3 `<md-gb-suggestion>` elements. |
| `heading` | Accessible prompt/question heading element (e.g. `<span slot="heading">Question?</span>`). |

---

## Layout Behavior & Precedence Rules

When `layout="auto"` is set, `<md-gb-suggestion-group>` dynamically adapts layout based on option count and inline width:

| Option Count | Inline Width | Group Layout | Effective Child Variant |
| :--- | :--- | :--- | :--- |
| 1 | Any | Single (inline-end aligned) | `single` (pill) |
| 2 | Any | Row (50/50 binary) | `binary` |
| 3 | ≥ 600px | Row (equal-width 3-up) | `binary` |
| 3 | < 600px | Stack (full-width column) | `multiple-choice` |
| > 3 | Any | Stack (fallback) | `multiple-choice` |

---

## Usage Examples

### Single Follow-Up Suggestion

```html
<md-gb-suggestion-group>
  <span slot="heading">Would you like to draft a follow-up response?</span>
  <md-gb-suggestion>
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    Draft response
  </md-gb-suggestion>
</md-gb-suggestion-group>
```

### Binary Suggestion Row (50/50)

```html
<md-gb-suggestion-group>
  <span slot="heading">Apply suggested edits to document?</span>
  <md-gb-suggestion aria-label="Yes, apply changes">
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    Yes, apply
  </md-gb-suggestion>
  <md-gb-suggestion aria-label="No, discard changes">
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    No, discard
  </md-gb-suggestion>
</md-gb-suggestion-group>
```

### Adaptive Multiple Choice Group

```html
<md-gb-suggestion-group>
  <span slot="heading">Choose summary format</span>
  <md-gb-suggestion>
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    Bullet-point overview
  </md-gb-suggestion>
  <md-gb-suggestion>
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    Executive summary
  </md-gb-suggestion>
  <md-gb-suggestion>
    <md-gb-icon slot="icon">prompt_suggestion</md-gb-icon>
    Detailed breakdown
  </md-gb-suggestion>
</md-gb-suggestion-group>
```
