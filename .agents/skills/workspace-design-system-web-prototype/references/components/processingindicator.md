# Processing Indicator (`<md-gb-processing-indicator>`)

The AI Processing Indicator (`<md-gb-processing-indicator>`) presents real-time AI working status using animated thinking dots or dynamic processing status pills with optional source icons.

## Loading Instructions

`<md-gb-processing-indicator>` ships as part of a self-registering bundle. Load it via a plain `<script src>` tag once per HTML document:

```html
<!-- Google-internal components bundle (registers md-gb-processing-indicator and md-gb-energy) -->
<script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
```

> **CRITICAL BUNDLE RULE**: Do NOT load `energy/md-gb-energy.js` alongside `md-gb-all.js`. Both define `<md-gb-energy>`, causing script conflicts that prevent `<md-gb-processing-indicator>` from registering.

## API Reference

### Attributes and Properties

|API|Type|Default|Description|
|---|---|---|---|
|`step` / `.step`|`'dots' \| 'processing'`|`'dots'`|Display mode. `'dots'` renders animated thinking dots; `'processing'` renders status text label and trailing source icons.|
|`label` / `.label`|`string`|`'Searching'`|Status text shown in the `'processing'` step. Truncates with ellipsis if longer than \~24 characters.|
|`thinking-label` / `.thinkingLabel`|`string`|`'Processing'`|Accessible ARIA name in the `'dots'` step, or fallback when `label` is empty.|
|`uncontained` / `.uncontained`|`boolean`|`false`|Removes container background fill, outline, and inline padding.|

### Slots

|Slot Name|Description|
|---|---|
|`slot="container"`|Custom background surface container, e.g., `<md-gb-energy slot="container" active state="processing">` for AI aura glows.|
|`slot="trailing"`|Source icons in the `'processing'` step. Add `class="processing-indicator-source-icon"` to each icon for overlapping 14px circle rings.|
|`(default)`|Decorative custom content.|

### Styling \& Customization

The processing pill is rendered inside the shadow root. To customize colors, override system tokens on the host element:

- `--md-sys-color-surface`: Controls fill and source icon ring outlines.
- `--md-sys-color-on-surface`: Controls label text and thinking dots color.

Do NOT add `bg-*` or `border-*` classes directly to the host element, as they paint rectangular boxes behind the rounded pill.

## Usage Examples

### Thinking Dots Step

```html
<md-gb-processing-indicator thinking-label="Analyzing prompt..."></md-gb-processing-indicator>
```

### Processing Status Pill with Source Icons

```html
<md-gb-processing-indicator step="processing" label="Searching the web">
  <span slot="trailing" class="processing-indicator-source-icon"
      style="background-color: var(--md-sys-color-primary-container); color: var(--md-sys-color-on-primary-container)">
    <md-gb-icon style="--md-icon-size: 10px">public</md-gb-icon>
  </span>
  <span slot="trailing" class="processing-indicator-source-icon"
      style="background-color: var(--md-sys-color-tertiary-container); color: var(--md-sys-color-on-tertiary-container)">
    <md-gb-icon style="--md-icon-size: 10px">description</md-gb-icon>
  </span>
</md-gb-processing-indicator>
```

### AI Energy Glow Combination

```html
<md-gb-processing-indicator step="processing" label="Generating summary">
  <md-gb-energy slot="container" active state="processing"></md-gb-energy>
</md-gb-processing-indicator>
```

### Dynamic JavaScript Step Switching

```html
<md-gb-processing-indicator id="ai-status-indicator"></md-gb-processing-indicator>

<script type="module">
  const indicator = document.getElementById('ai-status-indicator');
  
  // Transition from thinking dots to processing step when model begins reading sources
  setTimeout(() => {
    indicator.label = 'Reading 3 sources';
    indicator.step = 'processing';
  }, 1500);
</script>
```
