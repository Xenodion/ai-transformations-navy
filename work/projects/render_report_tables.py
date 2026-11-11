"""Render editable report-table data to slide-ready PNG and SVG figures.

Run with --extract once to transfer Markdown tables from the report to the
JSON source and replace them with image links. Later edits belong in the JSON;
run again without --extract to regenerate the figures.
"""
import argparse
import json
import re
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "deliverables/report/full_strategy_report_draft.md"
DATA = ROOT / "work/projects/report_tables.json"
ASSETS = ROOT / "deliverables/report/assets"

def parse_report():
    lines = REPORT.read_text(encoding="utf-8").splitlines()
    out, tables, heading = [], [], "Report"
    i = 0
    while i < len(lines):
        if lines[i].startswith("#"):
            heading = re.sub(r"^#+\s*", "", lines[i])
        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[ :|\-]+\|$", lines[i + 1]):
            block = [lines[i]]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                block.append(lines[i]); i += 1
            rows = [[re.sub(r"\*\*", "", cell.strip()) for cell in line.strip().strip("|").split("|")] for line in block]
            number = len(tables) + 1
            name = f"report_table_{number:02d}"
            tables.append({"id": name, "title": heading, "rows": rows})
            out.append(f"![{heading} — table {number}](assets/{name}.png)")
            continue
        out.append(lines[i]); i += 1
    return tables, "\n".join(out) + "\n"

def render(item):
    rows = item["rows"]
    ncols = len(rows[0])
    if any(len(row) != ncols for row in rows):
        raise ValueError(f"Uneven columns: {item['id']}")
    # Narrative columns need more room than years and monetary figures.
    weights = []
    for col in range(ncols):
        content = [len(r[col]) for r in rows]
        weights.append(min(3.6, max(1.0, (max(content) / 28) ** .65)))
    widths = [x / sum(weights) for x in weights]
    figwidth = 16
    wrapped = []
    for row in rows:
        wrapped.append(["\n".join(textwrap.wrap(value, max(7, int(widths[j] * 110)), break_long_words=True, break_on_hyphens=False)) or " " for j, value in enumerate(row)])
    heights = [max(cell.count("\n") + 1 for cell in row) * .30 + .23 for row in wrapped]
    figheight = max(2.3, sum(heights) + 1.0)
    fig, ax = plt.subplots(figsize=(figwidth, figheight))
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

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--extract", action="store_true")
    args = parser.parse_args()
    if args.extract:
        if DATA.exists():
            raise SystemExit("JSON already exists; remove it deliberately before re-extraction.")
        tables, new_report = parse_report()
        if not tables: raise SystemExit("No tables found")
    else:
        tables = json.loads(DATA.read_text(encoding="utf-8")); new_report = None
    ASSETS.mkdir(parents=True, exist_ok=True)
    for item in tables: render(item)
    if args.extract:
        DATA.write_text(json.dumps(tables, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        REPORT.write_text(new_report, encoding="utf-8")
    print(f"Rendered {len(tables)} tables in PNG and SVG")

if __name__ == "__main__": main()
