"""Generate three slide-ready portfolio charts and refresh portfolio_charts.ipynb.

All project figures are read from long_list.md, so a correction there reaches the
charts on the next run. The 5-year value is a derived calculation on the assumptions
named below, not a business case: step 18 owns the NPV.
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import nbformat
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.ticker import NullLocator
from nbclient import NotebookClient

HERE = Path(__file__).resolve().parent
LONG_LIST = HERE / "long_list.md"
ASSETS = HERE / "assets"
NOTEBOOK = HERE / "portfolio_charts.ipynb"

# Official TotalEnergies colours.
BLEU, ORANGE, CYAN = "#00509E", "#F37021", "#00A3E0"
GREY, INK, MUTED, RULE = "#A3ABB5", "#1B2430", "#5B6673", "#E6E9ED"
COLORS = {"H1": BLEU, "H2": ORANGE, "H3": CYAN, "Enabler": GREY}
LEGEND = {"H1": "H1 Core", "H2": "H2 Adjacent", "H3": "H3 Transformational", "Enabler": "Enabler"}
TEXT_ON = {"H1": "white", "H2": INK, "H3": INK, "Enabler": INK}

RAMP_MONTHS = 24  # Assumption: linear ramp from first value to full scale.
WINDOW_MONTHS = 60
ILLUSTRATIVE_HURDLE = 0.12  # Worked example in the course; step 18 sets the real hurdle.
AREA_PER_M = 150  # Bubble area in points^2 per $M of 3-year cost.

# long_list.md section 5 counts P10 as H2 although most of its value is the H1 yield lever.
HORIZON_OVERRIDE = {"P10": "H2"}
NAMES = {
    "P01": "Refining PdM", "P02": "Upstream Surveillance", "P03": "Wells Construction", "P04": "Renewables Fleet",
    "P05": "Copilot Value", "P06": "Procurement Analytics", "P07": "Safety Vision", "P08": "Retail Retention",
    "P09": "LNG Voyages", "P10": "Cracker Yield", "P11": "Virtual Power",
    "P12": "e-SAF Catalysts", "P13": "Store Losses & Pricing", "E01": "Value Register",
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

LABEL_SIDE = {
    "P01": "bottom",
    "P02": "top",
    "P03": "right",
    "P04": "top",
    "P05": "left",
    "P06": "top",
    "P07": "right",
    "P08": "left",
    "P09": "right",
    "P10": "right",
    "P11": "top",
    "P12": "bottom",
    "P13": "bottom",
    "E01": "left",
}

mpl.rcParams.update({
    "font.family": ["Segoe UI", "Arial", "DejaVu Sans"],
    "font.size": 12,
    "text.color": INK,
    "text.parse_math": False,  # "$" must stay literal in labels.
    "svg.fonttype": "none",  # Text stays editable once pasted into slides.
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})


def _table_rows(text: str) -> dict[str, list[str]]:
    """Map each project ID to its cells in a markdown table excerpt."""
    rows = re.findall(r"^\| ([PE]\d\d) \|(.*)\|$", text, re.MULTILINE)
    return {pid: [cell.strip() for cell in cells.split("|")] for pid, cells in rows}


def load_projects() -> pd.DataFrame:
    """Read horizon, value, timing and cost per project from long_list.md."""
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
        records.append({
            "id": pid,
            "name": NAMES[pid],
            "branch": BRANCHES[pid],
            "horizon": HORIZON_OVERRIDE.get(pid, horizon.group()),
            "value_mid": sum(map(float, value.groups())) / 2 if value else float("nan"),
            "months": sum(map(float, first_value.groups())) / 2,
            "cost": float(costs[pid][3]),
        })
    return pd.DataFrame(records)


def five_year_value(value_mid: float, months: float, rate: float = 0.0) -> float:
    """Return cumulative gross value in $M over the window, on a linear ramp."""
    return sum(
        value_mid / 12 * min(1.0, max(0.0, (m - months) / RAMP_MONTHS)) / (1 + rate) ** (m / 12)
        for m in range(1, WINDOW_MONTHS + 1)
    )


def _five_year(df: pd.DataFrame, rate: float = 0.0) -> pd.Series:
    return df.apply(lambda r: five_year_value(r.value_mid, r.months, rate), axis=1)


def _shares(values: pd.Series, horizons: pd.Series) -> dict[str, float]:
    """Return the percentage of the total held by each horizon, skipping empty ones."""
    totals = values.groupby(horizons).sum()
    totals = totals[totals > 0]
    return (100 * totals / totals.sum()).to_dict()


def _p03_as_h2(df: pd.DataFrame) -> pd.Series:
    return df.horizon.where(df.id != "P03", "H2")


def sensitivity(df: pd.DataFrame) -> pd.DataFrame:
    """Show how the H1 and H2 value shares react to window, discounting and P03's tag."""
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


