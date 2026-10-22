# Divider (`<md-gb-divider>`)

The Divider (`<md-gb-divider>`) provides thin structural separation lines across horizontal rows or vertical columns.

## Import

```javascript
import '@material/web/labs/gb/components/divider/md-gb-divider.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `vertical` / `.vertical` | `boolean` | `false` | When true, renders a vertical divider line instead of horizontal. |

### CSS Classes

```javascript
import dividerStylesheet from '@material/web/labs/gb/components/divider/divider.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.divider` | Root | Root divider class. |
| `.divider-vertical` | Modifier | Vertical orientation modifier. |

## Usage Examples

### Horizontal Divider

```html
<div class="flex flex-col gap-3">
  <div>Section Header Above</div>
  <md-gb-divider></md-gb-divider>
  <div>Section Content Below</div>
</div>
```

### Vertical Divider

```html
<div class="flex items-center gap-4 h-10">
  <span>Left Action</span>
  <md-gb-divider vertical></md-gb-divider>
  <span>Right Action</span>
</div>
```
