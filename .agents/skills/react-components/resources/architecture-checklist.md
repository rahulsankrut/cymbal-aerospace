# Architecture Quality Gate

### Structural integrity

-   [ ] Logic extracted to custom hooks in `src/hooks/`.
-   [ ] No monolithic files; strictly Atomic/Composite modularity under
    `src/components/`.
-   [ ] All static text/URLs moved to `src/data/mockData.ts`.

### Type safety and syntax

-   [ ] Props declare `[ComponentName]Props` with `readonly` properties (or
    `Readonly<T>`).
-   [ ] File is syntactically valid TypeScript (`npx tsc --noEmit` passes with
    no unused imports or errors).
-   [ ] Placeholders from templates (e.g., `StitchComponent`) have been replaced
    with actual names.

### Styling and theming

-   [ ] Dark mode (`dark:`) applied to all color classes.
-   [ ] No hardcoded hex values; use theme-mapped Tailwind classes synced with
    `style-guide.json`.
