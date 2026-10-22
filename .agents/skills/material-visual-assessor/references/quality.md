<!-- disableFinding(LINE_OVER_80) -->

# Quality

> **Quality & State Modality Evaluation Rule:**
>
> *   **Visual-Only Mode (Static Screenshot)**: `IF` evaluating a static
>     screenshot, `THEN` the agent `MUST` evaluate visible layout, spacing
>     rhythm, typography wrapping, and visible component states (`"Yes"` or
>     `"No"`), and `MUST` mark criteria tagged `[Requires Code Inspection]` or
>     targeting transient/interactive states absent from the viewport (e.g.,
>     keyboard focus rings, empty states, skeleton loaders, error alerts,
>     scrolled headers, or mobile OS system bars) as `"N/A"`.
> *   **Code-Only / Hybrid Mode**: `IF` evaluating source code or a hybrid
>     bundle, `THEN` the agent `MUST` inspect CSS media queries
>     (`prefers-color-scheme`, `prefers-reduced-motion`), semantic attributes
>     (`aria-label`, `type`), `:focus-visible` focus styles, and state/scroll
>     declarations directly from code (`"Yes"` or `"No"`, or `"N/A"` if the
>     target feature does not exist in the application).

1.  [ID: quality_color_theme_consistency] Does the UI maintain consistent tonal
    theme roles across all surfaces without mixing mismatched light and dark
    container surfaces in the same view? [Metric type: Adherence] [Weight: 5]

2.  [ID: quality_color_prefers_color_scheme] Does styling configure display
    theme preferences using media queries (e.g., `@media (prefers-color-scheme:
    dark)`) or semantic platform theme tokens? [Requires Code Inspection]
    [Metric type: Adherence] [Weight: 3]

3.  [ID: quality_typography_no_clipping_wrapping] Are all text labels, headings,
    and navigation titles fully visible without unexpected line clipping,
    awkward mid-word breaks, or truncation ellipsis? [Metric type: Hygiene]
    [Weight: 5]

4.  [ID: quality_grid_spacing_8dp_alignment] Do layout margins, container
    padding, and spacing gaps between adjacent elements align to a visible 4dp /
    8dp (4px / 8px) incremental spatial grid rhythm? [Metric type: Hygiene]
    [Weight: 3]

5.  [ID: quality_edge_margins_page_boundaries] Do primary content containers and
    cards maintain visible breathing margins from the screen boundaries rather
    than flush colliding against viewport edges? [Metric type: Hygiene] [Weight:
    3]

6.  [ID: quality_shape_nested_corner_proportionality] If rounded containers
    contain nested child elements (such as inner cards or buttons), do the inner
    corner radii appear proportionally smaller than outer corners? [Metric type:
    Hygiene] [Weight: 3]

7.  [ID: quality_shape_continuous_corner_radii] On iOS or Material card
    containers, do container corners appear smoothly and continuously rounded
    (pill, squircle, or standard system radii) rather than sharp or unstyled?
    [Metric type: Adherence] [Weight: 3]

8.  [ID: quality_elevation_backdrop_blur] If translucent floating bars, glass
    sheets, or vibrancy overlays sit over scrollable content (such as Liquid
    Glass on iOS or Material Glass overlays), does the overlay feature a
    translucent blur/vibrancy treatment while ensuring all foreground text
    labels and icons maintain clear legibility and contrast (>= 4.5:1) over
    underlying content? [Metric type: Adherence] [Weight: 5]

9.  [ID: quality_interactive_focus_ring_visible] If a control is focused via
    keyboard/D-pad navigation (or when inspecting `:focus-visible` focus styles
    in code), is a high-contrast focus indicator ring clearly defined and
    visible without obstruction? (Mark `"N/A"` in Visual-Only mode if no control
    is in a focused state). [Metric type: Hygiene] [Weight: 5]

10. [ID: quality_states_empty_actionable_cta] If an empty or zero-data state is
    shown, does the view feature clear explanatory copy accompanied by at least
    one prominent, actionable CTA button? [Metric type: Hygiene] [Weight: 3]

11. [ID: quality_loading_skeleton_dimensions] If skeleton loading cards are
    visible, do their placeholder shapes and container heights match the
    proportions of the actual content cards being loaded? [Metric type: Hygiene]
    [Weight: 3]

