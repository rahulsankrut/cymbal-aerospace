# Education & Interactive Simulations Design Guidelines

This reference covers interactive educational sandboxes, conceptual learning
simulations, scientific process visualizers, math interactive models, and
rubric-based assessment interfaces.

--------------------------------------------------------------------------------

## 1. Scope & Taxonomy Coverage

-   **Biological & Chemical Process Simulations**:
    -   *The Bohr Effect / Hemoglobin Oxygen Affinity*: Red blood cell
        navigation, CO2/pH acid traps, oxygen dissociation curve visual shift,
        delivery phase animation.
    -   *Plant Vascular Systems (Xylem & Phloem)*: Direct-II canonical signal
        flow representation, water/mineral uptake, leaf feedback gain
        regulation.
-   **Mathematical & Statistical Visualizers**:
    -   *Ratio & Proportion Explorers*: Interactive comparative scaling bars,
        visual ingredient mixers, dual geometric scale sliders.
    -   *Probability Decision Trees*: Sampling with replacement visualization,
        branch expansion animations, outcome counter nodes.
-   **Conceptual Geometry & Architectural Exploration**:
    -   Interactive geometric object construction, progressive discovery stages
        from basic polygons to sacred geometry patterns.
-   **Interactive Hardware Assembly**:
    -   Motherboard layout explorer, front panel I/O connector guides,
        cable-to-header connection feedback.
-   **Automated Rubric Grading Tools**:
    -   Criteria matrices, level descriptors, automated score visual tallies,
        teacher feedback summaries.

--------------------------------------------------------------------------------

## 2. Visual Architecture & Layout Rules

### A. Two-Zone Sandbox Layout

Educational simulations benefit from a balanced split layout:

-   **Left / Top Zone (Interactive Stage)**: Large visual canvas or interactive
    diagram displaying the system in motion ($60\%\text{--}70\%$ of screen
    width/height).
-   **Right / Bottom Zone (Control & Concept Deck)**: Parameter sliders,
    step-by-step playback controls (Play, Pause, Step Forward, Reset), and
    real-time concept annotations.

### B. Progressive Disclosure & Guided Learning Stages

-   **Stage Progression**: Group concepts into progressive tiers (e.g. `Stage 1:
    The Resting State` $\to$ `Stage 2: High Activity / Sprint`).
-   **Interactive Affordances**: Sliders with clear tick marks, dual-state
    toggles, and step controllers with prominent active states.
-   **Visual Feedback on Action**: When a user drags a slider or plugs a cable
    into a motherboard socket, supply immediate visual confirmation (glowing
    socket outline, particle flow acceleration, or dual-coded color shift
    accompanied by explicit state text).

### C. Scientific Diagram & Flow Clarity

-   **Flow Visualizations (Signals / Fluids / Molecules)**: Use smooth
    directional flow arrows, moving particle pulses along pathways, and labeled
    summation nodes.
-   **Mathematical Curves**: Display live coordinate axes with high-contrast
    curve lines, clearly marked data points, and labeled equilibrium markers
    (e.g. $Hb(O_2)_4 + H^+ \rightleftharpoons HbH^+ + 4O_2$).

--------------------------------------------------------------------------------

## 3. Typography & Color Strategies

-   **Typography**: Clean, friendly, and highly legible pairings — pair `Plus
    Jakarta Sans`, `Outfit`, or `Bricolage Grotesque` (or `Fraunces` for
    humanities) for distinctive display titles (22px–28px SemiBold) with `Plus
    Jakarta Sans` or `DM Sans` for body text. Never default to generic Inter.
    Formulas and variables must be rendered in italicized math serif or
    monospace (`KaTeX` style math font, `IBM Plex Mono`).
-   **60-30-10 Educational Color Budget**:
    -   **60% Dominant Canvas / Stage**: Soft clean off-white (`#F8FAFC`) or
        deep slate (`#0F172A`).
    -   **30% Structural Panels & Axes**: Hairline container borders (`#E2E8F0`
        / `#1E293B`), neutral white/slate card backdrops, axis coordinate grids.
    -   **10% Semantic Focal Accents**:
    -   Oxygenated / Nominal: Vibrant Azure (`#0284C7`) or Emerald (`#059669`)
        with `● NOMINAL` text label.
    -   Acidic / High CO2 / High Load: Coral Red (`#DC2626`) or Amber
        (`#D97706`) with `▲ ELEVATED` text label.
    -   Phloem / Sugar Transport: Golden Marigold (`#EAB308`)
    -   Xylem / Water Transport: Cerulean Blue (`#0EA5E9`)

--------------------------------------------------------------------------------

## 4. `generate_image` Recipes for Educational Concepts

```typescript
// 1. Biological Science Diagram Background
generate_image({
  Prompt: "Scientific illustration of plant cellular structure showing xylem and phloem vessels with water molecules, clean educational textbook style, vibrant natural green and cyan lighting, high resolution.",
  ImageName: "diagram_plant_vascular_system",
  AspectRatio: "16:9"
});

// 2. Geometry Learning Header Visual
generate_image({
  Prompt: "Elegant geometric composition of the Golden Ratio spiral and overlapping geometric platonic solids, gold metallic linework on dark slate blueprint texture, architectural aesthetic.",
  ImageName: "hero_sacred_geometry",
  AspectRatio: "16:9"
});

// 3. Motherboard Component Graphic
generate_image({
  Prompt: "Clean top-down technical illustration of a modern computer motherboard showing labeled PCIe slots, RAM channels, and front panel I/O headers, crisp vector blueprint art style.",
  ImageName: "diagram_motherboard_layout",
  AspectRatio: "4:3"
});
```

--------------------------------------------------------------------------------

## 5. Anti-Patterns to Avoid

-   ❌ **No Wall-of-Text Explanations**: Avoid dumping long textbook paragraphs
    above the interactive canvas; use bite-sized contextual callouts tied
    directly to user interaction.
-   ❌ **No Unlabeled Sliders**: Every control slider must feature a visible
    label, current numeric value, and unit of measurement (e.g., `pH Level:
    7.2`).
-   ❌ **No Non-Interactive Static Diagrams**: Educational models must respond
    dynamically to user manipulation; never leave a static placeholder image in
    place of an interactive simulation.
-   ❌ **No Hue-Only State Signaling**: Never use red/green color alone to
    communicate nominal vs error states; always include explicit icon glyphs and
    text labels.
