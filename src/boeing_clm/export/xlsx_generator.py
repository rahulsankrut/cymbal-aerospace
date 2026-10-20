"""
SharePoint Deviation Matrix .xlsx Generator for Boeing CLM.
Uses openpyxl to build a styled 4-worksheet workbook:
  1. Executive Summary
  2. Clause Sign-Off Matrix
  3. BigQuery Precedents
  4. Immutable Audit Trail
"""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

from boeing_clm.models import DealWorkbenchState

BOEING_NAVY = "0033A0"
BOEING_SLATE = "1E3A8A"
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
TITLE_FONT = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
SUBTITLE_FONT = Font(name="Calibri", size=11, bold=True, color=BOEING_NAVY)
BOLD_FONT = Font(name="Calibri", size=10, bold=True, color="111827")
REGULAR_FONT = Font(name="Calibri", size=10, bold=False, color="1F2937")

NAVY_FILL = PatternFill(start_color=BOEING_NAVY, end_color=BOEING_NAVY, fill_type="solid")
SLATE_FILL = PatternFill(start_color=BOEING_SLATE, end_color=BOEING_SLATE, fill_type="solid")
ZEBRA_FILL = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

STATUS_FILLS: Dict[str, PatternFill] = {
    "APPROVED": PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid"),
    "CONFLICT": PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"),
    "PENDING": PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid"),
    "UNTOUCHED": PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid"),
}

RISK_FILLS: Dict[str, PatternFill] = {
    "CRITICAL": PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"),
    "HIGH": PatternFill(start_color="FFEDD5", end_color="FFEDD5", fill_type="solid"),
    "MOD": PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid"),
    "NONE": PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid"),
}

THIN_BORDER_SIDE = Side(border_style="thin", color="CBD5E1")
CELL_BORDER = Border(
    left=THIN_BORDER_SIDE,
    right=THIN_BORDER_SIDE,
    top=THIN_BORDER_SIDE,
    bottom=THIN_BORDER_SIDE,
)


def _style_header_row(ws: Worksheet, row_idx: int, col_count: int, fill: PatternFill = NAVY_FILL) -> None:
    ws.row_dimensions[row_idx].height = 24
    for col_idx in range(1, col_count + 1):
        cell = ws.cell(row=row_idx, column=col_idx)
        cell.font = HEADER_FONT
        cell.fill = fill
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = CELL_BORDER


def _set_column_widths(ws: Worksheet, widths: List[int]) -> None:
    for idx, width in enumerate(widths, start=1):
        col_letter = get_column_letter(idx)
        ws.column_dimensions[col_letter].width = width


def _build_executive_summary_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "Executive Summary"
    ws.views.sheetView[0].showGridLines = True

    ws.merge_cells("A1:B1")
    title_cell = ws["A1"]
    title_cell.value = f"CYMBAL AEROSPACE CORPORATION — CLM DEVIATION MATRIX ({state.deal_id})"
    title_cell.font = TITLE_FONT
    title_cell.fill = NAVY_FILL
    title_cell.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 30

    ws.append(["Metadata Field", "Value"])
    _style_header_row(ws, 2, 2, SLATE_FILL)

    summary_rows = [
        ("Deal ID", state.deal_id),
        ("Buyer (Prime OEM)", "Cymbal Aerospace Corporation"),
        ("Supplier / Vendor Name", state.vendor_name),
        ("Supplier Tier", state.supplier_tier),
        ("Aircraft Program", state.boeing_program),
        ("Contract Value (USD)", f"${state.contract_value_usd:,.2f}"),
        ("Proforma Stack", state.proforma_stack),
        ("Pricing Model", state.pricing_model),
        ("SOW Cap Clause Reference", state.sow_cap_clause_ref),
        ("Overall Deal Status", state.status),
        ("Total Clauses Parsed", state.total_clauses_parsed),
        ("Untouched Clauses Count", state.untouched_clauses_count),
        ("Redlined Clauses Count", state.redlined_clauses_count),
        ("Active Cross-Clause Conflicts", len(state.active_conflicts)),
        ("M365 SharePoint Folder Link", state.sharepoint_folder_url),
        ("SharePoint Deviation Matrix File", state.deviation_matrix_xlsx),
        ("BigQuery Dataset", state.bigquery_dataset),
        ("Last Updated (UTC)", state.updated_at),
    ]

    for offset, (k, v) in enumerate(summary_rows, start=3):
        ws.append([k, v])
        k_cell = ws.cell(row=offset, column=1)
        v_cell = ws.cell(row=offset, column=2)
        k_cell.font = BOLD_FONT
        v_cell.font = REGULAR_FONT
        k_cell.border = CELL_BORDER
        v_cell.border = CELL_BORDER
        k_cell.alignment = Alignment(vertical="center")
        v_cell.alignment = Alignment(vertical="center", wrap_text=True)
        if offset % 2 == 1:
            k_cell.fill = ZEBRA_FILL
            v_cell.fill = ZEBRA_FILL

    # Active Conflicts section
    next_row = len(summary_rows) + 4
    ws.cell(row=next_row, column=1, value="Cross-Clause Conflict Governance").font = SUBTITLE_FONT
    header_row = next_row + 1
    conflict_headers = [
        "Rule ID",
        "Rule Type",
        "Source Clause",
        "Target Clause",
        "Severity",
        "Conflict Title",
        "Description",
        "Harmonized Resolution",
    ]
    for col_i, h_text in enumerate(conflict_headers, start=1):
        ws.cell(row=header_row, column=col_i, value=h_text)
    _style_header_row(ws, header_row, len(conflict_headers), SLATE_FILL)

    if state.active_conflicts:
        for c_idx, conflict in enumerate(state.active_conflicts, start=header_row + 1):
            row_vals = [
                conflict.rule_id,
                conflict.rule_type,
                f"{conflict.source_clause_id} ({conflict.source_sme_team})",
                f"{conflict.target_clause_id} ({conflict.target_sme_team})",
                conflict.severity,
                conflict.conflict_title,
                conflict.conflict_description,
                conflict.harmonized_resolution_text,
            ]
            for col_i, val in enumerate(row_vals, start=1):
                c = ws.cell(row=c_idx, column=col_i, value=val)
                c.font = REGULAR_FONT
                c.border = CELL_BORDER
                c.fill = STATUS_FILLS["CONFLICT"]
                c.alignment = Alignment(vertical="top", wrap_text=True)
    else:
        r_idx = header_row + 1
        ws.cell(row=r_idx, column=1, value="NONE")
        ws.cell(row=r_idx, column=2, value="HARMONIZED")
        ws.cell(row=r_idx, column=3, value="-")
        ws.cell(row=r_idx, column=4, value="-")
        ws.cell(row=r_idx, column=5, value="CLEAR")
        ws.cell(row=r_idx, column=6, value="Zero Active Cross-Clause Conflicts")
        ws.cell(
            row=r_idx,
            column=7,
            value="All redlined clauses and SOW pricing locks are harmonized.",
        )
        ws.cell(row=r_idx, column=8, value="Ready for Counter-Proposal Dispatch")
        for col_i in range(1, 9):
            c = ws.cell(row=r_idx, column=col_i)
            c.font = REGULAR_FONT
            c.border = CELL_BORDER
            c.fill = STATUS_FILLS["APPROVED"]

    _set_column_widths(ws, [34, 68, 20, 20, 20, 32, 48, 48])


