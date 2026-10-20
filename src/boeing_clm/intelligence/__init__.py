"""Boeing CLM precedent search and conflict intelligence modules."""
from boeing_clm.intelligence.conflict_detector import (
    BigQueryConflictDetector,
    is_rule_triggered,
    row_to_conflict_model,
)
from boeing_clm.intelligence.precedent_engine import (
    BigQueryPrecedentEngine,
    build_playbook_options,
)

__all__ = [
    "BigQueryConflictDetector",
    "BigQueryPrecedentEngine",
    "build_playbook_options",
    "is_rule_triggered",
    "row_to_conflict_model",
]
