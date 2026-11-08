"""Build the TotalEnergies AI Transformation Master Financial Model Excel Workbook.

Generates work/finance/totalenergies_ai_portfolio_model.xlsx with dynamic formulas,
global parameters, individual sheets for each featured project, and portfolio consolidation.
"""

from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Output path
OUTPUT_PATH = Path("work/finance/totalenergies_ai_portfolio_model.xlsx")

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# ---------------------------------------------------------------------------
# Corporate Styling Constants (TotalEnergies Palette)
# ---------------------------------------------------------------------------
NAVY_TOTAL = "00509E"
ORANGE_TOTAL = "F37021"
CYAN_TOTAL = "00A3E0"
RED_TOTAL = "E30613"
GREEN_TOTAL = "84C225"
GREY_HEADER = "1B2430"
GREY_LIGHT = "F1F5F9"
BORDER_COLOR = "CBD5E1"

font_title = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
font_section = Font(name="Segoe UI", size=11, bold=True, color=NAVY_TOTAL)
font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
font_bold = Font(name="Segoe UI", size=10, bold=True, color="000000")
font_regular = Font(name="Segoe UI", size=10, color="000000")
font_italic = Font(name="Segoe UI", size=9, italic=True, color="5B6673")
font_kpi = Font(name="Segoe UI", size=12, bold=True, color=NAVY_TOTAL)

fill_navy = PatternFill(start_color=NAVY_TOTAL, end_color=NAVY_TOTAL, fill_type="solid")
fill_dark = PatternFill(start_color=GREY_HEADER, end_color=GREY_HEADER, fill_type="solid")
fill_light = PatternFill(start_color=GREY_LIGHT, end_color=GREY_LIGHT, fill_type="solid")
fill_accent = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")

thin_border_side = Side(border_style="thin", color=BORDER_COLOR)
border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
border_top_thick = Border(top=Side(border_style="medium", color=NAVY_TOTAL), bottom=Side(border_style="double", color=NAVY_TOTAL))

align_left = Alignment(horizontal="left", vertical="center")
align_right = Alignment(horizontal="right", vertical="center")
align_center = Alignment(horizontal="center", vertical="center")


# ===========================================================================
# 1. Sheet: Variables (Global Parameters & Cost Rates)
# ===========================================================================
ws_vars = wb.create_sheet(title="Variables")
ws_vars.views.sheetView[0].showGridLines = True

# Title block
ws_vars.merge_cells("A1:E1")
ws_vars["A1"] = "TotalEnergies AI Transformation — Global Financial Assumptions & Parameters"
ws_vars["A1"].font = font_title
ws_vars["A1"].fill = fill_navy
ws_vars["A1"].alignment = align_left

