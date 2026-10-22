# Checkbox (`<md-gb-checkbox>`)

The `<md-gb-checkbox>` component provides a form checkbox control for multi-select choices, binary list toggles, or indeterminate parent selections.

## Import

```javascript
import '@material/web/labs/gb/components/checkbox/md-gb-checkbox.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `checked` / `.checked` | `boolean` | `false` | Whether or not the checkbox is currently selected. |
| `defaultchecked` / `.defaultChecked` | `boolean` | `false` | Initial default checked state. |
| `indeterminate` / `.indeterminate` | `boolean` | `false` | Sets indeterminate state (dash icon) when partial selection exists in child items. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user interaction. |
| `required` / `.required` | `boolean` | `false` | Marks the checkbox form control as required. |
| `error` / `.error` | `boolean` | `false` | Renders the checkbox in an error state. |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@change` | `Event` | Fired when the checked state changes from user action. |
| `@input` | `Event` | Fired during user interaction. |

## CSS Classes & Utility Styling

```javascript
import checkboxStylesheet from '@material/web/labs/gb/components/checkbox/checkbox.css' with {type: 'css'};
```

* `.checkbox`: Root checkbox control class.

## Usage Examples

### Basic States

```html
<label class="flex items-center gap-s100 typescale-body-md">
  <md-gb-checkbox></md-gb-checkbox>
  Unchecked Option
</label>

<label class="flex items-center gap-s100 typescale-body-md">
  <md-gb-checkbox checked></md-gb-checkbox>
  Checked Option
</label>

<label class="flex items-center gap-s100 typescale-body-md">
  <md-gb-checkbox indeterminate></md-gb-checkbox>
  Partially Selected Parent
</label>

<label class="flex items-center gap-s100 typescale-body-md text-error">
  <md-gb-checkbox error></md-gb-checkbox>
  Error State Required Field
</label>

<label class="flex items-center gap-s100 typescale-body-md opacity-50">
  <md-gb-checkbox disabled></md-gb-checkbox>
  Disabled Option
</label>
```
