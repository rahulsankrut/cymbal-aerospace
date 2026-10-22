# Date Picker

1.  [ID: date_picker_purpose] Is the date picker presented as a calendar grid or
    direct text entry? [Metric type: Hygiene] [Weight: 3]

2.  [ID: date_picker_modal_corner_radius] Do modal date pickers use a rounded
    rectangle container with generously rounded corners? [Metric type: Hygiene]
    [Weight: 3]

3.  [ID: date_picker_keyboard_toggle_icon] Does the component provide an edit
    icon to switch to direct text input? [Metric type: Hygiene] [Weight: 3]

4.  [ID: date_picker_selected_day_circle] Is the selected day indicator
    represented as a solid filled circle? [Metric type: Hygiene] [Weight: 3]

#### iOS Platform & Liquid Glass Adherence

1.  [ID: ios_native_date_picker_usage] In this iOS application, if a date picker
    is present, is it implemented using Apple native UIDatePicker / SwiftUI
    DatePicker rather than an Android/Web Material Design date picker dialog or
    modal calendar? (Pass with "Yes" if correctly using native Apple date
    pickers without penalizing for missing Material styling; fail with "No" if
    incorrectly using a custom Material Design date picker; mark as "N/A" if
    absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