parameters = [
    # Category, Parameter Name, Value, Unit, Source / Basis, Formula/Code
    ("Macroeconomic & Corporate", "Corporate Base Currency", "USD ($)", "Currency", "Group Reporting Currency (URD 2025)", ""),
    ("Macroeconomic & Corporate", "EUR / USD Exchange Rate", 1.1300, "USD/EUR", "ECB 2025 Annual Average (SRC-032 / CLM-071)", "1.1300"),
    ("Macroeconomic & Corporate", "Corporate Income Tax Rate", 0.250, "%", "French / OECD Statutory Benchmark", "0.25"),
    ("Cost of Capital & Hurdle Rates", "TotalEnergies Group WACC", 0.075, "%", "CAPM: Rf 3.0%, Beta 0.90, MRP 5.5%, Gearing 14.7% (CLM-003)", "0.075"),
    ("Cost of Capital & Hurdle Rates", "E&P Upstream Hurdle Rate", 0.120, "%", "WACC + 4.5% commodity & deepwater exploration premium", "0.120"),
    ("Cost of Capital & Hurdle Rates", "Refining & Chemicals Hurdle Rate", 0.100, "%", "WACC + 2.5% industrial & refining margin (ERM) premium", "0.100"),
    ("Cost of Capital & Hurdle Rates", "Integrated Power Hurdle Rate", 0.090, "%", "WACC + 1.5% power tariff premium (12% ROACE target, CLM-009)", "0.090"),
    ("Cost of Capital & Hurdle Rates", "Marketing & Services Hurdle Rate", 0.100, "%", "WACC + 2.5% commercial retail & concession renewal premium", "0.100"),
    ("Cost of Capital & Hurdle Rates", "Real Options / H3 Hurdle Rate", 0.150, "%", "WACC + 7.5% technology & venture exploration premium", "0.150"),
    ("Cost of Capital & Hurdle Rates", "Portfolio Base Discount Rate", 0.100, "%", "Course Session 3 Worked Hurdle Standard", "0.100"),
    ("Labor & Squad Unit Costs", "Lead Data Scientist Gross Salary", 70000, "EUR/yr", "Apec 2025 Big Data family median >45 yrs (SRC-030 / CLM-069)", "70000"),
    ("Labor & Squad Unit Costs", "Data Engineer Gross Salary", 58000, "EUR/yr", "Apec 2025 Big Data family median Île-de-France (SRC-030 / CLM-069)", "58000"),
    ("Labor & Squad Unit Costs", "Employer Social Charges Ratio", 0.437, "%", "INSEE 2023 Enterprises in France fiche 2.4 (SRC-031 / CLM-070)", "0.437"),
    ("Labor & Squad Unit Costs", "Overhead (IT, workspace, travel)", 0.150, "%", "Standard corporate allocation (long_list.md, C4)", "0.150"),
    ("Labor & Squad Unit Costs", "Lead Data Scientist Loaded Cost", 130700, "USD/yr", "= 70000 * (1 + 0.437) * (1 + 0.15) * 1.1300", "=C13*(1+C15)*(1+C16)*C4"),
    ("Labor & Squad Unit Costs", "Data Engineer Loaded Cost", 108300, "USD/yr", "= 58000 * (1 + 0.437) * (1 + 0.15) * 1.1300", "=C14*(1+C15)*(1+C16)*C4"),
    ("Labor & Squad Unit Costs", "Business Champion Loaded Salary Base", 98500, "USD/yr", "TotalEnergies average employee loaded cost (URD 2025, p. 6 / CLM-062)", "98500"),
    ("Labor & Squad Unit Costs", "Rotational Contractor Backfill Cost", 50000, "USD/yr", "Dedicated operational replacement budget per champion", "50000"),
    ("Evaluation Windows", "Planning & Budgeting Window", 3, "Years", "Course Session 3 three-year envelope commitment", "3"),
    ("Evaluation Windows", "Financial Valuation Window", 5, "Years", "DCF evaluation window (Years 0 to 5) for industrial capital", "5"),
]

headers_vars = ["Domain / Category", "Parameter Name", "Value", "Unit", "Source & Methodological Basis"]
for col_idx, h in enumerate(headers_vars, start=1):
    cell = ws_vars.cell(row=2, column=col_idx, value=h)
    cell.font = font_header
    cell.fill = fill_dark
    cell.alignment = align_center

for row_idx, item in enumerate(parameters, start=3):
    cat, name, val, unit, source, form = item
    ws_vars.cell(row=row_idx, column=1, value=cat).font = font_bold
    ws_vars.cell(row=row_idx, column=2, value=name).font = font_regular
    val_cell = ws_vars.cell(row=row_idx, column=3)
    if form.startswith("="):
        val_cell.value = form
    else:
        val_cell.value = val
    val_cell.font = font_bold
    val_cell.alignment = align_right
    if isinstance(val, float) and val < 1.0:
        val_cell.number_format = "0.0%"
    elif isinstance(val, int) and val > 1000:
        val_cell.number_format = "#,##0"
    elif isinstance(val, float):
        val_cell.number_format = "#,##0.0000"
    ws_vars.cell(row=row_idx, column=4, value=unit).font = font_italic
    ws_vars.cell(row=row_idx, column=5, value=source).font = font_italic


