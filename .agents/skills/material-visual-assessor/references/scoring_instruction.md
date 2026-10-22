<!-- disableFinding(G3DOC_JINJA) -->

# Scoring Instruction

This instruction defines how to calculate the overall Material Design 3
compliance assessment score and subcategory scores using the **Dual-Metric
Governance Model**.

--------------------------------------------------------------------------------

## 1. Dual-Metric Governance Model

To prevent compliance inflation (where generic usability hygiene masks a lack of
system-specific adoption), the rubric divides all evaluated criteria into two
mutually exclusive buckets based on their `[Metric type: ...]` tag:

-   **UI Hygiene (Usability & Polish):** Evaluates general visual polish, grid
    alignment, contrast, spacing, legibility, and usability (`[Metric type:
    Hygiene]`).
-   **Material 3 Adherence (System Specs):** Evaluates strict compliance with
    official Material 3 tokens, component geometry, typography families (Google
    Sans), and color roles (`[Metric type: Adherence]`).

--------------------------------------------------------------------------------

## 2. 4-Tier Severity Framework

Criteria carry assigned point weights $w_i$ based on their visual and structural
importance:

-   **Tier 0 (Brand Signature Anchors — Weight = 10):** Non-negotiable brand
    identity pillars and system anchor rules (e.g., sentence case
    capitalization, surface color role separation, standard leading icons,
    active navigation pill containers, primary action reservation, iOS native
    control enforcement [checkbox, switch, segmented control, app bar, menus,
    date pickers], and iOS Always-On Liquid Glass anchors [FAB, Nav Bar, Dialog,
    Bottom Sheet, Nav Rail]).
-   **Tier 1 (Critical Component & Layout Rules — Weight = 5):** High-impact
    layout constraints, core accessibility, dialog scrims, visual hierarchy, and
    layer placement (e.g., pane counts, hardware clipping, whitespace division,
    text legibility over imagery, prominent actions, iOS Liquid Glass opt-in
    layer placement [Buttons, Search, Tabs, Banners], and Liquid Glass text
    legibility).
-   **Tier 2 (Key Material Patterns & Component Rules — Weight = 3):** Standard
    component geometry, layout patterns, and usability configurations (e.g.,
    button variant hierarchy, badge shapes, menu elevation, subtitle lines,
    typescale typography, granular color roles).
-   **Tier 3 (Visual Polish — Weight = 1):** Minor formatting, casing, and
    alignment polish (e.g., visual alignment, divider stroke thickness,
    icon/label spacing).

--------------------------------------------------------------------------------

## 3. Criteria Filtering & Exclusions

`FOR EACH` criterion in `criteriaStatus`:

-   **Scored Criteria:** `IF` `answer` is `"Yes"` (or `met: true`) or `"No"` (or
    `met: false`), `THEN` the scorer `MUST` include its point weight $w_i$ in
    the denominator (possible points) and, when `"Yes"` / `true`, in the
    numerator (earned points).
-   **Excluded Criteria:** `IF` `answer` is `"N/A"` or a HEX color value, `THEN`
    the scorer `MUST` exclude the criterion so it contributes `0` to both the
    numerator (earned points) and denominator (possible points).

--------------------------------------------------------------------------------

## 4. The Adherence Multiplier Formula

Rather than enforcing arbitrary binary pass/fail gates, the framework calculates
a single continuous percentage score (0–100%) using the Adherence Multiplier.
The UI Hygiene score serves as the baseline quality metric, scaled directly by
the Material 3 Adherence rate.

### Step 1: UI Hygiene Score (%)

$$\text{UI Hygiene Score (\%)} = \left( \frac{\sum_{\text{Passed Hygiene}}
w_i}{\sum_{\text{Evaluated Hygiene}} w_i} \right) \times 100$$

*   `IF` no Hygiene criteria are evaluated (denominator = 0), `THEN`
    `hygiene_score` (`hygieneScore`) `MUST` default to `"N/A"`.

### Step 2: Material 3 Adherence Score (%)

