"""
Deterministic HTML diff generator for Boeing CLM clause redlines.
Renders <span class="diff-del">...</span> and <span class="diff-add">...</span>
from either native Word OOXML Track Changes segments or untracked text comparisons.
"""
from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
import re
from typing import List, Literal, Sequence, Tuple

SegmentType = Literal["same", "del", "ins"]


@dataclass(frozen=True)
class DiffSegment:
    segment_type: SegmentType
    text: str


def render_segments_to_diff_html(segments: Sequence[DiffSegment]) -> str:
    """
    Render ordered DiffSegments ('same', 'del', 'ins') into inline HTML markup
    matching the frozen contract: <span class="diff-del">...</span> and <span class="diff-add">...</span>.
    """
    parts: List[str] = []
    for seg in segments:
        if not seg.text:
            continue
        if seg.segment_type == "same":
            parts.append(seg.text)
        elif seg.segment_type == "del":
            parts.append(f'<span class="diff-del">{seg.text}</span>')
        elif seg.segment_type == "ins":
            parts.append(f'<span class="diff-add">{seg.text}</span>')
    return "".join(parts)


_TOKEN_SPLIT_RE = re.compile(r"(\s+)")


def compute_untracked_diff(
    baseline_text: str, vendor_text: str
) -> Tuple[List[str], List[str], str]:
    """
    Fallback deterministic word-level diff if a .docx paragraph was modified without
    Word Track Changes (<w:ins>/<w:del>) enabled.
    Returns (insertions, deletions, diff_html).
    """
    if baseline_text == vendor_text:
        return [], [], baseline_text

    base_tokens = [t for t in _TOKEN_SPLIT_RE.split(baseline_text) if t]
    vend_tokens = [t for t in _TOKEN_SPLIT_RE.split(vendor_text) if t]

    matcher = SequenceMatcher(None, base_tokens, vend_tokens, autojunk=False)
    segments: List[DiffSegment] = []
    insertions: List[str] = []
    deletions: List[str] = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            segments.append(DiffSegment("same", "".join(base_tokens[i1:i2])))
        elif tag == "delete":
            del_str = "".join(base_tokens[i1:i2])
            deletions.append(del_str)
            segments.append(DiffSegment("del", del_str))
        elif tag == "insert":
            ins_str = "".join(vend_tokens[j1:j2])
            insertions.append(ins_str)
            segments.append(DiffSegment("ins", ins_str))
        elif tag == "replace":
            del_str = "".join(base_tokens[i1:i2])
            ins_str = "".join(vend_tokens[j1:j2])
            deletions.append(del_str)
            insertions.append(ins_str)
            segments.append(DiffSegment("del", del_str))
            segments.append(DiffSegment("ins", ins_str))

    return insertions, deletions, render_segments_to_diff_html(segments)
