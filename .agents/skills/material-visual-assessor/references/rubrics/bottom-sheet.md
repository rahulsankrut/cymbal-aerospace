# Bottom Sheet

1.  [ID: bottom_sheet_top_corners_rounded] If a standard or modal bottom sheet
    container is present, do its top-left and top-right corners comply with the
    specification: corner radius of 28dp (sys.shape.corner.extra-large-top /
    md.sys.shape.corner.extra-large.top) with 0dp bottom corners? [Metric type:
    Hygiene] [Weight: 10]

2.  [ID: bottom_sheet_higher_surface_color] If the page background and bottom
    sheet are both visible (i.e. no modal scrim), does the bottom sheet appear
    to use a higher surface color role (visibly darker than `#FFFFFF` in light
    mode, lighter in dark mode) than the background? (In Light Mode, if a bottom
    sheet such as the `"Ask Gemini"` sheet uses pure white `#FFFFFF` matching
    the `#FFFFFF` main background—relying only on a drop shadow rather than a
    darker `surface-container` tone—evaluate as `"No"`; mark as N/A if the
    background is a full-bleed photo, image, map, or canvas.) [Metric type:
    Hygiene] [Weight: 3]

3.  [ID: bottom_sheet_drag_handle] Is there a drag handle present on the bottom
    sheet? (If a bottom sheet container such as the `"Ask Gemini"` bottom input
    sheet is present without a drag handle pill, evaluate as `"No"`, NOT
    `"N/A"`; mark as N/A only if no bottom sheet exists on screen.) [Metric
    type: Hygiene] [Weight: 3]

4.  [ID: bottom_sheet_drag_handle_top_middle] Is the drag handle placed in the
    top-middle of the sheet? (Evaluate as `"No"` if a bottom sheet is present
    without a top-middle drag handle; mark as N/A only if no bottom sheet exists
    on screen.) [Metric type: Hygiene] [Weight: 3]

5.  [ID: bottom_sheet_visible_margins] If the UI is mobile landscape or larger
    window size than mobile, are there clearly visible margins around the bottom
    sheet (left, right, and top)? The bottom sheet should not appear to be
    touching those screen edges. [Metric type: Hygiene] [Weight: 3]

6.  [ID: ios_lg_bottom_sheet_glass_adherence] On iOS, if a Bottom Sheet
    container is present on the functional layer, does it feature the
    translucent Liquid Glass / Material Glass effect? (Pass with "Yes" if the
    sheet exhibits translucent blur while maintaining foreground legibility;
    fail with "No" if using a flat opaque surface container fill; mark as "N/A"
    if absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
