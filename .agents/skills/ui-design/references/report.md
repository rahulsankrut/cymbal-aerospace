# Before/after report

A single HTML page lets reviewers see the whole change in a minute and gives the
CL a lasting record.

## Contents

1.  One-sentence summary and 3–4 numbers (pages changed, first paint, LCP,
    bundle size).
2.  "What changed" cards: one per theme (tokens, shared components, a rebuilt
    widget, performance), 2–3 short lines each.
3.  One before/after slider per page, same viewport and data, with 2–3 short
    notes each.
4.  A grid of before/after pairs for states: hover, focus, menus, empty, error.
5.  The performance table, with how and where it was measured.
6.  Open questions and judgment calls for the user.

## Build it from the screenshot sets

-   `before/` and `after_vN/` share file names, so a small script can generate
    the page by looping over the names.
-   Convert shots to lossless WebP, which is much smaller than PNG and keeps
    text sharp: `magick in.png -define webp:lossless=true out.webp`.
-   Keep CSS and JS in files next to `index.html` (or inline them with CSP
    hashes). Avoid inline event handlers such as `onclick=`, which strict CSPs
    block.
-   Before sharing, check the page with gbrowser: tabs switch, sliders move,
    images load.

A slider that works with mouse and keyboard, using a native range input:

```html
<div class="compare">
  <img src="img/03_list_after.webp" alt="After">
  <img class="before" src="img/03_list_before.webp" alt="Before">
  <input type="range" min="0" max="100" value="50"
         aria-label="Before and after divider">
</div>
```

```css
.compare { position: relative; --pos: 50%; }
.compare img { display: block; width: 100%; }
.compare .before {
  position: absolute; inset: 0; height: 100%;
  object-fit: cover; object-position: top left;
  clip-path: inset(0 calc(100% - var(--pos)) 0 0);
}
.compare input {
  position: absolute; inset: 0; width: 100%; height: 100%;
  margin: 0; opacity: 0; cursor: ew-resize;
}
.compare::after {
  content: ""; position: absolute; inset: 0 auto 0 var(--pos);
  width: 2px; background: #fff; box-shadow: 0 0 0 1px rgb(0 0 0 / 25%);
  pointer-events: none;
}
.compare:focus-within { outline: 2px solid #1a73e8; outline-offset: 4px; }
```

```js
for (const c of document.querySelectorAll('.compare')) {
  const range = c.querySelector('input');
  range.addEventListener('input', () => {
    c.style.setProperty('--pos', `${range.value}%`);
  });
}
```

If the two shots differ in height, the "before" image is cropped from the top
left instead of stretched.

## Host it on CNS

-   Upload the folder and make it world-readable (see the
    [filesystems skill](/learning/gemini/agents/skills/filesystems/SKILL.md)),
    then share `https://cnsviewer-static.corp.google.com/cns/{path}/index.html`.
-   cnsviewer-static serves HTML with a CSP `sandbox` that allows scripts but
    not same-origin, so the page has an opaque origin: storage such as
    `localStorage` is unavailable, and `'self'` in your own CSP may not match in
    every browser. List `https://cnsviewer-static.corp.google.com` explicitly in
    `img-src`.
-   Screenshots of internal tools can contain user data or confidential details.
    Use test data or crop, or upload to a directory with a TTL and narrower
    permissions.

Put the report link at the top of the CL description so reviewers open it first.
