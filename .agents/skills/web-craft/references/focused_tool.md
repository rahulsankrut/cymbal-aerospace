# Focused Tool

This is the experience type for when the user needs a **purpose-built
interactive tool** — something that lets them compute a result, simulate a
system, track progress, or look up information. The artifact is shaped entirely
around a specific task and the user's inputs drive it.

## What task does this tool serve?

Before building anything, identify the specific task: **what does this tool let
the user accomplish that a static page or prose explanation can't?** That answer
determines the tool's scope, its inputs and outputs, and what the user should
see first.

**The core value should be immediately visible.** For a calculator, that's the
result or verdict — show the answer prominently, then let the user change inputs
to see it shift. For a tracker, that's the current state — what's done, what's
pending, where things stand. For a simulator, that's the model itself — the
thing the user can manipulate directly.

## Calculator (input to output)

When the user needs to compute a result from their own parameters:

-   **Clear input-to-output layout**: Inputs on one side or top, outputs
    clearly separated on the other. Never mix them.
-   **Lead with the result**: Place the primary output or verdict prominently —
    above or beside the inputs, not below them. The math supports the answer;
    the answer comes first.
-   **Show your work**: Display intermediate calculations so the user can
    understand and trust the output — not just the final number.
-   **Grouped, validated inputs**: Related inputs grouped together with smart
    defaults and validation. Constrain to domain-realistic ranges.
-   **Preset buttons**: Common scenarios the user can load with one click (e.g.,
    "30-year fixed," "15-year fixed," "ARM"). These teach by example.
-   **Live computation**: Outputs update as inputs change. No "Calculate" button
    unless the computation is genuinely expensive.
-   **Reference defaults**: Open on reference values from the source or typical
    figures, labeled as such (e.g., "6.8% — 30-year average"), so the user sees
    a working result immediately and knows where the numbers come from.
-   **Validated ranges**: Constrain to domain-realistic values — if source data
    says typical range is 3–8%, don't allow 500%.
-   **Constraint enforcement**: If two variables must sum to 100%, adjusting one
    automatically adjusts the other. The tool should never produce absurd
    outputs.
-   **Edge cases**: Handle gracefully — divide-by-zero explains what went wrong,
    out-of-range values flag the issue, empty inputs show a helpful prompt.
-   **Copy / Reset affordances**: Let users save results or start fresh.
-   **State persistence**: Restore saved inputs on load
    (`window.notebookAppApi.getAppState()`) and persist on change
    (`window.notebookAppApi.setAppState()`).

## Tracker (ongoing state)

When the user needs to record, monitor, or manage items over time — a habit
tracker, a checklist, a progress log, a planner:

-   **Current state up front**: The user should immediately see where things
    stand — what's complete, what's pending, overall progress. This is the
    equivalent of "lead with the result" for ongoing work.
-   **Easy input**: Adding, checking off, or updating items should be fast and
    low-friction. The interaction the user repeats most should be the simplest.
-   **Derived state**: Compute and display meaningful summaries from the user's
    entries — completion percentage, streaks, totals, trends. The tracker's
    value isn't just storage; it's showing the user something about their own
    data they wouldn't see from a list alone.
-   **State persistence**: Trackers hold the user's ongoing work. Restore saved
    state on load (`window.notebookAppApi.getAppState()`) and persist every
    change (`window.notebookAppApi.setAppState()`). Losing a user's entries is
    the worst failure mode for a tracker.
-   **Empty start**: Begin with no entries. The empty state shows what the
    tracker will display and makes adding the first entry the obvious action.

## Simulator (direct manipulation)

When the user needs to develop intuition through hands-on interaction with a
model or system — physics, mechanics, algorithms, ecological systems:

-   **The model is the interface**: Let users manipulate the simulation
    directly — drag, pull, adjust parameters — rather than filling in form
    fields and clicking "Run."
-   **Immediate visual feedback**: The model responds to every interaction in
    real time. Latency breaks the sense of causality.
-   **Progressive build-up**: Start with the simplest version of the system
    (one variable, one piston, one agent). Add complexity as the user explores
    deeper.
-   **Side-by-side math and visuals**: Where relevant, show the underlying
    equation alongside the interactive model so users can verify their intuition
    against the math.
-   **Constrained parameters**: Sliders, bounded inputs, and snapping behavior
    keep the simulation in physically or conceptually valid ranges.
-   **Reduced-motion compliance**: Keep the interaction model intact under
    `prefers-reduced-motion`; only remove transitions and animations so state
    snaps instantly.
