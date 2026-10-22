# Checkbox (`<md-gb-checkbox>`)

The Checkbox (`<md-gb-checkbox>`) allows users to select one or more items from a list or toggle a standalone setting on or off.

## Import

```javascript
import '@material/web/labs/gb/components/checkbox/md-gb-checkbox.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `checked` / `.checked` | `boolean` | `false` | Whether the checkbox is checked. |
| `defaultchecked` / `.defaultChecked` | `boolean` | `false` | Default checked state for form reset behavior. |
| `indeterminate` / `.indeterminate` | `boolean` | `false` | Renders the checkbox in a mixed/indeterminate dash state. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |
| `required` / `.required` | `boolean` | `false` | Marks the checkbox as required for form validation. |
| `error` / `.error` | `boolean` | `false` | Displays error state validation styling. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@change` | `Event` | Fired when checked state changes from user interaction. |
| `@input` | `Event` | Fired when checked state changes from user interaction. |

### CSS Classes

```javascript
import checkboxStylesheet from '@material/web/labs/gb/components/checkbox/checkbox.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.checkbox` | Root | Component root class. |

## Usage Examples

### States Overview

```html
<div class="flex flex-col gap-3">
  <label class="flex items-center gap-2 cursor-pointer">
    <md-gb-checkbox></md-gb-checkbox>
    <span class="typescale-body-medium">Unchecked Checkbox</span>
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <md-gb-checkbox checked></md-gb-checkbox>
    <span class="typescale-body-medium">Checked Checkbox</span>
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <md-gb-checkbox indeterminate></md-gb-checkbox>
    <span class="typescale-body-medium">Indeterminate / Mixed Selection</span>
  </label>

  <label class="flex items-center gap-2 cursor-pointer">
    <md-gb-checkbox error checked></md-gb-checkbox>
    <span class="typescale-body-medium text-error">Validation Error Checkbox</span>
  </label>

  <label class="flex items-center gap-2 opacity-50 cursor-not-allowed">
    <md-gb-checkbox disabled></md-gb-checkbox>
    <span class="typescale-body-medium">Disabled Checkbox</span>
  </label>
</div>
```
