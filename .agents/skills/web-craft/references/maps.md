# Maps

All maps in web-craft are built from **public-domain vector geometry** (Natural
Earth, US Census) — never from raster map tiles.

> **There is no approved tile server.** Do NOT call `L.tileLayer()`. Do NOT use
> a `{z}/{x}/{y}` URL from OpenStreetMap, CartoDB, Stadia/Stamen, Mapbox, or
> Esri. They will be blocked by CSP and flagged by the validator.

Leaflet still works perfectly without tiles: you render country/state polygons
as a GeoJSON layer and keep every interaction (pan, zoom, `flyTo`, markers,
popups, polylines). Every snippet below is verified working.

## Pick a pattern

| Want                           | Use                               | Pattern |
| ------------------------------ | --------------------------------- | ------- |
| Pan/zoom world map, route,     | Leaflet + vector basemap          | 1       |
: popups                         :                                   :         :
| Shade US states by a value     | Plotly `choropleth` (simplest) or | 4, 2    |
:                                : Leaflet                           :         :
| Shade 1000+ regions (counties) | Leaflet + canvas renderer         | 3       |
| Route / points on a globe      | Plotly `scattergeo` or D3         | 5, 6    |
| Custom projection, rotatable   | D3 `geoPath`                      | 6       |
: globe                          :                                   :         :
| Roam + animated route trails   | ECharts `registerMap`             | 7       |
| US state / metro, zoom 5–11    | Leaflet + counties, filtered      | 9       |
| City / neighborhood scale      | Schematic (no street data exists) | 8       |

Accessor keys and feature counts for every dataset are in **Datasets and
accessor keys** below. Use them exactly — guessing the object key is the most
common way these maps break.

## Match the dataset to your zoom

**This is the most common way a vector map fails, and it fails silently.** A
tile server always had something to draw at every zoom level. Vector geometry
does not. If you zoom in past the resolution of your dataset, the viewport ends
up entirely inside a single polygon, and the map paints as one flat fill — no
borders, no coastline, no console error. It looks like a CSS bug, so it is easy
to ship by accident.

Leaflet zoom | What fills the screen   | Load this
------------ | ----------------------- | ---------------------------------------
0–4          | World, continents       | `world-atlas@2.0.2/countries-110m.json`
5–6          | One country, neighbours | `world-atlas@2.0.2/countries-50m.json`
5–8          | US, multi-state region  | `us-atlas@3.0.1/states-10m.json`
7–11         | US state, metro area    | `us-atlas@3.0.1/counties-10m.json`
12+          | City, neighborhood      | Nothing exists — use pattern 8

**At zoom 6 or higher, `countries-110m` is the wrong dataset.** Measured: at
`zoom: 9` over Sacramento, `countries-110m` puts exactly **1** polygon in the
viewport (the USA) and the map is blank; `counties-10m` filtered to California
puts **15** on screen. Same centre, same zoom — see pattern 9.

Outside the US there is no county-equivalent set bundled here, so
`countries-50m` is the floor. Past roughly zoom 7 on non-US geography, prefer
the pattern 8 schematic over an empty basemap.

> **Check before you finalize:** does at least one border or coastline fall
> inside the *initial* viewport? If not, zoom out or load finer geometry. Do not
> rely on the reader panning to find the map.

## Datasets and accessor keys

Each file is a TopoJSON `Topology`. Convert it with `topojson.feature(topo,
topo.objects.<KEY>)` before handing it to a renderer. These keys and feature
counts are verified — use them exactly. The CDN URLs are in
**references/allowed_cdns.md**.

`world-atlas@2.0.2` (world geography):

File             | Object key          | Features | Join property
:--------------- | :------------------ | -------: | :----------------
`countries-110m` | `objects.countries` | 177      | `properties.name`
`countries-50m`  | `objects.countries` | 241      | `properties.name`
`land-110m`      | `objects.land`      | 1        | — (landmass only)

`us-atlas@3.0.1` (US geography):

File           | Object key         | Features | Join property
:------------- | :----------------- | -------: | :------------------
`states-10m`   | `objects.states`   | 56       | `properties.name`
`counties-10m` | `objects.counties` | 3231     | `id` (5-digit FIPS)
`nation-10m`   | `objects.nation`   | 1        | —

`us-atlas states-10m` and `counties-10m` also expose `objects.nation` for a
clean outer border.

> **Trap: never use `states-albers-10m.json` with Leaflet.** That file is
> **pre-projected** into Albers screen coordinates (bbox `[-57…957, 12…606]`),
> not latitude/longitude. Leaflet expects lat/lng and will render it as a
> distorted smear. It is only usable in D3 via `d3.geoIdentity()`. For Leaflet
> always use `states-10m.json`.

