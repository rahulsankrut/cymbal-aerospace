"""
OOXML .docx Track Changes and Comment Parser for Boeing CLM.
Parses word/document.xml and word/comments.xml inside a .docx zip archive using lxml.etree
to reconstruct baseline text, vendor redline text, insertions, deletions, vendor comments,
and inline diff HTML for each clause.
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import zipfile

from lxml import etree

from boeing_clm.ingestion.clause_segmenter import (
    ClauseHeaderMetadata,
    is_heading_2_paragraph,
    parse_heading_metadata,
    resolve_clause_metadata,
)
from boeing_clm.ingestion.diff_engine import (
    DiffSegment,
    render_segments_to_diff_html,
)
from boeing_clm.models import ExtractedClauseDiff

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _extract_plain_text(el: etree._Element) -> str:
    """Extract all regular <w:t> text inside an element."""
    return "".join(t.text or "" for t in el.findall(f".//{{{W_NS}}}t"))


def _parse_comments_xml(zf: zipfile.ZipFile) -> Dict[str, str]:
    """
    Parse word/comments.xml if present in the .docx archive and return a mapping
    from comment w:id -> comment text string.
    """
    if "word/comments.xml" not in zf.namelist():
        return {}

    raw_xml = zf.read("word/comments.xml")
    root = etree.fromstring(raw_xml)
    comments_by_id: Dict[str, str] = {}

    for c_el in root.findall(f".//{{{W_NS}}}comment"):
        c_id = c_el.get(f"{{{W_NS}}}id")
        if c_id is None:
            continue
        text = _extract_plain_text(c_el).strip()
        if text:
            comments_by_id[str(c_id)] = text

    return comments_by_id


def _parse_clause_paragraph(
    p_el: etree._Element,
    comments_by_id: Dict[str, str],
) -> Tuple[str, str, List[str], List[str], List[str], List[DiffSegment]]:
    """
    Walk a clause body <w:p> element in document order, reconstructing:
    - boeing_baseline_text (regular <w:r><w:t> + <w:del><w:r><w:delText>)
    - vendor_redline_text (regular <w:r><w:t> + <w:ins><w:r><w:t>)
    - insertions
    - deletions
    - vendor_comments (via <w:commentRangeStart>, <w:commentRangeEnd>, <w:commentReference>)
    - segments (list of DiffSegment for diff_html)
    """
    baseline_parts: List[str] = []
    vendor_parts: List[str] = []
    insertions: List[str] = []
    deletions: List[str] = []
    comment_ids: List[str] = []
    segments: List[DiffSegment] = []

    def _record_comment_id(cid: Optional[str]) -> None:
        if cid is not None and cid not in comment_ids:
            comment_ids.append(cid)

    for child in p_el:
        tag = child.tag
        if tag == f"{{{W_NS}}}r":
            # Check for commentReference inside this run
            for cref in child.findall(f".//{{{W_NS}}}commentReference"):
                _record_comment_id(cref.get(f"{{{W_NS}}}id"))
            run_text = "".join(t.text or "" for t in child.findall(f".//{{{W_NS}}}t"))
            if run_text:
                baseline_parts.append(run_text)
                vendor_parts.append(run_text)
                segments.append(DiffSegment("same", run_text))
        elif tag == f"{{{W_NS}}}del":
            del_text = "".join(
                dt.text or ""
                for dt in child.findall(f".//{{{W_NS}}}delText")
            )
            if del_text:
                deletions.append(del_text)
                baseline_parts.append(del_text)
                segments.append(DiffSegment("del", del_text))
        elif tag == f"{{{W_NS}}}ins":
            ins_text = "".join(
                t.text or ""
                for t in child.findall(f".//{{{W_NS}}}t")
            )
            if ins_text:
                insertions.append(ins_text)
                vendor_parts.append(ins_text)
                segments.append(DiffSegment("ins", ins_text))
        elif tag in (f"{{{W_NS}}}commentRangeStart", f"{{{W_NS}}}commentRangeEnd"):
            _record_comment_id(child.get(f"{{{W_NS}}}id"))

    vendor_comments = [
        comments_by_id[cid] for cid in comment_ids if cid in comments_by_id
    ]

    return (
        "".join(baseline_parts),
        "".join(vendor_parts),
        insertions,
        deletions,
        vendor_comments,
        segments,
    )


def parse_redlined_docx(docx_path: str | Path) -> List[ExtractedClauseDiff]:
    """
    Parse word/document.xml and word/comments.xml inside a .docx archive using lxml.etree
    and return a validated list of ExtractedClauseDiff models.
    """
    path = Path(docx_path)
    if not path.exists():
        raise FileNotFoundError(f"DOCX file not found: {path}")

    with zipfile.ZipFile(path, "r") as zf:
        if "word/document.xml" not in zf.namelist():
            raise ValueError(f"Invalid .docx archive (missing word/document.xml): {path}")
        doc_xml = zf.read("word/document.xml")
        comments_by_id = _parse_comments_xml(zf)

    doc_root = etree.fromstring(doc_xml)
    body_el = doc_root.find(f"{{{W_NS}}}body")
    if body_el is None:
        return []

    paragraphs = body_el.findall(f"{{{W_NS}}}p")

    # Determine if the document uses Heading 2 clause headers
    has_heading2 = any(is_heading_2_paragraph(p) for p in paragraphs)

    results: List[ExtractedClauseDiff] = []

    if has_heading2:
        current_meta: Optional[ClauseHeaderMetadata] = None
        for p_el in paragraphs:
            if is_heading_2_paragraph(p_el):
                heading_text = _extract_plain_text(p_el)
                current_meta = parse_heading_metadata(heading_text)
                continue

            if current_meta is None:
                continue

            (
                baseline_text,
                vendor_text,
                insertions,
                deletions,
                vendor_comments,
                segments,
            ) = _parse_clause_paragraph(p_el, comments_by_id)

            if not baseline_text and not vendor_text:
                continue

            diff_html = render_segments_to_diff_html(segments)
            has_redline = bool(insertions or deletions or (baseline_text != vendor_text))

            results.append(
                ExtractedClauseDiff(
                    clause_id=current_meta.clause_id,
                    proforma_doc=current_meta.proforma_doc,
                    clause_ref=current_meta.clause_ref,
                    clause_title=current_meta.clause_title,
                    sme_team=current_meta.sme_team,
                    sme_owner_label=current_meta.sme_owner_label,
                    risk_level=current_meta.risk_level,
                    regulatory_flag=current_meta.regulatory_flag,
                    has_redline=has_redline,
                    boeing_baseline_text=baseline_text,
                    vendor_redline_text=vendor_text,
                    insertions=insertions,
                    deletions=deletions,
                    vendor_comments=vendor_comments,
                    diff_html=diff_html,
                )
            )
            current_meta = None
    else:
        # Fallback for generic .docx without Heading 2 metadata tags: align by section numbers
        for p_el in paragraphs:
            (
                baseline_text,
                vendor_text,
                insertions,
                deletions,
                vendor_comments,
                segments,
            ) = _parse_clause_paragraph(p_el, comments_by_id)

            probe_text = baseline_text or vendor_text
            if not probe_text:
                continue

            meta = resolve_clause_metadata(None, probe_text)
            if meta is None:
                continue

            diff_html = render_segments_to_diff_html(segments)
            has_redline = bool(insertions or deletions or (baseline_text != vendor_text))

            results.append(
                ExtractedClauseDiff(
                    clause_id=meta.clause_id,
                    proforma_doc=meta.proforma_doc,
                    clause_ref=meta.clause_ref,
                    clause_title=meta.clause_title,
                    sme_team=meta.sme_team,
                    sme_owner_label=meta.sme_owner_label,
                    risk_level=meta.risk_level,
                    regulatory_flag=meta.regulatory_flag,
                    has_redline=has_redline,
                    boeing_baseline_text=baseline_text,
                    vendor_redline_text=vendor_text,
                    insertions=insertions,
                    deletions=deletions,
                    vendor_comments=vendor_comments,
                    diff_html=diff_html,
                )
            )

    return results
