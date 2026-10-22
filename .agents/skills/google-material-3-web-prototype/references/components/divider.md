# Divider (`<md-gb-divider>`)

The `<md-gb-divider>` component renders a thin horizontal or vertical rule to visually separate content regions, card sections, or list groups.

## Import

```javascript
import '@material/web/labs/gb/components/divider/md-gb-divider.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `vertical` / `.vertical` | `boolean` | `false` | When true, renders a vertical divider instead of horizontal. |

## CSS Classes & Utility Styling

```javascript
import dividerStylesheet from '@material/web/labs/gb/components/divider/divider.css' with {type: 'css'};
```

* `.divider`: Root divider element.
* `.divider-vertical`: Vertical layout modifier class.

## Usage Examples

### Horizontal Divider

```html
<div class="flex flex-col gap-s200">
  <div class="typescale-body-md">Upper Content Block</div>
  <md-gb-divider></md-gb-divider>
  <div class="typescale-body-md">Lower Content Block</div>
</div>
```

### Vertical Divider

```html
<div class="flex items-center gap-s200 h-10">
  <span class="typescale-body-md">Left Item</span>
  <md-gb-divider vertical style="height: 100%;"></md-gb-divider>
  <span class="typescale-body-md">Right Item</span>
</div>
```
