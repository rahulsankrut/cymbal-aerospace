---
name: ux-heuristic-review
description: >-
  Evaluates user interfaces and Critical User Journeys (CUJs) against Nielsen's
  10 Usability Heuristics. Generates structured reports with severity ratings,
  evidence screenshots, and design recommendations. Supports live web apps
  (via browser navigation), static screenshots, and recorded screencasts.
  Use when performing a UX heuristic evaluation, auditing UI usability, or
  reviewing a CUJ for friction points.
  Don't use for backend performance evaluation, quantitative usability testing,
  security audits, or accessibility (a11y) compliance reviews (use
  pa11y-ux-linter for a11y).
---

# UX Heuristic Review

This skill guides the process of evaluating a user interface against usability
heuristics, specifically focusing on identifying difficulties and opportunities
for improvement.

## Overview

This skill enables an agent to: 1. Understand a Critical User Journey (CUJ) to
be evaluated. 2. Execute the CUJ (or observe a user executing it) to identify
friction points. 3. Analyze the interface against Nielsen's 10 Usability
Heuristics. 4. Generate a structured report with severity ratings and
recommendations.

## Related Skills

*   **Defining CUJs**: Use
    [writing-cujs](http://google3/learning/gemini/agents/skills/writing_cujs/SKILL.md)
    to define and structure Critical User Journeys before performing a review.
*   **Accessibility Auditing**: For dedicated accessibility (a11y) reviews
    against GAR/WCAG standards (especially Figma Greenlines), use
    [pa11y-ux-linter](http://google3/labs/ux/agent_skills/pa11y_ux_linter/SKILL.md)
    instead of this skill.

## Input Requirements

*   **Web Applications**: Requires a valid URL to the application.
*   **Static Interfaces**: Supports screenshots in PNG or JPEG format.
*   **Recorded Interactions**: Supports screencast links (e.g.,
    `http://screencast.googleplex.com/...`) or accessible video files.

## Don't Use When

*   **Evaluating non-UI aspects**: Do not use for evaluating backend
    performance, API design, or system architecture unless it directly impacts
    the user interface visibility of status or error recovery.
*   **Quantitative usability testing**: Do not use for measuring task completion
    times or click rates across a large user base.
*   **Security audits**: Do not use for verifying security protocols or data
    encryption.
*   **Accessibility (a11y) audits**: Do not use for auditing designs against
    accessibility standards (like GAR or WCAG). Use
    [pa11y-ux-linter](http://google3/labs/ux/agent_skills/pa11y_ux_linter/SKILL.md)
    instead.

## The 10 Usability Heuristics

All 10 heuristics should be considered. However, the user may ask you to focus
on a specific subset of the heuristics.

1.  **Visibility of system status**: Keep users informed about what is going on.
2.  **Match between system and the real world**: Speak the users' language.
3.  **User control and freedom**: Support undo and redo; provide emergency
    exits.
4.  **Consistency and standards**: Follow platform conventions.
    *   *Google Adaptation*: Verify alignment with **Material Design** (go/m3)
        and consistent use of **Material Symbols** (go/symbols). Ensure color
        usage complies with Google brand standards (go/identity).
5.  **Error prevention**: Eliminate error-prone conditions.
6.  **Recognition rather than recall**: Minimize user memory load.
7.  **Flexibility and efficiency of use**: Provide accelerators for experts.
8.  **Aesthetic and minimalist design**: Avoid irrelevant information.
9.  **Help users recognize, diagnose, and recover from errors**: Clear error
    messages suggesting solutions.
10. **Help and documentation**: Easy to search, focused on user's task.
    *   *Google Adaptation*: Ensure help links use official channels (e.g.,
        `support.google.com` or appropriate internal `go/` links for internal
        tools).

## Severity Ratings

Use the following scale to rate the impact of identified difficulties:

*   **0**: I don't agree that this is a usability problem at all.
*   **1**: **Cosmetic problem only**: Need not be fixed unless extra time is
    available on project.
*   **2**: **Minor usability problem**: Fixing this should be given low
    priority.
*   **3**: **Major usability problem**: Important to fix, so should be given
    high priority.
*   **4**: **Usability catastrophe**: Imperative to fix this before product can
    be released.

## Workflow

When asked to perform a UX Heuristic Review:

1.  **Clarify the CUJ**: Ensure you understand the goal and steps of the
    journey.
2.  **Execute and Record**:
    -   If the target is a web app, use the `browser_subagent` to attempt to
        complete the CUJ.
    -   The `browser_subagent` will automatically record a video.
    -   If the target is provided as a screenshot or existing video, skip to
        analysis.
3.  **Analyze**: Review the interaction logs or video against the heuristics.
4.  **Report**: Generate a report using the template below.

## Report Template

The report should begin with a summary of the evaluation to provide context and
a high-level overview, suitable for an executive summary or introductory slide.

### Evaluation Summary

-   **CUJ Evaluated**: [Brief description of the goal and steps of the journey]
-   **Overall Impression**: [High-level summary of usability and takeaways]
-   **Summary of Issues**: [List issues ordered by severity, or 'None']

For each heuristic where difficulties are found, use the following structure.
Order the sections by severity, starting with the most severe issues (Severity

4\) down to the least severe (Severity 1). Keep observations and recommendations
concise (preferably as bullet points) to facilitate direct mapping to slides.

### [Heuristic Name]

-   **Severity**: [0-4]
-   **Evidence**: [Link to screenshot or video timestamp, e.g.,
    `![Evidence](file:///absolute/path/to/screenshot.png)`]
-   **Difficulties/Observations**:
    -   [Point 1: Describe the specific UX difficulty.]
    -   [Point 2: Describe another difficulty if applicable.]
-   **Opportunities/Recommendations**:
    -   [Point 1: Describe opportunity to improve the UI.]
    -   [Point 2: Describe another recommendation if applicable.]

--------------------------------------------------------------------------------

Example:

### Visibility of system status

-   **Severity**: 3
-   **Evidence**: ![Saving State](file:///absolute/path/to/saving_state.png)
-   **Difficulties/Observations**:
    -   When clicking 'Save', there is no visual indication that the operation
        is in progress.
    -   The user might click multiple times, potentially causing duplicate
        submissions.
-   **Opportunities/Recommendations**:
    -   Add a loading spinner or a progress bar to indicate the saving state.
    -   Disable the 'Save' button while the operation is in progress.
