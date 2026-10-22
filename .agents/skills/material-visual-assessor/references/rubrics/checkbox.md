# Checkbox

1.  [ID: checkbox_usage] Are checkboxes used for multi-select options or toggles
    requiring a "Submit" step? [Metric type: Hygiene] [Weight: 3]

2.  [ID: checkbox_square_corner_radius] Are checkboxes shaped as squares with
    slightly rounded corners? (On iOS, if an app correctly uses native Apple
    selection controls/checkmarks rather than a square Material checkbox, mark
    as "N/A" for this Material-specific shape rule; if an iOS app incorrectly
    implements a custom Material square checkbox, evaluate under
    ios_native_checkbox_usage.) [Metric type: Hygiene] [Weight: 3]

3.  [ID: checkbox_checkmark_visibility] Is the checkmark icon only visible when
    the checkbox is in the selected or indeterminate state? [Metric type:
    Hygiene] [Weight: 3]

4.  [ID: checkbox_no_drop_shadow] Does the checkbox component stay flat without
    using drop shadows? [Metric type: Hygiene] [Weight: 3]

#### iOS Platform & Liquid Glass Adherence

1.  [ID: ios_native_checkbox_usage] In this iOS application, if a checkbox or
    multi-selection control is present, is it implemented using Apple native
    list checkmarks/selection controls (e.g., UITableViewCell.accessoryType =
    .checkmark or native SwiftUI List selection) rather than an Android/Web
    Material Design checkbox? (Pass with "Yes" if correctly using native Apple
    controls without penalizing for missing Material styling; fail with "No" if
    incorrectly using a Material checkbox on iOS; mark as "N/A" if absent or
    non-iOS.) [Metric type: Adherence] [Weight: 10]
