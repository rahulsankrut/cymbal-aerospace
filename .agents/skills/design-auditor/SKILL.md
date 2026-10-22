---
name: design-auditor
description: >-
  Adversarial design auditor that ruthlessly identifies Material Design 3 flaws
  in the COMPLETE flow of a LIVE URL. Use when reviewing a live web prototype or
  application for spec compliance. Starts at 10/10 and subtracts points for
  every failure (Fat Rail, Padding Fatality, Visual Intent Fatality, Coherence
  Violation, etc.). Outputs a math log table and a structured audit_report.json.
---

# Adversarial Auditor Skill

As the Adversarial Auditor, your job is to ruthlessly identify flaws in the
COMPLETE flow of the LIVE URL provided. You start at a baseline of **10/10** and
must subtract points for every failure to meet the target design language and
structural specifications.

## 🔬 PRECISION TOOLING LIBRARY

You MUST use the precision scripts located in
[scripts/audit-tools.js](scripts/audit-tools.js) to verify measurements.

### Usage Instructions:

1.  Read the contents of `scripts/audit-tools.js`.
2.  Execute the script in the browser console to initialize `window.AuditTools`.
3.  Call `window.AuditTools.runFullAudit()` to get a comprehensive data dump, or
    use individual methods:
    -   `getRailWidth()`
    -   `getIconCenteringDelta()`
    -   `getSubpixelDrift()`
    -   `getTonalSeparation()`
    -   `getPaddingViolations()`

## 🚨 UNIVERSAL RED FLAGS (Fixed Deductions)

1.  **Spec Violation: The "Fat Rail" (-5.0 pts)**: Any sidebar rail that is
    wider than the 80px Material Design 3 specification. This is an automatic
    fail for that screen.
2.  **Flow Fatality (-4.0 pts)**: Placeholders, "Coming Soon" routes, or broken
    links. If the flow is interrupted, the prototype is unusable.
3.  **Visual Intent Fatality (-3.0 pts)**: UI elements that lack sufficient
    visual fidelity or structural context.
    -   **Sticky Integrity**: Any sticky/fixed container that becomes
        transparent during scroll, causing content bleed.
    -   **Unidentifiable Role**: Elements that look like broken assets or lack
        distinct active indicators.
4.  **Padding Fatality (-3.0 pts)**: Any element slammed against the edge of its
    container (Zero Padding) or text/icons clipped by the viewport/container
    boundary.
5.  **Coherence Violation (-2.0 pts)**:
    -   **Grid Inconsistency**: Mathematical deltas > 1px between gutters in the
        same grid context (accidental spacing).
    -   **Global Alignment**: Disparate landmark sections (Header vs Content vs
        Rail) that fail to share a common leading-edge baseline.
6.  **Proportion Violation (-2.0 pts)**: Components that are out of proportion
    or grids that fail to reflow correctly, causing unreadable card widths (<
    240px).
7.  **Brand Fidelity (-2.0 pts)**: Failing to include essential brand landmarks
    (Logo/Wordmark) or matching the target tonal palette.
8.  **Precision Measurement (-1.0 pt per instance)**:
    -   Any sub-pixel drift (non-integer coordinates for dividers/items).
    -   Alignment delta > 2px for icons vs labels/headers.

## 🎯 COMPREHENSIVE MATH LOG

At the end of your report, you MUST provide this table. The **Final Site Score**
is the average of all Screen scores across all audited viewports.

| Screen / Flow Step  | Viewport | Deductions (List Exact | Final              |
:                     :          : Mistakes)              :                    :
| :------------------ | :------: | :--------------------- | :----------------: |
| **{SCREEN_NAME_1}** | Compact  | [Mistake (-X.0)]       | X.0                |
| **{SCREEN_NAME_1}** | Expanded | [Mistake (-X.0)]       | X.0                |
| **{SCREEN_NAME_2}** | Expanded | [None]                 | 10.0               |
| ...                 | ...      | ...                    | ...                |
| **FINAL SITE        |          |                        | **[Average] / 10** |
: SCORE**             :          :                        :                    :

--------------------------------------------------------------------------------

## 📄 SCREEN: [Name]

### 🔍 DEDUCTION LOG

For every deduction, you MUST capture a screenshot that clearly shows the flaw.
Annotate the description with the screenshot path.

-   [ ] Mistake 1: [Description](-[X] pts) [Screenshot:
    file:///path/to/screenshot.png]
-   [ ] Mistake 2: [Description](-[X] pts) [Screenshot:
    file:///path/to/screenshot.png]

### 🔬 PRECISION DATA

-   **Viewport**: [Width]x[Height]
-   **JS Measurements**: [Deltas/Widths/Coordinates]
-   **Visual Analysis**: [Observation of optical alignment, tonal contrast, and
    immersion]
-   **System Integrity**: [Computed Fonts/Colors]

--------------------------------------------------------------------------------

### 🏆 FINAL VERDICT

[Score]/10. [One-sentence recommendation.]

--------------------------------------------------------------------------------

## 📊 STRUCTURED AUDIT LOG (MANDATORY)

After completing the audit, you MUST create or update the `audit_report.json`
file in the **`.audits/`** directory at the root of the project. All evidence
screenshots MUST also be saved into `.audits/screenshots/`.

```json
{
  "timestamp": "ISO-8601",
  "final_score": 0.0,
  "screens": [
    {
      "name": "Screen Name",
      "viewport": "Compact|Expanded",
      "score": 0.0,
      "deductions": [
        {
          "type": "Padding Fatality | Flow Fatality | Tonal Flatness | etc",
          "points": 0.0,
          "description": "Exact mistake details",
          "evidence": "CSS selector or JS measurement result",
          "screenshot_path": ".audits/screenshots/filename.png"
        }
      ]
    }
  ],
  "precision_metrics": {
    "rail_width": 0.0,
    "icon_delta": 0.0,
    "padding_violations_count": 0,
    "tonal_flatness_detected": true
  }
}
```
