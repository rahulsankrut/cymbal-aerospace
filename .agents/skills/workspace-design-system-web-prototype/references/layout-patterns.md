# Layout Patterns Reference

This reference provides detailed structural templates and implementation patterns for multi-pane application shells, dashboard grid layouts, master-detail views, collapsible side sheets, and sticky header feeds in the Workspace Design System (`workspace-design-system`).

## Master-Detail Split Pane Pattern

The master-detail pattern is standard for productivity tools, email clients, and item inspection views. On compact screens (<600px), it displays the list view full-width. On medium and expanded screens (>=600px), it splits into a 2-column side-by-side view.

```html
<div class="flex flex-col h-screen bg-surface text-on-surface">
  <!-- Top Application Header -->
  <md-gb-app-bar size="sm">
    <md-gb-icon-button slot="leading" aria-label="Menu">
      <md-gb-icon>menu</md-gb-icon>
    </md-gb-icon-button>
    <span>Workspace Items</span>
  </md-gb-app-bar>

  <!-- Split Pane Area -->
  <div class="flex flex-1 overflow-hidden">
    <!-- Navigation Rail / Primary Sidebar -->
    <md-gb-nav-rail class="hidden sm:block">
      <md-gb-nav-rail-item active icon="inbox" label="Inbox"></md-gb-nav-rail-item>
      <md-gb-nav-rail-item icon="send" label="Sent"></md-gb-nav-rail-item>
      <md-gb-nav-rail-item icon="star" label="Starred"></md-gb-nav-rail-item>
    </md-gb-nav-rail>

    <!-- List / Master Column -->
    <aside class="w-full sm:w-80 border-e border-[var(--ws-sys-color-divider)] overflow-y-auto bg-surface-container-low">
      <md-gb-list>
        <md-gb-list-item headline="Project Update" supporting-text="Summary of Q3 deliverables...">
          <md-gb-icon slot="start">folder</md-gb-icon>
        </md-gb-list-item>
        <md-gb-list-item headline="Design Review" supporting-text="Feedback on Workspace components...">
          <md-gb-icon slot="start">palette</md-gb-icon>
        </md-gb-list-item>
      </md-gb-list>
    </aside>

    <!-- Detail Content Pane -->
    <main class="hidden sm:flex flex-1 flex-col overflow-y-auto p-s300 space-y-s200 bg-surface">
      <md-gb-card color="filled">
        <div class="p-s300 space-y-s200">
          <h2 class="typescale-headline-sm text-on-surface">Project Update Detail</h2>
          <p class="typescale-body-md text-on-surface max-w-[65ch]">
            Detailed inspection view showing item metadata, active controls, and main body copy constrained to standard line lengths.
          </p>
        </div>
      </md-gb-card>
    </main>
  </div>
</div>
```

## Dashboard Analytics Grid Pattern

Dashboard analytics layouts arrange KPI metric cards, line charts, and data tables into an adaptive grid matrix.

