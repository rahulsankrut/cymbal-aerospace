<!-- disableFinding(HTML_BROKEN) -->
<!-- disableFinding(LINE_OVER_80) -->

# Geometric Disambiguation Matrices

This delegate reference file defines the 4 Geometric Disambiguation Matrices
used by the `ui-detector` skill during Passes 1–3 of the Coarse-to-Fine Spatial
Scan.

--------------------------------------------------------------------------------

## Matrix 1: Horizontal & Vertical Bars

| Viewport Anchor  | Child Item       | Primary           | `functionalAliases` & |
: & Container      : Anatomy          : `mappedComponent` : Deviation Directive   :
: Geometry         :                  :                   :                       :
| :--------------- | :--------------- | :---------------- | :-------------------- |
| Top-anchored     | Screen title,    | **`App bar`**     | `IF` a top horizontal |
: horizontal strip : brand wordmark,  :                   : strip anchored to the :
: (opaque,         : leading nav      :                   : top viewport edge     :
: transparent, or  : `Icon button`,   :                   : contains              :
: surface-matched) : `Search bar`,    :                   : navigation/action     :
:                  : trailing action  :                   : `Icon button`s, title :
:                  : `Icon button`s,  :                   : text, `Search bar`,   :
:                  : or `Avatar`      :                   : or `Avatar`           :
:                  :                  :                   : (including iOS 26+    :
:                  :                  :                   : `UINavigationBar`     :
:                  :                  :                   : trailing              :
:                  :                  :                   : `UIBarButtonItem`s    :
:                  :                  :                   : enclosed in a shared  :
:                  :                  :                   : system Liquid Glass   :
:                  :                  :                   : pill/capsule          :
:                  :                  :                   : platter), `THEN` the  :
:                  :                  :                   : agent `MUST` emit     :
:                  :                  :                   : parent **`App bar`**  :
:                  :                  :                   : AND each individual   :
:                  :                  :                   : child control (`Icon  :
:                  :                  :                   : button`, `Search      :
:                  :                  :                   : bar`, `Avatar`)       :
:                  :                  :                   : (`MUST NOT` emit      :
:                  :                  :                   : `Button group`,       :
:                  :                  :                   : `Segmented button`,   :
:                  :                  :                   : or `Toolbar` for top  :
:                  :                  :                   : bar action platters); :
:                  :                  :                   : `ELSE IF` a header    :
:                  :                  :                   : row (e.g. place title :
:                  :                  :                   : `"Golden Gate         :
:                  :                  :                   : Bridge"` + Share /    :
:                  :                  :                   : Close `'X'` buttons)  :
:                  :                  :                   : sits inside a         :
:                  :                  :                   : **`Bottom sheet`**    :
:                  :                  :                   : overlaid over a map   :
:                  :                  :                   : canvas, `THEN` the    :
:                  :                  :                   : agent `MUST` classify :
:                  :                  :                   : it as a **`Bottom     :
:                  :                  :                   : sheet`** header       :
:                  :                  :                   : (`MUST NOT` emit      :
:                  :                  :                   : **`App bar`**);       :
:                  :                  :                   : `ELSE` classify       :
:                  :                  :                   : standalone top        :
:                  :                  :                   : elements by their     :
:                  :                  :                   : individual container  :
:                  :                  :                   : geometry.             :
| Bottom           | 3–5 persistent   | **`Navigation     | `IF` a bottom         |
: full-width       : top-level        : bar`**            : container is an       :
: docked bar (100% : destinations     :                   : elevated floating     :
: viewport width,  : (`Icon` + label, :                   : stadium/pill with     :
: flush edges;     : active pill      :                   : inset outer margins,  :
: `MUST NOT` be an : indicator)       :                   : `THEN` the agent      :
: elevated         :                  :                   : `MUST NOT` classify   :
: floating pill    :                  :                   : it as **`Navigation   :
: with inset       :                  :                   : bar`** (these `MUST`  :
: margins)         :                  :                   : be classified as      :
:                  :                  :                   : **`Toolbar`**); `ELSE :
:                  :                  :                   : IF` a bottom          :
:                  :                  :                   : full-width flush bar  :
:                  :                  :                   : houses persistent     :
:                  :                  :                   : top-level navigation  :
:                  :                  :                   : destinations, `THEN`  :
:                  :                  :                   : the agent `MUST` emit :
:                  :                  :                   : parent **`Navigation  :
:                  :                  :                   : bar`** AND child      :
:                  :                  :                   : destination controls  :
:                  :                  :                   : (`Icon button` /      :
:                  :                  :                   : `Icon`) plus any      :
:                  :                  :                   : attached `Badge`;     :
:                  :                  :                   : `ELSE` the agent      :
:                  :                  :                   : `MUST` evaluate the   :
:                  :                  :                   : bar as a `Bottom App  :
:                  :                  :                   : Bar`.                 :
| Bottom           | Contextual       | **`Bottom App     | `IF` a bottom         |
: full-width       : action `Icon     : Bar`**            : full-width bar houses :
: docked bar with  : button`s +       :                   : contextual screen     :
: contextual       : optional         :                   : actions rather than   :
: actions          : inset/cradled    :                   : persistent top-level  :
:                  : `FAB`            :                   : destinations, `THEN`  :
:                  :                  :                   : the agent `MUST`      :
:                  :                  :                   : classify it as        :
:                  :                  :                   : **`Bottom App Bar`**  :
:                  :                  :                   : and `MUST` emit child :
:                  :                  :                   : `Icon button`s and    :
:                  :                  :                   : `FAB`; `ELSE` the     :
:                  :                  :                   : agent `MUST` classify :
:                  :                  :                   : it as **`Navigation   :
:                  :                  :                   : bar`**.               :
| Elevated         | Action icons OR  | **`Toolbar`**     | `IF` an elevated      |
: stadium/pill     : top-level        : (`variant\:       : stadium/pill          :
: container (inset : destination      : "Floating         : container with inset  :
: outer margins,   : icons/labels,    : toolbar"`)        : outer margins houses  :
: rounded pill     : optionally       :                   : actions or            :
: ends, floating   : accompanied by   :                   : destinations, `THEN`  :
: above canvas) OR : adjacent         :                   : the agent `MUST`      :
: local action     : standalone       :                   : assign                :
: strip            : action controls  :                   : `mappedComponent\:    :
:                  :                  :                   : "Toolbar"` with       :
:                  :                  :                   : `variant\: "Floating  :
:                  :                  :                   : toolbar"`, `MUST`     :
:                  :                  :                   : apply Step 5 of the   :
:                  :                  :                   : Thinking Path to      :
:                  :                  :                   : derive                :
:                  :                  :                   : `functionalAliases`   :
:                  :                  :                   : and                   :
:                  :                  :                   : `designDeviationNote` :
:                  :                  :                   : whenever its          :
:                  :                  :                   : functional role       :
:                  :                  :                   : diverges from         :
:                  :                  :                   : standard toolbar      :
:                  :                  :                   : usage, and `MUST`     :
:                  :                  :                   : emit any adjacent     :
:                  :                  :                   : independent controls  :
:                  :                  :                   : as separate sibling   :
:                  :                  :                   : components; `ELSE`    :
:                  :                  :                   : the agent `MUST`      :
:                  :                  :                   : classify full-width   :
:                  :                  :                   : flush bottom bars as  :
:                  :                  :                   : `Navigation bar` or   :
:                  :                  :                   : `Bottom App Bar`.     :
| Narrow vertical  | 3–7 vertically   | **`Navigation     | `IF` a narrow leading |
: strip docked     : stacked          : rail`**           : vertical strip houses :
: along leading    : icon-above-label :                   : stacked               :
: edge             : destinations +   :                   : icon-above-label      :
: (tablet/desktop) : optional top     :                   : destinations, `THEN`  :
:                  : `FAB`            :                   : the agent `MUST` emit :
:                  :                  :                   : parent **`Navigation  :
:                  :                  :                   : rail`** AND child     :
:                  :                  :                   : `Icon button` /       :
:                  :                  :                   : `Icon` items plus any :
:                  :                  :                   : optional `FAB` or     :
:                  :                  :                   : `Badge`; `ELSE` the   :
:                  :                  :                   : agent `MUST` evaluate :
:                  :                  :                   : wide vertical panels  :
:                  :                  :                   : as `Navigation        :
:                  :                  :                   : drawer` or `Side      :
:                  :                  :                   : sheet`.               :
| Wide vertical    | Full-width       | **`Navigation     | `IF` a wide leading   |
: panel at leading : horizontal       : drawer`**         : vertical panel houses :
: edge (coplanar   : icon + text      :                   : horizontal            :
: or modal with    : destination rows :                   : destination rows,     :
: scrim)           : and section      :                   : `THEN` the agent      :
:                  : headers          :                   : `MUST` emit parent    :
:                  :                  :                   : **`Navigation         :
:                  :                  :                   : drawer`** AND child   :
:                  :                  :                   : `List item` /         :
:                  :                  :                   : `Button` / `Chip`     :
:                  :                  :                   : rows and `Divider`s;  :
:                  :                  :                   : `ELSE` the agent      :
:                  :                  :                   : `MUST` evaluate       :
:                  :                  :                   : secondary utility     :
:                  :                  :                   : panels as `Side       :
:                  :                  :                   : sheet`.               :

