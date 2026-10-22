# Search

1.  [ID: search_container_rounded_corners] If a Search Bar container is present,
    does it comply with the specification: container height of 56dp and a fully
    rounded pill corner radius of 28dp (sys.shape.corner.full /
    md.sys.shape.corner.full)? [Metric type: Hygiene] [Weight: 10]

2.  [ID: search_hint_text_contains_search] If an empty/unfocused search bar is
    present, does the search container contain clear hint text that includes the
    word "Search"? [Metric type: Hygiene] [Weight: 3]

3.  [ID: search_max_two_trailing_icons] Does the search container contain at
    most 2 trailing icon buttons? [Metric type: Hygiene] [Weight: 3]

4.  [ID: search_clear_icon_button] If query text is entered inside the search
    bar, does a clear text "x" icon button display trailing the text? [Metric
    type: Hygiene] [Weight: 3]

5.  [ID: ios_lg_search_layer_adherence] On iOS, for Search or Search Bar
    controls, does the component enable the Liquid Glass variant when placed on
    the Functional Layer (floating over content or docked) and default to
    Non-Glass when embedded on the Content Layer? (Pass with "Yes" if layer
    placement matches the variant; fail with "No" if mismatched; mark as "N/A"
    if absent or non-iOS.) [Metric type: Adherence] [Weight: 5]