--------------------------------------------------------------------------------

## 1. Leaflet + vector basemap (the OSM replacement)

The default choice for interactive geography. Renders 177 countries; the
container background becomes the ocean.

Load these three in `<head>` (exact URLs, all CSP-allowlisted):

```text
leaflet CSS  https://unpkg.com/leaflet@1.9.4/dist/leaflet.css
leaflet JS   https://unpkg.com/leaflet@1.9.4/dist/leaflet.js
topojson     https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js
```

```html
<style>
  /* Explicit height is mandatory; ocean colour lives on the container. */
  #map { height: 520px; min-height: 520px; background: #CFE0EC; }
  .leaflet-container { background: #CFE0EC; }
</style>
<div id="map"></div>
<script>
  const map = L.map('map', {
    center: [38, 70], zoom: 3, scrollWheelZoom: false
  });
  map.attributionControl.addAttribution(
      'Boundaries: Natural Earth (public domain)');

  fetch('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json')
    .then(r => r.json())
    .then(topo => {
      const geo = topojson.feature(topo, topo.objects.countries);
      L.geoJSON(geo, {
        style: { fillColor: '#EDE4D3', fillOpacity: 1,
                 color: '#B9A98C', weight: 0.6 }
      }).addTo(map);

      // Route + stops use ordinary [lat, lng] - unchanged from tile maps.
      const stops = [['Samarkand', 39.627, 66.975],
                     ['Baghdad', 33.3152, 44.3661]];
      const route = L.polyline(stops.map(s => [s[1], s[2]]),
                               { color: '#B4532A', weight: 3,
                                 dashArray: '6 4' }).addTo(map);
      stops.forEach(s => {
        L.circleMarker([s[1], s[2]], {
          radius: 6, color: '#7A2E12', fillColor: '#D97742',
          fillOpacity: 1, weight: 2
        }).bindPopup('<strong>' + s[0] + '</strong>').addTo(map);
      });
      map.fitBounds(route.getBounds(), { padding: [30, 30] });
      map.invalidateSize();
    });
</script>
```

The example above opens at `zoom: 3`, which is the range `countries-110m`
supports. **If your map opens at zoom 5 or higher, this dataset is wrong** — the
viewport will sit inside one polygon and render as a blank fill. Go back to
**Match the dataset to your zoom** and load `countries-50m` (241 features),
`us-atlas@3.0.1/states-10m.json` + `objects.states`, or county geometry via
pattern 9.

**Resolution matters for small countries.** `countries-110m` carries 177
features and drops microstates — Singapore is simply not in it. If your data
includes small nations, load `countries-50m` instead, or the country will
silently disappear with no error.

**Joining data to geometry.** Countries and states join on `properties.name`,
using the dataset's exact spelling (`United States of America`, `South Korea`).
Counties are different: their only property is a bare, non-unique name, so join
on the feature `id` — the 5-digit FIPS **string**. Never parse it as a number or
you will strip the leading zero from every county in states 01–09.

## 2. Leaflet choropleth (region shading with Leaflet interactions)

Join your data on the verified `properties.name` field.

```javascript
const DATA = { 'California': 92, 'Texas': 78, 'New York': 71 };
const shade = v => v === undefined ? '#EFE9DD'
               : v > 80 ? '#7A2E12' : v > 60 ? '#B4532A'
               : v > 45 ? '#D97742' : '#F5D9C4';

fetch('https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-10m.json')
  .then(r => r.json())
  .then(topo => {
    const geo = topojson.feature(topo, topo.objects.states);
    const layer = L.geoJSON(geo, {
      style: f => ({ fillColor: shade(DATA[f.properties.name]),
                     fillOpacity: 0.95, color: '#FFFFFF', weight: 1 }),
      onEachFeature: (f, l) =>
          l.bindPopup(f.properties.name + ': ' +
                      (DATA[f.properties.name] ?? 'no data'))
    }).addTo(map);
    map.fitBounds(layer.getBounds(), { padding: [20, 20] });
  });
```

Always render a "no data" colour. State names must match exactly —
`properties.name` is the plain English name (`"California"`, not `"CA"`).

## 3. Dense polygons — use the canvas renderer

At county density (3231 polygons) the default SVG renderer becomes sluggish.
Switch to canvas:

```javascript
const map = L.map('map', { preferCanvas: true, renderer: L.canvas() });
// ...
L.geoJSON(counties, { renderer: L.canvas(), style: ... }).addTo(map);
```

Verified: 3231 counties + 56 state outlines render in ~430 ms. Draw the
`objects.states` outline on top for legibility. Note that canvas-rendered layers
are not individually inspectable in the DOM.

