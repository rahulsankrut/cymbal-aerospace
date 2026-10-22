# Ripple (`ripple` / `<md-ripple>`)

The Ripple primitive provides interactive touch and pointer surface feedback states across custom containers.

## Import

```javascript
// Stylesheet import
import rippleStylesheet from '@material/web/labs/gb/components/ripple/ripple.css' with {type: 'css'};

// Custom element import
import '@material/web/ripple/ripple.js';
```

## API Reference

### Custom Element (`<md-ripple>`)

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `for` / `.for` | `string` | `''` | Target element ID to attach pointer ripple animations to. |

### CSS Classes

| Class | Type | Description |
| --- | --- | --- |
| `.ripple` | Root | Root ripple element. |
| `.ripple-host` | Modifier | Host container class setting relative positioning and overflow clipping. |
| `.ripple-target` | Part | Target element attached to ripple feedback. |

## Usage Examples

### Custom Card Ripple Surface

```html
<div class="relative overflow-hidden p-6 bg-surface-container rounded-xl cursor-pointer">
  <md-ripple></md-ripple>
  <h3 class="typescale-title-medium text-on-surface">Interactive Custom Card</h3>
  <p class="typescale-body-small text-on-surface-variant">Clicking anywhere on this card triggers a material surface ripple effect.</p>
</div>
```
