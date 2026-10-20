"""
Counter-Proposal .docx Generator for Boeing CLM.
Generates a complete 12-clause .docx contract with:
- Executive Summary header & metadata table for state.deal_id
- All 12 clauses in order
- Genuine Word OOXML Track Changes (<w:del> and <w:ins> authored by "Boeing CLM Counter-Proposal")
  for redlined clauses
- Genuine word/comments.xml containing each SME's rationale linked via
  <w:commentRangeStart>, <w:commentRangeEnd>, and <w:commentReference>
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Any, Dict, List
import zipfile

from docx import Document
from lxml import etree

from boeing_clm.models import DealWorkbenchState

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
COMMENTS_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
COMMENTS_CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"

COUNTER_PROPOSAL_AUTHOR = "Cymbal CLM Counter-Proposal"


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
    Generate a complete 12-clause counter-proposal .docx contract with:
    - Executive Summary header & metadata table for state.deal_id (state.vendor_name,
      state.contract_value_usd, state.status).
    - All 12 clauses in order, with native Word <w:del> and <w:ins> Track Changes XML nodes
      (authored by "Boeing CLM Counter-Proposal") and word/comments.xml containing each SME's
      rationale linked via <w:commentRangeStart>/<w:commentRangeEnd>/<w:commentReference>.
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

    # Executive Summary Metadata Table
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
        ("SharePoint Folder URL", state.sharepoint_folder_url),
        ("BigQuery Dataset", state.bigquery_dataset),
    ]
    table = doc.add_table(rows=len(meta_rows), cols=2)
    for idx, (label, val) in enumerate(meta_rows):
        row_cells = table.rows[idx].cells
        row_cells[0].text = label
        row_cells[1].text = str(val)

    rev_id = 200
    comment_id = 1
    comments_to_inject: List[Dict[str, Any]] = []
    timestamp = state.updated_at or "2026-10-16T18:00:00Z"

    for clause in state.clauses:
        meta_header = (
            f"[{clause.clause_id}] {clause.clause_ref} — {clause.clause_title} "
            f"| SME_TEAM={clause.sme_team} | OWNER={clause.sme_owner_label} "
            f"| RISK={clause.risk_level} | REG={clause.regulatory_flag}"
        )
        doc.add_heading(meta_header, level=2)
        p = doc.add_paragraph()
        p_el = p._p

        counter_text = clause.selected_counter_text or clause.boeing_baseline_text

        if not clause.has_redline:
            _append_run(p_el, counter_text)
            continue

        rationale_text = (clause.sme_rationale or "").strip()
        has_comment = bool(rationale_text)

        if has_comment:
            etree.SubElement(
                p_el, f"{{{W_NS}}}commentRangeStart", {f"{{{W_NS}}}id": str(comment_id)}
            )

        # Inject <w:del> with vendor_redline_text (or baseline if vendor was accepted verbatim)
        deleted_text = (
            clause.vendor_redline_text
            if counter_text != clause.vendor_redline_text
            else clause.boeing_baseline_text
        )
        if deleted_text:
            rev_id += 1
            _append_del(
                p_el,
                rev_id=rev_id,
                text=deleted_text,
                author=COUNTER_PROPOSAL_AUTHOR,
                date_str=timestamp,
            )

        rev_id += 1
        _append_ins(
            p_el,
            rev_id=rev_id,
            text=counter_text,
            author=COUNTER_PROPOSAL_AUTHOR,
            date_str=timestamp,
        )

        if has_comment:
            etree.SubElement(
                p_el, f"{{{W_NS}}}commentRangeEnd", {f"{{{W_NS}}}id": str(comment_id)}
            )
            r_ref = etree.SubElement(p_el, f"{{{W_NS}}}r")
            etree.SubElement(
                r_ref, f"{{{W_NS}}}commentReference", {f"{{{W_NS}}}id": str(comment_id)}
            )
            reviewer_label = clause.sme_reviewer or clause.sme_team
            comment_body = (
                f"[{clause.sme_team} — {reviewer_label} | {clause.sme_status}] {rationale_text}"
            )
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
