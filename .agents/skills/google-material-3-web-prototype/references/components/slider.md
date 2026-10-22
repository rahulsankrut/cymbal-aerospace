# Slider (`<md-gb-slider>`)

The `<md-gb-slider>` component allows users to make numeric selections from a range of values using single-handle, range selection, or centered track variants.

## Import

```javascript
import '@material/web/labs/gb/components/slider/md-gb-slider.js';
```

## API Reference

### Attributes and Properties

| API | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `min` / `.min` | `number` | `0` | Minimum allowed value. |
| `max` / `.max` | `number` | `100` | Maximum allowed value. |
| `value` / `.value` | `number` | `0` | Value of single-handle slider. |
| `value-start` / `.valueStart` | `number` | `0` | Start value of range selection slider. |
| `value-end` / `.valueEnd` | `number` | `100` | End value of range selection slider. |
| `step` / `.step` | `number \| 'any'` | `1` | Interval step between discrete values. |
| `size` / `.size` | `'xs' \| 'sm' \| 'md' \| 'lg' \| 'xl'` | `'xs'` | Handle and track scale variant. |
| `orientation` / `.orientation` | `'horizontal' \| 'vertical'` | `'horizontal'` | Track orientation. |
| `range` / `.range` | `boolean` | `false` | Enables dual-thumb range selection mode. |
| `centered` / `.centered` | `boolean` | `false` | Expands active track outward from middle (0 point). |
| `ticks` / `.ticks` | `boolean` | `false` | Displays discrete indicator dots along step intervals. |
| `labeled` / `.labeled` | `boolean` | `false` | Shows floating value indicator popup on hover/active. |
| `disabled` / `.disabled` | `boolean` | `false` | Disables interaction. |
| `value-label` / `.valueLabel` | `string` | `''` | Custom value string for single handle indicator. |
| `value-label-start` / `.valueLabelStart` | `string` | `''` | Custom start value string for range indicator. |
| `value-label-end` / `.valueLabelEnd` | `string` | `''` | Custom end value string for range indicator. |

### Slots

| Slot Name | Description |
| :--- | :--- |
| `icon` | Leading inset icon ligature (supported on standard horizontal `md`, `lg`, and `xl` sliders). |

### Events

| Event | Type | Description |
| :--- | :--- | :--- |
| `@input` | `InputEvent` | Fired continuously while user drags handle. |
| `@change` | `Event` | Fired when user releases handle to commit value. |

## CSS Classes & Utility Styling

```javascript
import sliderStylesheet from '@material/web/labs/gb/components/slider/slider.css' with {type: 'css'};
```

* `.slider`: Root slider element.
* `.slider-track`, `.slider-track-box`, `.slider-active`, `.slider-inactive-lead`, `.slider-inactive-trail`, `.slider-boundary-stop`, `.slider-icon`, `.slider-handles`, `.slider-handle`, `.slider-handle-nub`, `.slider-label`, `.slider-label-content`: Slider child parts.

## Usage Examples

### Continuous & Discrete Sliders

```html
<!-- Continuous single slider -->
<md-gb-slider min="0" max="100" value="50" labeled></md-gb-slider>

<!-- Discrete slider with step ticks -->
<md-gb-slider min="0" max="100" step="10" value="30" ticks labeled></md-gb-slider>
```

### Centered Slider

```html
<md-gb-slider centered min="-50" max="50" step="10" value="0" ticks labeled></md-gb-slider>
```

### Range Slider

```html
<md-gb-slider range min="0" max="100" value-start="20" value-end="80" labeled></md-gb-slider>
```

### Slider with Leading Icon

```html
<md-gb-slider min="0" max="100" value="65" size="md" labeled>
  <md-gb-icon slot="icon">volume_up</md-gb-icon>
</md-gb-slider>
```
