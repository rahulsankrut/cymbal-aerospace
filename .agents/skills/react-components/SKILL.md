---
name: react-components
description: >-
  Converts Stitch screen HTML designs from `/workspace/screens/`
  into modular Vite, React, TypeScript, and Tailwind CSS components with
  automated static validation.
---

# Stitch to React Components (`react-components`)

You are a frontend engineer focused on transforming Stitch screen designs into
clean, modular React + TypeScript + Tailwind CSS code inside `/workspace`.

## Skill Assets (`<skill-dir>`)

This skill folder (`<skill-dir>`, located at
`/home/stitch_design/skills/design-to-code/react-components` in the DevBox VM)
is **read-only** (`root:root`). Never write files back into `<skill-dir>`; write
all project files into `/workspace/` using `run_command` (`cat <<'EOF' > ...`),
since the Stitch Actor's `write_to_file` tool is reserved for single-file Stitch
HTML screen artifacts.

-   **Component Template**: `<skill-dir>/resources/component-template.tsx`
-   **Gold Standard Example**: `<skill-dir>/examples/gold-standard-card.tsx`
-   **Base Style Guide**: `<skill-dir>/resources/style-guide.json`
-   **Architecture Checklist**:
    `<skill-dir>/resources/architecture-checklist.md`
-   **Component Validator**: `<skill-dir>/scripts/validate.js`

## Screen Retrieval

1.  **Read from VM workspace (`/workspace/screens/`)**:
    -   Read the target screen HTML files (and screenshots/assets if present)
        directly from `/workspace/screens/{screen_id}/*.html` using `view_file`
        or `run_command`.
2.  **Design audit**:
    -   Inspect each screen HTML file in `/workspace/screens/{screen_id}/` to
        confirm layout structure, typography, color tokens, and component
        boundaries.

## Architectural Rules

*   **Modular components**: Break the design into independent Atomic/Composite
    files under `src/components/`. Avoid monolithic single-file outputs.
*   **Logic isolation**: Move event handlers and business logic into custom
    hooks in `src/hooks/`.
*   **Data decoupling**: Move all static text, image URLs, and lists into
    `src/data/mockData.ts`.
*   **Type safety**: Every component must declare a TypeScript interface named
    `[ComponentName]Props` with `readonly` properties (or wrapped in
    `Readonly<T>`).
*   **Style mapping & dark mode**:
    *   Extract the `tailwind.config` theme values (colors, fonts, spacing) from
        the screen HTML `<head>`.
    *   Merge those tokens with `<skill-dir>/resources/style-guide.json` and
        write the project's synced `/workspace/style-guide.json` and
        `/workspace/tailwind.config.js`.
    *   Use theme-mapped Tailwind classes (with `dark:` variants applied to
        color classes) instead of arbitrary hex codes (`bg-[#...]`).

## Execution Steps

1.  **Project setup**:
    -   In `/workspace`, ensure a Vite + React + TypeScript + Tailwind CSS
        project structure exists (`package.json`, `tsconfig.json`,
        `vite.config.ts`, `tailwind.config.js`, `index.html`, `src/main.tsx`,
        `src/App.tsx`). If `node_modules` is missing in `/workspace`, run `npm
        install` via `run_command`.
2.  **Data layer**:
    -   Create `/workspace/src/data/mockData.ts` containing all structured text,
        links, and mock items extracted from the screen HTML.
3.  **Component drafting**:
    -   Review `<skill-dir>/examples/gold-standard-card.tsx` as the reference
        implementation.
    -   Use `<skill-dir>/resources/component-template.tsx` as a base, replacing
        all instances of `StitchComponent` with the actual component name.
4.  **Application wiring**:
    -   Update `/workspace/src/App.tsx` to assemble and render the generated
        components.
5.  **Quality check**:

    -   Run the zero-dependency validator script on every generated component
        file:

        ```bash
        node /home/stitch_design/skills/design-to-code/react-components/scripts/validate.js /workspace/src/components/<ComponentName>.tsx
        ```
    -   Verify the final output against
        `<skill-dir>/resources/architecture-checklist.md`.
    -   Verify TypeScript compilation and production bundling cleanly terminate
        (do **not** run `npm run dev` in the foreground, as `run_command` is
        synchronous and will hang):

        ```bash
        npx tsc --noEmit && npx vite build
        ```

## Troubleshooting

*   **Validation errors**: Review the output of `scripts/validate.js` and fix
    any missing `[ComponentName]Props` interfaces, unreplaced `StitchComponent`
    placeholders, or hardcoded hex color codes.
