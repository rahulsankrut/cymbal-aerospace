# Allowed CDN Dependencies

When building standalone `.html` artifacts, **ONLY** import external libraries
and resources from the **exact pinned URLs** listed below. Unapproved hosts,
unlisted npm packages, floating tags (`@latest`, major-only `@4`), and raster
map tile servers are blocked by `validate_html_artifact.py` (`ERROR`) and iframe
Content Security Policy (CSP).

## Pre-Approved Snippets & Datasets

Library / Dataset       | Type                  | Exact Pinned URL / HTML Snippet
:---------------------- | :-------------------- | :------------------------------
**Tailwind CSS**        | CSS                   | `https://cdn.tailwindcss.com/3.4.17`
**Google Fonts**        | Fonts                 | `https://fonts.googleapis.com/css2?family=...`
**Material Symbols**    | Icons                 | `https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@400`
**Lucide Icons**        | Icons                 | `https://unpkg.com/lucide@1.43.0/dist/umd/lucide.min.js`
**Leaflet.js**          | Interactive Maps      | JS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.js`<br>CSS: `https://unpkg.com/leaflet@1.9.4/dist/leaflet.css`<br>**Vector basemap only — no tile layer. See references/maps.md.**
**World TopoJSON**      | Map Data (countries)  | `https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json`<br>`https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-50m.json`
**World Land**          | Map Data (landmass)   | `https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-110m.json`
**US TopoJSON**         | Map Data (10m)        | `https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-10m.json`<br>`https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/counties-10m.json`<br>`https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/nation-10m.json`<br>`https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-albers-10m.json`
**TopoJSON Client**     | TopoJSON Parser       | `https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js`
**Chart.js**            | Charts                | `https://cdn.jsdelivr.net/npm/chart.js@4.5.1/dist/chart.umd.min.js`
**D3.js**               | Charts & Viz          | `https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js`
**Plotly.js**           | Charts + Geo/Maps     | `https://cdn.jsdelivr.net/npm/plotly.js-dist-min@2.32.0/plotly.min.js`
**Plotly Geo TopoJSON** | Map TopoJSON          | Call `Plotly.setPlotConfig({ topojsonURL: 'https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/' })` before `Plotly.newPlot(...)` (e.g. `https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/usa_110m.json`, `https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/world_110m.json`)
**Apache ECharts**      | Charts                | `https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min.js`
**Scrollama**           | Scrollytelling        | `https://cdn.jsdelivr.net/npm/scrollama@3.2.0/build/scrollama.min.js`
**KaTeX**               | Math Formulas         | JS: `https://cdn.jsdelivr.net/npm/katex@0.18.2/dist/katex.min.js`<br>CSS: `https://cdn.jsdelivr.net/npm/katex@0.18.2/dist/katex.min.css`<br>Auto-render: `https://cdn.jsdelivr.net/npm/katex@0.18.2/dist/contrib/auto-render.min.js`
**Math.js**             | Computer Algebra      | `https://cdn.jsdelivr.net/npm/mathjs@12.4.3/lib/browser/math.js`
**Three.js**            | 3D / WebGL            | Classic UMD: `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js`<br>ES Module: `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js`
**Tone.js**             | Audio / Synthesis     | `https://cdn.jsdelivr.net/npm/tone@14.9.17/build/Tone.js`
**Matter.js**           | 2D Physics            | `https://cdn.jsdelivr.net/npm/matter-js@0.19.0/build/matter.min.js`
**Cannon-es**           | 3D Physics            | ES Module (`<script type="module">`): `https://cdn.jsdelivr.net/npm/cannon-es@0.20.0/dist/cannon-es.js`
**Mermaid.js**          | Diagrams / Schematics | `https://cdn.jsdelivr.net/npm/mermaid@11.17.2/dist/mermaid.min.js`
**Cytoscape.js**        | Network Graphs        | `https://cdn.jsdelivr.net/npm/cytoscape@3.34.3/dist/cytoscape.min.js`

## Exact Version Pinning & Open-Source License Policy

-   **Strict Per-Package Allowlist**: Only the exact package names and pinned
    versions in the table above may be loaded. Do **NOT** import arbitrary npm
    packages from `cdn.jsdelivr.net` or `unpkg.com`, and never use floating
    version tags (`@latest`, `@4`, `@7`).
