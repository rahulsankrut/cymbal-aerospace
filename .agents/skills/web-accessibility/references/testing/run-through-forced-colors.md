---
title: "Final Run Through: forced-colors"
gar_id: "Web 1.16(d)"
shortname: gar-web-run-through-forced-colors
keywords: [forced colors, high contrast, windows high contrast, color palette, visibility, low vision]
---

     | Taglist
---- | ------------------------------------
tags | #design-focused #based-in-en-301-549

# Final Run Through: forced-colors (encountered by way of High Contrast Black on Windows)

GAR 2026 | Formerly Web 1.16(d)

Is all content and functionality visible and usable when Windows High Contrast
mode (or `forced-colors` mode) is active?

`Shortname`: gar-web-run-through-forced-colors

## **User impact of Final Run Through: forced-colors**

### **Meeting this criterion**

1.  Supports **users who prefer strongly `contrasting` colors** and **users who
    have low vision** and may need forced-colors/`High Contrast Black` Mode to
    efficiently read and consume content.

### **Potential user impact of failing**

More details on the potential user impact of failing

*   **Risk: Unusable Product** <br/>
    If your product does not support forced-colors or High Contrast Black (on
    Windows), users with low vision who rely on these features to perceive
    content will not be able to view content or navigate controls, resulting in
    an unusable product.

## **Overview of Final Run Through: forced-colors**

Goal: Support forced-colors/High Contrast Black Mode.

