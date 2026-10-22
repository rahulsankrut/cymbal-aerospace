# Radio (`<md-gb-radio>`)

The Radio component (`<md-gb-radio>`) allows users to select a single option from a set of mutually exclusive choices.

## Import

```javascript
import '@material/web/labs/gb/components/radio/md-gb-radio.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` / `.checked` | `boolean` | `false` | Whether the radio button is selected. |
| `defaultchecked` / `.defaultChecked` | `boolean` | `false` | Default checked state for form resets. |
| `name` / `.name` | `string` | `''` | Form control name. Radios sharing the same `name` form a mutually exclusive group. |
| `required` / `.required` | `boolean` | `false` | Marks the radio group as required for form submission. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when radio selection state changes. |
| `@input` | `Event` | Fired when radio selection state changes. |

### CSS Classes

```javascript
import radioStylesheet from '@material/web/labs/gb/components/radio/radio.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.radio` | Root | Component root class. |

## Usage Examples

### Radio Group Selection

```html
<div class="flex flex-col gap-3" role="radiogroup" aria-label="Execution mode selection">
  <label class="flex items-center gap-3 cursor-pointer">
    <md-gb-radio name="execution-mode" value="auto" checked></md-gb-radio>
    <div class="flex flex-col">
      <span class="typescale-body-medium font-medium">Automatic execution</span>
      <span class="typescale-body-small text-on-surface-variant">Run agent tasks without explicit approval</span>
    </div>
  </label>

  <label class="flex items-center gap-3 cursor-pointer">
    <md-gb-radio name="execution-mode" value="guided"></md-gb-radio>
    <div class="flex flex-col">
      <span class="typescale-body-medium font-medium">Guided execution</span>
      <span class="typescale-body-small text-on-surface-variant">Require user confirmation for critical steps</span>
    </div>
  </label>

  <label class="flex items-center gap-3 opacity-50 cursor-not-allowed">
    <md-gb-radio name="execution-mode" value="restricted" disabled></md-gb-radio>
    <span class="typescale-body-medium">Restricted sandbox (Disabled)</span>
  </label>
</div>
```