-   **Literal URLs Only**: Copy each library or dataset URL exactly as written
    in the table above. Do not build these URLs at runtime (string concatenation
    or template literals), and do not use protocol-relative `//` URLs, CSS
    `@import`, CSS `url(...)`, or `srcset` to load them. The validator cannot
    check URLs written those ways, and the CSP will block them.
-   **License Policy**: All pre-approved libraries and datasets above are
    verified under permissive/notice open-source licenses (`MIT`,
    `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `Apache-2.0`, `OFL-1.1`, and US
    Census / Natural Earth Public Domain; dual-licensed sub-components elect
    `MIT` or `Apache-2.0`). Copyleft (`GPL`, `LGPL`, `AGPL`), reciprocal
    (`MPL-2.0`, `EPL`, `CC-BY-SA`, `ODbL`), and proprietary/commercial packages
    are strictly prohibited.

## Map Datasets

Maps are built from **public-domain vector geometry** (Natural Earth, US Census)
rendered by Leaflet, Plotly, D3, or ECharts. Raster map tiles are banned
outright — see **Critical Prohibitions & Common Traps** below.

The dataset URLs are in the table above. **`references/maps.md` is the single
source of truth for everything else about maps** — the approved patterns with
working code, which dataset to load at which zoom, the verified TopoJSON
accessor keys, and the join traps. Read it before building any map.

When using Plotly geographic traces (`type: 'choropleth'`, `type: 'scattergeo'`,
`locationmode: 'USA-states'`), always configure:

```javascript
Plotly.setPlotConfig({
  topojsonURL: 'https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/'
});
```

before calling `Plotly.newPlot(...)` so Plotly loads its Natural Earth vector
TopoJSON (`usa_110m.json`, `world_110m.json`, etc.) from the pinned jsDelivr
package rather than `cdn.plot.ly`.

## Permitted Origins (CSP Allowlist)

-   **Scripts, Styles, Fonts, & Connect (`connect-src`, `script-src`,
    `style-src`)**:
    -   `cdn.tailwindcss.com`, `fonts.googleapis.com`, `maps.googleapis.com`,
        `*.gstatic.com`
    -   `cdn.jsdelivr.net`, `cdnjs.cloudflare.com`, `unpkg.com`, `cdn.plot.ly`
-   **Images (`image-src`)**:
    -   All script/style origins above, plus `*.google.com`, `*.ggpht.com`
    -   `*.googleusercontent.com`
    -   `blob:` and `data:` URIs

## Extra Allowlisted URL Policy Hosts (Non-Fetched Namespaces & Citations)

In addition to the CSP origins above, the tool-input URL security policy permits
the following hosts and domains as non-fetched identifiers or reference URLs in
HTML artifacts (do not fetch scripts, styles, or data from them, as iframe CSP
blocks network requests to them):

<!-- LINT.IfChange(nos_html_extra_url_allowlist) -->

-   **XML & Metadata Namespaces / Placeholders**: `w3.org` (such as inline SVG
    `xmlns="http://www.w3.org/2000/svg"`), `schema.org` (JSON-LD `@context` and
    `@type`), `ogp.me` (Open Graph namespaces), `example.com` (RFC 2606 reserved
    placeholder)
-   **Approved Educational & Reference Domains**: `openstax.org`, `quizlet.com`,
    `brainly.com`, `brainly.com.br`, `knowt.com`, `eur-lex.europa.eu`

<!-- LINT.ThenChange(//depot/google3/java/com/google/labs/language/tailwind/boqnodes/orchestration/service/config/nos_agency_url_policy.textproto:nos_html_extra_url_allowlist) -->

## Critical Prohibitions & Common Traps

1.  **Map Tile Providers (ALL BANNED)**: Do NOT use OpenStreetMap, CartoDB,
    Stadia/Stamen, Mapbox, or Esri tile URLs. Do NOT call `L.tileLayer()` at
    all. Plotly's `scattermapbox`, `choroplethmapbox`, `densitymapbox`,
    `scattermap`, `choroplethmap`, and `densitymap` traces are banned for the
    same reason — they pull raster tiles; use `scattergeo` / `choropleth`, which
    are pure vector. Build maps from the public-domain vector geometry above —
    see `references/maps.md`.
2.  **External Data / Audio / 3D Model URLs**: Do NOT `fetch()` datasets from
    `raw.githubusercontent.com` or public APIs. Do NOT load external audio files
    (`soundjay.com`) or 3D models (`.gltf` on GitHub). Synthesize audio via
    Tone.js / Web Audio API and generate 3D scenes via procedural Three.js
    geometries.
