# Slider (`<md-gb-slider>`)

The Slider (`<md-gb-slider>`) lets users select single values or range spans from a continuous or discrete scale.

## Import

```javascript
import '@material/web/labs/gb/components/slider/md-gb-slider.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| --- | --- | --- | --- |
| `min` / `.min` | `number` | `0` | Minimum value scale limit. |
| `max` / `.max` | `number` | `100` | Maximum value scale limit. |
| `value` / `.value` | `number` | `0` | Value for single-handle sliders. |
| `value-start` / `.valueStart` | `number` | `0` | Start handle value in range mode (`range=true`). |
| `value-end` / `.valueEnd` | `number` | `100` | End handle value in range mode (`range=true`). |
| `step` / `.step` | `number \| 'any'` | `1` | Step interval between values. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'xs'` | Handle and track size variant. |
| `orientation` / `.orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Slider layout orientation. |
| `range` / `.range` | `boolean` | `false` | Enables dual-handle range selection. |
| `centered` / `.centered` | `boolean` | `false` | When true, active track expands outward from center origin. |
| `ticks` / `.ticks` | `boolean` | `false` | Displays discrete indicator dots along step intervals. |
| `labeled` / `.labeled` | `boolean` | `false` | Displays floating numeric value tooltip on hover or drag. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables user drag and keyboard adjustment. |
| `value-label` / `.valueLabel` | `string` | `''` | Custom formatted string for single slider value label. |
| `value-label-start` / `.valueLabelStart` | `string` | `''` | Custom string for start value label in range mode. |
| `value-label-end` / `.valueLabelEnd` | `string` | `''` | Custom string for end value label in range mode. |

### Slots

| Slot Name | Description |
| --- | --- |
| `slot="icon"` | Leading inset icon ligature (e.g. `<md-gb-icon slot="icon">volume_up</md-gb-icon>`) supported on horizontal `md`, `lg`, and `xl` sliders. |

### Events

| Event Name | Type | Description |
| --- | --- | --- |
| `@input` | `InputEvent` | Fired dynamically during active thumb dragging. |
| `@change` | `Event` | Fired when drag or keyboard interaction finishes. |

### CSS Classes

```javascript
import sliderStylesheet from '@material/web/labs/gb/components/slider/slider.css' with {type: 'css'};
```

| Class | Type | Description |
| --- | --- | --- |
| `.slider` | Root | Root slider element. |
| `.slider-track`, `.slider-active`, `.slider-handles`, `.slider-handle`, `.slider-label` | Parts | Inner slider parts. |

## Usage Examples

### Continuous Slider with Labeled Value

```html
<md-gb-slider min="0" max="100" value="50" labeled aria-label="Volume level"></md-gb-slider>
```

### Discrete Slider with Ticks

```html
<md-gb-slider min="0" max="100" step="10" value="30" ticks labeled aria-label="Step scale"></md-gb-slider>
```

### Centered Origin Slider

```html
<md-gb-slider centered min="-50" max="50" step="10" value="0" ticks labeled aria-label="Balance adjustment"></md-gb-slider>
```

### Range Selection Slider

```html
<md-gb-slider range min="0" max="100" value-start="20" value-end="80" labeled aria-label-start="Minimum price" aria-label-end="Maximum price"></md-gb-slider>
```

### Medium Slider with Inset Icon

```html
<md-gb-slider min="0" max="100" value="65" size="md" labeled aria-label="Audio volume">
  <md-gb-icon slot="icon">volume_up</md-gb-icon>
</md-gb-slider>
```
