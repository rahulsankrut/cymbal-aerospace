"""Boeing CLM OOXML .docx Track Changes Ingestion & Diff Engine."""
from boeing_clm.ingestion.clause_segmenter import (
    CANONICAL_CLAUSE_REGISTRY,
    ClauseHeaderMetadata,
    is_heading_2_paragraph,
    parse_heading_metadata,
    resolve_clause_metadata,
)
from boeing_clm.ingestion.diff_engine import (
    DiffSegment,
    compute_untracked_diff,
    render_segments_to_diff_html,
)
from boeing_clm.ingestion.docx_track_changes import parse_redlined_docx

__all__ = [
    "CANONICAL_CLAUSE_REGISTRY",
    "ClauseHeaderMetadata",
    "DiffSegment",
    "compute_untracked_diff",
    "is_heading_2_paragraph",
    "parse_heading_metadata",
    "parse_redlined_docx",
    "render_segments_to_diff_html",
    "resolve_clause_metadata",
]
