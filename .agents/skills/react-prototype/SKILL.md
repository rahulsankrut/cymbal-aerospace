---
name: react-prototype
description: >-
    Build an interactive multi-screen React prototype from existing screen
    mockups as a single self-contained HTML file using CDN-hosted libraries. Use
    only when the user explicitly asks to combine existing static screens into a
    clickable prototype; never use for initial screen design (use
    hifi-mockup-kit instead).
---

# React Prototype (CDN)

## Overview

Build an interactive, navigable prototype from the provided screen designs. The
output is a **single self-contained HTML file** that uses CDN-hosted React,
ReactDOM, and Tailwind CSS. No build tools, no npm, no sandbox filesystem —
everything is inline.

## Mandatory Boilerplate

Every generated HTML file MUST start with this exact boilerplate. Do NOT change
the CDN URLs, do NOT remove any script tags, and do NOT add `type="module"` to
the Babel script tag.

```html
<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APP_TITLE</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- React 18 via CDN -->
  <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

  <!-- Babel for in-browser JSX -->
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body class="min-h-screen bg-white">
  <div id="root"></div>
  <script type="text/babel">
    // ALL React code goes here
  </script>
</body>
</html>
```

### Critical Layout Rule

Use `min-h-screen` (not `h-full` or `h-screen`) on the `<body>` and root layout
elements. In `srcdoc` iframes, percentage-based heights resolve to 0px because
there is no fixed-height ancestor. `min-h-screen` uses `100vh` which works
correctly.

## Workflow

1.  **Read screens** — View the HTML of each screen from the
    project's `screens/` directory.
2.  **Generate** — Create a single HTML file following the boilerplate above.
    Faithfully reproduce the screens' layout, styling, and content.
3.  **Write the file** — Write an artifact:
    `<workspace-root>/screens/<screen-id>/Prototype.html`
4.  **Respond** — Reply with a brief summary. Do NOT include HTML code in your
    response.

## Behavioral Rules

1.  ALL code (HTML, CSS, JS/JSX) goes in a **single file**. No imports, no
    external files, no build step.
2.  Use Tailwind CSS utility classes for all styling.
3.  **Faithfully** reproduce the input screen designs. Do NOT add features,
    animations, sound effects, or content not present in the originals.
4.  Use React functional components with hooks for state management.
5.  For multi-screen prototypes, implement client-side routing using a simple
    state variable (no react-router needed in CDN mode):

    ```jsx
    const [page, setPage] = React.useState('home');
    // Render different components based on `page`
    ```

6.  Mock all data — do NOT add real API calls or external data fetching.

7.  Do NOT use `localStorage`, `sessionStorage`, `cookies`, or `indexedDB` — the
    app runs in a sandboxed iframe where these are blocked.

8.  Preserve image file paths from the original screens. Images are generated
    by the image pipeline and referenced as local file paths — carry them over
    unchanged. Do NOT replace them with external URLs (Unsplash, Picsum,
    placehold.co, etc.) — external URLs will not render.

9.  Do NOT use `data:image` URIs — they bloat the output.

10. Wire up all navigation elements (links, buttons) to page state changes.

11. Implement basic state for interactive elements (modals, tabs, forms).

## Quality Checklist

Before writing the output, verify:

-   [ ] Boilerplate matches the template exactly (CDN URLs, Babel tag)
-   [ ] `min-h-screen` used instead of `h-full` on body and root layouts
-   [ ] All screens are implemented and navigable
-   [ ] Tailwind classes used for all styling
-   [ ] No localStorage/sessionStorage/cookies usage
-   [ ] No data:image URIs
-   [ ] Output written as an artifact
-   [ ] Response does not contain HTML code