$$\text{Material 3 Adherence Score (\%)} = \left(
\frac{\sum_{\text{Passed Adherence}} w_i}{\sum_{\text{Evaluated Adherence}} w_i}
\right) \times 100$$

*   `IF` no Adherence criteria are evaluated (denominator = 0), `THEN` the
    Adherence multiplier `MUST` default to `1.0` (`100%`) so the Final
    Compliance Score equals the UI Hygiene Score.

### Step 3: Final Compliance Score (%)

$$\text{Final Compliance Score (\%)} = \text{UI Hygiene Score (\%)} \times
\left( \frac{\text{Material 3 Adherence Score (\%)}}{100} \right)$$

*   The scorer `MUST` round all percentage scores (`hygiene_score` /
    `hygieneScore`, `adherence_score` / `adherenceScore`, `final_score` /
    `finalScore` / `score`) to the nearest whole integer.

--------------------------------------------------------------------------------

## 5. Thresholds & Interpretation Ranges

-   **85% – 100% (Production Ready / PASSED):** High UI polish combined with
    strict Material 3 adoption (`hygiene_score >= 85`, `adherence_score >= 85`,
    and `final_score >= 85`).
-   **50% – 84% (In Transition / NEEDS_REFINEMENT):** Clean layout and good
    hygiene, but contains custom styling, legacy components, or missing brand
    styles requiring remediation.
-   **0% – 49% (Non-Material / Custom App / NEEDS_REFINEMENT):** The application
    operates primarily on custom branding or non-standard components, resulting
    in low system adoption.

--------------------------------------------------------------------------------

## 6. Subcategory Score Calculation

Individual subcategory scores in the JSON compliance report (`app_bar_score`,
`color_score`, `fab_score`, `typography_score`, `navigation_bar_score`,
`layout_score`, `bottom_sheet_score`, `button_score`, `aurora_score` — or their
`camelCase` aliases `appBarScore`, `colorScore`, `fabScore`, `typographyScore`,
`navigationBarScore`, `layoutScore`, `bottomSheetScore`, `buttonScore`,
`auroraScore`) `MUST` be calculated using the exact same weighted formula
applied exclusively to criteria matching the respective category prefix:

| Subcategory Score Field    | Criteria Prefix  | Applicable Sources           |
:                            : Filter           :                              :
| :------------------------- | :--------------- | :--------------------------- |
| **`typography_score`**     | `[Typography]`   | Foundational `rubric.md`     |
| **`color_score`**          | `[Color]`        | Foundational `rubric.md`     |
| **`layout_score`**         | `[Layout]`       | Foundational `rubric.md`     |
| **`app_bar_score`**        | `[App bars]` or  | `rubrics/app-bars.md`        |
:                            : `[App bar]`      :                              :
| **`button_score`**         | `[Buttons]` or   | `rubrics/buttons.md`         |
:                            : `[Button]`       :                              :
| **`fab_score`**            | `[FABs]` or      | `rubrics/fabs.md`            |
:                            : `[FAB]`          :                              :
| **`navigation_bar_score`** | `[Nav Bars]`     | `rubrics/navigation-bars.md` |
| **`bottom_sheet_score`**   | `[Bottom Sheet]` | `rubrics/bottom-sheet.md`    |
| **`aurora_score`**         | `[Aurora]`       | `rubrics/aurora.md`          |

--------------------------------------------------------------------------------

## 7. Zero-Denominator & Absent Component Handling

`IF` a component was absent from the screen (or all evaluated criteria in that
subcategory returned `"N/A"`), `THEN` the possible points (denominator) for that
subcategory is `0`:

-   **Required Value:** The corresponding subcategory score field in the JSON
    output `MUST` be `"N/A"` (e.g., `"bottom_sheet_score": "N/A"` /
    `"bottomSheetScore": "N/A"`).
-   **Prohibited Value:** The scorer `MUST NOT` output `0` or `0%` for absent
    subcategories, because `0` indicates total compliance failure rather than
    component absence.
