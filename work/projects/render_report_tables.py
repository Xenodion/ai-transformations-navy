"""Render the report's numeric tables to PNG and SVG figures.

Source: work/projects/report_tables.json (numeric tables only; text tables
stay in Markdown in the report). Edit the JSON, then run this script.
Reconcile financial entries with the model whenever figures change.
"""
import json
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "work/projects/report_tables.json"
ASSETS = ROOT / "deliverables/report/assets"


def render(item: dict) -> None:
    rows = item["rows"]
    ncols = len(rows[0])
    if any(len(row) != ncols for row in rows):
        raise ValueError(f"Uneven columns: {item['id']}")
    # Label columns need more room than years and monetary figures.
    weights = [min(3.6, max(1.0, (max(len(r[c]) for r in rows) / 28) ** .65)) for c in range(ncols)]
    widths = [x / sum(weights) for x in weights]
    wrapped = [["\n".join(textwrap.wrap(v, max(7, int(widths[j] * 110)), break_long_words=True, break_on_hyphens=False)) or " "
                for j, v in enumerate(row)] for row in rows]
    heights = [max(cell.count("\n") + 1 for cell in row) * .30 + .23 for row in wrapped]
    fig, ax = plt.subplots(figsize=(16, max(2.3, sum(heights) + 1.0)))
    ax.axis("off")
    ax.set_title(item["title"], loc="left", fontsize=19, fontweight="bold", color="#003b71", pad=16)
    table = ax.table(cellText=wrapped, colWidths=widths, cellLoc="left", bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False); table.set_fontsize(11)
    total = sum(heights)
    for (r, c), cell in table.get_celld().items():
        cell.set_height(heights[r] / total)
        cell.set_edgecolor("#d7e0e8"); cell.set_linewidth(.6)
        cell.set_facecolor("#003b71" if r == 0 else ("#f1f5f8" if r % 2 == 0 else "white"))
        cell.get_text().set_color("white" if r == 0 else "#172b3d")
        cell.get_text().set_fontweight("bold" if r == 0 else "normal")
        cell.get_text().set_parse_math(False)
    fig.subplots_adjust(left=.02, right=.98, top=.88, bottom=.04)
    for ext in ("png", "svg"):
        fig.savefig(ASSETS / f"{item['id']}.{ext}", dpi=180, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    tables = json.loads(DATA.read_text(encoding="utf-8"))
    ASSETS.mkdir(parents=True, exist_ok=True)
    for item in tables:
        render(item)
    print(f"Rendered {len(tables)} tables in PNG and SVG")


if __name__ == "__main__":
    main()
