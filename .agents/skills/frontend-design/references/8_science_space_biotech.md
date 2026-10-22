# Science, Space & Biotech Design Reference

This guide covers design aesthetics, visual hierarchy, layout architecture, and
precision data presentation for scientific dashboards, aerospace telemetry,
laboratory instrumentation, genomics/biotech analyzers, and physical simulation
interfaces.

--------------------------------------------------------------------------------

## 1. Aesthetic DNA & Visual Tone

Scientific and aerospace interfaces must evoke **precision, calibration, and
empirical authority**.

-   **60-30-10 Theme & Palette Budget**:
    -   **60% Dominant Primary Background**: Clinical pristine white (`#FFFFFF`)
        / lab slate (`#F8FAFC`) or deep space obsidian (`#07090E` / `#0B0E17`).
    -   **30% Structural Panels & Grids**: Flat slate panels (`#F1F5F9` /
        `#111827`), hairline borders (`#E2E8F0` / `#1E293B`), coordinate axes.
    -   **10% Precision Telemetry Accents**: Single calibrated phosphor accent:
        laser cyan (`#06B6D4`), telemetry amber (`#F59E0B`), or cobalt
        (`#2563EB`).
-   **Surface Texture**: Monochromatic flat surfaces with crisp 1px hairline
    borders (`border border-slate-200 dark:border-slate-800`). Avoid heavy blur
    cards, thick gradients, or decorative drop shadows.
-   **Precision Atmosphere**: Dense information density with disciplined
    whitespace, high legibility, and technical geometry.

--------------------------------------------------------------------------------

## 2. Typographic System & Precision Notation

Scientific data demands exact alignment, unambiguous glyphs, and standardized
unit notation.

-   **Font Pairing**:
    -   **Interface & Labels**: Clean technical neo-grotesque or geometric
        sans-serif (`IBM Plex Sans`, `Plus Jakarta Sans`, `Epilogue`, `Chakra
        Petch`, `Public Sans`, `DM Sans`).
    -   **Data, Coordinates, Timestamps & Measurements**: Dedicated tabular
        monospace font (JetBrains Mono, IBM Plex Mono, Space Mono, or `font-mono
        tabular-nums`).
-   **Metric Formatting Rules**:
    -   **Tabular Numerals**: Always use `font-mono tabular-nums` for
        fluctuating numeric values to prevent layout jitter.
    -   **Unit Hierarchy**: Separate numeric values from units visually. Make
        the numeric value large and prominent (`text-2xl font-semibold`), while
        the unit is smaller and muted (`text-xs uppercase font-mono
        text-slate-400 ml-1.5`).
    -   **Standardized Notations**: Use accurate scientific symbols
        ($\mu\text{m}$, $\text{nm}$, $\text{GHz}$, $\text{mAh/g}$,
        $\text{mol/L}$, $^{\circ}\text{C}$, $\Delta v$, $\text{eV}$).
    -   **Significant Figures**: Display numbers with uniform decimal precision
        across columns (e.g. `98.420%`, `0.0034 nm`).

```
[ METRIC DISPLAY SPECIFICATION ]

+------------------------------------------------------+
| VOLUMETRIC COULOMBIC EFFICIENCY                      | <- text-xs tracking-wider uppercase text-slate-400
| 99.84 %                                              | <- text-3xl font-mono font-bold text-slate-900
| DELTA: +0.012 % / cycle                              | <- text-xs font-mono text-emerald-600
+------------------------------------------------------+
```

--------------------------------------------------------------------------------

## 3. Layout Architecture & Workspace Zones

Scientific tools typically require simultaneous parameter control and visual
inspection.

### Recommended Layout Pattern: Asymmetric Split Console

1.  **Top Telemetry Ribbon (36px - 44px)**:
    -   System state indicator (e.g., `MISSION ELAPSED TIME: T+04:12:09`,
        `SYSTEM STATUS: NOMINAL`, `SAMPLE RUN #1042-B`).
    -   Global calibration selector, active preset dropdown, and snapshot export
        button.
2.  **Left Control & Parameter Column (300px - 380px fixed width)**:
    -   Grouped collapsible parameter accordions.
    -   Stepper inputs, fine-grained slider rails with numeric readouts, toggle
        matrices, and variable boundary controls.
    -   Run / Trigger execution bar anchored at bottom.
3.  **Main Viewport / Canvas Stage (Flex-1 remaining width)**:
    -   High-fidelity visualization area (e.g., 2D/3D molecular structure,
        orbital trajectory canvas, spectrographic waterfall, particle
        simulation).
    -   Overlay HUD controls: Zoom/Pan reset, layer visibility toggles, axis
        coordinate overlays, and crosshair probes.
4.  **Bottom Time-Series & Telemetry Tray (200px - 280px)**:
    -   Multi-channel wave graphs, live error rate ribbons, or laboratory batch
        comparison tables.

--------------------------------------------------------------------------------

## 4. Scientific Data Visualizations & Chart Patterns

### Chart 1: Spider / Radar Parameter Calibration

-   Clean polygonal grid with 4–8 radial axes.
-   Subtle hairline grid polygons (`stroke-slate-300 dark:stroke-slate-700`).
-   Semi-transparent fill area (`fill-cyan-500/20 stroke-cyan-500 stroke-2`).
-   Axis vertex labels formatted in uppercase monospace with min/max bounds.

### Chart 2: Dual-Axis Efficiency & Decay Curves

-   Crisp SVG line charts with zero fill or subtle gradient fill below the
    primary curve.
-   Clear categorical line distinctions (e.g., Solid line for *Theoretical
    Model*, dashed line for *Empirical Trial*).
-   Interactive hairline crosshair tooltip that snaps to data points and
    displays exact $(x, y)$ coordinates in a compact monospace HUD.

### Chart 3: Genomic & Spectrographic Heatmaps

-   Discrete color-step ramps (e.g. Viridis, Coolwarm, or monochromatic
    Cyan-to-Amber scale).
-   Clear color legend with min, midpoint, and max values clearly annotated.
-   1px cell spacing for discrete matrix inspections.

--------------------------------------------------------------------------------

## 5. Micro-Interactions & State Indicators

-   **Status Indicators (Text-First, Non-Hue-Only)**: Report instrument state as
    an explicit text label with a glyph (`● Nominal`, `▲ Drifting`, `✖
    Critical`) colored by semantic tone (`text-emerald-600`, `text-amber-600`,
    `text-rose-600`). Do not add separate decorative dot elements or pulsing
    rings; a standalone dot is only justified when it tracks a live, changing
    stream state and sits directly beside its label.
-   **Parameter Scrubbers**: Fine-resolution sliders with subtle tick marks,
    double-click to manual-entry modal, and keyboard arrow step support.
-   **Crosshair Affordance**: Canvas viewports should switch cursor to
    `cursor-crosshair` with live coordinate floating labels in the corner.