When
[forced-colors](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)
is enabled, users select a small palette of colors that overrides nearly all
colors specified in web pages. The most common way this is encountered is in
High Contrast Black (HCB) on Windows in Chrome. You can
[test High Contrast Black on any platform using Chrome DevTools](https://developer.chrome.com/blog/new-in-devtools-98/#forced-colors)
in Chrome 98 and above.

Chrome’s implementation of HCB (starting from Chrome 89) preserves most
background images, text is rendered with a "backplate", a background that helps
to ensure adequate contrast for readability, and you can use CSS to detect this
mode and override it so fixes are much easier than in the past. Firefox has also
matched this behavior as of Firefox 89.

If your product cannot support forced-colors (e.g., you develop on WebGL and
Canvas 2D), you will need to ensure support for High Contrast Black on Windows.

## **How to meet this criterion**

### **Proper implementations of forced-colors:**

1.  While enabling the system level High Contrast Black theme in Windows, the
    user selects their background color as black. While accessing a web page
    from Chrome and without changing any other settings, the background
    correctly renders in black.
2.  It is okay to override forced-colors for a color picker, color palette,
    logos, flags, real-life photos, product screenshots, scientifically used
    colors such as a heatmap or medical presentations, or any other graphics or
    images where presenting the actual “original” color is significant or
    essential.

### **Improper implementations of forced-colors:**

1.  Grey favorite buttons may disappear in High Contrast mode due to CSS
    conflicts with High Contrast mode.
2.  Pop-ups or dialogs that have a border in the “light” mode lose their borders
    with forced-colors enabled.

### **UX: How to design Final Run Through: forced-colors**

*   If shadows are used for elevation in the default mode, they may get dropped
    with forced-colors enabled. Pop-ups or dialogs typically lose their borders,
    and shadow effects disappear, so design with
    [alternative attributes to shadows and outlines](https://docs.google.com/presentation/d/1gSgrS0VOf-ydZCxeaQXnbkF4bkB0MdBFujKUWdRkqqM/edit#slide=id.g4e02695857_1_31).
*   Review go/high-contrast,
    [High Contrast Fix guideline](https://docs.google.com/document/d/1_1LWDZ407ixoHA-aGytQBUllSW5Z-wcm7F3m2-TNR38/edit#heading=h.9hzkcc6uen0m),
    and, if testing Firefox, the WIP go/firefox-hcm-testing doc. Also, download
    the
    [High Contrast Mode Chrome Extension](https://chrome.google.com/webstore/detail/high-contrast/djcfdncoelnlbldjfhinnjlhdjlikmph?hl=en)
    to ensure that designs translate well in a limited palette (i.e. black and
    white, etc.).
*   Supporting forced-colors for Chrome and High Contrast Black on Windows is
    required if you are developing with CSS/HTML. Canvas 2D and WebGL support is
    still in progress so for these implementations (or other feasibility
    concerns your Eng team raises) you will need to ensure your color palette
    will work in High Contrast Black mode.
*   Read
    [MDN's CSS forced-colors overview](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/forced-colors)
    and
    [Windows’ styling high contrast for forced colors blog](https://blogs.windows.com/msedgedev/2020/09/17/styling-for-windows-high-contrast-with-new-standards-for-forced-colors/).
    *   The properties the MDN article calls out as having “special behavior” in
        forced-colors mode especially need to be accounted for.

### **Engineers: How to build Final Run Through: forced-colors**

*   Supporting forced-colors for Firefox, Chrome, and High Contrast Black on
    Windows is required if you are developing with CSS/HTML. Canvas 2D and WebGL
    support is still in progress so for these implementations (or other
    feasibility concerns your team raises) you will need to ensure your color
    palette will work in High Contrast Black mode.
*   Refer to go/high-contrast.
    *   If you are unable to implement forced-colors, you will need to partner
        with your designers to ensure your color palette will work in High
        Contrast Black mode.

### Good Code Examples

```css
/* Using system colors for compatibility */
.button {
  border: 1px solid transparent; /* Initially transparent */
  background-color: Canvas;
  color: CanvasText;
}

/* Ensure focus indicators are visible */
.button:focus {
  outline: 2px solid Highlight;
  outline-offset: 2px;
}

/* Example of preserving a color picker */
.color-swatch {
  forced-color-adjust: none;
}

/* Using SVG icons that can inherit system colors */
.icon {
  fill: currentColor;
}

/* Adding borders for elements that rely on background color differences */
@media (forced-colors: active) {
  .card {
    border: 1px solid Highlight;
  }
  .selected-item {
    outline: 1px dashed Highlight;
  }
}
```

```html
<button class="button">Action</button>

<div class="color-picker">
  <div class="color-swatch" style="background-color: red;"></div>
  <div class="color-swatch" style="background-color: blue;"></div>
</div>

<svg class="icon" role="presentation"> <path d="..."/> </svg>

<div class="card">Card Content</div>
<div class="selected-item">Selected</div>
```

### Code Examples to Avoid

```css
/* Relying on background-color to differentiate elements */
.status-ok { background-color: lightgreen; }
.status-warn { background-color: lightyellow; }
/* These will likely look the same in forced colors mode */

/* Invisible borders or outlines in default mode */
.transparent-button {
  border: 1px solid white; /* Invisible on white background */
  background: white;
  color: black;
}
/* May become completely invisible if Canvas is white */

/* Using background images for essential icons or borders */
.icon-bg {
  background-image: url('icon.png');
  width: 24px; height: 24px;
}
/* Background images may be turned off */

/* Overriding system colors in a way that breaks contrast */
@media (forced-colors: active) {
  .bad-button {
    background-color: black !important;
    color: black !important; /* Text becomes invisible */
  }
}
```

### **Testers: How to test Final Run Through: forced-colors**

[How To Activate High Contrast In Windows video](https://broadcast.corp.google.com/ui/player/01a90f35-ae07-420d-b0ca-5f1a0d5f6f40)
(52 seconds)

[How To Activate High Contrast Mode in Chrome video](https://broadcast.corp.google.com/ui/player/cf7c7871-4a0d-4b24-a41d-45cf76e1da78)
(1 minute 9 seconds)

[What to Look For While Performing High Contrast Testing video](https://broadcast.corp.google.com/ui/player/609912c8-f4a2-4ee6-aca7-15eef9b795ce)
(1 minute 15 seconds)

*   On any platform, you can
    [test High Contrast Black via Chrome DevTools](https://developer.chrome.com/blog/new-in-devtools-98/#forced-colors)
    in Chrome 98 and above.
    *   In Chrome 98 and higher:
        *   Open Chrome, observe that much of your application's theme has been
            overridden and is now displayed in white-on-black with links in
            yellow.
        *   Ensure that icons, and `sprites` in particular, are still visible in
            Chrome.
*   For Windows testing:
*   Enable the default
    [High Contrast mode on Windows](https://support.microsoft.com/en-us/windows/use-high-contrast-mode-in-windows-10-fedc744c-90ac-69df-aed5-c8a90125e696),
    then use Chrome to verify the contrast changes.
    *   High Contrast Black theme from Settings > Ease of Access > High
        contrast > Turn on high contrast, or using the shortcut “Left Alt + Left
        Shift + PrintScreen”. You can verify this has been applied by observing
        that the whole OS now has a bright white on black theme with almost no
        grays, with links in yellow and selected text in cyan.
        *   In Chrome 89 and higher:
            *   Open Chrome, observe that much of your application's theme has
                been overridden and is now displayed in white-on-black with
                links in yellow.
            *   Ensure that icons, and sprites in particular, are still visible
                in Chrome. If your PA supports Edge, you should also confirm
                icons and sprites are still visible.
            *   In Chrome, and if you support Edge, ensure that the
                forced-colors are overridden where that would make sense (as an
                example, if a user is picking the color of a phone to purchase,
                those color swatches should be preserved).
*   Review the UI:
    1.  Use keyboard navigation to Interact with all focusable content and
        verify all visible aspects of the UI are present.
    2.  Navigate the UI using the mouse to interact with elements to ensure all
        visible aspects of the UI are present
*   Verify that all visible aspects of a `UI` that are available in the default
    mode, such as focus indicators, control outlines on list boxes and edit text
    areas, are present and meaningful in HCB, despite the limited color palette.
    Components and `controls` should still function and be displayed
    consistently, legibly, and the UI should be understandable.

    For example, the following two screenshots, one utilizing HCM and the other
    at typical contrast, each contain two buttons side-by-side. The first button
    says “No thanks”, and the second button says “Show question.” In the HCM
    screenshot, the focus indicator is invisible.

    ![Two buttons at typical contrast. The left button is labeled "No thanks" and highlighted, the right button is labeled "Show question".](/company/teams/gar/images/web-1-16d-1.png)

    ![The same buttons (labeled "No thanks" and "Show question") in High Contrast Mode. The focus indicator on the "No thanks" button is invisible.](/company/teams/gar/images/web-1-16d-2.png)

*   If shadows are used for elevation in the default mode, you should ensure
    that an alternative is present with forced-colors enabled. Pop-ups or
    dialogs typically lose their borders, and shadow effects disappear, so
    please verify these carefully if they exist in your product.