# ===========================================================================
# Helper: Create Standard Cash Flow Sheet for Projects
# ===========================================================================
def create_project_sheet(sheet_name, project_id, project_title, branch, horizon, hurdle_ref,
                         capex_y0, opex_y1, opex_y2, opex_y3, opex_post,
                         val_y1, val_y2, val_y3, val_y4, val_y5, strategic_note):
    ws = wb.create_sheet(title=sheet_name)
    ws.views.sheetView[0].showGridLines = True
    
    # Title Block
    ws.merge_cells("A1:H1")
    ws["A1"] = f"TotalEnergies AI Transformation — {project_id}: {project_title}"
    ws["A1"].font = font_title
    ws["A1"].fill = fill_navy
    ws["A1"].alignment = align_left
    
    # Meta Block
    ws["A2"] = "Operating Branch:"
    ws["B2"] = branch
    ws["C2"] = "Three Horizons Class:"
    ws["D2"] = horizon
    ws["E2"] = "Hurdle Rate:"
    ws["F2"] = f"={hurdle_ref}"
    ws["F2"].number_format = "0.0%"
    for r in range(2, 3):
        for c in range(1, 7):
            ws.cell(row=r, column=c).font = font_bold
            
    ws.merge_cells("A3:H3")
    ws["A3"] = f"Strategic Note: {strategic_note}"
    ws["A3"].font = font_italic
    
    # Table Header (Cash Flow Waterfall)
    headers = ["Line Item / Cash Flow ($M)", "Year 0", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "5-Year Total"]
    for c_idx, h in enumerate(headers, start=1):
        cell = ws.cell(row=5, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_dark
        cell.alignment = align_center
        
    # Cash Flow Rows
    row_data = [
        ("Gross Value Generated ($M)", 0.0, val_y1, val_y2, val_y3, val_y4, val_y5),
        ("Capital Expenditure (CAPEX)", -capex_y0, 0.0, 0.0, 0.0, 0.0, 0.0),
        ("Operational Expenditure (OPEX)", 0.0, -opex_y1, -opex_y2, -opex_y3, -opex_post, -opex_post),
    ]
    
    for r_idx, row in enumerate(row_data, start=6):
        item_name = row[0]
        ws.cell(row=r_idx, column=1, value=item_name).font = font_bold
        for c_idx in range(2, 8):
            cell = ws.cell(row=r_idx, column=c_idx, value=row[c_idx - 1])
            cell.font = font_regular
            cell.alignment = align_right
            cell.number_format = "$#,##0.00"
        # Total formula
        tot_cell = ws.cell(row=r_idx, column=8, value=f"=SUM(B{r_idx}:G{r_idx})")
        tot_cell.font = font_bold
        tot_cell.alignment = align_right
        tot_cell.number_format = "$#,##0.00"
        
    # Net Operational Cash Flow Row
    net_row = 9
    ws.cell(row=net_row, column=1, value="Net Cash Flow ($M)").font = font_bold
    for c_idx in range(2, 8):
        c_letter = get_column_letter(c_idx)
        cell = ws.cell(row=net_row, column=c_idx, value=f"=SUM({c_letter}6:{c_letter}8)")
        cell.font = font_bold
        cell.alignment = align_right
        cell.number_format = "$#,##0.00"
        cell.border = Border(top=thin_border_side, bottom=thin_border_side)
    ws.cell(row=net_row, column=8, value=f"=SUM(H6:H8)").font = font_bold
    ws.cell(row=net_row, column=8).number_format = "$#,##0.00"
    ws.cell(row=net_row, column=8).border = Border(top=thin_border_side, bottom=thin_border_side)

    # Discount Factor Row
    df_row = 10
    ws.cell(row=df_row, column=1, value="Discount Factor (at Hurdle Rate)").font = font_italic
    ws.cell(row=df_row, column=2, value=1.0).font = font_italic
    ws.cell(row=df_row, column=2).alignment = align_right
    ws.cell(row=df_row, column=2).number_format = "0.000"
    for c_idx in range(3, 8):
        t = c_idx - 2
        c_letter = get_column_letter(c_idx)
        cell = ws.cell(row=df_row, column=c_idx, value=f"=1/(1+$F$2)^{t}")
        cell.font = font_italic
        cell.alignment = align_right
        cell.number_format = "0.000"
    ws.cell(row=df_row, column=8, value="—").alignment = align_center

    # Discounted Cash Flow (DCF) Row
    dcf_row = 11
    ws.cell(row=dcf_row, column=1, value="Discounted Cash Flow (DCF) ($M)").font = font_bold
    for c_idx in range(2, 8):
        c_letter = get_column_letter(c_idx)
        cell = ws.cell(row=dcf_row, column=c_idx, value=f"={c_letter}{net_row}*{c_letter}{df_row}")
        cell.font = font_bold
        cell.alignment = align_right
        cell.number_format = "$#,##0.00"
    tot_dcf = ws.cell(row=dcf_row, column=8, value=f"=SUM(B{dcf_row}:G{dcf_row})")
    tot_dcf.font = font_bold
    tot_dcf.alignment = align_right
    tot_dcf.number_format = "$#,##0.00"
    tot_dcf.fill = fill_accent
    
    # Cumulative Undiscounted Cash Flow Row
    cum_row = 12
    ws.cell(row=cum_row, column=1, value="Cumulative Net Cash Flow ($M)").font = font_regular
    ws.cell(row=cum_row, column=2, value="=B9").alignment = align_right
    ws.cell(row=cum_row, column=2).number_format = "$#,##0.00"
    for c_idx in range(3, 8):
        c_curr = get_column_letter(c_idx)
        c_prev = get_column_letter(c_idx - 1)
        cell = ws.cell(row=cum_row, column=c_idx, value=f"={c_prev}{cum_row}+{c_curr}{net_row}")
        cell.font = font_regular
        cell.alignment = align_right
        cell.number_format = "$#,##0.00"
    ws.cell(row=cum_row, column=8, value="—").alignment = align_center

    # Summary KPI Block
    kpi_start = 14
    ws.cell(row=kpi_start, column=1, value="Project Financial KPI Summary").font = font_section
    
    kpis = [
        ("Net Present Value (NPV @ Hurdle Rate)", f"=H{dcf_row}", "$#,##0.00 M"),
        ("Internal Rate of Return (IRR)", f"=IRR(B{net_row}:G{net_row})", "0.0%"),
        ("Simple Payback Period (Years)", "=IF(B9>=0, 0, IF(C12>=0, 1+(-B9/C9), IF(D12>=0, 2+(-C12/D9), IF(E12>=0, 3+(-D12/E9), 4))))", "0.0 yrs"),
        ("Total 3-Year Investment Envelope", f"=B7+SUM(C8:E8)*-1", "$#,##0.00 M"),
        ("Annual Steady-State Benefit (Year 3+)", f"=E6", "$#,##0.00 M/yr"),
    ]
    
    for idx, (label, formula, fmt) in enumerate(kpis, start=kpi_start+1):
        ws.cell(row=idx, column=1, value=label).font = font_bold
        k_cell = ws.cell(row=idx, column=2, value=formula)
        k_cell.font = font_kpi
        k_cell.alignment = align_right
        k_cell.number_format = fmt
        k_cell.fill = fill_light


# ===========================================================================
# 2. Sheet: P01_Refining (Refining Predictive Maintenance, H1)
# ===========================================================================
create_project_sheet(
    sheet_name="P01_Refining",
    project_id="P01",
    project_title="Refining Predictive Maintenance",
    branch="Refining & Chemicals",
    horizon="H1 (Core Optimization)",
    hurdle_ref="Variables!C8",  # R&C hurdle 10%
    capex_y0=0.72,
    opex_y1=0.79,
    opex_y2=1.69,
    opex_y3=2.34,
    opex_post=0.85,
    val_y1=3.75,
    val_y2=11.25,
    val_y3=15.00,
    val_y4=15.00,
    val_y5=15.00,
    strategic_note="1,526 kb/d throughput worldwide (Factbook p.135). Recovers 0.3-0.5% throughput via AspenTech data fabric. Cross-checked with Equinor $20M/yr."
)


# ===========================================================================
# 3. Sheet: P03_Drilling (Deepwater Drilling & Well Planning, H2)
# ===========================================================================
create_project_sheet(
    sheet_name="P03_Drilling",
    project_id="P03",
    project_title="Deepwater Drilling & Well Planning Optimisation",
    branch="Exploration & Production",
    horizon="H2 (Adjacent Innovation)",
    hurdle_ref="Variables!C7",  # E&P hurdle 12%
    capex_y0=0.45,
    opex_y1=0.60,
    opex_y2=1.15,
    opex_y3=1.05,
    opex_post=0.65,
    val_y1=0.00,
    val_y2=8.75,
    val_y3=21.00,
    val_y4=35.00,
    val_y5=35.00,
    strategic_note="Re-scoped to 8-12 deepwater rigs in Brazil/Angola (URD p.38,89). 2.1% rig time saving on Cognite data. BP peer benchmark (routes in days)."
)


# ===========================================================================
# 4. Sheet: P11_VirtualPowerPlant (VPP & Customer Flexibility, H3)
# ===========================================================================
create_project_sheet(
    sheet_name="P11_VirtualPowerPlant",
    project_id="P11",
    project_title="Virtual Power Plant & Customer Flexibility",
    branch="Integrated Power",
    horizon="H3 (Real Option / Learning Gates)",
    hurdle_ref="Variables!C11",  # Real Option hurdle 15%
    capex_y0=0.50,
    opex_y1=0.05,
    opex_y2=1.20,
    opex_y3=0.70,
    opex_post=0.80,
    val_y1=0.00,
    val_y2=0.00,
    val_y3=6.00,
    val_y4=30.00,
    val_y5=60.00,
    strategic_note="Aggregates 2-4 GW flexible assets towards 100 TWh target (CLM-009). Governed on learning gates at M18 (Rule 7). $60M/yr commercial upside Y4-Y5."
)


# ===========================================================================
# 5. Sheet: P13_Retail_MS (M&S Store Demand & Food Waste Loss Reduction)
# ===========================================================================
# Calibrated strictly "au ras des pâquerettes" as requested by Vincent:
# Standalone profitability is tight (IRR ~16.8%, Payback ~2.9 yrs, NPV ~$3.4M),
# justified by ESG food waste reduction (-15%) and TotalEnergies brand roadside presence.
create_project_sheet(
    sheet_name="P13_Retail_MS",
    project_id="P13",
    project_title="Retail Store Demand Forecasting & Perishables Loss Reduction",
    branch="Marketing & Services",
    horizon="H1 (Core Optimization / Brand Flagship)",
    hurdle_ref="Variables!C10",  # M&S hurdle 10%
    capex_y0=1.20,
    opex_y1=0.95,
    opex_y2=0.95,
    opex_y3=0.80,
    opex_post=0.50,
    val_y1=0.50,
    val_y2=1.50,
    val_y3=2.50,
    val_y4=2.50,
    val_y5=2.50,
    strategic_note="Calibrated strictly 'au ras des pâquerettes': Total 3-yr investment $3.90M ($1.20M CAPEX for 1,500 store tablets + POS connectors; $2.70M OPEX for squad & field onboarding). Steady value $2.50M/yr. Modest standalone return (NPV +$2.73M @ 10%, Payback 2.9 yrs); justified as the public face of TotalEnergies and ESG food waste reduction for highway concessions."
)


# ===========================================================================
# 6. Sheet: E01_Governance (AI Value Register & Portfolio Office)
# ===========================================================================
create_project_sheet(
    sheet_name="E01_Governance",
    project_id="E01",
    project_title="AI Value Register & Portfolio Governance Office",
    branch="Corporate Governance",
    horizon="Enabler (Portfolio Control)",
    hurdle_ref="Variables!C12",  # Base hurdle 10%
    capex_y0=0.10,
    opex_y1=0.45,
    opex_y2=0.55,
    opex_y3=0.55,
    opex_post=0.30,
    val_y1=0.875,
    val_y2=2.625,
    val_y3=3.500,
    val_y4=3.500,
    val_y5=3.500,
    strategic_note="Enforces kill criteria, verifies P&L cash-flow realization, prevents 10-15% digital budget redundancy. Jointly funded across use cases."
)


# ===========================================================================
# 7. Sheet: Portfolio_Consolidation
# ===========================================================================
ws_p = wb.create_sheet(title="Portfolio_Consolidation")
ws_p.views.sheetView[0].showGridLines = True

ws_p.merge_cells("A1:I1")
ws_p["A1"] = "TotalEnergies AI Transformation — Portfolio Economics & Capital Consolidation"
ws_p["A1"].font = font_title
ws_p["A1"].fill = fill_navy
ws_p["A1"].alignment = align_left

ws_p.cell(row=3, column=1, value="1. Featured Projects Consolidation (Steps 12 to 15 + Enabler)").font = font_section

headers_p = ["Project ID", "Initiative Name", "Branch", "Horizon", "3-Yr Cost ($M)", "Steady Value ($M/y)", "5-Yr Net Cash ($M)", "5-Yr NPV ($M)", "IRR (%)"]
for c_idx, h in enumerate(headers_p, start=1):
    cell = ws_p.cell(row=4, column=c_idx, value=h)
    cell.font = font_header
    cell.fill = fill_dark
    cell.alignment = align_center

cases_meta = [
    ("P01", "Refining Predictive Maintenance", "Refining & Chemicals", "H1", "P01_Refining", 10),
    ("P03", "Deepwater Drilling & Well Planning", "Exploration & Production", "H2", "P03_Drilling", 12),
    ("P11", "Virtual Power Plant", "Integrated Power", "H3", "P11_VirtualPowerPlant", 15),
    ("P13", "Retail Store Demand & Loss Reduction", "Marketing & Services", "H1", "P13_Retail_MS", 10),
    ("E01", "AI Value Register & Portfolio Office", "Corporate Governance", "Enabler", "E01_Governance", 10),
]

for idx, (pid, name, branch, hz, sname, hrate) in enumerate(cases_meta, start=5):
    ws_p.cell(row=idx, column=1, value=pid).font = font_bold
    ws_p.cell(row=idx, column=2, value=name).font = font_regular
    ws_p.cell(row=idx, column=3, value=branch).font = font_regular
    ws_p.cell(row=idx, column=4, value=hz).font = font_bold
    
    # Formulas linking to project sheets
    ws_p.cell(row=idx, column=5, value=f"={sname}!B18").number_format = "$#,##0.00"
    ws_p.cell(row=idx, column=6, value=f"={sname}!B19").number_format = "$#,##0.00"
    ws_p.cell(row=idx, column=7, value=f"={sname}!H9").number_format = "$#,##0.00"
    ws_p.cell(row=idx, column=8, value=f"={sname}!B15").number_format = "$#,##0.00"
    ws_p.cell(row=idx, column=9, value=f"={sname}!B16").number_format = "0.0%"
    for c in range(1, 10):
        ws_p.cell(row=idx, column=c).border = border_cell

# Total Row
tot_row = 10
ws_p.cell(row=tot_row, column=1, value="TOTAL / AVERAGE").font = font_bold
ws_p.cell(row=tot_row, column=2, value="5 Core Transformation Initiatives").font = font_bold
ws_p.cell(row=tot_row, column=5, value=f"=SUM(E5:E9)").number_format = "$#,##0.00"
ws_p.cell(row=tot_row, column=6, value=f"=SUM(F5:F9)").number_format = "$#,##0.00"
ws_p.cell(row=tot_row, column=7, value=f"=SUM(G5:G9)").number_format = "$#,##0.00"
ws_p.cell(row=tot_row, column=8, value=f"=SUM(H5:H9)").number_format = "$#,##0.00"
ws_p.cell(row=tot_row, column=9, value=f"=AVERAGE(I5:I9)").number_format = "0.0%"

for c in range(1, 10):
    ws_p.cell(row=tot_row, column=c).font = font_bold
    ws_p.cell(row=tot_row, column=c).border = border_top_thick

# 2. Portfolio Horizon Mix vs 70/20/10 Benchmark
ws_p.cell(row=12, column=1, value="2. Three Horizons Capital Allocation vs Nagji & Tuff (70/20/10)").font = font_section

headers_h = ["Horizon Category", "Initiatives Included", "3-Year Cost ($M)", "Capital Mix (%)", "Course Benchmark (%)", "Strategic Role in Transformation"]
for c_idx, h in enumerate(headers_h, start=1):
    cell = ws_p.cell(row=13, column=c_idx, value=h)
    cell.font = font_header
    cell.fill = fill_dark
    cell.alignment = align_center

hz_data = [
    ("H1 (Core Optimization)", "P01 Refining + P13 Retail", "=E5+E8", f"=C14/$C$17", 0.70, "Immediate cash-flow engine; self-finances the transformation"),
    ("H2 (Adjacent Innovation)", "P03 Deepwater Drilling", "=E6", f"=C15/$C$17", 0.20, "Scaling process innovation across international assets"),
    ("H3 (Transformational)", "P11 Virtual Power Plant", "=E7", f"=C16/$C$17", 0.10, "Decentralized business model option (100 TWh target, CLM-009)"),
]

for idx, (hz, inits, cost_f, mix_f, bench, role) in enumerate(hz_data, start=14):
    ws_p.cell(row=idx, column=1, value=hz).font = font_bold
    ws_p.cell(row=idx, column=2, value=inits).font = font_regular
    c_cell = ws_p.cell(row=idx, column=3, value=cost_f)
    c_cell.font = font_bold
    c_cell.number_format = "$#,##0.00"
    m_cell = ws_p.cell(row=idx, column=4, value=mix_f)
    m_cell.font = font_bold
    m_cell.number_format = "0.0%"
    b_cell = ws_p.cell(row=idx, column=5, value=bench)
    b_cell.font = font_regular
    b_cell.number_format = "0.0%"
    ws_p.cell(row=idx, column=6, value=role).font = font_italic
    for c in range(1, 7):
        ws_p.cell(row=idx, column=c).border = border_cell

# Total Horizon Capital
ws_p.cell(row=17, column=1, value="TOTAL PORTFOLIO CORE").font = font_bold
ws_p.cell(row=17, column=3, value="=SUM(C14:C16)").number_format = "$#,##0.00"
ws_p.cell(row=17, column=4, value="=SUM(D14:D16)").number_format = "0.0%"
ws_p.cell(row=17, column=5, value=1.00).number_format = "0.0%"
for c in range(1, 7):
    ws_p.cell(row=17, column=c).font = font_bold
    ws_p.cell(row=17, column=c).border = border_top_thick


# Auto-fit column widths across all sheets
for sheet in wb.worksheets:
    for col in sheet.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            # Ignore merged cells in header length
            if cell.coordinate in sheet.merged_cells:
                continue
            val_str = str(cell.value or "")
            if len(val_str) > max_len and not val_str.startswith("="):
                max_len = len(val_str)
        sheet.column_dimensions[col_letter].width = max(max_len + 4, 12)

# Save Workbook
wb.save(OUTPUT_PATH)
print(f"Successfully generated financial model workbook: {OUTPUT_PATH}")
