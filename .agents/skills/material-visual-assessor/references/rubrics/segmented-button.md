# Segmented Button

1.  [ID: segmented_button_usage] Are segmented buttons used to toggle between
    complementary views (e.g., Day/Week/Month)? [Metric type: Hygiene] [Weight:
    3]

2.  [ID: segmented_button_inner_segments_dividers] Are the inner segments
    separated by clean internal dividing lines? [Metric type: Hygiene] [Weight:
    3]

3.  [ID: segmented_button_content_centered] Are all text labels and associated
    icons centered perfectly within their segment? [Metric type: Hygiene]
    [Weight: 1]

4.  [ID: segmented_button_no_drop_shadow] Does the container stay flat without a
    drop shadow for elevation? [Metric type: Hygiene] [Weight: 3]

#### iOS Platform & Liquid Glass Adherence

1.  [ID: ios_native_segmented_control_usage] In this iOS application, if a
    segmented control is present, is it implemented using Apple native
    UISegmentedControl / SwiftUI Picker segmented styling rather than Material
    Design segmented buttons? (Pass with "Yes" if correctly using native Apple
    segmented control without penalizing for missing Material styling; fail with
    "No" if incorrectly using Material-styled segmented buttons on iOS; mark as
    "N/A" if absent or non-iOS.) [Metric type: Adherence] [Weight: 10]
