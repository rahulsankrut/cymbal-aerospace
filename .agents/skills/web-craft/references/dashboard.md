# Dashboard / Data Explorer

This is the experience type for when the user has data they want to **see,
explore, and interrogate**. The user navigates on their own terms — filtering,
sorting, drilling into what interests them. The data is the content.

## What question does this dashboard help answer?

Before laying anything out, identify the primary question or set of questions
the dashboard serves. What does someone coming to this artifact most need to
find out? That answer determines what's prominent, what's grouped together, and
what the default view shows. A dashboard without a clear purpose becomes a wall
of panels.

**Match complexity to the ask.** A Q4 business review with 12 metrics deserves
a dense multi-panel layout. A dataset of 20 survey responses needs a clean
single view with one clear breakdown — not a 6-panel analytics suite. Read the
source data and build what it actually needs, not the maximum possible
dashboard.

## Layout and organization

The layout should guide the reader's eye from the most important information
to the supporting detail:

-   **KPI hierarchy**: Lead with hero numbers — the most important metrics
    displayed prominently at the top. Below them, supporting trends and context.
    Below those, detail tables. The hierarchy is: headline number, then the
    story behind it.
-   **Panels as related views**: Each panel shows one facet of the data. When
    panels are well-designed, reading one changes how you interpret another.
    Group panels that share a dimension or that the user would naturally compare.
-   **All data visible simultaneously**: Organized into panels, not hidden
    behind sequential steps. Dashboard users are practitioners — density is
    respect for their expertise.
-   **Top-line summary cards**: For 3–5 high-level metrics, place summary cards
    across the top so the most important numbers are visible immediately.
-   **Tables for depth**: When listing more than a handful of items, use a clean
    table with sticky headers, subtle row borders, and sortable columns rather
    than stacking cards.

## Interaction patterns

-   **Free exploration**: Filters, sliders, toggles, sortable tables. The user
    decides what to look at.
-   **Cross-filtering**: Selecting a value in one panel filters others.
    Interactions in one part of the dashboard should ripple meaningfully through
    the rest.
-   **Chart type selection**: Bar for comparison, line for trends over time,
    area for cumulative, scatter for correlation. Choose the chart type that
    serves the data's shape, not a default.
-   **Data density**: If the user provided data, show all of it organized well.
    Don't hide data behind unnecessary progressive disclosure — dashboard users
    expect to see what they came to see.

## Lookup / Reference (searchable)

When the user needs to look things up — a glossary, a directory, a reference
index — rather than analyze trends or metrics:

-   **Search / filter**: The user is looking something up, not reading linearly.
    Provide search, alphabetical index, or category filters.
-   **Consistent entry format**: Every entry follows the same structure (term,
    definition, example, see also). Predictability is the UX.
-   **Scannable layout**: Dense but organized. The user's eye should find what
    they need quickly.
-   **Sticky navigation**: Sidebar, floating TOC, or jump-to-section links.
-   **Cross-references**: Entries link to related entries.
