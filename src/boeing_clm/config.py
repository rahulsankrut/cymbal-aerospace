"""Frozen configuration for Boeing CLM."""
from pathlib import Path
import os


def _resolve_project_root() -> Path:
    env_root = os.getenv("BOEING_CLM_ROOT")
    if env_root and (Path(env_root) / "specs").exists():
        return Path(env_root).resolve()
    rel_root = Path(__file__).resolve().parents[2]
    if (rel_root / "specs").exists():
        return rel_root
    if (Path.cwd() / "specs").exists():
        return Path.cwd().resolve()
    return rel_root


PROJECT_ROOT = _resolve_project_root()
SPECS_DIR = PROJECT_ROOT / "specs"
GOLDEN_FIXTURES_DIR = SPECS_DIR / "04_golden_fixtures"
EXPORTS_DIR = PROJECT_ROOT / "data" / "exports"

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "vertex-ai-demos-468803")
BQ_DATASET = os.getenv("BQ_DATASET", "boeing_clm")
BQ_LOCATION = os.getenv("BQ_LOCATION", "US")
BQ_CONNECTION_ID = os.getenv("BQ_CONNECTION_ID", "vertex-ai-demos-468803.us.vertex_ai")
BQ_EMBEDDING_MODEL = f"`{GCP_PROJECT_ID}.{BQ_DATASET}.text_embedding_005`"
DEFAULT_DEAL_ID = "BA-2026-AV-8921"

GOLDEN_BASELINE_DOCX = GOLDEN_FIXTURES_DIR / "Boeing_GP1_Standard.docx"
GOLDEN_VENDOR_REDLINE_DOCX = GOLDEN_FIXTURES_DIR / "Vendor_Redlined_GP1.docx"
GOLDEN_EXPECTED_DIFFS_JSON = GOLDEN_FIXTURES_DIR / "expected_extracted_diffs.json"
