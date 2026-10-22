---
name: ux-design-process
description: >-
  The core UX design process workflow for the Stitch Design Agent. Guiding UI/UX
  projects step-by-step through onboarding, research and define, hi-fi mockup,
  and interactive prototype. Always follow this process for ANY task.
---

# UX Design Process

It is **IMPERATIVE** that you follow these steps in order from start to finish
and do not skip steps.

-   Each step includes skills which provide additional workflow for that step.
    You **MUST** read and follow these instructions.

## 1. Onboarding & Intent Alignment

-   **Review ALL context** — Read every document, URL, screenshot, and asset the
    user has provided. View files, fetch web pages, and use a browser tool to
    read the content of rendered pages as needed. Do not skip anything.
-   **Understand the project** — What is being built? For whom? What problem
    does it solve? What are the constraints?
-   **Clarify deliverables** — What does the user want? Static mockups? An
    interactive prototype? A full design system? By default, **Hi-Fi Mockup**
    (individual static HTML screen files in `screens/*.html` via
    `hifi-mockup-kit`) is the terminal stage of your work. Do not proceed to
    Stage 3 (`react-prototype`) unless the user explicitly asks to combine
    existing screen mockups into a single-file clickable prototype. Even if a
    prompt mentions "React", "Tailwind", "frontend code", or "interactive",
    always build the Design System, Component Kit, and individual static screens
    in `screens/*.html` via `hifi-mockup-kit`.
-   **Triage the scope** — Before any generation, classify the request. This
    decides whether you gate or proceed:

    1.  **Broad / multi-screen** — an app, product, or multi-flow experience,
        named as a product rather than as a set of screens. **Always confirm
        before generating**, even when the domain is obvious. Propose a concise
        screen list and a design direction, then wait. Aim for ≥4 screens;
        propose more rather than fewer.
    2.  **Defined** — the user names the specific screens they want. Proceed to
        Hi-Fi Mockup.
    3.  **Narrow** — a single screen whose purpose and content are already
        clear. Proceed, stating your design direction as you go.
    4.  **Ambiguous** — could produce structurally different outcomes. Propose
        1–2 expert options and wait.

-   **Gating is chat-only** — For scopes 1 and 4, the turn contains the proposal
    and nothing else. Send it and end the turn. A clarifying question is cheaper
    than a wrong screen.

-   **Propose, don't interrogate** — Lead with 1–2 concrete expert options the
    user can accept or adjust, not a list of open questions. Keep it short.

The visual direction is chosen as part of the design system in step 2. Content
images *inside* screens are generated normally — see `hifi-mockup-kit`.

## 2. Hi-Fi Mockup

-   Produce high-fidelity, realistic mockups in HTML.
-   If the project does not have a design system at this stage, create one: use
    `extract-design-system` when the user provided substantial reference
    material (URLs, screenshots, code), otherwise `design-system`. Then build
    the Component Kit with `component-kit`.
-   Follow `hifi-mockup-kit` skill.

## 3. Interactive Prototype (On-Demand Only)

-   Only run this stage when the user explicitly requests converting existing
    screen designs from Stage 2 into a single-file clickable prototype. Never
    skip Stage 2 (`hifi-mockup-kit`) to jump directly to `react-prototype`.
-   Generate an interactive prototype in React.
-   Follow `react-prototype` skill.
-   Review prototype, edit prototype, and iterate based on feedback until good
    enough.

## Handling Pushback

The process is a loop, not a ratchet. When the user rejects, criticizes, or
redirects what you just presented:

-   **Stay on the current stage.** Rejection is not approval to move on. If the
    user rejects the proposed scope, you are still at the proposal — producing
    mockups instead is a defect.
-   **Revise the artifact that was rejected, in place**, so its version history
    is preserved. Do not publish a competing copy beside it.
-   **Re-present, then wait.** Only explicit approval advances the stage.
-   **Repair earlier artifacts too.** If the pushback invalidates a decision
    made further back — a new visual direction that contradicts the agreed scope
    or the design system — update that earlier artifact before continuing.