12. [ID: quality_accessibility_screen_reader_labels] Do standalone icon buttons,
    custom controls, and images contain explicit semantic labels (e.g.,
    `contentDescription`, `accessibilityLabel`, or `aria-label`)? [Requires Code
    Inspection] [Metric type: Adherence] [Weight: 5]

13. [ID: quality_accessibility_prefers_reduced_motion] Are motion transitions
    configured with reduced-motion queries (e.g., `@media
    (prefers-reduced-motion: reduce)`) or platform accessibility checks?
    [Requires Code Inspection] [Metric type: Adherence] [Weight: 5]

14. [ID: quality_aurora_spark_icon_brand_tint] If AI assistance or generative
    features are present, are they signaled with the standardized Material
    Symbols spark indicator icon with appropriate brand color tint? [Metric
    type: Adherence] [Weight: 3]

15. [ID: quality_aurora_streaming_text_container] When AI streaming text output
    is displayed, is the generated content contained within a dedicated bounding
    card or bubble that preserves layout structure? [Metric type: Hygiene]
    [Weight: 3]

16. [ID: quality_writing_no_conversational_fluff] Does UI instructional text
    avoid conversational filler words ('please', 'sorry', 'thank you') and
    first-person corporate pronouns ('I', 'we')? [Metric type: Hygiene] [Weight:
    1]

17. [ID: quality_writing_actionable_error_messages] If error messages or
    validation alerts are present, do they explicitly state what problem
    occurred and provide a clear recovery action? [Metric type: Hygiene]
    [Weight: 3]

18. [ID: quality_writing_button_cta_verb_length] Do action button CTAs begin
    with an active verb and contain at most 3 words (e.g., 'Save draft',
    'Confirm order', 'Get started')? [Metric type: Hygiene] [Weight: 1]

19. [ID: quality_writing_platform_native_verbs] If instructional interaction
    copy (e.g., 'Tap', 'Click', 'Press') is present, does it adhere to
    platform-native interaction vocabulary (e.g., 'Tap' on iOS/mobile touch vs.
    'Click' or 'Press' on Web/Desktop)? [Metric type: Adherence] [Weight: 1]

20. [ID: quality_forms_static_field_labels] Do form text fields maintain visible
    static labels or permanent container helper text rather than relying solely
    on disappearing placeholder prompts? [Metric type: Hygiene] [Weight: 3]

21. [ID: quality_forms_native_input_types] Are input fields configured with
    appropriate semantic types (e.g., `type="email"`, `keyboardType="numeric"`)
    to invoke the correct input keypad? [Requires Code Inspection] [Metric type:
    Adherence] [Weight: 3]

22. [ID: quality_wayfinding_persistent_search_bar] On search-centric views, is a
    static, discoverable search bar anchored prominently at the top of the
    content area? [Metric type: Hygiene] [Weight: 5]

23. [ID: quality_adaptive_window_size_classes] Does navigation match the window
    size class: bottom navigation bar on compact mobile portrait views, or
    navigation rail / drawer on expanded desktop views? [Metric type: Adherence]
    [Weight: 10]

24. [ID: quality_adaptive_hinge_foldable_avoidance] If a foldable or dual-screen
    device layout is displayed, are critical interactive controls, dialogs, and
    text columns positioned safely away from the physical center hinge fold?
    [Metric type: Adherence] [Weight: 5]

25. [ID: quality_adaptive_horizontal_overflow_scroll] Does body text and primary
    list content fit within the viewport width without triggering unintended
    horizontal scrollbars? [Metric type: Hygiene] [Weight: 5]

26. [ID: quality_canvas_edge_to_edge_system_bars] If mobile system status or
    gesture navigation bars are visible in the viewport, does the primary
    application surface render full-bleed behind transparent or translucent
    system bars without artificial opaque letterboxing? [Metric type: Adherence]
    [Weight: 5]

27. [ID: quality_scroll_lift_on_scroll_headers] If content is scrolled under a
    top app bar (or lift-on-scroll behavior is defined in code), does the bar
    display an elevated tonal color, subtle divider/shadow, or blur to visually
    separate the header from scrolling content? [Metric type: Adherence]
    [Weight: 3]

28. [ID: quality_scaffolds_canonical_expressive_layouts] For tablet or desktop
    screen widths, does the view implement a recognized canonical multi-pane
    scaffold (List-Detail, Supporting Pane, or Feed)? [Metric type: Adherence]
    [Weight: 5]
