# List

1.  [ID: list_corners_contained_uncontained] In list layouts, do
    uncontained/edge-to-edge list item containers have a corner radius of 0dp
    (sys.shape.corner.none), while contained/card list items use a corner radius
    of 12dp (sys.shape.corner.medium) or 16dp (sys.shape.corner.large)? [Metric
    type: Hygiene] [Weight: 10]

2.  [ID: list_supporting_text_lines] If list item supporting text is present, is
    it limited to a maximum of 3 lines? (Mark as "N/A" if the container is part
    of a conversational messaging stream, chat transcript, or timeline where
    narrative body text wrapping is required.) [Metric type: Hygiene] [Weight:
    3]

3.  [ID: list_avatar_vs_thumbnail_shape] If leading avatars or media thumbnails
    are present in list items, are circular avatar shapes used for people while
    square/rounded rectangles are used for products/media? [Metric type:
    Hygiene] [Weight: 3]

4.  [ID: list_controls_edge_placement] If selection controls (checkboxes,
    switches, or radio buttons) are present in list items, are they positioned
    at the absolute leading or trailing edge? [Metric type: Hygiene] [Weight: 3]

5.  [ID: ios_native_list_usage] In this iOS application, if a list or table view
    is present, is it rendered using Apple native table/list controls
    (UITableView, UICollectionView, or SwiftUI List) rather than custom
    non-native list implementations? (Pass with "Yes" if correctly using native
    Apple lists; fail with "No" if incorrectly implementing non-native list
    wrappers; mark as "N/A" if absent or non-iOS.) [Metric type: Adherence]
    [Weight: 5]
