# Scrollytelling

The default build for a Narrative: the scroll **changes a visual**. Load this
whenever the spine (Step 2) has any evolving or recurring visual — most
narratives. Two modes, one small engine.

## Which mode

**references/narrative.md** chooses the mode from your spine. Two exist:
**sticky scroller** (beats are views of one evolving visual — pin it; the
dominant form) and **in-flow scenes** (each beat is its own distinct scene,
drawn once as it enters view then scrolls away, nothing pinned). Only when the
prose has no evolving visual at all do you keep visuals inline instead.

## How to wire it

Use **scrollama** — it is on the allowlist via the jsDelivr npm mirror
(`https://cdn.jsdelivr.net/npm/scrollama@3.2.0/build/scrollama.min.js`; see
`references/allowed_cdns.md`). It's dependency-free, handles resize/offset for
you, and is the **only** clean way to get continuous `progress` scrubbing.
Native `IntersectionObserver` is a fine zero-dependency fallback for plain
discrete steps.

Two rules regardless of engine:

-   Put `position: sticky` on the **graphic `<figure>`** — NEVER on `<header>`
    (hard anti-pattern; the validator flags it).
-   Guard on load and render the initial state, so a CDN hiccup degrades to a
    readable first frame instead of a blank one: `if (window.scrollama) {
    …setup… }` and call `render(0)` unconditionally.
-   **No `overflow` ancestor** (the #1 cause of a dead scroller). The sticky
    `<figure>` must not sit inside ANY ancestor whose `overflow` is not
    `visible` — `overflow: hidden` / `overflow-y` / `auto` / `scroll` on
    `.page-grid`, `main`, or a wrapping `<section>` silently disables the pin,
    so the graphic scrolls away after the first beat and the graphic column goes
    blank. The required scaffold therefore uses `.page-grid { overflow-x: clip;
    }` (safe: clips horizontal blowout without creating a scroll container) —
    NOT `overflow: hidden`. `overflow-x: clip` on `html, body` is fine (scroll
    root). `transform` / `filter` / `perspective` on an ancestor break the pin
    too.

### Sticky scroller — use the scaffold

The full, working sticky-scroller reference implementation is
`/workspace/skill_scripts/web-craft/scrollytelling_scaffold.html`. Keep its
**PIN CORE** CSS and **ENGINE** `<script>` verbatim — together they encode the
four rules above (sticky on the `<figure>`, no `overflow` ancestor, `render(0)`
on load, scrollama with a native `IntersectionObserver` fallback) — then replace
the `STEPS` array and `renderGraphic(i)` with your content. Two wiring gotchas:
give any chart/map box an explicit `min-height` (it collapses to 0 otherwise),
and call `scroller.resize` (and `map.invalidateSize()` for Leaflet) on window
`resize`. The scaffold's rules already use the design-style token names
(`--background`, `--on-surface`, `--primary`, `--font-label`, ...); its `:root`
holds placeholder values only. Replace that `:root` with the chosen style's
block plus the **references/design_foundation.md** tokens.

### In-flow scenes

No `sticky`. Each scene is a normal-flow block; fire its one-time draw when it
enters, then stop watching it:

```javascript
const io = new IntersectionObserver((entries, obs) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add('is-visible'); // draw/animate once
    obs.unobserve(e.target);              // never re-fire
  });
}, { threshold: 0.35 });
document.querySelectorAll('.scene').forEach((el) => io.observe(el));
```

### Continuous scrub (optional, scrollama only)

For a value that tracks scroll *position* (a counter filling, a line drawing in
proportion), use one tall step and `progress`:

```javascript
scrollama().setup({ step: '.step', offset: 0.5, progress: true })
  .onStepProgress(({ progress }) => setState(progress)); // progress ∈ [0,1]
```

## Non-negotiables

-   **Fire once.** Never loop or re-animate on every scroll — the banned "scroll
    waterfall."
-   **Every step = a real state/scene change.** If a step doesn't change what
    the reader sees or understands, it's decoration — cut it.
-   **Reduced motion — keep the pin, drop the tweens.** Under `@media
    (prefers-reduced-motion: reduce)` do NOT un-pin the graphic (that drifts the
    shared visual off-screen while later beats fire, tested). Keep `position:
    sticky` and the step logic; only remove the CSS `transition`s / chart
    animations so states snap instantly. If a single graphic genuinely can't
    hold all states without motion, fall back to stacked small-multiples (one
    static snapshot per beat).
-   **Progressive disclosure, not gatekeeping.** Content must exist in the DOM
    and be reachable by scroll alone; never require JS to reveal essential text.

## Feasibility (what to build vs. avoid)

-   ✅ **Graphic sequence** (swap discrete states), **animated transition**
    (tween between states), **pan & zoom** over a map/image — all render cleanly
    now with CSS/SVG, Leaflet, D3, or Chart.js. For Leaflet maps: use a vector
    basemap (no tile layers — see `references/maps.md`), disable
    `scrollWheelZoom`, and keep `flyTo` durations modest (~1s) so fast scrolls
    stay legible. Vector basemaps have no tiles to load, so they don't flash
    grey during rapid scrubbing.
-   ⚠️ **Show-and-play** (scroll triggers a short audio/animation via Tone.js or
    CSS) — fine as an in-flow scene; keep it one-shot and reduced-motion-safe.
-   ⛔ **Moviescroller** (scroll scrubs a video frame-by-frame) — out of scope in
    a single self-contained file: it needs external video/frame assets the CSP
    forbids (see `references/allowed_cdns.md`). An asset-pipeline feature, not a
    web-craft one.