def _note(fig: Figure, text: str) -> None:
    fig.text(0.02, 0.02, text, fontsize=9.5, color=MUTED, va="bottom")


def _legend(fig: Figure, handles: list[Line2D]) -> None:
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.015, 0.985),
               ncol=len(handles), frameon=False, fontsize=11.5, handletextpad=0.3,
               columnspacing=1.8)


def _swatch(label: str, color: str, size: float = 11) -> Line2D:
    return Line2D([], [], marker="o", ls="", color=color, markersize=size, label=label)


def bubble_chart(df: pd.DataFrame) -> Figure:
    """Plot value at scale against time to first value on one pair of axes."""
    fig, ax = plt.subplots(figsize=(13.33, 7.5))
    ticks = [2, 5, 10, 20, 50, 100, 200]
    ax.set_yscale("log")
    ax.set_ylim(1.6, 180)
    ax.set_xlim(0, 42)
    ax.hlines(ticks, 0, 42, color=RULE, lw=1, zorder=0)

    for row in df.itertuples():
        y = row.value_mid
        area = row.cost * AREA_PER_M
        ax.scatter(row.months, y, s=area, color=COLORS[row.horizon], edgecolor="white",
                   linewidth=2, zorder=3)
        gap = area**0.5 / 2 + 5
        side = LABEL_SIDE.get(row.id, "right")
        offset = {"right": (gap, 0), "left": (-gap, 0), "top": (0, gap), "bottom": (0, -gap)}[side]
        ha = {"right": "left", "left": "right", "top": "center", "bottom": "center"}[side]
        va = "bottom" if side == "top" else ("top" if side == "bottom" else "center")
        branch_tag = f" [{BRANCH_SHORT.get(row.branch, '')}]"
        ax.annotate(f"{row.id} {row.name}{branch_tag}", (row.months, y), xytext=offset,
                    textcoords="offset points", ha=ha, va=va, fontsize=11.5)

    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_yticks(ticks, [f"${t}M" for t in ticks])
    ax.set_xticks([0, 6, 12, 18, 24, 30, 36])
    ax.tick_params(length=0, labelsize=12)
    ax.spines[:].set_visible(False)
    ax.set_xlabel("Months to first value, midpoint", labelpad=10)
    ax.set_ylabel("Gross value at full scale, $M per year, log scale", labelpad=10)

    size_keys = [_swatch(f"${c}M 3-year cost", GREY, (c * AREA_PER_M) ** 0.5) for c in (2, 5)]
    _legend(fig, [_swatch(LEGEND[h], COLORS[h]) for h in COLORS] + size_keys)
    _note(fig, "Midpoints of wide ranges. All 14 candidate projects monetized (including safety, options and enablers). "
               "Overlaps not removed. Source: work/projects/long_list.md.")
    fig.subplots_adjust(left=0.085, right=0.98, top=0.9, bottom=0.14)
    return fig


def allocation_chart(df: pd.DataFrame) -> Figure:
    """Compare the course reference mix with cost and 5-year value by horizon."""
    five = _five_year(df).fillna(0)
    rows = [
        ("Course reference\n70-20-10 heuristic", {"H1": 70.0, "H2": 20.0, "H3": 10.0}),
        (f"Candidate pool\n3-year cost, ${df.cost.sum():.1f}M", _shares(df.cost, df.horizon)),
        (f"5-year gross value\nas tagged, ${five.sum():.0f}M", _shares(five, df.horizon)),
        (f"5-year gross value\nif P03 is H2, ${five.sum():.0f}M", _shares(five, _p03_as_h2(df))),
    ]
    fig, ax = plt.subplots(figsize=(13.33, 6))
    for y, (_, shares) in enumerate(rows):
        left = 0.0
        for horizon in COLORS:
            width = shares.get(horizon, 0.0)
            if not width:
                continue
            ax.barh(y, width, left=left, height=0.56, color=COLORS[horizon],
                    edgecolor="white", linewidth=2)
            label = f"{horizon} {width:.1f}%" if width >= 8 else f"{width:.1f}%"
            ax.text(left + width / 2, y, label, ha="center", va="center", fontsize=12,
                    color=TEXT_ON[horizon])
            left += width

    ax.set_xlim(0, 100)
    ax.invert_yaxis()
    ax.set_yticks(range(len(rows)), [label for label, _ in rows], fontsize=12, color=INK)
    ax.set_xticks([])
    ax.tick_params(length=0)
    ax.spines[:].set_visible(False)
    _legend(fig, [_swatch(LEGEND[h], COLORS[h]) for h in COLORS])
    _note(fig, f"All 14 candidate projects monetized (including safety, options and enablers).\n"
               f"Derived: midpoints, linear {RAMP_MONTHS}-month ramp after first value "
               "(assumption), undiscounted, overlaps not removed. Reference is a course heuristic.")
    fig.subplots_adjust(left=0.17, right=0.98, top=0.9, bottom=0.14)
    return fig


