# Navigation Bars

> **Navigation Bar Presence Gate (`IF/THEN/ELSE`)**:
>
> *   `IF` no bottom **Navigation bar** component (3 to 5 persistent top-level
>     destinations docked at the bottom of the viewport) exists on the screen
>     (for example, a map canvas overlaid by a Bottom Sheet with action buttons
>     and secondary `Tabs` such as `"Overview"`), `THEN` **all** Navigation bar
>     questions below—including implicit prompts like *"Is the active item
>     indicated with a filled pill-shaped container?"* (`nav_bars_active_pill`)
>     and `nav_bars_label_present`—`MUST` be answered **`"N/A"`** (`MUST NOT`
>     evaluate secondary `Tabs` or Bottom Sheet buttons as Navigation Bar
>     items).

1.  [ID: nav_bars_bottom_location] If a “Navigation bar” component is present,
    is it located at the very bottom of the screen? (Mark as N/A if no
    Navigation bar is present.) [Metric type: Adherence] [Weight: 3]

2.  [ID: nav_bars_active_pill] If a Navigation Bar is present (including when
    asked *"Is the active item indicated with a filled pill-shaped
    container?"*), does the active destination indicator comply with the
    specification: height 32dp, width 64dp, corner radius 16dp / pill
    (sys.shape.corner.full), filled with sys.color.secondary-container?
    (Evaluate as `"No"` if a bottom Navigation Bar highlights the active icon
    without a filled pill-shaped container; mark as `"N/A"` if no bottom
    Navigation Bar exists on screen.) [Metric type: Adherence] [Weight: 10]

3.  [ID: nav_bars_to_items] If a Navigation bar is present, are there between
    3-5 items in the navigation bar? (Mark as N/A if no Navigation bar is
    present.) [Metric type: Adherence] [Weight: 3]

4.  [ID: nav_bars_label_present] If a Navigation bar is present, is there a
    label present for each navigation icon? (Mark as N/A if no Navigation bar is
    present.) [Metric type: Adherence] [Weight: 3]

5.  [ID: nav_bars_label_below_icon] If a Navigation bar is present and the
    viewport uses a compact window size (e.g., mobile portrait), is there a
    label placed below the icon? (Mark as N/A if no Navigation bar is present.)
    [Metric type: Hygiene] [Weight: 3]

6.  [ID: nav_bars_label_trailing] If a Navigation bar is present and the
    viewport uses a medium or larger window size (e.g., tablet/desktop), is the
    label placed trailing the icon (right of the icon in LTR languages)? (Mark
    as N/A if no Navigation bar is present.) [Metric type: Adherence] [Weight:
    3]

7.  [ID: ios_lg_navbar_glass_adherence] On iOS, if a docked bottom Navigation
    Bar is present on the functional layer, does it feature the translucent
    Liquid Glass / Material Glass effect? (Pass with "Yes" if the navigation bar
    exhibits backdrop blur and translucency where content passes legibly
    underneath; fail with "No" if using a solid opaque fill; mark as "N/A" if
    absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