--------------------------------------------------------------------------------

## Matrix 2: Selection & Cluster Controls

| Container       | Visual          | Primary           | `functionalAliases`  |
: Border &        : Selection       : `mappedComponent` : & Child Directive    :
: Segment         : Affordance      :                   :                      :
: Geometry        :                 :                   :                      :
| :-------------- | :-------------- | :---------------- | :------------------- |
| Horizontal      | Active bottom   | **`Tabs`**        | `IF` a horizontal    |
: strip sharing a : underline bar   : (parent) +        : strip switches       :
: continuous      : or pill         : **`Tab`**         : sibling sub-views    :
: bottom baseline : indicator       : (children)        : via an active        :
: OR transparent  : switching       :                   : underline or pill    :
: unselected      : sub-views       :                   : indicator, `THEN`    :
: items           :                 :                   : the agent `MUST`     :
:                 :                 :                   : emit parent          :
:                 :                 :                   : **`Tabs`**, child    :
:                 :                 :                   : **`Tab`** items, and :
:                 :                 :                   : any attached         :
:                 :                 :                   : **`Badge`**; `ELSE`  :
:                 :                 :                   : the agent `MUST`     :
:                 :                 :                   : evaluate enclosed    :
:                 :                 :                   : multi-segment        :
:                 :                 :                   : controls as          :
:                 :                 :                   : `Segmented button`.  :
| Single          | Shared outer    | **`Segmented      | `IF` 2 or more       |
: continuous      : border,         : button`**         : adjacent interactive :
: outer           : internal        :                   : segments share a     :
: stadium/rounded : vertical        :                   : single continuous    :
: border divided  : dividers,       :                   : outer border and     :
: into 2–5 fused  : active segment  :                   : internal dividing    :
: segments        : fill + optional :                   : seams, `THEN` the    :
: sharing         : checkmark or    :                   : agent `MUST` emit    :
: internal        : active icon     :                   : **`Segmented         :
: dividing seams  : highlight       :                   : button`**, `MUST`    :
:                 :                 :                   : apply Step 5 to      :
:                 :                 :                   : include `"Button     :
:                 :                 :                   : group"` in           :
:                 :                 :                   : `functionalAliases`, :
:                 :                 :                   : and `MUST` emit      :
:                 :                 :                   : child `Button` /     :
:                 :                 :                   : `Icon button`        :
:                 :                 :                   : segments; `ELSE` the :
:                 :                 :                   : agent `MUST`         :
:                 :                 :                   : classify binary      :
:                 :                 :                   : thumb-on-track       :
:                 :                 :                   : controls as          :
:                 :                 :                   : **`Switch`**.        :
| Independent     | Individual      | **`Chip`**        | `IF` a compact       |
: compact         : borders/fills   :                   : pill/rounded element :
: pill/rounded    : representing    :                   : represents a         :
: boxes           : facets,         :                   : selectable filter,   :
: representing    : filters,        :                   : active scope/range   :
: filter          : categories,     :                   : selector, category   :
: criteria,       : active ranges,  :                   : tag, or inline       :
: active          : or              :                   : status/metric pill   :
: scope/range     : status/metadata :                   : inside headers,      :
: selectors,      : attributes      :                   : bars, cards, lists,  :
: categories, or  :                 :                   : or drawers, `THEN`   :
: status tags     :                 :                   : the agent `MUST`     :
:                 :                 :                   : emit **`Chip`** and  :
:                 :                 :                   : `MUST` apply Step 5  :
:                 :                 :                   : to populate          :
:                 :                 :                   : `functionalAliases`  :
:                 :                 :                   : with any secondary   :
:                 :                 :                   : role; `ELSE` the     :
:                 :                 :                   : agent `MUST`         :
:                 :                 :                   : classify primary     :
:                 :                 :                   : imperative action    :
:                 :                 :                   : triggers as          :
:                 :                 :                   : **`Button`**.        :
| 2+ discrete     | Separate or     | **`Button         | `IF` 2 or more       |
: action buttons  : coordinated     : group`**          : discrete buttons     :
: grouped locally : button          : (parent) +        : form a coordinated   :
: side-by-side    : containers      : **`Button`** /    : control cluster,     :
: (transport,     : acting as a     : **`Icon button`** : `THEN` the agent     :
: directional,    : unified control : (children)        : `MUST` emit parent   :
: keypad,         : cluster         :                   : **`Button group`**   :
: formatting, or  :                 :                   : AND child            :
: hardware        :                 :                   : **`Button`** /       :
: controls)       :                 :                   : **`Icon button`**    :
:                 :                 :                   : controls and `MUST`  :
:                 :                 :                   : apply Step 5 if      :
:                 :                 :                   : segments also toggle :
:                 :                 :                   : modes; `ELSE`        :
:                 :                 :                   : (including place     :
:                 :                 :                   : sheet action strips  :
:                 :                 :                   : combining a Filled   :
:                 :                 :                   : `"Directions"`       :
:                 :                 :                   : button with Filled   :
:                 :                 :                   : Tonal `"Start"` /    :
:                 :                 :                   : `"Ask"` / `"Call"` / :
:                 :                 :                   : `"Save"` pills and   :
:                 :                 :                   : `"Suggest an edit"`  :
:                 :                 :                   : Text button) emit    :
:                 :                 :                   : standalone           :
:                 :                 :                   : **`Button`** items   :
:                 :                 :                   : using different      :
:                 :                 :                   : container style      :
:                 :                 :                   : variants (`Yes`).    :
:                 :                 :                   : Do NOT identify      :
:                 :                 :                   : adjacent action      :
:                 :                 :                   : icons hosted inside  :
:                 :                 :                   : the top iOS          :
:                 :                 :                   : navigation bar or    :
:                 :                 :                   : search header (even  :
:                 :                 :                   : when enclosed in a   :
:                 :                 :                   : shared iOS system    :
:                 :                 :                   : Liquid Glass         :
:                 :                 :                   : pill/capsule         :
:                 :                 :                   : platter) as a        :
:                 :                 :                   : Material `Button     :
:                 :                 :                   : group`, `Segmented   :
:                 :                 :                   : button`, or          :
:                 :                 :                   : `Toolbar`; evaluate  :
:                 :                 :                   : them as individual   :
:                 :                 :                   : action controls      :
:                 :                 :                   : (`Icon button`)      :
:                 :                 :                   : within the parent    :
:                 :                 :                   : `App bar`.           :
| Primary leading | Asymmetric pair | **`Split          | `IF` an asymmetric   |
: action button   : with flat inner : button`**         : button pair shares   :
: paired with a   : seam edges +    :                   : flat inner edges     :
: trailing        : fully rounded   :                   : separated by a       :
: secondary       : outer pill      :                   : narrow seam, `THEN`  :
: trigger         : edges           :                   : the agent `MUST`     :
: separated by a  :                 :                   : emit parent **`Split :
: narrow vertical :                 :                   : button`**, leading   :
: seam            :                 :                   : **`Button`**,        :
:                 :                 :                   : trailing **`Icon     :
:                 :                 :                   : button`**, and       :
:                 :                 :                   : internal seam        :
:                 :                 :                   : **`Divider`**;       :
:                 :                 :                   : `ELSE` the agent     :
:                 :                 :                   : `MUST` classify      :
:                 :                 :                   : symmetric            :
:                 :                 :                   : multi-button         :
:                 :                 :                   : clusters as `Button  :
:                 :                 :                   : group` or `Segmented :
:                 :                 :                   : button`.             :

