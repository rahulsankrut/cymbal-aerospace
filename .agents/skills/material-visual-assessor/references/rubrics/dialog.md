# Dialog

1.  [ID: dialog_container_rounded_corners] Do dialog containers have generously
    rounded corners? [Metric type: Hygiene] [Weight: 3]

2.  [ID: dialog_scrim_backdrop] Do dialogs utilize a scrim to block interaction
    with underlying content? [Metric type: Hygiene] [Weight: 5]

3.  [ID: dialog_max_two_buttons] Does the dialog contain at most two action
    buttons aligned to the trailing edge? [Metric type: Hygiene] [Weight: 3]

4.  [ID: dialog_drop_shadow_elevation] Do dialogs utilize a drop shadow (or M3
    tonal surface elevation; mark "N/A" if dark mode or a dark scrim obscures
    shadow visibility) to elevate over background content? [Metric type:
    Hygiene] [Weight: 3]

5.  [ID: ios_lg_dialog_glass_adherence] On iOS, if a Dialog modal container is
    present on the functional layer, does it feature the translucent Liquid
    Glass / Material Glass effect over the backdrop/scrim? (Pass with "Yes" if
    the dialog container exhibits translucent backdrop blur while preserving
    content legibility; fail with "No" if using a flat opaque surface fill; mark
    as "N/A" if absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
