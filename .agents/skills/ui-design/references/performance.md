# Load performance for UI changes

## Compare production builds

Compare two production builds of the same app: the baseline and your change. Use
the deployed production app as the baseline if you can reach it headlessly;
otherwise build the base revision in a second workspace. Build and serve both
the way the app ships (optimized, minified, compressed), each on its own port.
Dev servers skip minification and compression, so their load times say little
about what users get.

When the user says the app feels slower, first check whether they are on a dev
server, then compare production builds before changing anything.

## Paint timings

```bash
/google/bin/releases/gemini-agents-gbrowser/gbrowser eval --no-proxy-server \
  --clean-profile --width 1440 --height 900 "{url}" "(async () => {
    const lcp = await new Promise((r) => new PerformanceObserver((l) => {
      const e = l.getEntries();
      r(Math.round(e[e.length - 1].startTime));
    }).observe({type: 'largest-contentful-paint', buffered: true}));
    const paint = Object.fromEntries(performance.getEntriesByType('paint')
      .map((e) => [e.name, Math.round(e.startTime)]));
    return JSON.stringify({...paint, lcp});
  })()"
```

-   Run it at least 3 times per build and report the median. `--clean-profile`
    starts each run with an empty cache: a cold load, which is what users notice
    most.
-   First paint shows when anything appears; LCP shows when the main content
    appears. A static shell improves first paint but not LCP, so report both and
    don't overstate the gain.
-   For apps that render their main content late, run the eval after it is on
    screen: add `--wait-for "{ready_selector}"`.

## Bytes

List the largest files the page loaded:

```bash
/google/bin/releases/gemini-agents-gbrowser/gbrowser eval --no-proxy-server \
  --clean-profile "{url}" "JSON.stringify(
    performance.getEntriesByType('resource')
      .map((e) => [e.name.split('?')[0].split('/').pop(), e.initiatorType,
        e.transferSize, e.decodedBodySize])
      .sort((a, b) => b[3] - a[3]).slice(0, 15))"
```

-   `transferSize` is bytes over the network (compressed); `decodedBodySize` is
    the size after decompression. Cross-origin files without a
    `Timing-Allow-Origin` header report 0.
-   Also compare the built bundle files on disk. For each notable increase, name
    the cause (a new library, an embedded WebAssembly module, a font) and decide
    whether to keep it, load it later, or drop it.

## Common causes and fixes

-   **Blank page until JS runs**: nothing renders before the bundle executes.
    Put a static shell (header, skeleton) in the HTML entry point, with its CSS
    in the page or loaded first.
-   **Multi-MB font download**: a full icon font with every glyph and variable
    axis. Pin the axes and list only the icons in use; see
    [Fonts and icons](tokens.md#fonts-and-icons).
-   **Text appears late or shifts**: several font requests, no preconnect, or
    render-blocking font CSS. Use one combined font request, `preconnect` to the
    font host, and `font-display: swap`.
-   **Slower first load after a change**: a large dependency landed in the main
    bundle (charts, markdown, WebAssembly). Load it on first use, or pick a
    lighter option.
-   **Layout jumps when data arrives**: skeleton sizes differ from the loaded
    content. Match them to the final layout.
-   **Janky scrolling on long lists**: heavy shadows, blur, or filters on every
    row, or derived data recomputed on every render. Flatten row styling and
    memoize derived data.

For a second opinion, ask the user to run Lighthouse in Chrome DevTools against
the production build. Its render-blocking and unused-code audits point to the
largest wins.
