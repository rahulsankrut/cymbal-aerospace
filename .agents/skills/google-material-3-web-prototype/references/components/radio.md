# Radio (`<md-gb-radio>`)

The `<md-gb-radio>` component provides a form radio button control for single selection within a group.

## Import

```javascript
import '@material/web/labs/gb/components/radio/md-gb-radio.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `checked` / `.checked` | `boolean` | `false` | Selected state of the radio button. |
| `defaultchecked` / `.defaultChecked` | `boolean` | `false` | Initial default checked state. |
| `name` / `.name` | `string` | `''` | Form control name. Radios sharing the same `name` form a mutually exclusive group. |
| `required` / `.required` | `boolean` | `false` | Marks the radio group as required. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when selection state changes. |
| `@input` | `Event` | Fired during user selection. |

## CSS Classes & Utility Styling

```javascript
import radioStylesheet from '@material/web/labs/gb/components/radio/radio.css' with {type: 'css'};
```

* `.radio`: Root radio control element class.

## Usage Examples

### Radio Group

```html
<div class="flex flex-col gap-s100" role="radiogroup" aria-label="Model Selection">
  <label class="flex items-center gap-s100 typescale-body-md">
    <md-gb-radio name="ai-model" value="flash" checked></md-gb-radio>
    Gemini 1.5 Flash (Fast response)
  </label>

  <label class="flex items-center gap-s100 typescale-body-md">
    <md-gb-radio name="ai-model" value="pro"></md-gb-radio>
    Gemini 1.5 Pro (High reasoning)
  </label>

  <label class="flex items-center gap-s100 typescale-body-md opacity-50">
    <md-gb-radio name="ai-model" value="ultra" disabled></md-gb-radio>
    Gemini Ultra (Unavailable)
  </label>
</div>
```