def _build_clause_signoff_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "Clause Sign-Off Matrix"
    headers = [
        "Clause ID",
        "Proforma",
        "Section Ref",
        "Clause Title",
        "Redlined?",
        "SME Team",
        "SME Owner",
        "Risk Level",
        "Regulatory Flag",
        "Boeing Baseline",
        "Vendor Redline",
        "Vendor Comment",
        "Selected Option",
        "Selected Counter-Position",
        "SME Status",
        "Reviewer",
        "SME Rationale",
    ]
    ws.append(headers)
    _style_header_row(ws, 1, len(headers), NAVY_FILL)

    for row_idx, clause in enumerate(state.clauses, start=2):
        row_values = [
            clause.clause_id,
            clause.proforma_doc,
            clause.clause_ref,
            clause.clause_title,
            "YES" if clause.has_redline else "NO",
            clause.sme_team,
            clause.sme_owner_label,
            clause.risk_level,
            clause.regulatory_flag,
            clause.boeing_baseline_text,
            clause.vendor_redline_text,
            clause.vendor_comment,
            clause.selected_option_key,
            clause.selected_counter_text,
            clause.sme_status,
            clause.sme_reviewer,
            clause.sme_rationale,
        ]
        ws.append(row_values)
        ws.row_dimensions[row_idx].height = 48

        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            cell.font = BOLD_FONT if col_idx in (1, 6, 8, 15) else REGULAR_FONT
            cell.border = CELL_BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if col_idx == 8:
                cell.fill = RISK_FILLS.get(clause.risk_level, ZEBRA_FILL)
            elif col_idx == 15:
                cell.fill = STATUS_FILLS.get(clause.sme_status, ZEBRA_FILL)
            elif row_idx % 2 == 1:
                cell.fill = ZEBRA_FILL

    _set_column_widths(
        ws,
        [14, 10, 16, 32, 12, 16, 26, 14, 28, 48, 48, 40, 20, 48, 16, 24, 44],
    )


