"""V3 report figures: operating model, readiness and funding gates.

Reads spend and expected cash from selected_chart_data.json; readiness scores
come from work/options/readiness_bottleneck.md (team assessment).
Run from the repository root: python work/projects/render_v3_charts.py
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from render_selected_charts import (D, NAVY, BLUE, TEAL, ORANGE, GREY, RED, PALE, export, finish)

# --- Operating model: today vs proposed -------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13, 6.2))


def box(ax, x, y, w, h, text, face, edge=NAVY, color=NAVY, weight='normal', size=9.5, ls='-'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.012,rounding_size=0.02',
                                facecolor=face, edgecolor=edge, linewidth=1.3, linestyle=ls))
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=size, color=color, weight=weight, wrap=True)


def arrow(ax, a, b, color=GREY, ls='-', lw=1.4, both=False):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle='<->' if both else '->', color=color, lw=lw, linestyle=ls))


ax = axes[0]; ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
ax.set_title('Today | one project, four separate lines', loc='left', fontsize=14, weight='bold', color=NAVY)
actors = [
    (.05, .64, 'Branch project lead\nleads the project', PALE),
    (.55, .64, 'Branch data engineer\nreports to branch IT/data,\nnot to the lead', PALE),
    (.05, .26, 'TDF data scientist\nsets data-science rules,\nno financial objective', PALE),
    (.55, .26, 'End user\ngives need and feedback,\nno decision power', PALE),
]
for x, y, t, f in actors:
    box(ax, x, y, .40, .2, t, f)
for a, b in [((.45, .74), (.55, .74)), ((.25, .64), (.25, .46)), ((.75, .64), (.75, .46)), ((.45, .36), (.55, .36)), ((.43, .64), (.57, .46))]:
    arrow(ax, a, b, color=GREY, ls=(0, (3, 3)), lw=1.1, both=True)
ax.text(.0, .08, 'Each actor answers to a different manager and objective.\nProgress reviews are spaced out; feedback loops are slow;\neach lead can follow only a few projects.', fontsize=9.5, color=RED)

ax = axes[1]; ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
ax.set_title('Proposed | one dedicated trio per project', loc='left', fontsize=14, weight='bold', color=NAVY)
box(ax, .15, .78, .70, .13, 'Branch project lead\n(usually the branch digital-transformation head)', BLUE, color='white', weight='bold', size=9)
ax.add_patch(FancyBboxPatch((.05, .30), .90, .36, boxstyle='round,pad=0.012,rounding_size=0.03', facecolor='#E6F4FB', edgecolor=TEAL, linewidth=1.8))
ax.text(.5, .62, 'Dedicated project trio | large share of working time | daily contact', ha='center', fontsize=9.5, color=NAVY, weight='bold')
for x, t in [(.08, 'TDF\ndata scientist'), (.375, 'Branch\ndata engineer'), (.67, 'Business\nexpert')]:
    box(ax, x, .36, .25, .17, t, 'white', edge=TEAL, weight='bold')
arrow(ax, (.5, .66), (.5, .78), color=BLUE, lw=2.2)
ax.text(.52, .715, 'day-to-day reporting\nand project objectives', fontsize=8.5, color=BLUE)
for x, t in [(.205, 'Digital Factory\nstandards'), (.5, 'Branch IT/data\nline'), (.795, 'Operations\nline')]:
    box(ax, x - .12, .08, .24, .12, t, 'white', edge=GREY, color=GREY, size=8.5, ls='--')
    arrow(ax, (x, .36), (x, .20), color=GREY, ls=(0, (3, 3)), lw=1.1)
ax.text(.0, -.02, 'Dual reporting: project lead for delivery, line managers for standards and careers.\nObjectives and continuation gates unchanged; shorter work cycles; more projects per lead.', fontsize=9.5, color=NAVY)
fig.subplots_adjust(left=.03, right=.98, top=.9, bottom=.07, wspace=.08)
export(fig, 'v3_operating_model')

# --- Readiness: current score and range vs programme target ---------------------------------
dims = ['Business strategy', 'Technology and data', 'AI delivery experience', 'Organisation and culture', 'AI governance']
score = [3, 3, 3.5, 2.5, 2.5]
low = [3, 2.5, 3, 2, 2]
high = [4, 3.5, 4, 3, 3]
target = [4, 3.5, 4, 3.5, 3.5]
fig, ax = plt.subplots(figsize=(10.5, 4.8)); y = np.arange(len(dims))[::-1]
ax.hlines(y, low, high, color='#B5C2CC', lw=8, label='Assessment range')
ax.scatter(score, y, s=150, color=BLUE, zorder=3, label='Current (outside-in)')
ax.scatter(target, y, s=150, facecolors='white', edgecolors=ORANGE, linewidths=2.2, zorder=3, label='Target after Gate 2')
for yi, s in zip(y, score):
    ax.text(s, yi + .28, f'{s:g}', ha='center', fontsize=9, weight='bold', color=NAVY)
ax.set_yticks(y, dims); ax.set_xlim(1, 5); ax.set_ylim(-.5, len(dims) - .2); ax.set_xticks([1, 2, 3, 4, 5], ['1 Exploring', '2 Planning', '3 Implementing', '4 Scaling', '5 Realizing'])
ax.set_title('AI readiness | strong foundations, delivery organisation lags', loc='left', pad=14)
finish(ax); ax.grid(axis='x', alpha=.5); ax.grid(axis='y', visible=False)
ax.legend(frameon=False, loc='lower right', fontsize=8.5)
fig.text(.02, .02, 'Team assessment from public sources and our insider observation; scores are not an internal audit.', fontsize=8.5, color=GREY)
fig.subplots_adjust(left=.24, bottom=.17, top=.86)
export(fig, 'v3_readiness')

# --- Funding tranches and gates ----------------------------------------------------------------
cost = D['portfolio']['annual_cost']
cum_exp = np.cumsum(D['portfolio']['Weighted']['cash'])
fig, ax = plt.subplots(figsize=(11.5, 5.4)); years = np.arange(6)
bars = ax.bar(years, cost, color=[ORANGE] + [BLUE] * 5, width=.55, label='Gross spend released (USD m)')
for b, v in zip(bars, cost):
    ax.text(b.get_x() + b.get_width() / 2, v + .15, f'${v:.2f}m', ha='center', fontsize=9, weight='bold', color=NAVY)
ax.plot(years, cum_exp, color=TEAL, marker='o', lw=2.3, label='Expected cumulative net cash (USD m)')
ax.axhline(0, color=GREY, lw=1)
top = max(cum_exp) + 2.5
ax.text(0, cost[0] + 1.0, 'Tranche 1\napproved now', ha='center', fontsize=8.5, color=ORANGE, weight='bold')
for x, label in [(0.5, 'Gate 0\n~day 90'), (1.5, 'Gate 1\nmonth 12'), (2.5, 'Gate 2\nmonth 24'), (3.5, 'Review\nmonth 36')]:
    ax.axvline(x, color=RED, ls='--', lw=1.2)
    ax.text(x + .04, top - .3, label, fontsize=8.5, color=NAVY, va='top')
ax.set_xticks(years, [f'Y{i}' for i in years]); ax.set_ylim(min(cum_exp) - 1.5, top)
ax.set_ylabel('USD m'); ax.set_title('Staged funding | each release follows a verified gate', loc='left', pad=14)
finish(ax); ax.legend(frameon=False, loc='lower right', fontsize=9)
fig.text(.07, .02, f'Expected trough -${-min(cum_exp):.1f}m at end Y1; expected break-even after {D["portfolio"]["Weighted"]["payback"]:.1f} years. '
         'Gates release funding project by project; a failed gate stops further avoidable spend.', fontsize=8.5, color=GREY)
fig.subplots_adjust(bottom=.15, top=.86)
export(fig, 'v3_funding_gates')
print('V3 charts exported')
