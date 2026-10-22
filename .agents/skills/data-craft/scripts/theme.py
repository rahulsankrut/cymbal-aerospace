"""house.theme — design tokens + one-call styling for matplotlib/seaborn/plotnine.

The look: a "quiet frame" (no top/right spines, soft horizontal gridlines only),
an editorial two-tier title, restrained type scale, generous whitespace.
Defaults follow Tufte/Knaflic + WCAG (see references).
"""

from __future__ import annotations

from typing import Any

import color as C

# Prompt-shipped payload: concise docstrings; lazy matplotlib/plotnine imports.
# pylint: disable=g-doc-args,g-import-not-at-top,g-multiple-import

# --- Type scale (points), modular ratio ~1.2. Tuned for screen + slide.
TYPE = {
    "title": 16,  # bold editorial takeaway headline
    "subtitle": 12,  # muted one-line context/method (dek)
    "axis_title": 11,
    "tick": 10,
    "annotation": 9.5,
    "source": 8,  # footnote / data source line (italic)
}

# --- Figure aspect presets (width, height) in inches.
ASPECT = {
    "report": (8.0, 5.0),  # default doc-embed
    "slide": (10.0, 5.63),  # 16:9
    "square": (6.0, 6.0),  # social / heatmap
    "wide": (12.0, 4.2),  # timelines / ranking strips
}

DPI = 200  # screen-crisp; use 300 for print


def apply(preset: str = "report") -> None:
  """Set matplotlib rcParams to the house style.

  Call once at the top of a script. `preset` selects a default figure size (see
  ASPECT).
  """
  import matplotlib as mpl

  w, h = ASPECT.get(preset, ASPECT["report"])
  mpl.rcParams.update({
      # figure / layout
      "figure.figsize": (w, h),
      "figure.dpi": DPI,
      "savefig.dpi": DPI,
      "figure.facecolor": C.PANEL,
      "axes.facecolor": C.PANEL,
      "figure.constrained_layout.use": True,
      "savefig.bbox": "tight",
      "savefig.pad_inches": 0.12,
      # font
      "font.family": "DejaVu Sans",
      "font.size": TYPE["tick"],
      "text.color": C.INK,
      "text.parse_math": False,
      "axes.unicode_minus": True,
      # axes / quiet frame
      "axes.edgecolor": C.SPINE,
      "axes.linewidth": 0.8,
      "axes.grid": True,
      "axes.grid.axis": "y",
      "axes.spines.top": False,
      "axes.spines.right": False,
      "axes.titlelocation": "left",
      "axes.titlesize": TYPE["title"],
      "axes.titleweight": "bold",
      "axes.titlepad": 14,
      "axes.titlecolor": C.INK,
      "axes.labelcolor": C.LABEL,
      "axes.labelsize": TYPE["axis_title"],
      "axes.axisbelow": True,
      # ticks
      "xtick.color": C.TICK,
      "ytick.color": C.TICK,
      "xtick.labelsize": TYPE["tick"],
      "ytick.labelsize": TYPE["tick"],
      "xtick.major.size": 0,
      "ytick.major.size": 0,
      # grid
      "grid.color": C.GRID,
      "grid.linewidth": 0.6,
      # lines / patches
      "lines.linewidth": 2.2,
      "lines.solid_capstyle": "round",
      "patch.edgecolor": "none",
      "legend.frameon": False,
      "legend.fontsize": TYPE["tick"],
      # color
      "axes.prop_cycle": mpl.cycler(color=C.OKABE_ITO),
      "image.cmap": C.SEQUENTIAL,
  })


def title(ax: Any, headline: str, subtitle: str | None = None) -> None:
  """Two-tier editorial title: bold takeaway + muted context line.

  Keep `headline` a *claim* (the so-what), not a neutral label.
  """
  ax.set_title(
      headline,
      loc="left",
      fontsize=TYPE["title"],
      fontweight="bold",
      color=C.INK,
      pad=(26 if subtitle else 14),
  )
  if subtitle:
    ax.text(
        0.0,
        1.02,
        subtitle,
        transform=ax.transAxes,
        fontsize=TYPE["subtitle"],
        color=C.SUBTLE,
        va="bottom",
    )


def source(ax: Any, text: str) -> None:
  """Add a small italic source/footnote line at the figure's bottom-left.

  Uses supxlabel so constrained_layout reserves space (no tick overlap).
  """
  fig = ax.figure
  fig.supxlabel(
      text,
      fontsize=TYPE["source"],
      color=C.SOURCE,
      style="italic",
      x=0.01,
      ha="left",
  )


def declutter(ax: Any, xgrid: bool = False, ygrid: bool = True) -> None:
  """Remove top/right spines, soften remaining spines, gridlines on y only.

  Note: only enable a grid axis when requested (passing line props with
  visible=False silently re-enables the grid in matplotlib).
  """
  for s in ("top", "right"):
    ax.spines[s].set_visible(False)
  for s in ("left", "bottom"):
    ax.spines[s].set_color(C.SPINE)
    ax.spines[s].set_linewidth(0.8)
  ax.grid(False)
  if ygrid:
    ax.grid(axis="y", color=C.GRID, linewidth=0.6)
  if xgrid:
    ax.grid(axis="x", color=C.GRID, linewidth=0.6)
  ax.tick_params(length=0)


# --- plotnine house theme (returns a composed theme object) -------------------
def plotnine_theme(base_size: int = 11) -> Any:
  from plotnine import (
      theme_minimal,
      theme,
      element_text,
      element_blank,
      element_line,
  )

  return theme_minimal(base_size=base_size) + theme(
      plot_title=element_text(
          size=TYPE["title"], weight="bold", color=C.INK, ha="left"
      ),
      plot_subtitle=element_text(
          size=TYPE["subtitle"], color=C.SUBTLE, ha="left"
      ),
      axis_title=element_text(size=TYPE["axis_title"], color=C.LABEL),
      axis_text=element_text(size=TYPE["tick"], color=C.TICK),
      panel_grid_major_x=element_blank(),
      panel_grid_minor=element_blank(),
      panel_grid_major_y=element_line(color=C.GRID, size=0.5),
      legend_title=element_blank(),
      legend_key=element_blank(),
      dpi=DPI,
  )
