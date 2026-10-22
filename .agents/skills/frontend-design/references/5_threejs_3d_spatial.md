# 3D Graphics & Spatial Applications Design Guidelines

This reference covers 3D viewports, Three.js / WebGL scenes, 3D games (e.g. 3D
car racing, first-person 3D snake), interactive 3D product visualizers, and
spatial geometry models.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **3D Racing & Vehicular Games**: Third-person chase cam, cockpit
    first-person view, dynamic track environments (city, highway, desert, night
    mode), motion blur visual effects, speedometer and tachometer HUDs.
-   **First-Person 3D Games**: E.g. *3D Snake*, labyrinth/maze navigation,
    smooth camera look-around, food item collectibles, snake body follow-curves,
    clear score HUD.
-   **Interactive 3D Product & Geometry Viewports**: 360-degree object
    inspection, orbit controls, material finish switchers (matte, metallic,
    frosted glass), dimensional exploded views.
-   **Spatial Concept Visualizations**: Biological/chemical molecular
    structures, planetary orbits, architectural wireframes.

--------------------------------------------------------------------------------

## 2. Visual Architecture & Viewport Composition

### A. Viewport Composition & Semantic Layering

-   **Full Viewport Immersion**: 3D canvases must fill their intended container
    or the entire viewport (`w-full h-full`) without creating scrollbars or
    awkward borders.
-   **Semantic DOM Overlay Architecture**: Essential headings, labels,
    navigation, and actions must live as semantic, selectable DOM text elements
    layered over the canvas (`z-10 pointer-events-auto`). Never render core UI
    copy directly into canvas pixels.
-   **HUD & UI Layering**: Position 2D UI overlays (Score, Lap times, Speed,
    Controls help) in a clean floating HUD with subtle dark frosted backing
    (`bg-black/40 backdrop-blur-sm border border-white/10`) and crisp white
    typography. Never let HUD elements obstruct the primary visual focus of the
    3D scene.
-   **WebGL Context & Fallback Safety**: Attach `webglcontextlost` and
    `webglcontextrestored` event listeners on the canvas element. Provide a
    graceful static image or 2D preview container if WebGL is unavailable or
    when reduced motion is preferred.

### B. Lighting, Materials & Atmosphere

-   **Three-Point Studio Lighting**: For product viewers and educational
    objects, combine a Key Light (directional, warm-tinted), Fill Light (soft
    ambient, cool-tinted), and Rim Light (sharp highlight from behind to
    separate the object from the background).
-   **Atmospheric Depth**: Use subtle exponential fog (`scene.fog`) matching the
    background color to create natural distance falloff in open 3D worlds
    (racing tracks, endless fields).
-   **Surface Material Realism**: Prefer physically-based materials
    (`MeshStandardMaterial` or `MeshPhysicalMaterial`) with calibrated roughness
    and metalness values rather than flat, unlit solid colors.

### C. Camera Choreography & Visual Feedback

-   **Smooth Interpolation**: Avoid abrupt camera snaps. Use smooth
    damping/lerping on camera position and target tracking for third-person
    vehicle following.
-   **Visual Impact & Speed Cues**: For high-speed racing or movement, introduce
    subtle field-of-view (FOV) widening during acceleration, dynamic camera tilt
    during sharp turns, and particle trails for collectibles.

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Futuristic & High-Speed Games (Racing / Sci-Fi)**: Monospace or angular
    geometric sans headers (`Chakra Petch`, `Orbitron`, `Oxanium`) for
    speedometers and lap times, paired with `Plus Jakarta Sans` for HUD
    controls. Deep obsidian surfaces with sharp neon accents (amber orange
    `#F59E0B`, electric cyan `#06B6D4`, racing red `#EF4444`).
-   **Product Viewers & Architectural Geometry**: Minimalist neutral palette
    (slate, off-white, platinum gray) paired with clean geometric sans (`Public
    Sans`, `Plus Jakarta Sans`, `DM Sans`, `Outfit`) that allows the 3D object's
    textures and materials to take center stage.
-   **Retro / Segmented Display Themes**: 1980s red segmented LED numerals
    (`#EF4444`) on dark brushed metal casings.

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for 3D Backgrounds & Skyboxes

```typescript
// 1. 3D Racing Environment Skybox / Background
generate_image({
  Prompt: "Cinematic night cityscape panorama with neon architectural horizon reflections on wet asphalt road, modern cyberpunk aesthetic, 16:9 panoramic background.",
  ImageName: "skybox_night_city_racing",
  AspectRatio: "16:9"
});

// 2. Desert Racing Track Backdrop
generate_image({
  Prompt: "Expansive desert highway landscape at sunset with dramatic sandstone canyons and golden hour rim lighting, clean horizon line, photorealistic scenery.",
  ImageName: "skybox_desert_highway",
  AspectRatio: "16:9"
});

// 3. Futuristic Vehicle Garage Texture
generate_image({
  Prompt: "Ultra-modern minimalist automotive showroom interior with polished concrete floor, geometric overhead LED strip lighting, high-end vehicle showcase pavilion.",
  ImageName: "bg_automotive_garage",
  AspectRatio: "16:9"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Blown-Out Lighting**: Avoid setting directional lights to excessive
    intensities that wash out object details and create harsh solid-white glare.
-   ❌ **No Obtrusive Controls Overlays**: Keep control instruction banners
    subtle (e.g., small bottom helper bar or discreet corner icon with tooltip);
    do not block the player's line of sight.
-   ❌ **No Unstyled Fallback Void**: If 3D rendering is initializing or
    suspended, provide a polished loading backdrop or styled placeholder graphic
    rather than a raw black void.