def branch_chart(df: pd.DataFrame) -> Figure:
    """Show 3-year candidate cost per branch, the one measure all 13 projects have."""
    pivot = (df.pivot_table(index="branch", columns="horizon", values="cost", aggfunc="sum")
             .reindex(BRANCH_ORDER).fillna(0))
    counts = df.branch.value_counts()
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False, kind="stable").index]

    fig, ax = plt.subplots(figsize=(13.33, 6))
    for y, (branch, row) in enumerate(pivot.iterrows()):
        left = 0.0
        for horizon in COLORS:
            if row[horizon]:
                ax.barh(y, row[horizon], left=left, height=0.56, color=COLORS[horizon],
                        edgecolor="white", linewidth=2)
                left += row[horizon]
        n = int(counts.get(branch, 0))
        label = f"${left:.1f}M, {n} project{'s' if n > 1 else ''}" if n else "No candidate"
        ax.text(left + 0.1, y, label, va="center", fontsize=12, color=INK if n else MUTED)

    ax.set_xlim(0, pivot.sum(axis=1).max() * 1.22)
    ax.invert_yaxis()
    ax.set_yticks(range(len(pivot)), pivot.index, fontsize=12.5, color=INK)
    ax.set_xticks([])
    ax.tick_params(length=0)
    ax.spines[:].set_visible(False)
    _legend(fig, [_swatch(LEGEND[h], COLORS[h]) for h in COLORS])
    _note(fig, "3-year base cost of the candidate long list. Group functions: Digital, procurement, "
               "HSE, value register. Source: work/projects/long_list.md.")
    fig.subplots_adjust(left=0.19, right=0.98, top=0.9, bottom=0.11)
    return fig


CHARTS = {
    "simple_portfolio_bubble": bubble_chart,
    "simple_capital_value_mix": allocation_chart,
    "simple_branch_distribution": branch_chart,
}


def build_notebook() -> None:
    """Rewrite portfolio_charts.ipynb from this module and execute it in place."""
    md, code = nbformat.v4.new_markdown_cell, nbformat.v4.new_code_cell
    nb = nbformat.v4.new_notebook(cells=[
        md("# Candidate AI projects: portfolio charts\n\n"
           "Generated by `generate_simple_charts.py` from `long_list.md`. "
           "All values are calculations on assumed inputs (a long list, not a portfolio)."),
        code("import generate_simple_charts as charts\n\ndf = charts.load_projects()\n"
             "df"),
        md("## 1. Value at scale against time to first value"),
        code("charts.bubble_chart(df);"),
        md("## 2. Capital reference, candidate cost and 5-year value\n\n"
           "H3 is unpriced in the long list, so it cannot appear in a value bar."),
        code("charts.allocation_chart(df);"),
        md("## 3. Value share sensitivity\n\n"
           "Which choice actually moves H1's share: the window, discounting, or P03's tag."),
        code("charts.sensitivity(df)"),
        md("## 4. Candidate cost by branch"),
        code("charts.branch_chart(df);"),
    ])
    NotebookClient(nb, timeout=120, kernel_name="python3",
                   resources={"metadata": {"path": str(HERE)}}).execute()
    nbformat.write(nb, str(NOTEBOOK))


def _check(df: pd.DataFrame) -> None:
    """Fail if the parse or the ramp arithmetic drifts from long_list.md."""
    assert df.horizon.value_counts().to_dict() == {"H1": 9, "H2": 2, "H3": 2, "Enabler": 1}
    assert df.value_mid.notna().sum() == 14, "All 14 candidate projects are now monetized"
    assert abs(five_year_value(12, 0) - 48.5) < 1e-9  # 12.5 ramp months + 36 full months.
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
