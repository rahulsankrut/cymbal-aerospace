# Focus Ring (`focus-ring` / `<md-focus-ring>`)

The Focus Ring primitive manages accessible keyboard focus outlines and high-contrast indicators across custom interactive elements.

## Import

```javascript
// Stylesheet import
import focusRingStylesheet from '@material/web/labs/gb/components/focus/focus-ring.css' with {type: 'css'};

// Custom element import
import '@material/web/focus/md-focus-ring.js';
```

## API Reference

### Custom Element (`<md-focus-ring>`)

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `for` / `.for` | `string` | `''` | ID of the target interactive element to attach focus state to. |
| `inward` / `.inward` | `boolean` | `false` | When true, renders the focus ring inside the bounds of the element. |

### CSS Classes

| Class | Type | Description |
| --- | --- | --- |
| `.focus-ring-outer` | Root | Outer focus indicator ring. |
| `.focus-ring-inner` | Root | Inner focus ring layer for high-contrast accessibility. |
| `.focus-ring-host` | Modifier | Host container setting up relative focus positioning. |
| `.focus-ring-target` | Part | Target element attached to focus rings. |

## Usage Examples

### Custom Element Usage

```html
<div class="relative inline-block">
  <button id="custom-action-btn" class="px-4 py-2 bg-primary text-on-primary rounded-full">
    Custom Interactive Action
  </button>
  <md-focus-ring for="custom-action-btn"></md-focus-ring>
</div>
```
