# FABs

> **FAB & FAB Menu Presence Gate (`IF/THEN/ELSE`)**:
>
> *   **Zero FABs Present (`all_fabs_only_one`)**: `IF` the screen contains
>     **zero** Floating Action Buttons (neither a Standard FAB nor an Extended
>     FAB exists), `THEN` all FAB questions—including `all_fabs_only_one`—`MUST`
>     be answered **`"N/A"`** (`MUST NOT` answer `"Yes"` or `"No"`).
> *   **Collapsed Extended FAB vs. Expanded FAB Menu (`fab_menu_*`)**: `IF` the
>     screen displays a single collapsed floating button (such as a `"Compose"`
>     Extended FAB) without an expanded speed-dial list of 2–6 related floating
>     action buttons above a circular `'x'` close trigger, `THEN` no **FAB
>     Menu** is present and all `fab_menu_*` questions (`fab_menu_circle`,
>     `fab_menu_to_actions`, `fab_menu_only_x_icon`) `MUST` be answered
>     **`"N/A"`**.

#### General

1.  [ID: all_fabs_only_one] If at least one Floating Action Button is present on
    the screen, does the active screen or viewport hierarchy contain at most ONE
    Floating Action Button component (FloatingActionButton or
    ExtendedFloatingActionButton)? (Mark as N/A if zero FABs are present on the
    screen.) [Metric type: Hygiene] [Weight: 10]

2.  [ID: all_fabs_on_top] Does the FAB appear to be on top of all other UI
    elements? [Metric type: Hygiene] [Weight: 5]

3.  [ID: all_fabs_prominent] If there are other actions on the screen, does the
    FAB appear more visually prominent than those actions (e.g., through its
    size, elevation, or use of the primary color)? [Metric type: Hygiene]
    [Weight: 5]

4.  [ID: all_fabs_location] Is the FAB positioned according to window size
    class: anchored at bottom-trailing with a 16dp margin from screen edges in
    compact/medium portrait views, or docked within the top slot of the
    Navigation Rail in expanded/desktop views? [Metric type: Hygiene] [Weight:
    10]

5.  [ID: all_fabs_drop_shadow] Does the FAB present use a drop shadow to create
    additional protection against a background? Note: If dark mode or a
    high-contrast background makes the presence of a shadow ambiguous or
    impossible to distinguish, mark this question as N/A. [Metric type: Hygiene]
    [Weight: 3]

#### Standard FAB

1.  [ID: standard_fab_square_rounded] If a standard FAB is present, does its
    container comply with the specification: size 56x56dp (or 40x40dp for Small
    FAB, 96x96dp for Large FAB) with a corner radius of 16dp
    (sys.shape.corner.large / 8dp for Small FAB / 28dp for Large FAB)? [Metric
    type: Adherence] [Weight: 10]

2.  [ID: standard_fab_filled_icon] If a standard FAB is present, does it feature
    ONLY a filled icon? [Metric type: Hygiene] [Weight: 3]

3.  [ID: ios_lg_fab_glass_adherence] On iOS, if a Floating Action Button
    (Standard FAB, Extended FAB, or FAB Menu) is present on the functional
    layer, is the translucent Liquid Glass / Material Glass effect applied?
    (Pass with "Yes" if the FAB container exhibits translucent blur and specular
    edge highlights over background content; fail with "No" if using a flat
    opaque color fill; mark as "N/A" if absent or non-iOS.) [Metric type:
    Adherence] [Weight: 10]

#### FAB Menu

1.  [ID: fab_menu_circle] If an expanded FAB menu is present, is the trigger FAB
    menu button a circle? (Mark as N/A if only a single collapsed Standard or
    Extended FAB is present.) [Metric type: Hygiene] [Weight: 3]

2.  [ID: fab_menu_to_actions] If an expanded FAB menu is present, does it show
    2-6 related actions floating above in separate containers? (Mark as N/A if
    only a single collapsed Standard or Extended FAB is present.) [Metric type:
    Hygiene] [Weight: 3]

3.  [ID: fab_menu_only_x_icon] If an expanded FAB menu is present, does the
    trigger FAB feature ONLY an “x” close icon? (Mark as N/A if only a single
    collapsed Standard or Extended FAB is present.) [Metric type: Hygiene]
    [Weight: 3]

4.  [ID: ios_lg_fab_menu_glass_adherence] On iOS, if an expanded FAB Menu is
    present, do the floating action menu containers and trigger button feature
    the translucent Liquid Glass effect? [Metric type: Adherence] [Weight: 10]

#### Extended FAB

1.  [ID: extended_fab_rectangle_rounded] If an Extended FAB is present, does its
    container comply with the specification: height 56dp (or 80dp for Large
    Extended FAB), with a corner radius of 16dp (sys.shape.corner.large) or
    fully rounded pill 28dp (sys.shape.corner.full), and 16dp start/end internal
    padding? [Metric type: Adherence] [Weight: 10]

2.  [ID: extended_fab_text_label] If an Extended FAB is present, does it have a
    text label? [Metric type: Hygiene] [Weight: 1]

3.  [ID: extended_fab_icon_left] If the extended FAB includes an icon, is the
    icon placed to the left of the text? [Metric type: Hygiene] [Weight: 1]

4.  [ID: extended_fab_filled_icon] If the extended FAB includes an icon, does it
    use the filled icon style? (If an Extended FAB uses an outlined/hollow icon
    glyph rather than a solid filled icon, evaluate as `"No"`.) [Metric type:
    Hygiene] [Weight: 3]