--------------------------------------------------------------------------------

## Matrix 3: Containers, Cards & Horizontal Flows

Spatial Flow & Surface Geometry                                                                                                                                               | Internal Content Complexity                                                                                                   | Primary `mappedComponent`                                                                                                       | `functionalAliases` & Deviation Directive
:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------
Bounded surface container (elevated, filled tonal, outlined, or low-contrast dark-theme tile)                                                                                 | Composite entity summary (multiple text styles, metrics, media, controls, or form/parameter slots)                            | **`Card`**                                                                                                                      | `IF` a bounded surface groups multi-element content, `THEN` the agent `MUST` emit **`Card`** and `MUST` inspect its interior for nested **`Button`**, **`Icon button`**, **`Chip`**, **`Badge`**, **`Progress indicator`**, **`Avatar`**, **`Divider`**, and **`Text field`** children; `ELSE` the agent `MUST` evaluate single-action surfaces as `Button` or `Chip`.
Single interactive container with 1 concise action label + optional icon                                                                                                      | Triggers a single imperative action                                                                                           | **`Button`** (or specific variant: `Filled button`, `Filled tonal button`, `Outlined button`, `Elevated button`, `Text button`) | `IF` a compact pill element represents a filter facet, active scope/range selector, category tag, or inline status indicator, `THEN` the agent `MUST` classify it as **`Chip`**; `ELSE` the agent `MUST` classify single-action triggers as **`Button`** (or its specific button variant).
Horizontal track of peer items exhibiting scroll/browse cues (`Edge Peek` cropping, scroll arrows, multi-browse hero layout, or horizontally scrolling structured data slots) | Multiple peer cards, media frames, or structured summary columns arranged along a horizontal axis                             | **`Carousel`**                                                                                                                  | `IF` a horizontal track exhibits scroll or browse affordances, `THEN` the agent `MUST` classify the track as **`Carousel`**, `MUST` emit its child items, and `MUST` apply Step 5 to derive `functionalAliases` and record a `designDeviationNote` whenever the track displays structured non-imagery data slots rather than M3 media cards; `ELSE` the agent `MUST` classify non-scrolling multi-column rows as static layout containers.
Vertical sequence of $\ge 2$ peer rows or vertically stacked composite cards along a shared scroll axis                                                                       | Repeating vertical rows (`List item`) or vertically stacked sibling `Card` containers (excluding conversational chat streams) | **`List`** (parent) + **`List item`** / **`Card`** (children)                                                                   | `IF` a vertical sequence is a conversational chat stream (asymmetrical, variable-width message bubbles in an alternating sender/recipient vertical scroll stream), `THEN` the agent `MUST NOT` classify the message bubbles or transcript as `List`, `List item`, or `Card` (leave standard chat bubbles unclassified so foundational typography and color checks evaluate them directly); `ELSE IF` a screen, pane, or sheet contains 2 or more vertically stacked `Card` or `List item` surfaces, `THEN` the agent `MUST` emit **BOTH** the enclosing parent **`List`** container **AND** the child **`Card`** / **`List item`** components; `ELSE` the agent `MUST` emit a single standalone surface without an enclosing `List`.

