---
title: "Final Run Through: Screen Magnified"
gar_id: "Web 1.16(a)"
shortname: gar-web-run-through-magnification
keywords: [magnification, zoom, OS level, low vision, visibility, screen magnifier]
---

     | Taglist
---- | -------------------------------------------------------
tags | #design-focused #interaction-modes #based-in-en-301-549

# Final Run Through: Screen Magnified

GAR 2026 | Formerly Web 1.16(a)

Is all content and functionality visible and usable when the screen is magnified
up to 400%?

`Shortname`: gar-web-run-through-magnification

## **User impact of Final Run Through: Screen Magnified**

### **Meeting this criterion**

1.  Supports **users with low vision** and **users of smaller devices** who may
    need OS level `screen magnification` to access the content, functionality,
    and features of your product in an enlarged `UI`.

### **Potential user impact of failing**

More details on the potential user impact of failing

*   **Risk: Unusable Product** <br/>
    If content cannot be magnified at the OS level, users with low vision who
    rely on magnification will not be able to access your product
    successfully.

## **Overview of Final Run Through: Screen Magnified**

Goal: Confirm all content and functionality in your product is usable with
magnification enabled at the OS level. This criteria is about magnifying the
entire OS and does not adjust viewport size, whereas
[GAR Web Final Run Through: Page Zoom](http://go/gar-web-run-through-page-zoom)
is about zooming in a browser that does adjust viewport size.

### Good Code Examples

```html
<!-- Content within the natural flow, no fixed positioning to obscure things -->
<body>
  <header>...</header>
  <main>
    <h1>Welcome</h1>
    <p>This content will scale well with OS magnification.</p>
  </main>
  <footer>...</footer>
</body>

<!-- Using relative units for text as a base -->
<style>
  body { font-size: 100%; }
  h1 { font-size: 2em; }
  p { font-size: 1em; }
</style>

<!-- Tooltips or popups that follow their trigger -->
<!-- (Handled by OS magnifier, ensure they don't detach) -->
<button aria-describedby="descId">Hover Me</button>
<div id="descId" role="tooltip">Tooltip content</div>
```

### Code Examples to Avoid

```html
<!-- Fixed position elements that can obscure content when magnified -->
<div style="position: fixed; bottom: 0; right: 0; background: lightgray; padding: 10px;">
  This might cover important content when zoomed.
</div>

<!-- Reliance on mouse hover to reveal critical information that's hard to target when magnified -->
<div class="hover-reveal">
  Hover to see details
  <span class="details">Critical Info!</span>
</div>
<style>
  .details { display: none; }
  .hover-reveal:hover .details { display: block; }
</style>

<!-- Extremely small click targets -->
<button style="font-size: 8px; padding: 1px;">Tiny Button</button>

<!-- Content that becomes unscrollable or cut off -->
<div style="width: 100vw; height: 100vh; overflow: hidden;">
  <div style="width: 200vw; height: 200vh;">
    Much content here, may be hard to navigate when OS zoomed.
  </div>
</div>
```

### **Testers: How to test Final Run Through: Screen Magnified**

*   Follow the specific steps relevant to ChromeOS, macOS, and Windows OS:
    *   [ChromeOS magnify](https://support.google.com/chromebook/answer/6320705?hl=en&ref_topic=9016892)
    *   [MacOS zoom](https://support.apple.com/en-us/HT210978)
    *   [Windows OS magnify](https://support.microsoft.com/en-us/windows/use-magnifier-to-make-things-on-the-screen-easier-to-see-414948ba-8b1c-d3bd-8615-0e5e32204198)
*   Ensure that your application content and functionality is preserved in
    Chrome and Firefox. You should observe that the screen is magnified, but the
    page layout should not change.
*   Revert to your original magnification level after completing this test.
