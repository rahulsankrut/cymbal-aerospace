"""Re-export frozen Pydantic v2 contracts from specs/02_domain_models.py."""
from importlib.util import module_from_spec, spec_from_file_location
import sys

from boeing_clm.config import SPECS_DIR

_spec_path = SPECS_DIR / "02_domain_models.py"
_spec = spec_from_file_location("specs_02_domain_models", _spec_path)
assert _spec and _spec.loader, f"Failed to locate frozen spec at {_spec_path}"
_mod = module_from_spec(_spec)
sys.modules["specs_02_domain_models"] = _mod
_spec.loader.exec_module(_mod)

StrictContractModel = _mod.StrictContractModel
ExtractedClauseDiff = _mod.ExtractedClauseDiff
OutcomeDistribution = _mod.OutcomeDistribution
PrecedentMatchItem = _mod.PrecedentMatchItem
PlaybookOption = _mod.PlaybookOption
PrecedentSearchResult = _mod.PrecedentSearchResult
SMEReviewSubmission = _mod.SMEReviewSubmission
CrossClauseConflict = _mod.CrossClauseConflict
AuditEventItem = _mod.AuditEventItem
ClauseWorkbenchItem = _mod.ClauseWorkbenchItem
DealWorkbenchState = _mod.DealWorkbenchState

__all__ = [
    "StrictContractModel",
    "ExtractedClauseDiff",
    "OutcomeDistribution",
    "PrecedentMatchItem",
    "PlaybookOption",
    "PrecedentSearchResult",
    "SMEReviewSubmission",
    "CrossClauseConflict",
    "AuditEventItem",
    "ClauseWorkbenchItem",
    "DealWorkbenchState",
]
