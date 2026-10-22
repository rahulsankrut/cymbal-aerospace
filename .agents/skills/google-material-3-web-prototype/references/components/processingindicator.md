# AI Processing Indicator (`<md-gb-processing-indicator>`)

The `<md-gb-processing-indicator>` component communicates that an AI model is actively working, displaying animated thinking dots or status label pills with optional source icons.

## Import \& Script Bundle Requirement

Google-internal components are **NOT** published on unpkg. You MUST load the self-registering bundle with a plain `<script src>` tag (load once per page; this bundle also registers `<md-gb-energy>`):

```html
<script src="https://static.corp.google.com/material-web/gbreeze/latest/components/md-gb-all.js"></script>
```

> **CRITICAL SCRIPT CONFLICT WARNING**: Never load the legacy `energy/md-gb-energy.js` script alongside `md-gb-all.js`. Both scripts define `<md-gb-energy>`, and if the legacy script runs first, `md-gb-all.js` throws an unhandled custom element re-registration exception before it can register `<md-gb-processing-indicator>`. Always replace `energy/md-gb-energy.js` with `md-gb-all.js`.

## API Reference

### Attributes and Properties

|API|Type|Default|Description|
|:---|:---|:---|:---|
|`step` / `.step`|`'dots' \| 'processing'`|`'dots'`|Display step mode. `'dots'` displays animated thinking dots; `'processing'` shows `label` text and `trailing` source icons.|
|`label` / `.label`|`string`|`'Searching'`|Status text in `'processing'` step mode. Text longer than \~24 characters truncates with an ellipsis.|
|`thinking-label` / `.thinkingLabel`|`string`|`'Processing'`|Accessible text label in `'dots'` step mode.|
|`uncontained` / `.uncontained`|`boolean`|`false`|Removes container fill, outline, and padding for borderless embedded displays.|

### Slots

|Slot Name|Description|
|:---|:---|
|`(default)`|Decorative custom content.|
|`container`|Custom background container slot, such as `<md-gb-energy slot="container" active state="processing">` for AI energy glows.|
|`trailing`|Source icons displayed after the status label in `'processing'` mode. Add `class="processing-indicator-source-icon"` for 14px source circles.|

## Customization \& Token Rules

The pill container is rendered inside a shadow root. Do NOT apply `bg-*` or `border-*` classes to the host element (it paints a square box behind the pill). Instead, override system color custom properties on the host:

* `--md-sys-color-surface`: Sets the container fill and icon ring background.
* `--md-sys-color-on-surface`: Sets the label text and thinking dots color.

## Accessibility

The host component exposes an indeterminate `progressbar` role with `aria-live="polite"`. Rendered visuals are decorative; do NOT slot essential or interactive content inside the component.

## Usage Examples

### Thinking Dots Mode

```html
<md-gb-processing-indicator thinking-label="AI model thinking..."></md-gb-processing-indicator>
```

### Processing Status with Overlapping Source Icons

```html
<md-gb-processing-indicator step="processing" label="Searching 3 sources">
  <span slot="trailing" class="processing-indicator-source-icon" style="background-color: var(--md-sys-color-primary-container); color: var(--md-sys-color-on-primary-container);">
    <md-gb-icon style="--md-icon-size: 10px;">public</md-gb-icon>
  </span>
  <span slot="trailing" class="processing-indicator-source-icon" style="background-color: var(--md-sys-color-tertiary-container); color: var(--md-sys-color-on-tertiary-container);">
    <md-gb-icon style="--md-icon-size: 10px;">description</md-gb-icon>
  </span>
</md-gb-processing-indicator>
```

### With AI Energy Surface Glow

```html
<md-gb-processing-indicator step="processing" label="Generating response">
  <md-gb-energy slot="container" active state="processing"></md-gb-energy>
</md-gb-processing-indicator>
```

### Dynamic JavaScript Step Switching

```html
<md-gb-processing-indicator id="ai-status"></md-gb-processing-indicator>

<script type="module">
  const indicator = document.getElementById('ai-status');

  // Step 1: Default thinking dots...
  setTimeout(() => {
    // Step 2: Switch to processing label with source info
    indicator.label = 'Reading 4 search results';
    indicator.step = 'processing';
  }, 2000);
</script>
```
