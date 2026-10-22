# Menu

1.  [ID: menu_usage] Is the menu used for contextual options, overflow actions,
    or dropdown selection? [Metric type: Hygiene] [Weight: 3]

2.  [ID: menu_items_single_line] Are menu items presented on a single line
    without wrapping? [Metric type: Hygiene] [Weight: 3]

3.  [ID: menu_drop_shadow_elevation] Does the menu container utilize a drop
    shadow (or M3 tonal surface elevation; mark "N/A" if dark mode or a dark
    background obscures shadow visibility) to elevate over underlying content?
    [Metric type: Hygiene] [Weight: 3]

4.  [ID: ios_native_menus_actionsheets_usage] In this iOS application, if menus
    or contextual action options are triggered, are they rendered using Apple
    native context menus (UIContextMenuInteraction) or Action Sheets
    (UIAlertController actionSheet style) rather than custom Android/Web-style
    Material menus? (Pass with "Yes" if correctly using Apple native context
    menus or action sheets without penalizing for missing Material styling; fail
    with "No" if incorrectly using Material surface container menus on iOS; mark
    as "N/A" if absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
