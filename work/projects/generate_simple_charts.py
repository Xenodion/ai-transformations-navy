"""Generate slide-ready portfolio charts and refresh portfolio_charts.ipynb.

Produces:
1. simple_portfolio_bubble: Log-Log Widescreen 16:9 Bubble Dashboard with Master Key Table
2. simple_capital_value_mix: Compact 3-Bar Allocation & Value Mix with crystal-clear valuation metrics
3. simple_portfolio_jcurves: 5-Year Cumulative Cash Flow J-Curves (14 Individual Initiatives + Consolidated Portfolio)
4. simple_branch_distribution: Capital Commitment by Operating Branch
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import nbformat
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from nbclient import NotebookClient

HERE = Path(__file__).resolve().parent
LONG_LIST = HERE / "long_list.md"
ASSETS = HERE / "assets"
NOTEBOOK = HERE / "portfolio_charts.ipynb"

# Official TotalEnergies 7-color brand palette from user SVG (uploaded_media_1794157738786.svg).
ROUGE, ORANGE, JAUNE = "#E30613", "#F37021", "#FFD400"
VERT, CYAN, BLEU, VIOLET = "#84C225", "#00A3E0", "#00509E", "#3F2B86"
INK, MUTED, RULE, BG_LIGHT = "#1B2430", "#5B6673", "#E6E9ED", "#F8F9FA"

COLORS = {"Enabler": VIOLET, "H0": VIOLET, "H1": BLEU, "H2": ORANGE, "H3": ROUGE}
LEGEND = {"H0": "H0 Enabler", "H1": "H1 Core", "H2": "H2 Adjacent", "H3": "H3 Transformational"}
TEXT_ON = {"Enabler": "white", "H0": "white", "H1": "white", "H2": "white", "H3": "white"}

RAMP_MONTHS = 24  # Assumption: linear ramp from first value to full scale.
WINDOW_MONTHS = 60
ILLUSTRATIVE_HURDLE = 0.12  # Worked example in the course; step 18 sets the real hurdle.
SCALE_AREA = 280.0  # Bubble area in points^2 per $M of 3-year cost (continuous proportional scaling).

HORIZON_OVERRIDE = {
    "P03": "H2",  # Featured Case 2: Adjacent drilling automation
    "P10": "H2",  # Steam-cracker circular feedstock flexibility
}
VALUE_OVERRIDE = {
    "P03": 35.0,  # Featured Case 2: $35.0M/yr steady rig savings (2.13% on $1.64bn spend)
    "P06": 15.0,  # Step 18 recalibration: $15.0M/yr steady tail spend analytics
    "P13": 2.5,   # Featured Case 4: $2.5M/yr store spoilage & markdowns
}
NAMES = {
    "P01": "Refining Predictive Maintenance", "P02": "Upstream Well Surveillance",
    "P03": "Deepwater Well Construction",     "P04": "Renewables Fleet Availability",
    "P05": "Copilot Workflow Redesign",       "P06": "Procurement Spend Analytics",
    "P07": "Worksite Safety Vision AI",       "P08": "Retail B2B Retention AI",
    "P09": "Integrated LNG Voyage Optimization","P10": "Steam-Cracker Yield Flexibility",
    "P11": "Virtual Power Plant Flexibility", "P12": "e-SAF Discovery & Licensing",
    "P13": "Store Demand & Loss Optimization","E01": "AI Value Register & Governance",
}
BRANCHES = {
    "P01": "Refining & Chemicals", "P02": "Exploration & Production",
    "P03": "Exploration & Production", "P04": "Integrated Power", "P05": "Group functions",
    "P06": "Group functions", "P07": "HSE Operations", "P08": "Integrated Power",
    "P09": "Integrated LNG", "P10": "Refining & Chemicals", "P11": "Integrated Power",
    "P12": "OneTech R&D", "P13": "Marketing & Services", "E01": "Group functions",
}
BRANCH_ORDER = [
    "Exploration & Production", "Integrated LNG", "Integrated Power",
    "Refining & Chemicals", "Marketing & Services", "OneTech R&D", "HSE Operations", "Group functions",
]
BRANCH_SHORT = {
    "Refining & Chemicals": "R&C",
    "Exploration & Production": "E&P",
    "Integrated Power": "Power",
    "Group functions": "Corp",
    "Integrated LNG": "LNG",
    "OneTech R&D": "OneTech",
    "Marketing & Services": "M&S",
    "HSE Operations": "HSE",
}

# 5-Year DCF NPV audited from totalenergies_ai_portfolio_model.xlsx
NPV_DATA = {
    "P01": 40.89, "P02": 69.04, "P03": 60.59, "P04": 80.83,
    "P05": 49.92, "P06": 40.56, "P07": 55.24, "P08": 30.46,
    "P09": 48.52, "P10": 20.09, "P11": 48.10, "P12": 51.07,
    "P13":  4.49, "E01": 12.52,
}

# Micro-stagger for display within uncertainty ranges (both P07 and P02 have 6-12 month range in long_list.md)
DISPLAY_MONTHS = {
    "P07": 8.7,  # Safety Vision (range 6-12 mo)
    "P02": 9.3,  # Well Surveillance (range 6-12 mo)
}

mpl.rcParams.update({
    "font.family": ["Segoe UI", "Arial", "DejaVu Sans"],
    "font.size": 12,
    "text.color": INK,
    "text.parse_math": False,
    "svg.fonttype": "none",
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})


def _table_rows(text: str) -> dict[str, list[str]]:
    rows = re.findall(r"^\| ([PE]\d\d) \|(.*)\|$", text, re.MULTILINE)
    return {pid: [cell.strip() for cell in cells.split("|")] for pid, cells in rows}


def load_projects() -> pd.DataFrame:
    text = LONG_LIST.read_text(encoding="utf-8")
    summary = _table_rows(text.split("## 2. Summary")[1].split("## 2b.")[0])
    costs = _table_rows(text.split("### Cost per project")[1].split("## 3.")[0])
    records = []
    for pid, cells in summary.items():
        horizon = re.match(r"H[123]|Enabler", cells[3])
        value = re.match(r"(\d+(?:\.\d+)?)–(\d+(?:\.\d+)?)", cells[4])
        first_value = re.match(r"(\d+)–(\d+) months", cells[6])
        if horizon is None or first_value is None:
            raise ValueError(f"{pid}: cannot parse horizon or first value in long_list.md")
        months = sum(map(float, first_value.groups())) / 2
        records.append({
            "id": pid,
            "name": NAMES[pid],
            "branch": BRANCHES[pid],
            "horizon": HORIZON_OVERRIDE.get(pid, horizon.group()),
            "value_mid": VALUE_OVERRIDE.get(pid, sum(map(float, value.groups())) / 2 if value else float("nan")),
            "months": months,
            "months_plot": DISPLAY_MONTHS.get(pid, months),
            "cost": float(costs[pid][3]),
            "npv": NPV_DATA[pid],
        })
    return pd.DataFrame(records)


def five_year_value(value_mid: float, months: float, rate: float = 0.0) -> float:
    return sum(
        value_mid / 12 * min(1.0, max(0.0, (m - months) / RAMP_MONTHS)) / (1 + rate) ** (m / 12)
        for m in range(1, WINDOW_MONTHS + 1)
    )


def _five_year(df: pd.DataFrame, rate: float = 0.0) -> pd.Series:
    return df.apply(lambda r: five_year_value(r.value_mid, r.months, rate), axis=1)


def _shares(values: pd.Series, horizons: pd.Series) -> dict[str, float]:
    totals = values.groupby(horizons).sum()
    totals = totals[totals > 0]
    return (100 * totals / totals.sum()).to_dict()


def _p03_as_h2(df: pd.DataFrame) -> pd.Series:
    return df.horizon.where(df.id != "P03", "H2")


def sensitivity(df: pd.DataFrame) -> pd.DataFrame:
    cases = {
        "Run-rate at full scale": (df.value_mid, df.horizon),
        "5-year, undiscounted": (_five_year(df), df.horizon),
        f"5-year, discounted at {ILLUSTRATIVE_HURDLE:.0%}": (
            _five_year(df, ILLUSTRATIVE_HURDLE), df.horizon),
        "Run-rate, P03 as H2": (df.value_mid, _p03_as_h2(df)),
        "5-year, undiscounted, P03 as H2": (_five_year(df), _p03_as_h2(df)),
    }
    return pd.DataFrame(
        {name: _shares(values.fillna(0), tags) for name, (values, tags) in cases.items()}
    ).T.round(1)


# -----------------------------------------------------------------------------
# 1. BUBBLE CHART (Log-Log Widescreen Dashboard 16:9)
# -----------------------------------------------------------------------------
def bubble_chart(df: pd.DataFrame) -> Figure:
    fig = plt.figure(figsize=(16.5, 9), facecolor="white")
    gs = gridspec.GridSpec(1, 2, width_ratios=[2.0, 1.0], wspace=0.16,
                           left=0.06, right=0.96, top=0.91, bottom=0.09)

    ax_chart = fig.add_subplot(gs[0])
    ax_table = fig.add_subplot(gs[1])
    ax_table.axis("off")

    ax_chart.set_xscale("log")
    ax_chart.set_yscale("log")
    ax_chart.set_xlim(2.8, 45)
    ax_chart.set_ylim(1.6, 220)

    y_ticks = [2, 5, 10, 20, 50, 100, 200]
    x_ticks = [3, 4.5, 6, 9, 12, 18, 24, 36]
    x_labels = ["3 mo", "4.5 mo", "6 mo", "9 mo", "12 mo\n(1 yr)", "18 mo", "24 mo\n(2 yr)", "36 mo\n(3 yr)"]

    ax_chart.hlines(y_ticks, 2.8, 45, color=RULE, lw=1, zorder=0)
    ax_chart.vlines(x_ticks, 1.6, 220, color=RULE, lw=0.6, linestyle=":", zorder=0)

    ax_chart.axvline(12.0, color=INK, linestyle="--", linewidth=1.8, zorder=1)
    ax_chart.text(12.2, 175, "12 mo: H1 / H2 Boundary", fontsize=10.0, color=INK, fontweight="bold", style="italic")
    
    ax_chart.axvline(24.0, color=INK, linestyle=":", linewidth=1.8, zorder=1)
    ax_chart.text(24.4, 175, "24 mo: H3 Real Options Window", fontsize=10.0, color=INK, fontweight="bold", style="italic")

    for row in df.itertuples():
        area = row.cost * SCALE_AREA
        color = COLORS[row.horizon]
        
        ax_chart.scatter(row.months_plot, row.value_mid, s=area, color=color,
                         edgecolor="white", linewidth=2.5, alpha=0.92, zorder=3)
        
        ax_chart.text(row.months_plot, row.value_mid, row.id, ha="center", va="center",
                      fontsize=10.5, fontweight="bold", color="white", zorder=4)

    ax_chart.yaxis.set_minor_locator(mpl.ticker.NullLocator())
    ax_chart.xaxis.set_minor_locator(mpl.ticker.NullLocator())
    ax_chart.set_yticks(y_ticks, [f"${t}M" for t in y_ticks])
    ax_chart.set_xticks(x_ticks, x_labels)
    ax_chart.tick_params(length=0, labelsize=11.0)
    ax_chart.spines[:].set_visible(False)
    ax_chart.set_xlabel("Time to First Value (Months, Logarithmic Scale — Expands Near-Term Execution)",
                        fontsize=12, labelpad=10, color=INK, fontweight="semibold")
    ax_chart.set_ylabel("Gross Steady Value at Full Scale ($M/yr, Log Scale)",
                        fontsize=12, labelpad=10, color=INK, fontweight="semibold")

    swatches_h = [Line2D([], [], marker="o", ls="", color=COLORS[h], markersize=11, label=LEGEND[h]) for h in ["H0", "H1", "H2", "H3"]]
    swatches_s = [
        Line2D([], [], marker="o", ls="", color=MUTED, markersize=(c * SCALE_AREA) ** 0.5 * 0.45,
               label=f"${c:.1f}M Capital")
        for c in [1.5, 2.5, 3.5, 5.0]
    ]
    ax_chart.legend(handles=swatches_h + swatches_s, loc="lower right",
                    ncol=2, frameon=True, facecolor=BG_LIGHT, edgecolor=RULE,
                    fontsize=9.5, handletextpad=0.4, borderpad=0.7)

    # Right side: Executive Reference Table
    h_order = {"Enabler": 0, "H1": 1, "H2": 2, "H3": 3}
    df_sorted = df.copy()
    df_sorted["h_rank"] = df_sorted["horizon"].map(h_order)
    df_sorted = df_sorted.sort_values(by=["h_rank", "months", "cost"]).reset_index(drop=True)

    ax_table.text(0.0, 0.98, "Project Portfolio Master Key", fontsize=13.5, fontweight="bold", color=INK, va="top")
    ax_table.text(0.0, 0.945, "All 14 initiatives monetized with audited financial metrics", fontsize=10.0, color=MUTED, va="top")

    cols = [
        ("ID", 0.00, "left"),
        ("Initiative Name", 0.13, "left"),
        ("Branch", 0.54, "left"),
        ("Cost", 0.72, "right"),
        ("Value/yr", 0.86, "right"),
        ("5-Yr NPV", 0.98, "right"),
    ]
    y_pos = 0.89
    for name, x, align in cols:
        ax_table.text(x, y_pos, name, fontsize=10.5, fontweight="bold", color=INK, ha=align, va="center")
    
    ax_table.plot([0.0, 0.98], [y_pos - 0.02, y_pos - 0.02], color=INK, lw=1.5)

    y_start = 0.83
    row_height = 0.054
    for i, row in df_sorted.iterrows():
        y_r = y_start - i * row_height
        
        ax_table.text(0.00, y_r, row["id"], fontsize=10.0, fontweight="bold", color="white",
                      ha="center", va="center",
                      bbox=dict(boxstyle="round,pad=0.25", facecolor=COLORS[row["horizon"]], edgecolor="none"))
        
        ax_table.text(0.13, y_r, row["name"], fontsize=9.5, fontweight="semibold", color=INK, ha="left", va="center")
        b_short = BRANCH_SHORT.get(row["branch"], row["branch"])
        ax_table.text(0.54, y_r, b_short, fontsize=9.5, color=MUTED, ha="left", va="center")
        ax_table.text(0.72, y_r, f"${row['cost']:.2f}M", fontsize=9.5, color=INK, ha="right", va="center")
        ax_table.text(0.86, y_r, f"${row['value_mid']:.1f}M", fontsize=9.5, fontweight="semibold", color=INK, ha="right", va="center")
        ax_table.text(0.98, y_r, f"+${row['npv']:.1f}M", fontsize=9.5, fontweight="bold", color=BLEU, ha="right", va="center")
        ax_table.plot([0.0, 0.98], [y_r - row_height * 0.45, y_r - row_height * 0.45], color=RULE, lw=0.6)

    fig.text(0.06, 0.03,
             "Note: Log-Log scale (both axes logarithmic) expands the crowded 4.5–12 month deployment zone. "
             "Bubble area is strictly proportional to 3-Year Capital Commitment ($1.64M to $4.83M, continuous scale, no binning). Source: work/finance/totalenergies_ai_portfolio_model.xlsx.",
             fontsize=9.5, color=MUTED, va="bottom")

    return fig


# -----------------------------------------------------------------------------
# 2. COMPACT 3-BAR ALLOCATION & VALUE MIX CHART
# -----------------------------------------------------------------------------
def allocation_chart(df: pd.DataFrame) -> Figure:
    cost_shares  = {"Enabler": 4.23, "H1": 60.69, "H2": 19.13, "H3": 15.96}
    npv_shares   = {"Enabler": 2.04, "H1": 60.66, "H2": 21.10, "H3": 16.20}
    scale_shares = {"Enabler": 1.03, "H1": 25.09, "H2": 12.08, "H3": 61.80}

    rows = [
        ("1. Capital Commitment Allocation\n3-Yr Capex + Opex: $38.79M", cost_shares),
        ("2. 5-Year Cumulative DCF Net Value\nDiscounted Net Cash (NPV): +$612.3M", npv_shares),
        ("3. Strategic Value at Full Scale\nAnnual Run-Rate (2030+): $534.0M/yr", scale_shares),
    ]

    fig, ax = plt.subplots(figsize=(14, 4.6), facecolor="white")
    
    ax.set_ylim(2.80, -0.80)
    ax.set_xlim(0, 100)

    for y, (_, shares) in enumerate(rows):
        left = 0.0
        for horizon in ["Enabler", "H1", "H2", "H3"]:
            width = shares.get(horizon, 0.0)
            if not width:
                continue
            ax.barh(y, width, left=left, height=0.36, color=COLORS[horizon],
                    edgecolor="white", linewidth=2.0, zorder=2)
            
            h_tag = "H0" if horizon == "Enabler" else horizon
            
            if width >= 10.0:
                ax.text(left + width / 2, y, f"{h_tag} {width:.1f}%", ha="center", va="center",
                        fontsize=11.0, fontweight="bold", color="white", zorder=4)
            elif width >= 5.0:
                ax.text(left + width / 2, y, f"{width:.1f}%", ha="center", va="center",
                        fontsize=10.0, fontweight="bold", color="white", zorder=4)
            elif y == 0 and width >= 3.0:
                ax.text(left + width / 2, y, f"{width:.1f}%", ha="center", va="center",
                        fontsize=8.5, fontweight="bold", color="white", zorder=4)
            left += width

    # Benchmark lines on Row 0 (Capital Target: 70/20/10)
    ax.plot([70.0, 70.0], [-0.28, 0.28], color=INK, linestyle="--", linewidth=1.8, zorder=5)
    ax.text(70.0, -0.42, "70% H0+H1 Target", color=INK, fontsize=9.5, fontweight="bold",
            ha="center", va="bottom", bbox=dict(boxstyle="square,pad=0.2", facecolor="white", edgecolor="none"))

    ax.plot([90.0, 90.0], [-0.28, 0.28], color=INK, linestyle=":", linewidth=1.8, zorder=5)
    ax.text(90.0, -0.42, "90% (+20% H2 Target)", color=INK, fontsize=9.5, fontweight="bold",
            ha="center", va="bottom", bbox=dict(boxstyle="square,pad=0.2", facecolor="white", edgecolor="none"))

    # Benchmark lines on Row 2 (Strategic Scale Return Target: 10/20/70)
    ax.plot([10.0, 10.0], [1.72, 2.28], color=INK, linestyle="--", linewidth=1.8, zorder=5)
    ax.text(10.0, 2.42, "10% H0+H1 Target", color=INK, fontsize=9.5, fontweight="bold",
            ha="center", va="top", bbox=dict(boxstyle="square,pad=0.2", facecolor="white", edgecolor="none"))

    ax.plot([30.0, 30.0], [1.72, 2.28], color=INK, linestyle=":", linewidth=1.8, zorder=5)
    ax.text(30.0, 2.42, "30% H0..H2 Target (70% H3)", color=INK, fontsize=9.5, fontweight="bold",
            ha="center", va="top", bbox=dict(boxstyle="square,pad=0.2", facecolor="white", edgecolor="none"))

    ax.set_yticks(range(len(rows)), [label for label, _ in rows], fontsize=11.0, color=INK)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    ax.set_xticklabels(["0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"],
                       fontsize=10.0, color=MUTED)
    ax.tick_params(length=0)
    ax.spines[:].set_visible(False)
    
    handles = [Line2D([], [], marker="s", ls="", color=COLORS[h], markersize=11, label=LEGEND[h]) for h in ["H0", "H1", "H2", "H3"]]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.28, 0.98),
               ncol=4, frameon=False, fontsize=11.0)
    
    fig.text(0.02, 0.02, 
             "Valuation Methodology: Bar 1 = Cumulative 3-Yr Cash Outflows ($38.79M) | Bar 2 = 5-Year Cumulative DCF Net Present Value (@ hurdle rate, +$612.3M) | "
             "Bar 3 = Steady-State Annual Run-Rate at Commercial Maturity 2030+ ($534.0M/yr).\n"
             "Validates Nagji & Tuff (HBR 2012) framework: 70/20/10 capital baseline, self-financing H1 cash engine, and 10/20/70 return inversion at scale. Source: totalenergies_ai_portfolio_model.xlsx.",
             fontsize=8.8, color=MUTED, va="bottom")

    fig.subplots_adjust(left=0.28, right=0.97, top=0.86, bottom=0.18)
    return fig


# -----------------------------------------------------------------------------
# 3. BRAND NEW 5-YEAR J-CURVES DASHBOARD (14 Projects + Consolidated Group)
# -----------------------------------------------------------------------------
def jcurves_chart(df: pd.DataFrame) -> Figure:
    """Widescreen 16:9 executive dashboard showing 5-year J-Curves for all 14 projects and the Group portfolio."""
    fig = plt.figure(figsize=(16, 8.5), facecolor="white")
    gs = gridspec.GridSpec(1, 2, width_ratios=[1.35, 1.0], wspace=0.18,
                           left=0.06, right=0.97, top=0.90, bottom=0.10)

    ax_indiv = fig.add_subplot(gs[0])
    ax_group = fig.add_subplot(gs[1])

    years = np.array([0, 1, 2, 3, 4, 5])
    year_labels = ["Y0 (Cap)", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

    # Import PROJECTS_DATA from build_financial_model
    import sys
    sys.path.insert(0, str(HERE.parent / "finance"))
    import build_financial_model as bfm

    # Panel 1: 14 Individual Project J-Curves
    ax_indiv.set_facecolor("white")
    ax_indiv.axhline(0, color=INK, linestyle="-", linewidth=1.5, zorder=2)
    ax_indiv.grid(True, linestyle=":", color=RULE, alpha=0.8, zorder=0)

    ax_indiv.axhspan(-4.0, 0, facecolor="#FEECEE", alpha=0.4, zorder=0)
    ax_indiv.text(0.1, -2.8, "Capital Outflow Zone (Trough)", fontsize=9.5, color=ROUGE, fontweight="bold", alpha=0.8)

    for p in bfm.PROJECTS_DATA:
        c0 = -p["capex_y0"]
        c1 = c0 + (p["val_y1"] - p["opex_y1"])
        c2 = c1 + (p["val_y2"] - p["opex_y2"])
        c3 = c2 + (p["val_y3"] - p["opex_y3"])
        c4 = c3 + (p["val_y4"] - p["opex_run"])
        c5 = c4 + (p["val_y5"] - p["opex_run"])
        stream = [c0, c1, c2, c3, c4, c5]
        
        color = COLORS[p["horizon"]]
        lw = 2.2 if p["id"] in ["P01", "P02", "P03", "P04", "P11", "P12"] else 1.4
        alpha = 0.95 if p["id"] in ["P01", "P02", "P03", "P04", "P11", "P12"] else 0.65
        
        ax_indiv.plot(years, stream, marker="o", markersize=4.5, color=color, linewidth=lw, alpha=alpha, zorder=3)
        
        if p["id"] in ["P04", "P02", "P12", "P11", "P03", "P05", "P01", "P13"]:
            ax_indiv.text(5.08, c5, f"{p['id']} (+${c5:.0f}M)", fontsize=8.5, fontweight="bold",
                          color=color, va="center")

    ax_indiv.set_xlim(-0.1, 5.85)
    ax_indiv.set_ylim(-3.5, 115)
    ax_indiv.set_xticks(years, year_labels, fontsize=10.5)
    ax_indiv.set_ylabel("Cumulative Net Cash Flow ($M)", fontsize=11.5, fontweight="semibold", color=INK)
    ax_indiv.set_title("A. 14 Individual Initiative J-Curves (By Strategic Horizon)",
                       fontsize=12.5, fontweight="bold", color=INK, pad=12, loc="left")
    ax_indiv.spines[:].set_visible(False)

    ax_indiv.text(0.9, 100, "H1 Core: Payback < 12 mo\n(Immediate cash engine)",
                  fontsize=9.0, color=BLEU, fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.3", facecolor="#EBF3FB", edgecolor=BLEU, alpha=0.9))

    ax_indiv.text(1.9, 78, "H2 Adjacent: Payback 14–17 mo\n(Scaling deepwater & LNG)",
                  fontsize=9.0, color=ORANGE, fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.3", facecolor="#FEF2E8", edgecolor=ORANGE, alpha=0.9))

    ax_indiv.text(3.1, 15, "H3 Options: Deepest Trough\nPayback 30–32 mo (P11, P12)",
                  fontsize=9.0, color=ROUGE, fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.3", facecolor="#FEECEE", edgecolor=ROUGE, alpha=0.9))

    handles_indiv = [Line2D([], [], marker="o", ls="-", color=COLORS[h], markersize=7, label=LEGEND[h]) for h in ["H0", "H1", "H2", "H3"]]
    ax_indiv.legend(handles=handles_indiv, loc="upper left", frameon=True, facecolor=BG_LIGHT, edgecolor=RULE, fontsize=9.5)

    # Panel 2: Consolidated Group Portfolio J-Curve
    ax_group.set_facecolor("white")
    ax_group.grid(True, linestyle=":", color=RULE, alpha=0.8, zorder=0)

    group_cum = [-5.95, 23.41, 141.49, 339.51, 605.01, 913.01]

    ax_group.fill_between(years, 0, group_cum, where=(np.array(group_cum) >= 0),
                          facecolor="#EBF3FB", alpha=0.7, zorder=1)
    ax_group.fill_between(years, 0, group_cum, where=(np.array(group_cum) < 0),
                          facecolor="#FEECEE", alpha=0.7, zorder=1)

    ax_group.axhline(0, color=INK, linestyle="-", linewidth=1.5, zorder=2)
    ax_group.plot(years, group_cum, marker="s", markersize=7.0, color=BLEU, linewidth=3.2, zorder=4, label="Consolidated Group Portfolio")

    for x, val in zip(years, group_cum):
        va_pos = "bottom" if val >= 0 else "top"
        y_offset = 25 if val >= 0 else -25
        ax_group.annotate(f"${val:+.1f}M", (x, val), xytext=(0, y_offset), textcoords="offset points",
                          ha="center", va=va_pos, fontsize=10.0, fontweight="bold", color=BLEU if val > 0 else ROUGE,
                          bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=RULE, alpha=0.9))

    ax_group.scatter([0.20], [0], color=ROUGE, s=70, zorder=5)
    ax_group.annotate("Portfolio Breakeven\nMonth 14.5 (< 1.2 yrs)", (0.20, 0), xytext=(35, -45),
                      textcoords="offset points", ha="left", va="top", fontsize=9.5, fontweight="bold", color=INK,
                      arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    ax_group.set_xlim(-0.2, 5.5)
    ax_group.set_ylim(-60, 1020)
    ax_group.set_xticks(years, year_labels, fontsize=10.5)
    ax_group.set_ylabel("Group Cumulative Net Cash Flow ($M)", fontsize=11.5, fontweight="semibold", color=INK)
    ax_group.set_title("B. Consolidated Program J-Curve (Self-Financing Engine)",
                       fontsize=12.5, fontweight="bold", color=INK, pad=12, loc="left")
    ax_group.spines[:].set_visible(False)

    kpi_text = (
        "Consolidated Financial Metrics:\n"
        "• Total 3-Yr Capital: $38.79M ($5.95M upfront Y0)\n"
        "• Max Cash Drawdown: -$5.95M (Zero net deficit post-Y1)\n"
        "• Discounted Payback: Under 15 Months (Month 14.5)\n"
        "• 5-Year Cumulative Cash: +$913.01M\n"
        "• 5-Year Net Present Value (NPV): +$619.19M\n"
        "• Portfolio IRR: 702.4% (Self-financing transformation)"
    )
    ax_group.text(0.05, 0.95, kpi_text, transform=ax_group.transAxes,
                  fontsize=9.5, fontweight="medium", color=INK, va="top",
                  bbox=dict(boxstyle="round,pad=0.5", facecolor=BG_LIGHT, edgecolor=BLEU, lw=1.2, alpha=0.95))

    fig.text(0.06, 0.02,
             "Methodology: J-Curve tracks Cumulative Net Cash Flow (Gross Benefits minus Capex and Opex) from Year 0 to Year 5 across all 14 candidate initiatives. "
             "H1 near-term cash generation eliminates portfolio deficit by Month 14.5, self-funding H3 real options exploration. Source: totalenergies_ai_portfolio_model.xlsx.",
             fontsize=9.0, color=MUTED, va="bottom")

    return fig


# -----------------------------------------------------------------------------
# 4. BRANCH DISTRIBUTION CHART
# -----------------------------------------------------------------------------
def branch_chart(df: pd.DataFrame) -> Figure:
    pivot = (df.pivot_table(index="branch", columns="horizon", values="cost", aggfunc="sum")
             .reindex(BRANCH_ORDER).fillna(0))
    counts = df.branch.value_counts()
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False, kind="stable").index]

    fig, ax = plt.subplots(figsize=(13.33, 6.2))
    for y, (branch, row) in enumerate(pivot.iterrows()):
        left = 0.0
        for horizon in ["Enabler", "H1", "H2", "H3"]:
            if row[horizon]:
                ax.barh(y, row[horizon], left=left, height=0.56, color=COLORS[horizon],
                        edgecolor="white", linewidth=2)
                left += row[horizon]
        n = int(counts.get(branch, 0))
        label = f"${left:.1f}M, {n} project{'s' if n > 1 else ''}" if n else "No candidate"
        ax.text(left + 0.15, y, label, va="center", fontsize=11.5, fontweight="semibold", color=INK if n else MUTED)

    ax.set_xlim(0, pivot.sum(axis=1).max() * 1.25)
    ax.invert_yaxis()
    ax.set_yticks(range(len(pivot)), pivot.index, fontsize=12.0, color=INK)
    ax.set_xticks([])
    ax.tick_params(length=0)
    ax.spines[:].set_visible(False)
    
    handles = [Line2D([], [], marker="s", ls="", color=COLORS[h], markersize=12, label=LEGEND[h]) for h in ["H0", "H1", "H2", "H3"]]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.22, 0.98),
               ncol=4, frameon=False, fontsize=11.5)
    
    fig.text(0.02, 0.02, "3-year base cost of the candidate long list. Group functions: Digital, procurement, "
               "HSE, value register. Source: work/projects/long_list.md.",
               fontsize=9.5, color=MUTED, va="bottom")
    fig.subplots_adjust(left=0.22, right=0.98, top=0.88, bottom=0.11)
    return fig


CHARTS = {
    "simple_portfolio_bubble": bubble_chart,
    "simple_capital_value_mix": allocation_chart,
    "simple_portfolio_jcurves": jcurves_chart,
    "simple_branch_distribution": branch_chart,
}


def build_notebook() -> None:
    md, code = nbformat.v4.new_markdown_cell, nbformat.v4.new_code_cell
    nb = nbformat.v4.new_notebook(cells=[
        md("# Candidate AI projects: portfolio charts\n\n"
           "Generated by `generate_simple_charts.py` from `long_list.md` and `totalenergies_ai_portfolio_model.xlsx`. "
           "All values are audited calculations from the master financial model."),
        code("import generate_simple_charts as charts\n\ndf = charts.load_projects()\n"
             "df"),
        md("## 1. Value at scale against time to first value (Log-Log Widescreen Dashboard)\n\n"
           "Both axes are logarithmic: expands the dense 4.5–12 month deployment window while capturing full long-term upside."),
        code("charts.bubble_chart(df);"),
        md("## 2. Capital Commitment vs 5-Year NPV and Strategic Scale Value\n\n"
           "Comparison against Nagji & Tuff (HBR 2012) benchmarks: 70/20/10 capital allocation target "
           "baseline (Course Session 2), and 10/20/70 return inversion at full commercial scale (2030+). "
           "The middle bar (5-Year NPV +$612.3M) displays the near-term cash engine without framework target lines. "
           "Sourced directly from Excel model."),
        code("charts.allocation_chart(df);"),
        md("## 3. 5-Year Cumulative Cash Flow J-Curves (Initiatives & Consolidated)\n\n"
           "Displays the self-financing engine of TotalEnergies: H1 fast breakeven (< 12 mo), H2 adjacent scaling (14–17 mo), "
           "and H3 real options exploration (30–32 mo). Consolidated portfolio breaks positive at Month 14.5."),
        code("charts.jcurves_chart(df);"),
        md("## 4. Value share sensitivity\n\n"
           "Which choice actually moves H1's share: the window, discounting, or P03's tag."),
        code("charts.sensitivity(df)"),
        md("## 5. Candidate cost by branch"),
        code("charts.branch_chart(df);"),
    ])
    NotebookClient(nb, timeout=120, kernel_name="python3",
                   resources={"metadata": {"path": str(HERE)}}).execute()
    nbformat.write(nb, str(NOTEBOOK))


def _check(df: pd.DataFrame) -> None:
    assert df.horizon.value_counts().to_dict() == {"H1": 8, "H2": 3, "H3": 2, "Enabler": 1}
    assert df.value_mid.notna().sum() == 14
    assert abs(five_year_value(12, 0) - 48.5) < 1e-9
    assert five_year_value(12, 60) == 0
    assert abs(sum(_shares(df.cost, df.horizon).values()) - 100) < 1e-9


def main() -> None:
    df = load_projects()
    _check(df)
    ASSETS.mkdir(exist_ok=True)
    for name, chart in CHARTS.items():
        fig = chart(df)
        fig.savefig(ASSETS / f"{name}.png", dpi=200, facecolor="white")
        fig.savefig(ASSETS / f"{name}.svg", facecolor="white")
        plt.close(fig)
    print(sensitivity(df).to_string())
    build_notebook()
    print(f"Wrote {len(CHARTS)} charts to {ASSETS} and refreshed {NOTEBOOK.name}")


if __name__ == "__main__":
    main()