def _build_bigquery_precedents_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "BigQuery Precedents"
    headers = [
        "Clause ID",
        "Section Ref",
        "SME Team",
        "Regulatory Lockout",
        "Total Matches",
        "Held Firm %",
        "Compromise Tier-1 %",
        "Accepted Vendor %",
        "Precedent Exception ID",
        "Historical Contract ID",
        "Supplier Name",
        "Supplier Tier",
        "Boeing Program",
        "Outcome Category",
        "Similarity Score",
        "Approval Authority",
        "Signed Date",
        "Final Agreed Language",
        "Negotiation Notes",
    ]
    ws.append(headers)
    _style_header_row(ws, 1, len(headers), NAVY_FILL)

    row_cursor = 2
    redlined_clauses = [c for c in state.clauses if c.has_redline]

    for clause in redlined_clauses:
        pa = clause.precedent_analysis
        if pa and pa.precedents:
            dist = pa.distribution
            for prec in pa.precedents:
                ws.append(
                    [
                        clause.clause_id,
                        clause.clause_ref,
                        clause.sme_team,
                        "LOCKED" if pa.regulatory_lockout else "ELIGIBLE",
                        dist.total_matches,
                        f"{dist.held_firm_pct}% ({dist.held_firm_count})",
                        f"{dist.compromise_tier_1_pct}% ({dist.compromise_tier_1_count})",
                        f"{dist.accepted_vendor_pct}% ({dist.accepted_vendor_count})",
                        prec.exception_id,
                        prec.contract_id,
                        prec.supplier_name,
                        prec.supplier_tier,
                        prec.boeing_program,
                        prec.outcome_category,
                        round(prec.similarity_score, 4),
                        prec.approval_authority,
                        prec.signed_date,
                        prec.final_agreed_language,
                        prec.negotiation_notes,
                    ]
                )
                ws.row_dimensions[row_cursor].height = 42
                for col_i in range(1, len(headers) + 1):
                    cell = ws.cell(row=row_cursor, column=col_i)
                    cell.font = REGULAR_FONT
                    cell.border = CELL_BORDER
                    cell.alignment = Alignment(vertical="top", wrap_text=True)
                    if row_cursor % 2 == 1:
                        cell.fill = ZEBRA_FILL
                row_cursor += 1
        else:
            dist = pa.distribution if pa else None
            ws.append(
                [
                    clause.clause_id,
                    clause.clause_ref,
                    clause.sme_team,
                    clause.regulatory_flag,
                    dist.total_matches if dist else 0,
                    f"{dist.held_firm_pct}%" if dist else "N/A",
                    f"{dist.compromise_tier_1_pct}%" if dist else "N/A",
                    f"{dist.accepted_vendor_pct}%" if dist else "N/A",
                    "-",
                    "-",
                    state.vendor_name,
                    state.supplier_tier,
                    state.boeing_program,
                    clause.selected_option_key.upper(),
                    1.0,
                    clause.sme_reviewer or clause.sme_owner_label,
                    state.updated_at[:10] if state.updated_at else "2026-10-16",
                    clause.selected_counter_text,
                    clause.sme_rationale,
                ]
            )
            ws.row_dimensions[row_cursor].height = 36
            for col_i in range(1, len(headers) + 1):
                cell = ws.cell(row=row_cursor, column=col_i)
                cell.font = REGULAR_FONT
                cell.border = CELL_BORDER
                cell.alignment = Alignment(vertical="top", wrap_text=True)
            row_cursor += 1

    _set_column_widths(
        ws,
        [14, 16, 16, 22, 14, 16, 20, 18, 22, 22, 24, 18, 18, 20, 16, 24, 14, 48, 44],
    )


def _build_audit_trail_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "Immutable Audit Trail"
    headers = [
        "Event ID",
        "Created At (UTC)",
        "Deal ID",
        "Clause ID",
        "SME Team",
        "Actor",
        "Action",
        "Selected Option Key",
        "Source Surface",
        "Rationale",
    ]
    ws.append(headers)
    _style_header_row(ws, 1, len(headers), NAVY_FILL)

    for row_idx, ev in enumerate(state.recent_events, start=2):
        ws.append(
            [
                ev.event_id,
                ev.created_at,
                ev.deal_id,
                ev.clause_id,
                ev.sme_team,
                ev.actor,
                ev.action,
                ev.selected_option_key,
                ev.source_surface,
                ev.rationale,
            ]
        )
        ws.row_dimensions[row_idx].height = 32
        for col_i in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_i)
            cell.font = REGULAR_FONT
            cell.border = CELL_BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if row_idx % 2 == 1:
                cell.fill = ZEBRA_FILL

    _set_column_widths(ws, [22, 24, 18, 14, 16, 28, 24, 22, 24, 56])


def generate_deviation_matrix_xlsx(
    state: DealWorkbenchState, output_path: str | Path
) -> Path:
    """
    Build and save the 4-worksheet SharePoint Deviation Matrix .xlsx workbook:
      - Sheet 1: Executive Summary
      - Sheet 2: Clause Sign-Off Matrix
      - Sheet 3: BigQuery Precedents
      - Sheet 4: Immutable Audit Trail
    """
    target_path = Path(output_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws_exec = wb.active
    assert ws_exec is not None
    _build_executive_summary_sheet(ws_exec, state)

    ws_matrix = wb.create_sheet(title="Clause Sign-Off Matrix")
    _build_clause_signoff_sheet(ws_matrix, state)

    ws_prec = wb.create_sheet(title="BigQuery Precedents")
    _build_bigquery_precedents_sheet(ws_prec, state)

    ws_audit = wb.create_sheet(title="Immutable Audit Trail")
    _build_audit_trail_sheet(ws_audit, state)

    wb.save(str(target_path))
    return target_path
