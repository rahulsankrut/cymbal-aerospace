# Contributing to the Web Accessibility Skill

This guide defines the mandatory file architecture, section templates, and
anti-duplication rules for `web_accessibility`. Every contributor—human or AI
agent—must follow these rules when adding or updating guidance.

## 1. Core Architectural Principles

1.  **Key on GAR 2027 Shortnames & Checkpoints (`http://go/gar-web` &
    `http://go/gar-checkpoints`):** Always reference official `gar-web-*`
    shortnames (e.g., `gar-web-accessibility-labels`, `gar-web-clear-purpose`,
    `gar-web-keyboard`) and GAR 2027 Checkpoints. Never use deprecated numeric
    identifiers (`GAR 1.1`, `GAR 1.2`, `GAR 1.11`).
2.  **1-Hop Progressive Disclosure & 800-Line Limit (`b/563096728`):** Every
    reference file in `references/` and `references/frameworks/` must be linked
    directly (1 hop) from `SKILL.md`. Keep `SKILL.md` under 200 lines (hard
    platform ceiling: 800 lines / 46,080 bytes) and keep each reference file
    under 200 lines.
3.  **Orthogonal Two-Layer Multi-Framework Architecture:**
    -   **Type 1 (Surface Attribute & i18n Syntax by Filename):** Documented in
        the compact **File Extension $\rightarrow$ Attribute & Localization
        Syntax Matrix** inside `SKILL.md`.
    -   **Type 2 (Deep Framework Component & Lifecycle Mechanics):** Documented
        in `references/frameworks/<framework>.md`.
    -   **Keep Topic Files Framework-Agnostic:** Code blocks in
        `references/<topic>.md` must use standard HTML, CSS, and JavaScript
        only. Never embed `.soy`, `.acx.html`, `.ng.html`, Lit, or Flutter code
        blocks inside topic files; place them in the matching
        `references/frameworks/*.md` file and add at most a 1-line pointer in
        the topic file.

## 2. Mandatory 4-Section Template for Topic Files (`references/<topic>.md`)

Every topic reference file (`accessible-names.md`, `keyboard.md`, `focus.md`,
`structure.md`, `forms.md`, `interaction-patterns.md`, `visuals.md`, `media.md`,
`updates-with-screen-reader.md`) must contain **only** these four top-level
numbered sections in this exact order:

```markdown
---
title: <Topic Title> (<gar-web-* shortnames>)
shortname: <primary-gar-web-shortname>
priority: MANDATORY_CRITICAL | HIGH
---

# <Topic Heading>

<1-sentence summary of the core accessibility goal.>

## 1. GAR Checkpoints & Core Rules

- **<Checkpoint / Criterion Name> (`<gar-web-shortname>`):** Imperative rules
  explaining *what* is required and *why* (user/AT impact). Omit tool history
  or background prose.

## 2. Decision Matrix

| Scenario / Component / Rank | Required Pattern | When to Use / Rationale |
| :--- | :--- | :--- |
| ... | ... | ... |

## 3. Implementation Patterns

### <Component or Interaction Header>

Group native default patterns and custom fallbacks under the same component
header using concise `<!-- GOOD -->` and `<!-- BAD -->` HTML/CSS/JS examples.

## 4. Blockers (Auto-Fail)

1. **<Blocker Name> (`<automated-rule-id>`):** Concrete anti-pattern or
   container trap that must never appear in generated or refactored code.
```

## 3. Mandatory 4-Section Template for Framework Files (`references/frameworks/<framework>.md`)

Every framework file (`angular-ts.md`, `dart-angulardart.md`, `soy-closure.md`,
`lit-polymer-wiz.md`, `flutter.md`) must contain **only** these four top-level
numbered sections:

1.  `## 1. Target File Extensions & Scope`: File extensions (`.ng.html`,
    `.acx.html`, `.dart`, `.soy`, `.ts`) and UI libraries covered.
2.  `## 2. Attribute Binding & Localization (i18n)`: Exact binding syntax for
    `aria-*`, `role`, `tabindex`, and mandatory localization wrappers
    (`i18n-aria-label`, `Intl.message`, `{msg}`).
3.  `## 3. Component Library Gotchas & Container Traps`: How composite
    components bind inner interactive targets vs. host containers (e.g.,
    `[buttonAriaLabel]`, `extraTriggerAttributes`, `<mat-label>` double-naming
    removal).
4.  `## 4. Focus & Async Lifecycle Management`: Post-render/animation focus
    restoration hooks, static typing (`@ViewChild(read: HtmlElement)`), and
    minimal-diff discipline.

## 4. "Integrate, Never Append" Editing Rules

When adding guidance for a new bug pattern or GAR checkpoint:

-   **Fold into existing sections:** Add new rules to `## 1. GAR Checkpoints &
    Core Rules`, new ranking/selection rows to `## 2. Decision Matrix`, new HTML
    code snippets under the matching component header in `## 3. Implementation
    Patterns`, and new traps/anti-patterns to `## 4. Blockers (Auto-Fail)`.
-   **Never append ad-hoc top-level sections:** Do not create `## 5. Special
    Rule for X` or standalone subsections for anti-patterns inside Section 3.
-   **Single Source of Truth (No Intra-File or Cross-File Duplication):**
    -   Do not repeat the `## 4. Blockers` list inside Section 1 ("Stop Words
        Problem") or Section 3 ("Container Trap").
    -   Do not duplicate link-naming rules (`gar-web-clear-purpose`) inside
        `structure.md`; all naming, alt text, and link/control purpose rules
        live in `accessible-names.md`.

## 5. Validation & Evaluation

Before mailing any CL that modifies this skill or its references:

```bash
/google/bin/releases/arca9-local-blaze-cli/blaze-for-agents test //learning/gemini/agents/skills/accessibility/web_accessibility:validate_web_accessibility_skill_test
/google/bin/releases/gemini-agents-evalin/evalin compare learning/gemini/agents/skills/accessibility/web_accessibility/EVAL.txtpb --baseline-workspace=head --num-runs=3
```
