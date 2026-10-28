"""
Counter-Proposal .docx Generator for Cymbal Aerospace CLM.
Generates a complete 12-clause .docx contract with:
- Executive Summary header & metadata table for state.deal_id
- All 12 clauses in order with clean, emoji-free Heading 2 section headers
- Surgical word-level Word OOXML Track Changes (<w:del>, <w:ins>, and regular <w:r> runs
  authored by "Cymbal Aerospace Legal & Procurement") for redlined clauses
- Sanitized counterparty-facing word/comments.xml (<75 words, collegial justification,
  zero internal SME names, precedent percentages, conflict/lockout IDs, walk-away floors,
  or internal URLs) linked via <w:commentRangeStart>, <w:commentRangeEnd>, and
  <w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference/></w:r>
"""
from __future__ import annotations

import difflib
from io import BytesIO
from pathlib import Path
import re
from typing import Any, Dict, List
import zipfile

from docx import Document
from docx.shared import Inches
from lxml import etree

from boeing_clm.models import ClauseWorkbenchItem, DealWorkbenchState

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
COMMENTS_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
COMMENTS_CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"

COUNTER_PROPOSAL_AUTHOR = "Cymbal Aerospace Legal & Procurement"

_EMOJI_STRIP_RE = re.compile(
    r"[✅⚠️⏳✓⚡🔒🛡️⚖️✦📊📋🔍🚨❌🟢🟡🔴"
    r"\U0001F300-\U0001FAFF\u2600-\u27BF\uFE0F]+"
)

_INTERNAL_SME_NAMES_RE = re.compile(
    r"\b(?:"
    r"Pradeep\s+Gupta|Megan\s+Bowen|Alex\s+Wilber|Miriam\s+Graham|"
    r"Diego\s+Siciliani|Nestor\s+Wilke|Adele\s+Vance|R\.\s*Vance|"
    r"M\.\s*Vance|Dr\.\s*K\.\s*Chen"
    r")\b(?:\s*\([^)]*\))?\s*:?",
    re.IGNORECASE,
)

_LEADING_ROLE_PREFIX_RE = re.compile(
    r"^\s*(?:\[[^\]]+\]\s*)?(?:[A-Z][a-zA-Z.\s&-]{2,40}\s*\([^)]+\)\s*:\s*)+",
)

# Canonical collegial 3-part counterparty explanations (<75 words) per explanations-for-redlines skill
_DEFAULT_COLLEGIAL_JUSTIFICATIONS: Dict[str, str] = {
    "GP1-03": (
        "To preserve Firm-Fixed-Price contract baseline certainty under Schedule A, "
        "unit pricing remains governed by GP1 §3.1 while commercial liability allocation "
        "is addressed separately within GP1 §19."
    ),
    "GP1-12": (
        "As an FAA Production Approval Holder under FAA 14 CFR Part 21, Cymbal Aerospace is "
        "regulatory-mandated to maintain a 36-month airworthiness warranty from aircraft "
        "delivery and unannounced source inspection access. Our counter-proposal protects "
        "Seller's facility operations by coordinating on-site escort protocols without "
        "restricting regulatory inspection rights."
    ),
    "GP1-19": (
        "Because flight-critical aerospace assemblies carry significant airworthiness exposure, "
        "a 1x Purchase Order cap with a combination IP carveout leaves recall risk unallocated. "
        "To provide Seller with predictable balance-sheet protection while addressing safety "
        "obligations, we propose a 200% (2x PO) general damages cap with uncapped airworthiness "
        "recall and system-integration IP indemnity."
    ),
    "SP3-04": (
        "While GP1 §3.1 establishes a Firm-Fixed-Price DDP baseline inclusive of standard import "
        "duties, we recognize that extraordinary post-execution Section 232 or 301 trade tariffs "
        "create raw-material cost volatility. We propose sharing verified new Section 232/301 "
        "tariff increases above the threshold 50/50 up to the agreed Purchase Order cap via "
        "bilateral Change Order."
    ),
    "SP5-03": (
        "Under DFARS 252.204-7012(c), our mandatory 72-hour DoD Cyber Crime Center reporting "
        "obligation begins upon discovery of a cybersecurity incident affecting Covered Defense "
        "Information, making a multi-day post-forensic notification window non-compliant. We "
        "require notification within 72 hours of discovery alongside forensic log preservation."
    ),
}


