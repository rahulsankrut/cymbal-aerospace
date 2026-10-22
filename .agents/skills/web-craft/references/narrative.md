# Narrative

The default archetype. A narrative gives the reader a **structured encounter
with ideas** — the author shapes how material unfolds, and the reader follows
that path. Narratives can range from chronological stories to thematic
explorations to data-driven arguments, and they often incorporate interactive
elements, data visualizations, maps, and other media alongside prose. What
unites them is authored sequencing: you're building understanding in an order
that matters.

## What the reader should take away

Before structuring anything, identify the core takeaways: **what are the most
important things the reader should understand after experiencing this artifact?**
What's most surprising, specific, or consequential in the sources?

One of those takeaways should anchor the opening — it's your hook: the most
surprising or consequential point, stated up front. The rest become the
substance the narrative builds toward or through. Every subsequent decision —
structure, element choice, pacing — should serve these takeaways. If a section
doesn't contribute to the reader reaching one of them, it probably doesn't
belong.

## Narrative arc

Choose the structural spine that serves the takeaways:

| Arc | When it fits |
|---|---|
| Chronological | Time is central to the story: events, evolution, a journey |
| Argumentative | You're making a case: thesis, evidence, conclusion |
| Comparative | The point is difference or similarity between things |
| Mystery / reveal | The conclusion is counterintuitive: open with it, then explain |
| Taxonomic | A domain explored category by category, each its own chapter |

These are patterns, not templates. Many narratives blend them — a chronological
story with a comparative section, an argument with a taxonomic middle. The arc
should serve the takeaways, not the other way around.

**Sequencing within the arc:** ideas should build on each other. Concept A
before concept B if B depends on A. Start with the specific and concrete before
the general and abstract — a real case, a vivid example, a grounded fact — then
widen. The reader arrives at complexity through a path.

## Composition: connecting text and media

A narrative is composed of sections, and sections often combine **multiple
elements** — a paragraph of prose alongside a chart, a table with a text
observation below it, an interactive element with a caption. The question for
each section is: **what combination of elements makes this idea land most
directly?**

Prose is one element, not the default one. Reach for whatever form communicates
best:

| What you're conveying               | Elements that tend to serve it well    |
| ----------------------------------- | -------------------------------------- |
| Trend or change over time           | Line or area chart, timeline,          |
:                                     : before/after slider                    :
| Comparison between entities         | Side-by-side layout, table,            |
:                                     : juxtaposition                          :
| Magnitude or proportion             | Bar chart, proportional visual         |
| Dense structured information        | Table. Not prose paragraphs — tables   |
:                                     : are load-bearing elements, not         :
:                                     : decoration.                            :
| Spatial or geographic relationship  | Map (Leaflet.js over public-domain     |
:                                     : Natural Earth vector geometry for real :
:                                     : geography — never raster tiles, see    :
:                                     : references/maps.md; styled SVG for     :
:                                     : abstract or historical borders)        :
| How a mechanism or system works     | Targeted interactive element: a slider |
:                                     : that lets the reader change one        :
:                                     : variable, a diagram the reader can     :
:                                     : step through, a prediction followed by :
:                                     : a reveal                               :
| Process or sequence                 | Step-through, annotated flow diagram   |
| A quantity the reader needs to feel | Physical analogy, scale comparison     |
: in scale                            :                                        :

These elements should be **intentionally connected** — placed and composed so
text, media, and interactive controls build a cohesive whole, not dumped
sequentially. The placement and interplay between elements matters as much as
the elements themselves.

When embedding interactive elements: they should make an idea tangible in a way
the other elements can't. They're especially valuable when the reader needs to
develop intuition for how something changes — seeing the effect of a variable,
stepping through a process, or testing a claim against the evidence.

## Scannability and structure

The artifact should be **legible at a glance**. Before reading in depth, the
reader should be able to understand what the artifact covers, how it's
organized, and where the major ideas live.

The vertical scroll is the primary navigation mechanism. Use strong visual
hierarchy and clear landmarks so the reader can orient themselves as they move
through the artifact. Top-level content should be exposed in the scroll flow,
not hidden behind tabs or clicks — users shouldn't have to navigate away from
the page to discover what the artifact contains. When secondary content
(methodology, definitions, additional detail) would clutter the main flow,
place it in collapsible sections inline, keeping it accessible without breaking
the scan.

**Section headers should state a finding or an argument, not just name a
topic.** "Cotton exports plunged 60% after the 1886 tariff" communicates more
at a glance than "Export History." When charts carry important data points,
annotate them directly at the moment that matters — label the turning point on
the line, not in a detached legend.

## Scroll-driven techniques

When the narrative has a central visual that evolves across sections — a map
tracing a route, a timeline accumulating events, a chart that builds up —
consider **pinning that visual** and letting the text steps drive changes to it
(the sticky scroller pattern). This is a powerful technique for journeys,
timelines, process walkthroughs, and "build from X to Y" arcs. The visual stays
in view while the reader scrolls through the beats that update it.

When each section is its own self-contained scene with no shared visual, let
sections **flow full-width** — each one entering the viewport, delivering its
content, and scrolling away naturally.

The scroll mechanic should fall out of the content — ask which mode the beats
call for, not which looks more impressive. For implementation details and the
build scaffold, see **references/scrollytelling.md**.

## Editorial sensibility

The design should feel considered and appropriate for the subject — not generic,
but also not costumed. Visual character comes from **layout choices, typography,
and color palette** (guided by the design system: see
**references/design_foundation.md**), not from decorative elements or heavy
theming. A narrative about marine biology doesn't need wave animations and
ocean-blue everything — it needs clear structure, well-chosen data
representations, and typography that fits the register.

Don't use emojis. They read as decoration standing in for design, and they
undercut the editorial quality the artifact is reaching for. Whatever an emoji
would have signaled — emphasis, category, status, tone — should come from
typography, color, spacing, or the data representation itself.

Alternate denser sections (data-heavy, multi-element) with more open, spacious
ones. Pacing in a narrative isn't just about content sequencing — it's about
visual rhythm too.
