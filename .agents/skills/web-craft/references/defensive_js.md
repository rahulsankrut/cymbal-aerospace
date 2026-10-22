# Defensive JavaScript Reference

Common failure patterns and their fixes.

--------------------------------------------------------------------------------

## String Escaping

An unescaped apostrophe or raw newline inside a `'...'` or `"..."` string
literal produces a SyntaxError that kills every function in the `<script>`
block. Use backtick template literals for all data strings:

```javascript
// Safe for apostrophes, double quotes, and newlines
const items = [
  { name: `Mac 'n' Cheese`, price: 12 },
  { name: `"Blue notes" -- flattened scale degrees` },
];
const step = {
  code: `print(f'Logs size: {len(data)}')\nprint(data[0])`,
};
step.vars.split('\n');
```

--------------------------------------------------------------------------------

## DOM Null Guards

Every `document.getElementById()` or `querySelector()` result must be checked
for null before chaining. Missing elements crash tabs, modals, and drag
interactions:

```javascript
// Correct
const el = document.getElementById('panel');
if (el) el.classList.add('active');

// Also correct for multiple operations
const btn = document.querySelector('.submit-btn');
if (!btn) return;
btn.disabled = true;
btn.textContent = 'Saving…';
```

--------------------------------------------------------------------------------

## Function Hoisting & onclick Handlers

Functions used in `onclick`, `onchange`, or `oninput` attributes must use
`function` declarations (hoisted). `const`/`let` arrow functions are not visible
at parse time:

```javascript
// Correct -- hoisted
function setFilter(type) {
  // filter logic
}

// Wrong -- not hoisted, every button throws ReferenceError
const setFilter = (type) => { ... };
```

Never use `<script type="module">` with inline HTML event handlers. Module
top-level scope is not attached to `window`, so `onclick="fn()"` will fail with
`ReferenceError: fn is not defined`.

--------------------------------------------------------------------------------

## Dual-Input Slider/Number Sync

Dedicated handlers for each input direction. A single shared function that reads
from a hardcoded element ID will snap the slider back on drag:

```javascript
// Correct -- dedicated handlers
function syncFromSlider(val) {
  document.getElementById('input-rate').value = val;
  updateCalculations();
}
function syncFromNumber(val) {
  document.getElementById('slider-rate').value = val;
  updateCalculations();
}
// HTML:
// <input type="range" id="slider-rate" oninput="syncFromSlider(this.value)">
// <input type="number" id="input-rate" oninput="syncFromNumber(this.value)">
```

--------------------------------------------------------------------------------

## Chart and Map Container Heights

Plotly, Leaflet, ECharts, and Chart.js measure `clientHeight` to scale. A
container with no explicit height (e.g., bare `flex-grow: 1` with no parent
height) evaluates to `0px` and renders blank:

```html
<!-- Always set an explicit min-height on chart/map containers -->
<div id="chart" style="min-height: 400px;"></div>
```

See **references/maps.md** for the approved map patterns and working code.
Raster map tiles are banned; Plotly `choropleth` and `scattergeo` are supported.

--------------------------------------------------------------------------------

## Canvas & Immediate-Mode Graphics

Canvas-based rendering requires explicit height, defensive render gating, and a
single animation loop owner:

```javascript
const canvas = document.getElementById('viz');
if (!canvas) return;
const ctx = canvas.getContext('2d');

// Set explicit pixel dimensions -- CSS size alone doesn't set canvas resolution
canvas.width = canvas.offsetWidth;
canvas.height = canvas.offsetHeight;

// Single animation loop -- never start multiple loops for the same canvas
let animId;
function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // draw ...
  animId = requestAnimationFrame(render);
}
cancelAnimationFrame(animId); // cancel any existing loop before starting
render();
```

--------------------------------------------------------------------------------

## Pre-flight Checklist

Before finalizing, scan for:

1.  Apostrophes and quotes in data string literals: switch to backticks
2.  Every `onclick`/`onchange`/`oninput` function: confirm it exists, uses a
    `function` declaration, and that the script is not `type="module"`
3.  Every slider and number pair: confirm dedicated handlers, no snap-back bug
4.  Every chart and map container: confirm an explicit `min-height` or `h-*` is
    declared
5.  Every `getElementById`/`querySelector`: confirm the target ID exists in the
    HTML and a null guard is present
6.  Trailing commas on last array or object entries: remove them (they break
    older parsers)
7.  All CDN links and `fetch()` calls: confirm they match
    **references/allowed_cdns.md**