def strip_heading_emojis(text: str) -> str:
    """Strip emojis and individual SME names from Heading 2 text ([P2-LEGAL-03])."""
    cleaned = _EMOJI_STRIP_RE.sub("", text or "")
    cleaned = _INTERNAL_SME_NAMES_RE.sub("", cleaned)
    cleaned = re.sub(r"\(\s*\)", "", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned


def _sanitize_counter_text_for_external(text: str) -> str:
    """Ensure external contract counter-text never leaks internal walk-away floors."""
    cleaned = _EMOJI_STRIP_RE.sub("", text or "")
    cleaned = re.sub(
        r",?\s*or\s+\d+(?:\.\d+)?x\s*\(\$?[\d,]+(?:\.\d+)?[MKB]?\)\s*(?:walk-away\s+)?floor\b",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\bwalk-away(?:\s+floor)?\b", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned


def sanitize_counterparty_comment(clause: ClauseWorkbenchItem | Dict[str, Any] | str) -> str:
    """
    Sanitize external <w:comment> text written into word/comments.xml:
    - Maximum <75 words
    - Collegial commercial/regulatory justification attributed to Cymbal Aerospace Legal & Procurement
    - Strips internal BigQuery precedent percentages, deal counts, internal conflict/lockout rule IDs
      (CONFLICT-, LOCKOUT-), internal walk-away floors (floor, walk-away), internal URLs
      (boeing_clm, sharepoint.com, 127.0.0.1), and individual SME names.
    """
    if isinstance(clause, str):
        clause_id = ""
        clause_ref = ""
        raw_text = clause
    elif isinstance(clause, dict):
        clause_id = str(clause.get("clause_id") or "")
        clause_ref = str(clause.get("clause_ref") or clause_id)
        raw_text = str(
            clause.get("external_justification")
            or clause.get("sme_rationale")
            or ""
        )
    else:
        clause_id = str(getattr(clause, "clause_id", "") or "")
        clause_ref = str(getattr(clause, "clause_ref", "") or clause_id)
        raw_text = str(
            getattr(clause, "external_justification", None)
            or getattr(clause, "sme_rationale", "")
            or ""
        )

    cleaned = _EMOJI_STRIP_RE.sub("", raw_text)
    cleaned = _LEADING_ROLE_PREFIX_RE.sub("", cleaned)
    cleaned = _INTERNAL_SME_NAMES_RE.sub("", cleaned)

    # Strip internal BigQuery precedent percentages and deal counts
    cleaned = re.sub(
        r"\(\s*\d+(?:\.\d+)?%\s*(?:precedent\s*)?(?:/\s*\d+\s*(?:of|/)\s*\d+\s*deals?)?\s*\)",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(
        r"\b\d+(?:\.\d+)?%\s*(?:\(\s*\d+\s*(?:of|/)\s*\d+\s*(?:deals?)?\s*\)\s*)?"
        r"(?:(?:historical|tier-1|avionics|aerospace|commercial)\s+)*"
        r"(?:precedent|held\s+firm|compromise|tier-1|deals?)\b",
        "commercial standard",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(
        r"\b\d+(?:\.\d+)?%\s*(?:precedent|held\s+firm|compromise|tier-1|deals)\b",
        "commercial standard",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(
        r"\(\s*\d+\s*(?:of|/)\s*\d+\s*(?:deals?|precedents?)?\s*\)",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(
        r"\b\d+\s*(?:of|/)\s*\d+\s*deals?\b",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )

    # Strip internal conflict/lockout rule IDs
    cleaned = re.sub(
        r"\b(?:CONFLICT|LOCKOUT)-[A-Z0-9_-]+\b",
        "contractual alignment",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(
        r"\bCONFLICT\s+WITH\s+[A-Z]+\s*[—\-:]?\s*",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\b(?:CONFLICT|LOCKOUT)-", "", cleaned, flags=re.IGNORECASE)

    # Strip internal walk-away floors
    cleaned = re.sub(
        r"(?:,?\s*or\s+|\s*/\s*)?\d+(?:\.\d+)?x\s*(?:\(\$?[\d,]+(?:\.\d+)?[MKB]?\)|/\s*\$?[\d,]+(?:\.\d+)?[MKB]?)\s*(?:walk-away\s+)?floor\b",
        "",
        cleaned,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"\bwalk-away(?:\s+floor)?\b", "commercial baseline", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bfloor\b", "baseline", cleaned, flags=re.IGNORECASE)

    # Strip internal URLs, hostnames, and BigQuery dataset names
    cleaned = re.sub(r"https?://[^\s)\]]+", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\b(?:[\w-]+\.)*sharepoint\.com(?:/[^\s)\]]*)?", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bvertex-ai-demos[-a-z0-9._]*\b", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bboeing_clm\b", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\b127\.0\.0\.1(?::\d+)?\b", "", cleaned, flags=re.IGNORECASE)

    # Clean up punctuation artifacts
    cleaned = re.sub(r"\(\s*[/,;:\-\s]*\)", "", cleaned)
    cleaned = re.sub(r"\[\s*[/,;:\-\s]*\]", "", cleaned)
    cleaned = re.sub(r"\s+([,.;:])", r"\1", cleaned)
    cleaned = re.sub(r"[:;,-]\s*[:;,-]+", ":", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip(" -:;,.|")

    fallback = _DEFAULT_COLLEGIAL_JUSTIFICATIONS.get(
        clause_id,
        "Cymbal Aerospace proposes this balanced commercial and regulatory counter-position to align contract terms across both parties.",
    )
    if not cleaned:
        body = fallback
    else:
        body = f"{cleaned}." if not cleaned.endswith(".") else cleaned
        if len(body.split()) < 18 and clause_id in _DEFAULT_COLLEGIAL_JUSTIFICATIONS:
            body = f"{body} {_DEFAULT_COLLEGIAL_JUSTIFICATIONS[clause_id]}"

    prefix = (
        f"[{COUNTER_PROPOSAL_AUTHOR} — {clause_ref}] "
        if clause_ref
        else f"[{COUNTER_PROPOSAL_AUTHOR}] "
    )
    full_comment = f"{prefix}{body}".strip()

    # Enforce strict <75 words cap (cap at 70 words)
    words = full_comment.split()
    if len(words) > 70:
        truncated = " ".join(words[:70]).rstrip(",;:-")
        if not truncated.endswith("."):
            truncated += "."
        full_comment = truncated

    return full_comment


def _append_run(p_el: etree._Element, text: str) -> None:
    r = etree.SubElement(p_el, f"{{{W_NS}}}r")
    t = etree.SubElement(r, f"{{{W_NS}}}t")
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def _append_del(
    p_el: etree._Element,
    rev_id: int,
    text: str,
    author: str = COUNTER_PROPOSAL_AUTHOR,
    date_str: str = "2026-10-16T18:00:00Z",
) -> None:
    del_el = etree.SubElement(
        p_el,
        f"{{{W_NS}}}del",
        {
            f"{{{W_NS}}}id": str(rev_id),
            f"{{{W_NS}}}author": author,
            f"{{{W_NS}}}date": date_str,
        },
    )
    r = etree.SubElement(del_el, f"{{{W_NS}}}r")
    dt = etree.SubElement(r, f"{{{W_NS}}}delText")
    dt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    dt.text = text


def _append_ins(
    p_el: etree._Element,
    rev_id: int,
    text: str,
    author: str = COUNTER_PROPOSAL_AUTHOR,
    date_str: str = "2026-10-16T18:00:00Z",
) -> None:
    ins_el = etree.SubElement(
        p_el,
        f"{{{W_NS}}}ins",
        {
            f"{{{W_NS}}}id": str(rev_id),
            f"{{{W_NS}}}author": author,
            f"{{{W_NS}}}date": date_str,
        },
    )
    r = etree.SubElement(ins_el, f"{{{W_NS}}}r")
    t = etree.SubElement(r, f"{{{W_NS}}}t")
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def _append_surgical_tracked_diff(
    p_el: etree._Element,
    vendor_text: str,
    counter_text: str,
    rev_id_start: int = 200,
    author: str = COUNTER_PROPOSAL_AUTHOR,
    date_str: str = "2026-10-16T18:00:00Z",
) -> int:
    """
    Tokenize vendor_text and counter_text with re.findall(r'\\S+\\s*|\\s+', text)
    and emit surgical word-level OOXML Track Changes using difflib.SequenceMatcher:
      - "equal"   -> regular <w:r><w:t xml:space="preserve">
      - "delete"  -> <w:del>
      - "insert"  -> <w:ins>
      - "replace" -> <w:del> followed by <w:ins>
    """
    vendor_tokens = re.findall(r"\S+\s*|\s+", vendor_text or "")
    counter_tokens = re.findall(r"\S+\s*|\s+", counter_text or "")
    matcher = difflib.SequenceMatcher(None, vendor_tokens, counter_tokens, autojunk=False)
    rev_id = rev_id_start

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            eq_chunk = "".join(vendor_tokens[i1:i2])
            if eq_chunk:
                _append_run(p_el, eq_chunk)
        elif tag == "delete":
            del_chunk = "".join(vendor_tokens[i1:i2])
            if del_chunk:
                rev_id += 1
                _append_del(p_el, rev_id=rev_id, text=del_chunk, author=author, date_str=date_str)
        elif tag == "insert":
            ins_chunk = "".join(counter_tokens[j1:j2])
            if ins_chunk:
                rev_id += 1
                _append_ins(p_el, rev_id=rev_id, text=ins_chunk, author=author, date_str=date_str)
        elif tag == "replace":
            del_chunk = "".join(vendor_tokens[i1:i2])
            ins_chunk = "".join(counter_tokens[j1:j2])
            if del_chunk:
                rev_id += 1
                _append_del(p_el, rev_id=rev_id, text=del_chunk, author=author, date_str=date_str)
            if ins_chunk:
                rev_id += 1
                _append_ins(p_el, rev_id=rev_id, text=ins_chunk, author=author, date_str=date_str)

    return rev_id


def _inject_comments_part(docx_bytes: bytes, comments_list: List[Dict[str, Any]]) -> bytes:
    """Inject word/comments.xml and package relationships into the .docx zip archive."""
    in_mem = BytesIO(docx_bytes)
    out_mem = BytesIO()

    nsmap = {"w": W_NS}
    comments_root = etree.Element(f"{{{W_NS}}}comments", nsmap=nsmap)
    for c in comments_list:
        c_el = etree.SubElement(
            comments_root,
            f"{{{W_NS}}}comment",
            {
                f"{{{W_NS}}}id": str(c["id"]),
                f"{{{W_NS}}}author": c["author"],
                f"{{{W_NS}}}date": c["date"],
                f"{{{W_NS}}}initials": "CA",
            },
        )
        p_el = etree.SubElement(c_el, f"{{{W_NS}}}p")
        _append_run(p_el, c["text"])

    comments_xml_bytes = etree.tostring(
        comments_root, xml_declaration=True, encoding="UTF-8", standalone="yes"
    )

    with zipfile.ZipFile(in_mem, "r") as zin, zipfile.ZipFile(out_mem, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                ct_root = etree.fromstring(data)
                exists = any(
                    el.get("PartName") == "/word/comments.xml"
                    for el in ct_root.findall(f"{{{CT_NS}}}Override")
                )
                if not exists:
                    etree.SubElement(
                        ct_root,
                        f"{{{CT_NS}}}Override",
                        {
                            "PartName": "/word/comments.xml",
                            "ContentType": COMMENTS_CONTENT_TYPE,
                        },
                    )
                data = etree.tostring(ct_root, xml_declaration=True, encoding="UTF-8", standalone="yes")
            elif item.filename == "word/_rels/document.xml.rels":
                rels_root = etree.fromstring(data)
                exists = any(
                    el.get("Type") == COMMENTS_REL_TYPE
                    for el in rels_root.findall(f"{{{REL_NS}}}Relationship")
                )
                if not exists:
                    etree.SubElement(
                        rels_root,
                        f"{{{REL_NS}}}Relationship",
                        {
                            "Id": "rIdCommentsCounter99",
                            "Type": COMMENTS_REL_TYPE,
                            "Target": "comments.xml",
                        },
                    )
                data = etree.tostring(rels_root, xml_declaration=True, encoding="UTF-8", standalone="yes")
            zout.writestr(item, data)
        zout.writestr("word/comments.xml", comments_xml_bytes)

    return out_mem.getvalue()


def generate_counter_proposal_docx(
    state: DealWorkbenchState, output_path: str | Path
) -> Path:
    """
    Generate a complete 12-clause external counter-proposal .docx contract with:
    - Executive Summary header & metadata table for state.deal_id (state.vendor_name,
      state.contract_value_usd, state.status) with explicit column widths.
    - All 12 clauses in order, with word-level surgical <w:del> and <w:ins> Track Changes XML nodes
      (authored by "Cymbal Aerospace Legal & Procurement") and sanitized word/comments.xml
      (<75 words, zero internal SME names, precedent %, rule IDs, floors, or internal URLs)
      linked via <w:commentRangeStart>/<w:commentRangeEnd>/<w:commentReference>.
    """
    target_path = Path(output_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    doc = Document()
    doc.add_heading(
        "CYMBAL AEROSPACE CORPORATION — CONSOLIDATED COUNTER-PROPOSAL CONTRACT (GP1 / SP3 / SP5)",
        level=1,
    )
    doc.add_paragraph(
        f"Deal ID: {state.deal_id} | Supplier: {state.vendor_name} ({state.supplier_tier}) | "
        f"Program: {state.boeing_program} | Value: ${state.contract_value_usd:,.2f} ({state.pricing_model}) | "
        f"Status: {state.status}"
    )

    # Executive Summary Metadata Table (sanitized for counterparty sharing, explicit column widths)
    meta_rows = [
        ("Deal ID", state.deal_id),
        ("Buyer (Prime OEM)", "Cymbal Aerospace Corporation"),
        ("Supplier Name", state.vendor_name),
        ("Supplier Tier", state.supplier_tier),
        ("Aircraft Program", state.boeing_program),
        ("Contract Value (USD)", f"${state.contract_value_usd:,.2f}"),
        ("Pricing Model & SOW Lock", f"{state.pricing_model} ({state.sow_cap_clause_ref})"),
        ("Proforma Stack", state.proforma_stack),
        ("Review Status", state.status),
        (
            "Clause Breakdown",
            f"{state.total_clauses_parsed} Total | {state.untouched_clauses_count} Untouched | "
            f"{state.redlined_clauses_count} Redlined",
        ),
        ("Counter-Proposal Author", COUNTER_PROPOSAL_AUTHOR),
    ]
    table = doc.add_table(rows=len(meta_rows), cols=2)
    table.autofit = False
    for idx, (label, val) in enumerate(meta_rows):
        row_cells = table.rows[idx].cells
        row_cells[0].width = Inches(2.2)
        row_cells[1].width = Inches(4.3)
        row_cells[0].text = label
        row_cells[1].text = str(val)

    rev_id = 200
    comment_id = 1
    comments_to_inject: List[Dict[str, Any]] = []
    timestamp = state.updated_at or "2026-10-16T18:00:00Z"

    for clause in state.clauses:
        clean_owner = strip_heading_emojis(clause.sme_owner_label)
        clean_title = strip_heading_emojis(clause.clause_title)
        clean_reg = strip_heading_emojis(clause.regulatory_flag)
        meta_header = strip_heading_emojis(
            f"[{clause.clause_id}] {clause.clause_ref} — {clean_title} "
            f"| SME_TEAM={clause.sme_team} | OWNER={clean_owner} "
            f"| RISK={clause.risk_level} | REG={clean_reg}"
        )
        doc.add_heading(meta_header, level=2)
        p = doc.add_paragraph()
        p_el = p._p

        raw_counter_text = clause.selected_counter_text or clause.boeing_baseline_text
        counter_text = _sanitize_counter_text_for_external(raw_counter_text)

        if not clause.has_redline:
            _append_run(p_el, counter_text)
            continue

        rationale_text = (clause.sme_rationale or "").strip()
        has_comment = bool(rationale_text or clause.has_redline)

        if has_comment:
            etree.SubElement(
                p_el, f"{{{W_NS}}}commentRangeStart", {f"{{{W_NS}}}id": str(comment_id)}
            )

        # Compare vendor_redline_text against counter_text (or baseline if vendor was accepted verbatim)
        deleted_text = (
            clause.vendor_redline_text
            if counter_text != clause.vendor_redline_text
            else clause.boeing_baseline_text
        )
        rev_id = _append_surgical_tracked_diff(
            p_el=p_el,
            vendor_text=deleted_text,
            counter_text=counter_text,
            rev_id_start=rev_id,
            author=COUNTER_PROPOSAL_AUTHOR,
            date_str=timestamp,
        )

        if has_comment:
            etree.SubElement(
                p_el, f"{{{W_NS}}}commentRangeEnd", {f"{{{W_NS}}}id": str(comment_id)}
            )
            r_ref = etree.SubElement(p_el, f"{{{W_NS}}}r")
            rpr_ref = etree.SubElement(r_ref, f"{{{W_NS}}}rPr")
            etree.SubElement(
                rpr_ref, f"{{{W_NS}}}rStyle", {f"{{{W_NS}}}val": "CommentReference"}
            )
            etree.SubElement(
                r_ref, f"{{{W_NS}}}commentReference", {f"{{{W_NS}}}id": str(comment_id)}
            )
            comment_body = sanitize_counterparty_comment(clause)
            comments_to_inject.append(
                {
                    "id": comment_id,
                    "author": COUNTER_PROPOSAL_AUTHOR,
                    "date": timestamp,
                    "text": comment_body,
                }
            )
            comment_id += 1

    buf = BytesIO()
    doc.save(buf)
    final_bytes = _inject_comments_part(buf.getvalue(), comments_to_inject)
    target_path.write_bytes(final_bytes)
    return target_path
