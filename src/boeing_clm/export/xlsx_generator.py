"""
SharePoint Deviation Matrix .xlsx Generator for Cymbal Aerospace CLM.
Uses openpyxl to build a banker-styled 5-worksheet workbook:
  1. 1_Executive_Summary
  2. 2_Clause_Deviation_Matrix
  3. 3_Cross_Clause_Conflict_Log
  4. 4_BigQuery_Precedent_Benchmarks
  5. 5_Portfolio_Tabular_Review

Follows institutional banker conventions (xlsx & tabular-review skills):
- Hardcoded numeric inputs: Blue font (0000FF)
- Same-sheet formulas: Black font (000000)
- Cross-sheet formula links: Green font (008000)
- Number formats: $#,##0 (currency), 0.0% (percentages), 0.0"x" (multiples), #,##0 (counts)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

from boeing_clm.ingestion.docx_track_changes import parse_redlined_docx
from boeing_clm.models import ClauseWorkbenchItem, DealWorkbenchState

BOEING_NAVY = "0033A0"
BOEING_SLATE = "1E3A8A"
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
TITLE_FONT = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
SUBTITLE_FONT = Font(name="Calibri", size=11, bold=True, color=BOEING_NAVY)
BOLD_FONT = Font(name="Calibri", size=10, bold=True, color="111827")
REGULAR_FONT = Font(name="Calibri", size=10, bold=False, color="1F2937")

# Banker font color coding (xlsx skill)
INPUT_BLUE_FONT = Font(name="Calibri", size=10, bold=False, color="0000FF")
FORMULA_BLACK_FONT = Font(name="Calibri", size=10, bold=True, color="000000")
CROSS_SHEET_GREEN_FONT = Font(name="Calibri", size=10, bold=True, color="008000")

# Institutional number formats
CURRENCY_FORMAT = "$#,##0"
PERCENT_FORMAT = "0.0%"
MULTIPLE_FORMAT = '0.0"x"'
INTEGER_FORMAT = "#,##0"

NAVY_FILL = PatternFill(start_color=BOEING_NAVY, end_color=BOEING_NAVY, fill_type="solid")
SLATE_FILL = PatternFill(start_color=BOEING_SLATE, end_color=BOEING_SLATE, fill_type="solid")
ZEBRA_FILL = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
SUMMARY_FILL = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")

STATUS_FILLS: Dict[str, PatternFill] = {
    "APPROVED": PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid"),
    "CONFLICT": PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"),
    "PENDING": PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid"),
    "PENDING_SME": PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid"),
    "UNTOUCHED": PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid"),
}

RISK_FILLS: Dict[str, PatternFill] = {
    "CRITICAL": PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid"),
    "HIGH": PatternFill(start_color="FFEDD5", end_color="FFEDD5", fill_type="solid"),
    "MOD": PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid"),
    "NONE": PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid"),
}

THIN_BORDER_SIDE = Side(border_style="thin", color="CBD5E1")
TOTAL_BOTTOM_SIDE = Side(border_style="thin", color="000000")
CELL_BORDER = Border(
    left=THIN_BORDER_SIDE,
    right=THIN_BORDER_SIDE,
    top=THIN_BORDER_SIDE,
    bottom=THIN_BORDER_SIDE,
)
TOTAL_BORDER = Border(
    left=THIN_BORDER_SIDE,
    right=THIN_BORDER_SIDE,
    top=THIN_BORDER_SIDE,
    bottom=TOTAL_BOTTOM_SIDE,
)

_DEFAULT_PRECEDENT_COUNTS: Dict[str, tuple[int, int, int]] = {
    "GP1-12": (14, 1, 1),
    "GP1-19": (4, 11, 1),
    "SP3-04": (5, 10, 1),
    "SP5-03": (15, 1, 0),
}


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
    ws.title = "1_Executive_Summary"
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

    # Rows 3..21 with explicit banker color coding and live formulas
    summary_specs: List[tuple[str, Any, Font, str | None]] = [
        ("Deal ID", state.deal_id, REGULAR_FONT, None),
        ("Buyer (Prime OEM)", "Cymbal Aerospace Corporation", REGULAR_FONT, None),
        ("Supplier / Vendor Name", state.vendor_name, REGULAR_FONT, None),
        ("Supplier Tier", state.supplier_tier, REGULAR_FONT, None),
        ("Aircraft Program", state.boeing_program, REGULAR_FONT, None),
        ("Contract Value (USD)", float(state.contract_value_usd), INPUT_BLUE_FONT, CURRENCY_FORMAT),
        ("Tier-1 Liability Cap Multiple", 2.0, INPUT_BLUE_FONT, MULTIPLE_FORMAT),
        ("Tier-1 Liability Cap Ceiling (USD)", "=B8*B9", FORMULA_BLACK_FONT, CURRENCY_FORMAT),
        ("Proforma Stack", state.proforma_stack, REGULAR_FONT, None),
        ("Pricing Model", state.pricing_model, REGULAR_FONT, None),
        ("SOW Cap Clause Reference", state.sow_cap_clause_ref, REGULAR_FONT, None),
        ("Overall Deal Status", state.status, BOLD_FONT, None),
        (
            "Total Clauses Parsed",
            "=COUNTA('2_Clause_Deviation_Matrix'!A2:A13)",
            CROSS_SHEET_GREEN_FONT,
            INTEGER_FORMAT,
        ),
        (
            "Untouched Clauses Count",
            "=COUNTIF('2_Clause_Deviation_Matrix'!F2:F13,\"NO\")",
            CROSS_SHEET_GREEN_FONT,
            INTEGER_FORMAT,
        ),
        (
            "Redlined Clauses Count",
            "=COUNTIF('2_Clause_Deviation_Matrix'!F2:F13,\"YES\")",
            CROSS_SHEET_GREEN_FONT,
            INTEGER_FORMAT,
        ),
        (
            "Approved Redlined Clauses Count",
            "=COUNTIFS('2_Clause_Deviation_Matrix'!F2:F13,\"YES\",'2_Clause_Deviation_Matrix'!G2:G13,\"APPROVED\")",
            CROSS_SHEET_GREEN_FONT,
            INTEGER_FORMAT,
        ),
        (
            "Active Cross-Clause Conflicts",
            "=COUNTA('3_Cross_Clause_Conflict_Log'!A2:A20)",
            CROSS_SHEET_GREEN_FONT,
            INTEGER_FORMAT,
        ),
        ("M365 SharePoint Folder Link", state.sharepoint_folder_url, REGULAR_FONT, None),
        ("SharePoint Deviation Matrix File", state.deviation_matrix_xlsx, REGULAR_FONT, None),
        ("BigQuery Dataset", state.bigquery_dataset, REGULAR_FONT, None),
        ("Last Updated (UTC)", state.updated_at, REGULAR_FONT, None),
    ]

    for offset, (label, val, val_font, num_fmt) in enumerate(summary_specs, start=3):
        ws.append([label, val])
        k_cell = ws.cell(row=offset, column=1)
        v_cell = ws.cell(row=offset, column=2)
        k_cell.font = BOLD_FONT
        v_cell.font = val_font
        if num_fmt:
            v_cell.number_format = num_fmt
        k_cell.border = CELL_BORDER
        v_cell.border = CELL_BORDER
        k_cell.alignment = Alignment(vertical="center")
        v_cell.alignment = Alignment(
            horizontal="right" if num_fmt else "left",
            vertical="center",
            wrap_text=not bool(num_fmt),
        )
        if offset % 2 == 1:
            k_cell.fill = ZEBRA_FILL
            v_cell.fill = ZEBRA_FILL

    _set_column_widths(ws, [38, 72])


def _build_clause_deviation_matrix_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "2_Clause_Deviation_Matrix"
    ws.views.sheetView[0].showGridLines = True
    # Note: Column A = Clause ID, Column F = Redlined? ("YES"/"NO"), Column G = SME Status ("APPROVED", etc.)
    headers = [
        "Clause ID",
        "Proforma",
        "Section Ref",
        "Clause Title",
        "SME Team",
        "Redlined?",
        "SME Status",
        "SME Owner",
        "Risk Level",
        "Regulatory Flag",
        "Boeing Baseline",
        "Vendor Redline",
        "Vendor Comment",
        "Selected Option",
        "Selected Counter-Position",
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
            clause.sme_team,
            "YES" if clause.has_redline else "NO",
            clause.sme_status,
            clause.sme_owner_label,
            clause.risk_level,
            clause.regulatory_flag,
            clause.boeing_baseline_text,
            clause.vendor_redline_text,
            clause.vendor_comment,
            clause.selected_option_key,
            clause.selected_counter_text,
            clause.sme_reviewer,
            clause.sme_rationale,
        ]
        ws.append(row_values)
        ws.row_dimensions[row_idx].height = 48

        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_idx)
            cell.font = BOLD_FONT if col_idx in (1, 5, 7, 9) else REGULAR_FONT
            cell.border = CELL_BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if col_idx == 7:
                cell.fill = STATUS_FILLS.get(clause.sme_status, ZEBRA_FILL)
            elif col_idx == 9:
                cell.fill = RISK_FILLS.get(clause.risk_level, ZEBRA_FILL)
            elif row_idx % 2 == 1:
                cell.fill = ZEBRA_FILL

    _set_column_widths(
        ws,
        [14, 10, 16, 32, 16, 12, 16, 26, 14, 28, 48, 48, 40, 20, 48, 24, 44],
    )


def _build_conflict_and_audit_log_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "3_Cross_Clause_Conflict_Log"
    ws.views.sheetView[0].showGridLines = True

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
    ws.append(conflict_headers)
    _style_header_row(ws, 1, len(conflict_headers), NAVY_FILL)

    # Rows 2..20 are reserved strictly for active conflicts so =COUNTA('3_Cross_Clause_Conflict_Log'!A2:A20)
    # evaluates to the exact number of active conflicts.
    for c_idx, conflict in enumerate(state.active_conflicts[:19], start=2):
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
        ws.row_dimensions[c_idx].height = 42

    # Immutable Audit Trail section begins at Row 22 (below A2:A20 conflict range)
    audit_title_row = 21
    ws.cell(row=audit_title_row, column=1, value="Immutable Governance Audit Trail").font = SUBTITLE_FONT

    audit_header_row = 22
    audit_headers = [
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
    for col_i, h_text in enumerate(audit_headers, start=1):
        ws.cell(row=audit_header_row, column=col_i, value=h_text)
    _style_header_row(ws, audit_header_row, len(audit_headers), SLATE_FILL)

    for offset, ev in enumerate(state.recent_events, start=audit_header_row + 1):
        ev_vals = [
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
        for col_i, val in enumerate(ev_vals, start=1):
            cell = ws.cell(row=offset, column=col_i, value=val)
            cell.font = REGULAR_FONT
            cell.border = CELL_BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if offset % 2 == 1:
                cell.fill = ZEBRA_FILL
        ws.row_dimensions[offset].height = 32

    _set_column_widths(ws, [26, 24, 22, 22, 18, 32, 36, 48, 24, 52])


def _build_bigquery_precedents_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    ws.title = "4_BigQuery_Precedent_Benchmarks"
    ws.views.sheetView[0].showGridLines = True
    # Columns E, F, G are Held Firm Count, Compromise Tier-1 Count, Accepted Vendor Count (Blue 0000FF inputs)
    # Column H is Total Matched Precedents using =SUM(E2:G2) (Black 000000 formula)
    # Columns I, J, K are Held Firm %, Compromise Tier-1 %, Accepted Vendor % using =IF(H2>0,E2/H2,0) (0.0%)
    headers = [
        "Clause ID",
        "Section Ref",
        "SME Team",
        "Regulatory Lockout",
        "Held Firm Count",
        "Compromise Tier-1 Count",
        "Accepted Vendor Count",
        "Total Matched Precedents",
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
        default_hf, default_comp, default_acc = _DEFAULT_PRECEDENT_COUNTS.get(
            clause.clause_id, (10, 5, 1)
        )
        if pa and pa.precedents:
            dist = pa.distribution
            for prec in pa.precedents:
                r = row_cursor
                ws.append(
                    [
                        clause.clause_id,
                        clause.clause_ref,
                        clause.sme_team,
                        "LOCKED" if pa.regulatory_lockout else "ELIGIBLE",
                        int(dist.held_firm_count),
                        int(dist.compromise_tier_1_count),
                        int(dist.accepted_vendor_count),
                        f"=SUM(E{r}:G{r})",
                        f"=IF(H{r}>0,E{r}/H{r},0)",
                        f"=IF(H{r}>0,F{r}/H{r},0)",
                        f"=IF(H{r}>0,G{r}/H{r},0)",
                        prec.exception_id,
                        prec.contract_id,
                        prec.supplier_name,
                        prec.supplier_tier,
                        prec.boeing_program,
                        prec.outcome_category,
                        round(float(prec.similarity_score), 4),
                        prec.approval_authority,
                        prec.signed_date,
                        prec.final_agreed_language,
                        prec.negotiation_notes,
                    ]
                )
                _style_precedent_row(ws, r, len(headers))
                row_cursor += 1
        else:
            dist = pa.distribution if pa else None
            hf_cnt = int(dist.held_firm_count) if dist else default_hf
            comp_cnt = int(dist.compromise_tier_1_count) if dist else default_comp
            acc_cnt = int(dist.accepted_vendor_count) if dist else default_acc
            r = row_cursor
            ws.append(
                [
                    clause.clause_id,
                    clause.clause_ref,
                    clause.sme_team,
                    clause.regulatory_flag,
                    hf_cnt,
                    comp_cnt,
                    acc_cnt,
                    f"=SUM(E{r}:G{r})",
                    f"=IF(H{r}>0,E{r}/H{r},0)",
                    f"=IF(H{r}>0,F{r}/H{r},0)",
                    f"=IF(H{r}>0,G{r}/H{r},0)",
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
            _style_precedent_row(ws, r, len(headers))
            row_cursor += 1

    _set_column_widths(
        ws,
        [14, 16, 14, 22, 16, 20, 20, 22, 14, 18, 16, 22, 22, 24, 18, 22, 18, 16, 24, 14, 48, 44],
    )


def _style_precedent_row(ws: Worksheet, row_idx: int, col_count: int) -> None:
    ws.row_dimensions[row_idx].height = 42
    for col_i in range(1, col_count + 1):
        cell = ws.cell(row=row_idx, column=col_i)
        cell.border = CELL_BORDER
        if col_i in (5, 6, 7):
            cell.font = INPUT_BLUE_FONT
            cell.number_format = INTEGER_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="top")
        elif col_i == 8:
            cell.font = FORMULA_BLACK_FONT
            cell.number_format = INTEGER_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="top")
        elif col_i in (9, 10, 11):
            cell.font = FORMULA_BLACK_FONT
            cell.number_format = PERCENT_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="top")
        elif col_i == 18:
            cell.font = INPUT_BLUE_FONT
            cell.number_format = PERCENT_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="top")
        else:
            cell.font = REGULAR_FONT
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        if row_idx % 2 == 1:
            cell.fill = ZEBRA_FILL


def _format_tabular_clause_cell(status: str, position: str, counter_text: str) -> str:
    clean_text = " ".join((counter_text or "").split())
    return f"[{status}] | {position} | {clean_text}"


def _extract_fixture_clause_summary(
    fixture_filename: str,
    fallback_cells: Dict[str, str],
    status_by_clause: Dict[str, tuple[str, str]],
) -> Dict[str, str]:
    golden_dir = Path(__file__).resolve().parents[3] / "specs" / "04_golden_fixtures"
    fixture_path = golden_dir / fixture_filename
    if not fixture_path.exists():
        return fallback_cells
    try:
        diffs = parse_redlined_docx(fixture_path)
        by_id = {d.clause_id: d for d in diffs}
        result: Dict[str, str] = {}
        for cid in ("GP1-12", "GP1-19", "SP3-04", "SP5-03"):
            status, pos = status_by_clause[cid]
            d = by_id.get(cid)
            if d is not None:
                text = d.boeing_baseline_text if pos == "hold_firm" else d.vendor_redline_text
                result[cid] = _format_tabular_clause_cell(status, pos, text)
            else:
                result[cid] = fallback_cells[cid]
        return result
    except Exception:
        return fallback_cells


def _build_portfolio_tabular_review_sheet(ws: Worksheet, state: DealWorkbenchState) -> None:
    """
    Build Worksheet 5 (`5_Portfolio_Tabular_Review`) per the `tabular-review` skill:
    - One row per portfolio deal (`BA-2026-AV-8921`, `BA-2026-TR-5510`, `BA-2026-LG-7740`)
    - Columns: Deal ID, Supplier, Program, Value ($ USD), and the 4 key negotiated clauses
      (`GP1 §12.2 Warranty & FAA Inspection`, `GP1 §19 Limitation of Liability`,
       `SP3 §4.1 Customs & Tariffs`, `SP5 §3.2 DFARS Cyber Reporting`) showing
      `[Status] | Position | Verbatim Counter-Language`
    - Bottom summary row using live =SUM(...) and =COUNTIF(...) formulas.
    """
    ws.title = "5_Portfolio_Tabular_Review"
    ws.views.sheetView[0].showGridLines = True

    headers = [
        "Deal ID",
        "Supplier",
        "Program",
        "Value ($ USD)",
        "GP1 §12.2 Warranty & FAA Inspection",
        "GP1 §19 Limitation of Liability",
        "SP3 §4.1 Customs & Tariffs",
        "SP5 §3.2 DFARS Cyber Reporting",
        "Liability Cap Multiple",
        "Portfolio Gate Status",
    ]
    ws.append(headers)
    _style_header_row(ws, 1, len(headers), NAVY_FILL)

    state_clauses_by_id: Dict[str, ClauseWorkbenchItem] = {c.clause_id: c for c in state.clauses}

    def _from_active_state(cid: str, fallback: str) -> str:
        c = state_clauses_by_id.get(cid)
        if c is None:
            return fallback
        return _format_tabular_clause_cell(
            c.sme_status,
            c.selected_option_key,
            c.selected_counter_text or c.boeing_baseline_text,
        )

    av8921_defaults = {
        "GP1-12": _format_tabular_clause_cell(
            "APPROVED",
            "hold_firm",
            "12.2 Seller warrants all Goods against defects in material, workmanship, and avionics firmware for thirty-six (36) months from initial aircraft delivery to Boeing's airline customer.",
        ),
        "GP1-19": _format_tabular_clause_cell(
            "APPROVED",
            "compromise_tier_1",
            "19.1 Seller's liability for general direct damages shall not exceed two hundred percent (200%) of total Purchase Order value ($90M), provided that airworthiness recall costs and 24.1 IP indemnity remain uncapped.",
        ),
        "SP3-04": _format_tabular_clause_cell(
            "APPROVED",
            "custom_harmonized",
            "4.1 All unit prices are DDP Cymbal Everett/Renton facility. Any verified Section 232/301 tariff increase exceeding 5% shall be shared 50/50 up to a strict maximum cap of 2.0% ($900,000) of Purchase Order value.",
        ),
        "SP5-03": _format_tabular_clause_cell(
            "APPROVED",
            "hold_firm",
            "3.2 Seller shall maintain NIST SP 800-171 controls and report any cybersecurity incident affecting Covered Defense Information within seventy-two (72) hours of discovery.",
        ),
    }

    tr5510_defaults = _extract_fixture_clause_summary(
        "Vanguard_Working_Review_TR5510.docx",
        fallback_cells={
            "GP1-12": _format_tabular_clause_cell(
                "APPROVED",
                "hold_firm",
                "12.2 Seller warrants all TRA-500 Thrust Reverser Actuator assemblies against defects in hydraulic seals, ballscrews, and workmanship for thirty-six (36) months from initial aircraft delivery.",
            ),
            "GP1-19": _format_tabular_clause_cell(
                "CONFLICT",
                "compromise_tier_1",
                "19.1 Seller's aggregate liability for direct damages, nacelle line-stoppage, and thrust reverser airworthiness recall costs shall not exceed 150% (1.5x / $57,000,000) of total Purchase Order value.",
            ),
            "SP3-04": _format_tabular_clause_cell(
                "APPROVED",
                "compromise_tier_1",
                "4.1 All TRA-500 unit prices are exclusive of new Section 232/301 tariffs on specialty Inconel/maraging steel actuator forgings exceeding 5%, shared 50/50 capped at 2.0% ($760,000) of PO value.",
            ),
            "SP5-03": _format_tabular_clause_cell(
                "APPROVED",
                "hold_firm",
                "3.2 Seller shall maintain NIST SP 800-171 controls for all TRA-500 digital test benches and report any cybersecurity incident affecting Covered Defense Information within seventy-two (72) hours of discovery.",
            ),
        },
        status_by_clause={
            "GP1-12": ("APPROVED", "hold_firm"),
            "GP1-19": ("CONFLICT", "compromise_tier_1"),
            "SP3-04": ("APPROVED", "compromise_tier_1"),
            "SP5-03": ("APPROVED", "hold_firm"),
        },
    )

    lg7740_defaults = _extract_fixture_clause_summary(
        "Meridian_Working_Review_LG7740.docx",
        fallback_cells={
            "GP1-12": _format_tabular_clause_cell(
                "APPROVED",
                "hold_firm",
                "12.2 Seller warrants all TLG-800 Titanium Main Landing Gear Assemblies against structural fatigue, forging inclusions, and defects in workmanship for thirty-six (36) months from initial aircraft delivery.",
            ),
            "GP1-19": _format_tabular_clause_cell(
                "APPROVED",
                "compromise_tier_1",
                "19.1 Seller's liability for general direct damages on TLG-800 landing gear assemblies shall not exceed two hundred percent (200% / $104,000,000) of total Purchase Order value, with uncapped AD recall and IP indemnity.",
            ),
            "SP3-04": _format_tabular_clause_cell(
                "APPROVED",
                "compromise_tier_1",
                "4.1 All TLG-800 unit prices are DDP Cymbal Everett/Charleston facility with verified new Section 232/301 titanium forging tariffs above 5% shared 50/50 capped at 2.0% ($1,040,000).",
            ),
            "SP5-03": _format_tabular_clause_cell(
                "APPROVED",
                "hold_firm",
                "3.2 Seller shall maintain NIST SP 800-171 controls for all CNC 5-axis machining cells and report any cybersecurity incident affecting TLG-800 technical data within seventy-two (72) hours of discovery.",
            ),
        },
        status_by_clause={
            "GP1-12": ("APPROVED", "hold_firm"),
            "GP1-19": ("APPROVED", "compromise_tier_1"),
            "SP3-04": ("APPROVED", "compromise_tier_1"),
            "SP5-03": ("APPROVED", "hold_firm"),
        },
    )

    portfolio_deals = [
        {
            "deal_id": "BA-2026-AV-8921",
            "supplier": state.vendor_name if state.deal_id == "BA-2026-AV-8921" else "Apex AeroSystems",
            "program": (
                state.boeing_program
                if state.deal_id == "BA-2026-AV-8921"
                else "Cymbal C900 / C700-MAX Flight Control Display Units (FCC-900)"
            ),
            "value_usd": float(state.contract_value_usd) if state.deal_id == "BA-2026-AV-8921" else 45_000_000.0,
            "clauses": (
                {cid: _from_active_state(cid, av8921_defaults[cid]) for cid in ("GP1-12", "GP1-19", "SP3-04", "SP5-03")}
                if state.deal_id == "BA-2026-AV-8921"
                else av8921_defaults
            ),
            "cap_multiple": 2.0,
            "gate_status": state.status if state.deal_id == "BA-2026-AV-8921" else "READY_FOR_DISPATCH",
        },
        {
            "deal_id": "BA-2026-TR-5510",
            "supplier": state.vendor_name if state.deal_id == "BA-2026-TR-5510" else "Vanguard Thrust Systems Corp.",
            "program": (
                state.boeing_program
                if state.deal_id == "BA-2026-TR-5510"
                else "777X / 787 Thrust Reverser Actuators (TRA-500)"
            ),
            "value_usd": float(state.contract_value_usd) if state.deal_id == "BA-2026-TR-5510" else 38_000_000.0,
            "clauses": (
                {cid: _from_active_state(cid, tr5510_defaults[cid]) for cid in ("GP1-12", "GP1-19", "SP3-04", "SP5-03")}
                if state.deal_id == "BA-2026-TR-5510"
                else tr5510_defaults
            ),
            "cap_multiple": 1.5,
            "gate_status": state.status if state.deal_id == "BA-2026-TR-5510" else "CONFLICT_DETECTED",
        },
        {
            "deal_id": "BA-2026-LG-7740",
            "supplier": state.vendor_name if state.deal_id == "BA-2026-LG-7740" else "Meridian Landing Gear Corp.",
            "program": (
                state.boeing_program
                if state.deal_id == "BA-2026-LG-7740"
                else "787-10 Titanium Main Landing Gear Assemblies (TLG-800)"
            ),
            "value_usd": float(state.contract_value_usd) if state.deal_id == "BA-2026-LG-7740" else 52_000_000.0,
            "clauses": (
                {cid: _from_active_state(cid, lg7740_defaults[cid]) for cid in ("GP1-12", "GP1-19", "SP3-04", "SP5-03")}
                if state.deal_id == "BA-2026-LG-7740"
                else lg7740_defaults
            ),
            "cap_multiple": 2.0,
            "gate_status": state.status if state.deal_id == "BA-2026-LG-7740" else "READY_FOR_DISPATCH",
        },
    ]

    for row_idx, d_row in enumerate(portfolio_deals, start=2):
        ws.append(
            [
                d_row["deal_id"],
                d_row["supplier"],
                d_row["program"],
                d_row["value_usd"],
                d_row["clauses"]["GP1-12"],
                d_row["clauses"]["GP1-19"],
                d_row["clauses"]["SP3-04"],
                d_row["clauses"]["SP5-03"],
                d_row["cap_multiple"],
                d_row["gate_status"],
            ]
        )
        ws.row_dimensions[row_idx].height = 54
        for col_i in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col_i)
            cell.border = CELL_BORDER
            if col_i == 1:
                cell.font = BOLD_FONT
                cell.alignment = Alignment(vertical="top", wrap_text=True)
            elif col_i == 4:
                cell.font = INPUT_BLUE_FONT
                cell.number_format = CURRENCY_FORMAT
                cell.alignment = Alignment(horizontal="right", vertical="top")
            elif col_i == 9:
                cell.font = INPUT_BLUE_FONT
                cell.number_format = MULTIPLE_FORMAT
                cell.alignment = Alignment(horizontal="right", vertical="top")
            elif col_i == 10:
                cell.font = BOLD_FONT
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                cell.fill = (
                    STATUS_FILLS["APPROVED"]
                    if d_row["gate_status"] == "READY_FOR_DISPATCH"
                    else STATUS_FILLS["CONFLICT"]
                )
            else:
                cell.font = REGULAR_FONT
                cell.alignment = Alignment(vertical="top", wrap_text=True)

    # Row 5: Bottom summary row using live =SUM(...) and =COUNTIF(...) formulas
    summary_row = 5
    ws.append(
        [
            "PORTFOLIO SUMMARY",
            "=COUNTA(A2:A4)",
            "3 Tier-1 Aerospace Programs (FCC-900 / TRA-500 / TLG-800)",
            "=SUM(D2:D4)",
            "=COUNTIF(E2:E4,\"*APPROVED*\")",
            "=COUNTIF(F2:F4,\"*APPROVED*\")",
            "=COUNTIF(G2:G4,\"*APPROVED*\")",
            "=COUNTIF(H2:H4,\"*APPROVED*\")",
            "=AVERAGE(I2:I4)",
            "=COUNTIF(J2:J4,\"READY_FOR_DISPATCH\")",
        ]
    )
    ws.row_dimensions[summary_row].height = 28
    for col_i in range(1, len(headers) + 1):
        cell = ws.cell(row=summary_row, column=col_i)
        cell.fill = SUMMARY_FILL
        cell.border = TOTAL_BORDER
        if col_i in (1, 3):
            cell.font = BOLD_FONT
            cell.alignment = Alignment(vertical="center", wrap_text=True)
        elif col_i == 4:
            cell.font = FORMULA_BLACK_FONT
            cell.number_format = CURRENCY_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="center")
        elif col_i == 9:
            cell.font = FORMULA_BLACK_FONT
            cell.number_format = MULTIPLE_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="center")
        else:
            cell.font = FORMULA_BLACK_FONT
            cell.number_format = INTEGER_FORMAT
            cell.alignment = Alignment(horizontal="right", vertical="center")

    _set_column_widths(ws, [20, 26, 36, 18, 48, 48, 48, 48, 18, 22])


def generate_deviation_matrix_xlsx(
    state: DealWorkbenchState, output_path: str | Path
) -> Path:
    """
    Build and save the 5-worksheet SharePoint Deviation Matrix .xlsx workbook:
      - Sheet 1: 1_Executive_Summary
      - Sheet 2: 2_Clause_Deviation_Matrix
      - Sheet 3: 3_Cross_Clause_Conflict_Log
      - Sheet 4: 4_BigQuery_Precedent_Benchmarks
      - Sheet 5: 5_Portfolio_Tabular_Review
    """
    target_path = Path(output_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws_exec = wb.active
    assert ws_exec is not None
    _build_executive_summary_sheet(ws_exec, state)

    ws_matrix = wb.create_sheet(title="2_Clause_Deviation_Matrix")
    _build_clause_deviation_matrix_sheet(ws_matrix, state)

    ws_conflict = wb.create_sheet(title="3_Cross_Clause_Conflict_Log")
    _build_conflict_and_audit_log_sheet(ws_conflict, state)

    ws_prec = wb.create_sheet(title="4_BigQuery_Precedent_Benchmarks")
    _build_bigquery_precedents_sheet(ws_prec, state)

    ws_tab = wb.create_sheet(title="5_Portfolio_Tabular_Review")
    _build_portfolio_tabular_review_sheet(ws_tab, state)

    wb.save(str(target_path))
    return target_path
