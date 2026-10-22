"""Render slide thumbnails from a .pptx.

Usage: python thumbnail.py deck.pptx thumbs/

Drives LibreOffice headless to convert .pptx → PDF, then pdftoppm to
rasterize each page to JPEG. Outputs `slide-N.jpg` per slide in `thumbs/`.
"""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).parent))
from soffice import run_soffice

try:
  import pypdfium2 as pdfium

  _HAS_PDFIUM = True
except ImportError:
  _HAS_PDFIUM = False


def thumbnail(pptx_path: Path, out_dir: Path, dpi: int = 96):
  out_dir.mkdir(parents=True, exist_ok=True)

  _has_pdfium = _HAS_PDFIUM

  _has_pdftoppm = bool(shutil.which("pdftoppm"))

  if not _has_pdfium and not _has_pdftoppm:
    print(
        "WARNING: pdftoppm and pypdfium2 not found; skipping thumbnail"
        " rasterization due to missing host dependencies.",
        file=sys.stdout,
    )
    return

  with tempfile.TemporaryDirectory() as td:
    td_path = Path(td)
    result = run_soffice([
        "--convert-to",
        "pdf",
        "--outdir",
        str(td_path),
        str(pptx_path),
    ])
    if result.returncode != 0:
      print(f"soffice failed: {result.stderr}", file=sys.stderr)
      sys.exit(1)

    pdfs = list(td_path.glob("*.pdf"))
    if not pdfs:
      print("ERROR: no PDF produced by soffice", file=sys.stderr)
      sys.exit(1)
    pdf_path = pdfs[0]

    if _has_pdfium:
      pdf = pdfium.PdfDocument(str(pdf_path))
      for i, page in enumerate(pdf, start=1):
        image = page.render(scale=dpi / 72.0).to_pil()
        image.save(str(out_dir / f"slide-{i}.jpg"), "JPEG")
      print(f"OK: wrote thumbnails to {out_dir}")
    else:
      out_prefix = out_dir / "slide"
      subprocess.run(
          ["pdftoppm", "-jpeg", "-r", str(dpi), str(pdf_path), str(out_prefix)],
          check=True,
      )
      print(f"OK: wrote thumbnails to {out_dir}")


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: thumbnail.py <deck.pptx> <out_dir/>", file=sys.stderr)
    sys.exit(2)
  thumbnail(Path(sys.argv[1]), Path(sys.argv[2]))
