---
title: "Final Run Through: Page Zoom"
gar_id: "Web 1.16(b)"
shortname: gar-web-run-through-page-zoom
keywords: [zoom, browser zoom, page zoom, low vision, reflow, single column, responsive]
---

     | Taglist
---- | -------
tags | #interaction-modes #design-focused #based-in-wcag-2-0 #based-in-en-301-549

# Final Run Through: Page Zoom

GAR 2026 | Formerly Web 1.16(b)

When the browser page is zoomed up to 200%, does all content reflow into a
single column without loss of information or functionality?

`Shortname`: gar-web-run-through-page-zoom

## **User impact of Final Run Through: Page Zoom**

### **Meeting this criterion**

1.  Enables **users with low vision** to view and interact with browser content
    in an enlarged way.

## **Overview of Final Run Through: Page Zoom**

Goal: Confirm all browser content, functionality, and features in your product
are usable with page zoom enabled. This adjusts the viewport size of web
content. It is acceptable for your content placement or layout to move but all
of the same content, functionality, and features must still be present. This
criteria is about zooming in a browser that does adjust viewport size, whereas
[GAR Web Final Run Through: Screen Magnified](http://go/gar-web-run-through-magnification)
is about magnifying the entire OS and does not adjust viewport size.

## **How to meet this criterion**

### **Principles:**

*   Confirm the application is also usable in Chrome and Firefox with page zoom
    enabled by 200% at a browser resolution of 1024x768 pixels. This width is
    the equivalent to resizing a browser window to 512 pixels, so using a
    responsive design and switching to a mobile layout when the window is that
    narrow (or smaller) is one acceptable way to make this work.
*   You must preserve the state of the page, including any user input and focus.
    Ensure that functionality remains when switching to the smaller layout.
*   Confirm that nothing within the application is cut off, overlaps,
    disappears, or is unusable and that the text and `UI` do in fact increase.
    *   It is okay for the placement or layout to move as a result of the larger
        size but the content needs to be available in a different place and
        behind accessible `controls`, if applicable.

Note: We are intentionally modifying
[`WCAG` SC 1.4.4](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-scale.html)
which requires that text can be resized up to 200% without loss of content or
functionality. Industry-wide browser and product website support for that change
isn’t well supported, and we expect WCAG’s SC (and this GAR criteria) to be
removed in the next few years. Until then, we are prioritizing browser zoom at
200%, which effectively yields the same results and scales text but in a more
reliable manner. This is also a temporary holdover while teams work to support
400% zoom and
[GAR Web: PW Responsive Design](http://go/gar-web-responsive-design).

### **UX and Engineers: How to design/build Final Run Through: Page Zoom**

Designers and developers should accommodate users who resize text, images, and
increase layout regions. Consider how the layout and buttons re-render in the
enlarged area. You should support an increase of 200%. Refer to the
[Resizing Text article](https://carbon.googleplex.com/google-material/pages/resizing-text)
for guidance on applying enlarged text to designs.

*   Remove the `user-scalable="no"` parameter from the content attribute of the
    `<meta name="viewport">` to allow zooming and ensure the maximum-scale
    parameter is ≥2 to support 200%. The higher you set the maximum-scale
    parameter, the higher zoom you will support. As of the time of this writing
    (August 2025), Chrome and Firefox both support page zoom up to 500%, and
    Safari supports up to 300% so consider supporting up to 500%.
    *   A meta viewport element tells the browser how to control the page's
        dimensions and to scale, but the ability to zoom can be prevented
        because of its use.
*   Do not prevent page-level horizontal or vertical scrolling.

### Good Code Examples

```html
<!-- Meta Viewport allowing zoom -->
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5">
</head>

<!-- Using relative units (em, rem, %) for sizing and spacing -->
<style>
  body { font-size: 16px; }
  .container { width: 100%; max-width: 1200px; padding: 1rem; }
  h1 { font-size: 2rem; margin-bottom: 1rem; }
  button { padding: 0.5em 1em; font-size: 1em; }
</style>

<!-- Flexbox/Grid for layout reflow -->
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <div style="flex: 1 1 300px;">Content Block 1</div>
  <div style="flex: 1 1 300px;">Content Block 2</div>
</div>

<!-- Media queries to adjust layout at zoom levels (simulated by width) -->
<style>
  @media (max-width: 512px) { /* Corresponds to 1024px at 200% zoom */
    .menu { display: none; } /* Hide complex menu */
    .hamburger-menu { display: block; } /* Show mobile menu trigger */
  }
</style>
```

### Code Examples to Avoid

```html
<!-- Preventing user scaling -->
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
</head>

<!-- Restricting maximum scale too much -->
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.5">
</head>

<!-- Fixed heights on containers with text content -->
<div style="height: 50px; overflow: hidden;">
  <p>This text might get cut off when zoomed as it grows beyond the fixed height.</p>
</div>

<!-- Absolute positioning that breaks layout on zoom -->
<div style="position: relative; height: 100px;">
  <button style="position: absolute; bottom: 5px; right: 5px;">
    Might overlap other content or become hard to use when zoomed.
  </button>
</div>

<!-- Elements that don't scale, causing layout issues -->
<input type="text" style="font-size: 10px;"> <!-- Will be tiny and hard to read/use when page is zoomed -->
```

### **Testers: How to test Final Run Through: Page Zoom**

*   Run [Parashu](http://go/parashu) to detect
    [some cases of inaccessible page zoom](http://go/accessibility-checker/gar-tags#gar5.1.16b)
    such as detecting whether zooming and scaling is disabled or whether
    clickable elements fail to increase in size when the page is zoomed to 200%.

Note: Parashu does not detect all page zoom related issues such as zooming using
keyboard controls, or detecting cases of overlapping content due to page zoom.
Follow the remaining steps to manually verify all cases of page zoom related
accessibility issues.

Confirm your product is usable in the latest versions of Chrome and Firefox at a
size of 1024x768 at 200%.

*   Manual testing option one: Use
    [Google’s internal Web Team’s Page Zoom Test (go/webtesting-accessibility),](/ads/common/testing/web/g3doc/user-guide/accessibility/zoom/index.md)
    code in a config file. This enables developers to set zoom scale while
    defaulting to the GAR-specified window size for testing Chrome, Firefox, and
    IE.
*   Manual testing option two: Press the keyboard command/control button and
    the + button until the screen is zoomed to 200%.
*   You can also set this in preferences by:
    *   Chrome > Preferences > Appearance > Page Zoom
    *   Firefox > Preferences > General > Zoom
    *   Safari > Preferences > Websites > Page Zoom > When visiting other
        websites
