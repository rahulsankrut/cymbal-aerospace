"""house — a pre-baked, colorblind-safe, editorial charting style for data-craft.

Import-first: complexity lives here, not in the prompt. Typical use:

    import sys; sys.path.insert(0, "/workspace/skill_scripts/data-craft")
    from house import theme, color, fmt
    theme.apply("report")
    fig, ax = plt.subplots()
    ...
    theme.title(ax, "Revenue nearly doubled in 2024", "Net revenue, $M")
    theme.declutter(ax); theme.source(ax, "Source: internal")
    house.save(fig, "/workspace/out/chart.png")
"""

from __future__ import annotations

from typing import Any

import annotate
from annotate import label_points
import charts
from charts import (  # pylint: disable=g-multiple-import
    bullet,
    bump,
    dumbbell,
    lollipop,
    ridgeline,
    slopegraph,
    sparklines,
    waterfall,
)
import color
import format as fmt
import theme

__all__ = [
    "color",
    "theme",
    "fmt",
    "annotate",
    "charts",
    "save",
    "label_points",
    "slopegraph",
    "dumbbell",
    "lollipop",
    "bump",
    "waterfall",
    "bullet",
    "ridgeline",
    "sparklines",
]


def save(fig: Any, path: str, **kw: Any) -> str:
  """Save a figure with house defaults (tight, house dpi)."""
  kw.setdefault("dpi", theme.DPI)
  kw.setdefault("bbox_inches", "tight")
  kw.setdefault("facecolor", color.PANEL)
  fig.savefig(path, **kw)
  return path
