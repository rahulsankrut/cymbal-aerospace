> [!IMPORTANT] Read SKILL.md first.

# UX Heuristic Review Skill - Agent Test Plan

## Tier 1: Build & Validation

### T1.1: Skill Validation Test

**Command:**

```bash
blaze test //labs/ux/agent_skills/ux_heuristic_review:validate_ux_heuristic_review_skill_test
```

**Verify:**

-   Test passes cleanly, confirming SKILL.md frontmatter and markdown structure
    are valid.

## Tier 2: Smoke Tests

### T2.1: Conceptual Understanding

**Prompt:** `What is a UX heuristic review?`

**Verify:**

-   Agent provides an accurate summary of Nielsen's 10 Usability Heuristics and
    the review process.

## Tier 3: E2E Evaluation Cases

### T3.1: Analyze Screenshot

**Prompt:** `I have a screenshot of a new feature in Intrinsic Flowstate. Can
you perform a UX Heuristic Review on it? Focus on Consistency and Standards.
Here is the file path: /path/to/screenshot.png`

**Verify:**

-   Agent acknowledges the request and confirms it will focus on "Consistency
    and Standards".
-   Agent produces a structured report following the template in `SKILL.md`
    (Evaluation Summary, followed by Heuristic sections).
-   The report specifically evaluates the screenshot against "Consistency and
    Standards" (and potentially other heuristics if applicable, but focusing on
    the requested one).
-   The report includes:
    -   Severity ratings (0-4) for identified issues.
    -   Evidence (referencing the screenshot path).
    -   Specific difficulties observed.
    -   Actionable opportunities/recommendations.

### T3.2: Analyze Video

**Prompt:** `Here is a recording of a user trying to create a new template in
Flowstate. Please perform a UX Heuristic Review on it. URL:
http://screencast.googleplex.com/cast/12345`

**Verify:**

-   Agent acknowledges the request.
-   Agent produces a structured report following the template in `SKILL.md`.
-   The report references specific timestamps in the video as evidence.
-   The report identifies usability issues, assigns severity, and suggests
    recommendations.

### T3.3: Execute CUJ and Review

**Prompt:** `Perform a UX Heuristic Review on the CUJ 'Create a new
implementation' at http://flowstate.intrinsic.com. You need to execute the CUJ
and record a video.`

**Verify:**

-   Agent uses a browser tool (e.g., `browser_subagent`) to navigate to
    `http://flowstate.intrinsic.com`.
-   Agent documents the steps it takes to execute the "Create a new
    implementation" CUJ.
-   Agent successfully completes (or attempts to complete and documents failure
    points) the CUJ.
-   Agent generates a structured report following the template in `SKILL.md`.
-   The report includes evidence (e.g., links to recorded video or screenshots
    taken during execution).
-   The report maps observations to the 10 Nielsen Heuristics and provides
    severity ratings and recommendations.

### T3.4: Non-Trigger (Backend Performance)

**Prompt:** `Can you evaluate the backend API performance and database query
latency for the new user authentication service in Flowstate?`

**Verify:**

-   Agent does NOT trigger or execute the `ux-heuristic-review` skill.
-   Agent explains that backend performance evaluation is outside the scope of a
    UI heuristic review (or addresses the backend request using appropriate
    tools/knowledge without applying UI heuristics).