```html
<main class="p-s300 space-y-s300 max-w-7xl mx-auto">
  <!-- Section Title -->
  <header class="flex justify-between items-center">
    <div>
      <h1 class="typescale-headline-md text-on-surface">Analytics Overview</h1>
      <p class="typescale-body-sm text-on-surface-variant">Real-time performance metrics</p>
    </div>
    <md-gb-button color="filled" size="sm">
      <md-gb-icon slot="icon">download</md-gb-icon>
      Export Report
    </md-gb-button>
  </header>

  <!-- Metric KPI Cards Row -->
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-s200">
    <md-gb-card color="filled">
      <div class="p-s200 space-y-s100">
        <span class="typescale-label-md text-on-surface-variant">Total Users</span>
        <div class="typescale-display-sm tabular-nums text-primary">124,850</div>
        <span class="typescale-label-sm text-[var(--ws-sys-color-extended-green-fill)]">+12.4% this week</span>
      </div>
    </md-gb-card>

    <md-gb-card color="filled">
      <div class="p-s200 space-y-s100">
        <span class="typescale-label-md text-on-surface-variant">Active Sessions</span>
        <div class="typescale-display-sm tabular-nums text-primary">8,420</div>
        <span class="typescale-label-sm text-[var(--ws-sys-color-extended-green-fill)]">+5.2% vs average</span>
      </div>
    </md-gb-card>

    <md-gb-card color="filled">
      <div class="p-s200 space-y-s100">
        <span class="typescale-label-md text-on-surface-variant">Avg Response Time</span>
        <div class="typescale-display-sm tabular-nums text-primary">142 ms</div>
        <span class="typescale-label-sm text-[var(--ws-sys-color-extended-green-fill)]">-18 ms optimization</span>
      </div>
    </md-gb-card>

    <md-gb-card color="filled">
      <div class="p-s200 space-y-s100">
        <span class="typescale-label-md text-on-surface-variant">Conversion Rate</span>
        <div class="typescale-display-sm tabular-nums text-primary">3.85%</div>
        <span class="typescale-label-sm text-[var(--ws-sys-color-extended-orange-fill)]">+0.1% target pace</span>
      </div>
    </md-gb-card>
  </div>

  <!-- Primary Content Grid (2:1 Column Split on Expanded Screens) -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-s300">
    <md-gb-card color="outlined" class="lg:col-span-2">
      <div class="p-s300 space-y-s200">
        <h2 class="typescale-title-lg text-on-surface">Traffic Volume History</h2>
        <div class="h-64 bg-surface-container-low rounded-md flex items-center justify-center border border-[var(--ws-sys-color-divider)]">
          <span class="typescale-body-md text-on-surface-variant">[ Chart Visualization Surface ]</span>
        </div>
      </div>
    </md-gb-card>

    <md-gb-card color="filled">
      <div class="p-s300 space-y-s200">
        <h2 class="typescale-title-lg text-on-surface">Recent System Activity</h2>
        <md-gb-list>
          <md-gb-list-item headline="Database Sync Complete" supporting-text="2 mins ago">
            <md-gb-icon slot="start">check_circle</md-gb-icon>
          </md-gb-list-item>
          <md-gb-list-item headline="New User Registration" supporting-text="14 mins ago">
            <md-gb-icon slot="start">person_add</md-gb-icon>
          </md-gb-list-item>
        </md-gb-list>
      </div>
    </md-gb-card>
  </div>
</main>
```

## Collapsible Side Sheet / Drawer Pattern

Side sheets dock alongside main content to present contextual details, filters, or AI prompt assistants without interrupting the main task area.

```html
<div class="flex h-screen bg-surface overflow-hidden">
  <!-- Main Workstation Column -->
  <main class="flex-1 overflow-y-auto p-s300 space-y-s200">
    <h1 class="typescale-headline-lg text-on-surface">Main Document Area</h1>
    <p class="typescale-body-lg text-on-surface max-w-[70ch]">
      Document text content stays fully readable in the main column while contextual controls or AI assistants open in the side sheet.
    </p>
  </main>

  <!-- Persistent / Collapsible Side Sheet Container -->
  <aside class="w-80 border-s border-[var(--ws-sys-color-divider)] bg-surface-container-low p-s300 flex flex-col space-y-s200 shadow-sm">
    <div class="flex justify-between items-center">
      <h2 class="typescale-title-md text-on-surface">Gemini Assistant</h2>
      <md-gb-icon-button aria-label="Close side sheet" size="xs">
        <md-gb-icon>close</md-gb-icon>
      </md-gb-icon-button>
    </div>

    <md-gb-divider></md-gb-divider>

    <div class="flex-1 overflow-y-auto space-y-s200">
      <md-gb-card color="tonal">
        <div class="p-s200 space-y-s100">
          <span class="typescale-label-md text-primary">Suggested Insight</span>
          <p class="typescale-body-sm text-on-surface">
            Analyzed document tone: Professional & clear.
          </p>
        </div>
      </md-gb-card>
    </div>
  </aside>
</div>
```