Join county data on `feature.id` (the 5-digit FIPS string), not on
`properties.name` — county names are not unique across states. Give counties
with no data an explicit neutral fill so a sparse dataset reads as "no data"
rather than as a rendering bug.

## 4. Plotly choropleth (least code for region shading)

Configure `topojsonURL` once so Plotly loads Natural Earth geometry from the
pinned jsDelivr package:

```javascript
Plotly.setPlotConfig({
  topojsonURL: 'https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/'
});
Plotly.newPlot('map', [{
  type: 'choropleth', locationmode: 'USA-states',
  locations: ['CA', 'TX', 'FL', 'NY'],
  z: [92, 78, 65, 71],
  colorscale: [[0, '#F5D9C4'], [1, '#7A2E12']],
  marker: { line: { color: '#FFFFFF', width: 1 } }
}], {
  geo: { scope: 'usa', bgcolor: '#FAF7F0',
         showlakes: true, lakecolor: '#CFE0EC' },
  margin: { t: 10, b: 10, l: 10, r: 10 }
}, { responsive: true, displayModeBar: false });
```

For world maps drop `locationmode` and pass ISO-3 codes in `locations`
(`locationmode: 'ISO-3'`).

> `scattermapbox`, `choroplethmapbox`, `densitymapbox`, `scattermap`,
> `choroplethmap`, and `densitymap` are BANNED (raster tiles). Use `scattergeo`
> and `choropleth`, which are pure vector.

## 5. Plotly scattergeo (routes, points, built-in projections)

```javascript
Plotly.setPlotConfig({
  topojsonURL: 'https://cdn.jsdelivr.net/npm/plotly.js@2.32.0/dist/topojson/'
});
Plotly.newPlot('map', [{
  type: 'scattergeo', mode: 'lines+markers',
  lat: [34.34, 39.63, 33.32], lon: [108.94, 66.98, 44.37],
  text: ['Chang\u2019an', 'Samarkand', 'Baghdad'],
  line: { width: 3, color: '#B4532A' },
  marker: { size: 8, color: '#D97742' }
}], {
  geo: { projection: { type: 'orthographic',
                       rotation: { lon: 70, lat: 30 } },
         showland: true, landcolor: '#EDE4D3',
         showocean: true, oceancolor: '#CFE0EC',
         showcountries: true, countrycolor: '#B9A98C' }
});
```

Useful `projection.type` values: `natural earth`, `orthographic` (globe),
`albers usa`, `mercator`.

## 6. D3 geoPath (custom projections & globes)

```javascript
const projection = d3.geoOrthographic()
    .scale(250).translate([w / 2, h / 2]).rotate([-70, -25]);
const path = d3.geoPath(projection);

svg.append('path').datum({ type: 'Sphere' })
   .attr('d', path).attr('fill', '#CFE0EC');
svg.append('path').datum(d3.geoGraticule10())
   .attr('d', path).attr('fill', 'none').attr('stroke', '#A9BFD0');

d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json')
  .then(topo => {
    const countries = topojson.feature(topo, topo.objects.countries);
    svg.append('g').selectAll('path').data(countries.features).join('path')
       .attr('d', path).attr('fill', '#EDE4D3').attr('stroke', '#B9A98C');
  });
```

> **Expected behaviour:** `geoOrthographic` clips the far hemisphere, so only
> ~144 of 177 countries produce path geometry at any rotation. That is correct,
> not a bug. A flat projection (`geoNaturalEarth1`) renders all 177. Never
> assert that every feature drew.

To rotate on scroll, update `projection.rotate([...])` and re-issue `.attr('d',
path)`.

## 7. ECharts registerMap

```javascript
fetch('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-110m.json')
  .then(r => r.json())
  .then(topo => {
    echarts.registerMap('world',
        topojson.feature(topo, topo.objects.countries));
    echarts.init(document.getElementById('map')).setOption({
      visualMap: { min: 0, max: 100,
                   inRange: { color: ['#F5D9C4', '#7A2E12'] } },
      series: [{ type: 'map', map: 'world', roam: true,
                 nameProperty: 'name',
                 data: [{ name: 'China', value: 92 }] }]
    });
  });
```

`nameProperty: 'name'` is required — it points ECharts at the `properties.name`
field these datasets use.

## 8. City & neighborhood scale — schematic, not fake streets

**No public-domain source has street geometry.** Natural Earth and us-atlas stop
at county level. For a walking tour or neighborhood map, do NOT pretend to draw
streets. Build an honest schematic: real coordinates, real relative distances,
no invented roads.

