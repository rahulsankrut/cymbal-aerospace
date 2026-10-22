"""house.annotate — the annotation layer for the house style.

Direct end/max/min labels, reference lines, signed delta callouts (with
redundant glyphs), and event bands. Hue is never load-bearing.
"""

from __future__ import annotations

from typing import Any

import color as C
import theme as T

# Prompt-shipped payload: numpy imported lazily inside helpers.
# pylint: disable=g-import-not-at-top


def label_last(
    ax: Any,
    x: Any,
    y: Any,
    text: str,
    color: str | None = None,
    bold: bool = True,
    dx: float = 6,
) -> None:
  """Direct end-of-line label (replaces a legend entry)."""
  color = color or C.INK
  ax.annotate(
      f" {text}",
      xy=(x[-1], y[-1]),
      xytext=(dx, 0),
      textcoords="offset points",
      va="center",
      fontsize=T.TYPE["annotation"],
      color=color,
      fontweight="bold" if bold else "normal",
  )


def label_extreme(
    ax: Any,
    x: Any,
    y: Any,
    mode: str = "max",
    fmt: str = "{:.0f}",
    color: str | None = None,
) -> None:
  """Mark and label the max or min point of a series."""
  import numpy as np

  color = color or C.NEGATIVE
  ya = np.asarray(y, dtype=float)
  i = int(np.argmax(ya)) if mode == "max" else int(np.argmin(ya))
  ax.scatter([x[i]], [ya[i]], s=36, color=color, zorder=5)
  ax.annotate(
      fmt.format(ya[i]),
      xy=(x[i], ya[i]),
      xytext=(0, 8),
      textcoords="offset points",
      ha="center",
      fontsize=T.TYPE["annotation"],
      color=color,
      fontweight="bold",
  )


def label_points(
    ax: Any,
    x: Any,
    y: Any,
    labels: Any,
    color: str | None = None,
    arrows: bool = True,
) -> list[Any]:
  """Label scatter/point coordinates and auto-repel collisions via adjustText."""
  color = color or C.INK
  xs, ys = list(x), list(y)
  texts = [
      ax.text(
          xi,
          yi,
          str(lbl),
          fontsize=T.TYPE["annotation"],
          color=color,
      )
      for xi, yi, lbl in zip(xs, ys, labels)
  ]
  try:
    from adjustText import adjust_text

    arrowprops = (
        {"arrowstyle": "-", "color": C.SUBTLE, "lw": 0.6} if arrows else None
    )
    adjust_text(
        texts,
        x=xs,
        y=ys,
        ax=ax,
        arrowprops=arrowprops,
        expand=(1.2, 1.4),
    )
  except ImportError:
    pass
  return texts


def refline(
    ax: Any,
    value: float,
    label: str | None = None,
    axis: str = "y",
    color: str | None = None,
) -> None:
  """Horizontal/vertical reference (target/benchmark) line + right label."""
  color = color or C.REFERENCE
  if axis == "y":
    ax.axhline(
        value, color=color, linewidth=1.2, linestyle=(0, (4, 2)), zorder=1
    )
    if label:
      ax.text(
          1.01,
          value,
          f" {label}",
          transform=ax.get_yaxis_transform(),
          va="center",
          ha="left",
          fontsize=T.TYPE["annotation"],
          color=color,
          clip_on=False,
      )
  else:
    ax.axvline(
        value, color=color, linewidth=1.2, linestyle=(0, (4, 2)), zorder=1
    )
    if label:
      ax.text(
          value,
          0.97,
          f" {label}",
          transform=ax.get_xaxis_transform(),
          va="top",
          ha="left",
          fontsize=T.TYPE["annotation"],
          color=color,
      )


def delta(ax: Any, x: Any, y: Any, value: float, pct: bool = True) -> None:
  """Signed delta callout with redundant up/down glyph (colorblind-safe)."""
  up = value >= 0
  glyph = "\u25b2" if up else "\u25bc"  # ▲ / ▼
  col = C.POSITIVE if up else C.NEGATIVE
  txt = f"{glyph} {value:+.0f}%" if pct else f"{glyph} {value:+,.0f}"
  ax.annotate(
      txt,
      xy=(x, y),
      xytext=(0, 10),
      textcoords="offset points",
      ha="center",
      fontsize=T.TYPE["annotation"],
      color=col,
      fontweight="bold",
  )


def event_band(
    ax: Any, start: Any, end: Any = None, label: str | None = None
) -> None:
  """Shade an event interval (or mark an instant) behind the data."""
  if end is not None:
    ax.axvspan(start, end, color="#000000", alpha=0.05, zorder=0)
    mid = start + (end - start) / 2
  else:
    ax.axvline(start, color=C.MUTE2, linewidth=1.0, zorder=0)
    mid = start
  if label:
    ax.text(
        mid,
        0.97,
        label,
        transform=ax.get_xaxis_transform(),
        ha="center",
        va="top",
        fontsize=T.TYPE["annotation"],
        color=C.SUBTLE,
    )
