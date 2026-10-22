"""house.format — number/currency/percent axis formatters (mizani + matplotlib)."""

from __future__ import annotations

from typing import Any

# Prompt-shipped payload: matplotlib/mizani imported lazily inside factories.
# pylint: disable=g-import-not-at-top,redefined-outer-name


def _compact(x: float) -> str:
  """1_500_000 -> '1.5M'; keeps 3 sig-figs-ish, strips trailing zeros."""
  ax = abs(x)
  for div, suf in ((1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")):
    if ax >= div:
      s = f"{x / div:.1f}".rstrip("0").rstrip(".")
      return f"{s}{suf}"
  return f"{x:.1f}".rstrip("0").rstrip(".") or "0"


def currency(prefix: str = "$", suffix: str = "", compact: bool = True) -> Any:
  """matplotlib FuncFormatter for money axes. compact -> $1.5M style."""
  from matplotlib.ticker import FuncFormatter

  if compact:
    return FuncFormatter(lambda x, _pos: f"{prefix}{_compact(x)}{suffix}")
  return FuncFormatter(lambda x, _pos: f"{prefix}{x:,.0f}{suffix}")


def percent(decimals: int = 0, scale: float = 1.0) -> Any:
  """matplotlib FuncFormatter for percent axes. scale=100 if data is 0-1."""
  from matplotlib.ticker import FuncFormatter

  return FuncFormatter(
      lambda x, _pos: f"{x * (100 if scale == 100 else 1):.{decimals}f}%"
  )


def comma() -> Any:
  """Thousands separators (12,345)."""
  from matplotlib.ticker import FuncFormatter

  return FuncFormatter(lambda x, _pos: f"{x:,.0f}")


def compact() -> Any:
  """Compact large numbers on an axis (1.5M, 12K)."""
  from matplotlib.ticker import FuncFormatter

  return FuncFormatter(lambda x, _pos: _compact(x))


# --- plotnine (mizani) equivalents, with a robust fallback -------------------
def pn_currency(
    prefix: str = "$", suffix: str = "", accuracy: float = 1
) -> Any:
  try:
    from mizani.labels import label_currency

    return label_currency(prefix=prefix, suffix=suffix, accuracy=accuracy)
  except ImportError:
    return lambda vals: [f"{prefix}{v:,.0f}{suffix}" for v in vals]


def pn_percent(accuracy: float = 1) -> Any:
  try:
    from mizani.labels import label_percent

    return label_percent(accuracy=accuracy)
  except ImportError:
    return lambda vals: [f"{v*100:.0f}%" for v in vals]


def pn_comma() -> Any:
  try:
    from mizani.labels import label_comma

    return label_comma()
  except ImportError:
    return lambda vals: [f"{v:,.0f}" for v in vals]
