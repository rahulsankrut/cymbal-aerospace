# Badge

1.  [ID: badge_usage] If badges (small circular dots or compact count pills) are
    present, are they appended directly to a host element (such as navigation
    icons, action icons, tabs, or avatars) rather than placed as standalone
    chips? (Pass with "Yes" if badges are anchored to a parent icon, tab, or
    avatar; fail with "No" if badges float as standalone chips or detached
    inline elements; mark as "N/A" if no badges are present.) [Metric type:
    Adherence] [Weight: 3]

2.  [ID: badge_container_shape] Are small badges shaped as simple solid circles,
    and large badges shaped as rounded rectangles? [Metric type: Hygiene]
    [Weight: 3]

3.  [ID: badge_mandatory_elements] If a large badge (with text/numbers) is
    present, does it contain label text inside its container? [Metric type:
    Hygiene] [Weight: 3]

4.  [ID: badge_large_label_length] If a large badge (with text/numbers) is
    present, is its label limited to 4 characters or fewer (including symbols
    like "+")? [Metric type: Adherence] [Weight: 3]

5.  [ID: badge_error_color_default] If a badge (small circular dot or compact
    count pill) is present, does it use an authorized semantic color role
    matching its intent: sys.color.error for notification and alert counts, a
    semantic status color (such as green, amber, or neutral grey) for presence,
    availability, or connectivity dots, or a system primary/tonal role
    (sys.color.primary or sys.color.secondary-container) for non-urgent unread
    indicators and contextual counts? (Pass with "Yes" if alert badges use
    sys.color.error or if status, presence, and non-urgent unread/count badges
    use intentional semantic or system color roles; fail with "No" if badges use
    arbitrary unmapped colors; mark as "N/A" if no badges are present.) [Metric
    type: Hygiene] [Weight: 3]