--------------------------------------------------------------------------------

## Matrix 4: Linear Tracks, Overlays & Generative AI

| Visual Anatomy & | Interaction /     | Primary           | `functionalAliases`  |
: Position         : State Semantics   : `mappedComponent` : & Branching          :
:                  :                   :                   : Directive            :
| :--------------- | :---------------- | :---------------- | :------------------- |
| Linear track or  | Measurable        | **`Progress       | `IF` a linear track  |
: circular ring    : completion        : indicator`**      : or circular ring     :
: with active vs.  : percentage        :                   : displays measurable  :
: inactive fill    : (`0%-100%`),      :                   : completion progress  :
: (without         : including thin    :                   : without a draggable  :
: draggable thumb) : playback or       :                   : thumb, `THEN` the    :
:                  : status lines on   :                   : agent `MUST` emit    :
:                  : cards/buttons     :                   : **`Progress          :
:                  :                   :                   : indicator`**; `ELSE` :
:                  :                   :                   : the agent `MUST`     :
:                  :                   :                   : evaluate tracks with :
:                  :                   :                   : draggable handles as :
:                  :                   :                   : `Slider`.            :
| Spinning ring,   | Indeterminate     | **`Loading        | `IF` an indicator    |
: looping linear   : wait state        : indicator`**      : represents an        :
: bar, or morphing : without           :                   : indeterminate wait   :
: shape            : measurable        :                   : state, `THEN` the    :
:                  : percentage        :                   : agent `MUST` emit    :
:                  :                   :                   : **`Loading           :
:                  :                   :                   : indicator`**; `ELSE` :
:                  :                   :                   : the agent `MUST`     :
:                  :                   :                   : emit `Progress       :
:                  :                   :                   : indicator` for       :
:                  :                   :                   : determinate          :
:                  :                   :                   : completion tracks.   :
| Linear track     | User-adjustable   | **`Slider`**      | `IF` a linear track  |
: with draggable   : value,            :                   : includes a draggable :
: circular or      : volume/brightness :                   : thumb handle, `THEN` :
: vertical thumb   : level, or         :                   : the agent `MUST`     :
: handle           : interactive media :                   : emit **`Slider`**    :
:                  : seek bar          :                   : and `MUST` apply     :
:                  :                   :                   : Step 5 if it also    :
:                  :                   :                   : conveys playback     :
:                  :                   :                   : progress; `ELSE` the :
:                  :                   :                   : agent `MUST` emit    :
:                  :                   :                   : `Progress            :
:                  :                   :                   : indicator`.          :
| Bottom-anchored  | Brief status      | **`Snackbar`** or | `IF` a messaging     |
: transient status : alert OR          : **`Banner`**      : strip is a compact,  :
: toast OR         : persistent notice :                   : transient floating   :
: persistent       : / privacy consent :                   : toast elevated over  :
: notice / consent : bar with action   :                   : the canvas, `THEN`   :
: bar              : button(s)         :                   : the agent `MUST`     :
:                  :                   :                   : classify it as       :
:                  :                   :                   : **`Snackbar`** and   :
:                  :                   :                   : `MUST` apply Step 5  :
:                  :                   :                   : to record any        :
:                  :                   :                   : secondary functional :
:                  :                   :                   : role; `ELSE` the     :
:                  :                   :                   : agent `MUST`         :
:                  :                   :                   : classify persistent  :
:                  :                   :                   : viewport-spanning or :
:                  :                   :                   : inline notice,       :
:                  :                   :                   : alert, or consent    :
:                  :                   :                   : bars as **`Banner`** :
:                  :                   :                   : (or **`Card`**) and  :
:                  :                   :                   : `MUST` apply Step 5  :
:                  :                   :                   : to record secondary  :
:                  :                   :                   : functional roles.    :
| Inline messaging | Pushes body       | **`Banner`**      | `IF` an inline       |
: container        : content downward; :                   : messaging container  :
: anchored below   : headline +        :                   : pushes content       :
: `App bar`        : supporting text + :                   : downward below the   :
:                  : action/dismiss    :                   : header, `THEN` the   :
:                  : button(s)         :                   : agent `MUST` emit    :
:                  :                   :                   : parent **`Banner`**  :
:                  :                   :                   : AND child            :
:                  :                   :                   : **`Button`** /       :
:                  :                   :                   : **`Icon button`**    :
:                  :                   :                   : controls; `ELSE` the :
:                  :                   :                   : agent `MUST`         :
:                  :                   :                   : evaluate modal       :
:                  :                   :                   : overlays as `Dialog` :
:                  :                   :                   : or `Bottom sheet`.   :
| Multi-color AI   | Ambient glow      | **`Aurora*`**     | `IF` a surface       |
: gradient mesh /  : (`Aurora`), chat  : (exact 1 of 6     : exhibits generative  :
: spark-attributed : bubble (`Aurora   : canonical         : AI spark/gradient    :
: generative AI    : chat bubble`),    : strings)          : attribution, `THEN`  :
: surfaces         : glowing input bar :                   : the agent `MUST` map :
:                  : (`Aurora prompt   :                   : it to the exact      :
:                  : field`),          :                   : matching `Aurora*`   :
:                  : horizontal AI     :                   : canonical string in  :
:                  : cards (`Aurora    :                   : Section 1 and `MUST` :
:                  : response          :                   : apply Step 5 to      :
:                  : carousel`),       :                   : include its          :
:                  : vertical AI steps :                   : underlying           :
:                  : (`Aurora response :                   : structural           :
:                  : list`), prompt    :                   : equivalent in        :
:                  : pills (`Aurora    :                   : `functionalAliases`; :
:                  : suggestions`)     :                   : `ELSE` the agent     :
:                  :                   :                   : `MUST` map standard  :
:                  :                   :                   : UI surfaces to their :
:                  :                   :                   : non-Aurora M3        :
:                  :                   :                   : canonical names.     :