```javascript
const map = L.map('map', { center: [40.708, -74.008], zoom: 15,
                           scrollWheelZoom: false });
// Real lat/lng stops + walking route.
const route = L.polyline(stops.map(s => [s[1], s[2]]),
                         { color: '#B4532A', weight: 4,
                           dashArray: '8 5' }).addTo(map);
stops.forEach((s, i) => {
  // Distance ring conveys scale without a basemap.
  L.circle([s[1], s[2]], { radius: 120, color: '#D97742',
                           fillOpacity: 0.12 }).addTo(map);
  L.circleMarker([s[1], s[2]], { radius: 9, color: '#7A2E12',
      fillColor: '#F4EFE6', fillOpacity: 1, weight: 3 })
   .bindTooltip((i + 1) + '. ' + s[0]).addTo(map);
});
map.fitBounds(route.getBounds(), { padding: [40, 40] });
```

Give the container a paper-grid background so the space reads as deliberate
cartography rather than a failed map:

```css
#map {
  height: 520px; background-color: #F4EFE6;
  background-image:
    linear-gradient(rgba(122,46,18,.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(122,46,18,.08) 1px, transparent 1px);
  background-size: 40px 40px;
}
```

Add a scale bar or "≈400 m between stops" labels so distances stay legible.

--------------------------------------------------------------------------------

## 9. Regional & state scale (zoom 5–11)

The gap between a world map and a city schematic. A state-wide or metro-area
story — a gold rush, a rail network, a campaign trail — needs county geometry;
country outlines give you nothing at this zoom.

`counties-10m.json` carries both `objects.counties` (3231) and `objects.states`
(56), so one fetch covers both layers. Filter counties to the state in view: 58
polygons render fine in SVG and stay individually interactive, whereas all 3231
would need the canvas renderer from pattern 3.

```javascript
const CA = '06';  // State FIPS prefix of the county id.
const map = L.map('map', { center: [38.65, -121.1], zoom: 9,
                           scrollWheelZoom: false });

fetch('https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/counties-10m.json')
  .then(r => r.json())
  .then(topo => {
    const counties = topojson.feature(topo, topo.objects.counties);
    const states = topojson.feature(topo, topo.objects.states);

    // id is the 5-digit FIPS string; the first two digits are the state.
    const inState = {
      type: 'FeatureCollection',
      features: counties.features.filter(
          f => String(f.id).slice(0, 2) === CA)
    };

    L.geoJSON(inState, {
      style: { fillColor: '#EDE4D3', fillOpacity: 1,
               color: '#C9BCA4', weight: 0.7 }
    }).addTo(map);
    // State outline on top keeps the region legible.
    L.geoJSON(states, {
      style: { fill: false, color: '#9C8B6E', weight: 1.6 }
    }).addTo(map);
    map.invalidateSize();
  });
```

Verified at `zoom: 9` over Sacramento: 58 California counties, 15 polygons
visible in the opening viewport. The same view with `countries-110m` shows 1.

County lines are subtle by design — they should read as texture behind your
route and markers, not compete with them. Keep `weight` below 1 and the fill
close to the page background.

**If you style these layers with `className` + CSS rather than the inline
`style` object, the outline layer must declare `fill: none` in the CSS.** `fill:
false` only makes Leaflet write a `fill="none"` presentation attribute, and any
CSS `fill` declaration beats a presentation attribute. An outline layer carrying
an opaque fill sits on top of the county layer and hides every boundary you just
loaded — the geometry is all present in the DOM, nothing errors, and the map
still renders as a flat fill.

--------------------------------------------------------------------------------

## Rules for every map

1.  **Explicit height.** `min-height: 400px` or similar. A bare `flex-grow` or
    `h-full` measures 0px and the map renders blank.
2.  **Match the dataset to the zoom.** At zoom 6+, `countries-110m` renders as a
    blank fill. Confirm at least one border or coastline is inside the opening
    viewport.
3.  **Stacked layers: only the bottom one gets a fill.** When you draw an
    outline layer over a detail layer, the top layer needs `fill: false` in the
    Leaflet options *and* `fill: none` if you style it through CSS. An opaque
    top layer hides the detail layer completely and reports no error.
4.  **`map.invalidateSize()`** after the container becomes visible (tab switch,
    accordion open, resize) — otherwise Leaflet mis-measures.
5.  **`scrollWheelZoom: false`** in scroll-driven layouts to avoid scroll traps.
6.  **Attribute the data**: "Boundaries: Natural Earth (public domain)" or "US
    Census". Never emit "© OpenStreetMap" — the data is not OSM.
7.  **Contrast**: vector land/ocean fills are yours to choose, so tune them
    against the page background. Keep route and marker colours clearly distinct
    from the land fill.
8.  **Never invent geography.** Plot only coordinates present in or derivable
    from the source material.
