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

from render_selected_charts import (D, NAVY, BLUE, TEAL, ORANGE, GREY, RED, PALE, WLABEL, export, finish)

# --- Operating model: today vs proposed -------------------------------------------------
GOOD = '#4E7A12'; TRIO_BG = '#E6F4FB'; LINE_BG = '#F2F5F9'
fig, axes = plt.subplots(1, 2, figsize=(13, 6.8))


def card(ax, x, y, w, h, title, desc=None, face=PALE, tcolor=NAVY, dcolor=GREY, edge='none', size=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.018',
                                facecolor=face, edgecolor=edge, linewidth=1))
    if desc:
        ax.text(x + w / 2, y + h * .62, title, ha='center', va='center', fontsize=size, weight='bold', color=tcolor)
        ax.text(x + w / 2, y + h * .34, desc, ha='center', va='center', fontsize=8.6, color=dcolor, linespacing=1.3)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha='center', va='center', fontsize=size, weight='bold', color=tcolor, linespacing=1.3)


def link(ax, a, b, color=GREY, lw=1, ls=(0, (3, 3)), head=None):
    ax.annotate('', xy=b, xytext=a, arrowprops=dict(arrowstyle=head or '-', color=color, lw=lw, linestyle=ls, shrinkA=0, shrinkB=0))


def panel(ax, tag, heading, result, rcolor):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    ax.text(0, 1.0, tag, fontsize=9, weight='bold', color=GREY, va='bottom')
    ax.text(0, .955, heading, fontsize=13, weight='bold', color=NAVY, va='top')
    ax.text(0, -.035, result, fontsize=9.5, color=rcolor, weight='bold', va='top', linespacing=1.4)


ax = axes[0]
panel(ax, 'TODAY', 'One project, four separate reporting lines',
      'Responsibility is dispersed: progress reviews are spaced out,\niterations are slow and each lead follows only a few projects.', RED)
cells = [(.02, .52, 'Branch project lead', 'leads the project'),
         (.52, .52, 'Branch data engineer', 'reports to branch IT/data,\nnot to the project lead'),
         (.02, .14, 'TDF data scientist', 'sets data-science rules,\nno financial objective'),
         (.52, .14, 'End user', 'gives the need and feedback,\nno decision power')]
for x, y, t, d in cells:
    card(ax, x, y, .44, .25, t, d)
for a, b in [((.46, .645), (.52, .645)), ((.46, .265), (.52, .265)), ((.24, .52), (.24, .39)), ((.74, .52), (.74, .39)), ((.46, .52), (.52, .39))]:
    link(ax, a, b)

ax = axes[1]
panel(ax, 'PROPOSED', 'One dedicated trio per project',
      'Shorter work cycles, more projects per lead, and AI practice\nspreads into the branches. Objectives and gates unchanged.', GOOD)
card(ax, .18, .74, .64, .14, 'Branch project lead', 'usually the branch digital-transformation head', face=BLUE, tcolor='white', dcolor='#D6E4F2')
ax.add_patch(FancyBboxPatch((.02, .30), .96, .34, boxstyle='round,pad=0,rounding_size=0.02', facecolor=TRIO_BG, edgecolor='none'))
ax.text(.5, .595, 'Dedicated trio  ·  large share of working time  ·  daily contact', ha='center', fontsize=9, weight='bold', color=BLUE)
for x, t in [(.05, 'TDF\ndata scientist'), (.365, 'Branch\ndata engineer'), (.68, 'Business\nexpert')]:
    card(ax, x, .35, .27, .18, t, face='white', edge=TEAL)
link(ax, (.5, .64), (.5, .74), color=BLUE, lw=2.2, ls='-', head='-|>')
ax.text(.53, .69, 'day-to-day reporting, project objectives', fontsize=8.5, color=BLUE, va='center')
for x, t in [(.185, 'Digital Factory\nstandards'), (.5, 'Branch IT/data\nline'), (.815, 'Operations\nline')]:
    card(ax, x - .135, .10, .27, .11, t, face=LINE_BG, tcolor=GREY, size=8.6)
    link(ax, (x, .35), (x, .21))
ax.text(.343, .28, 'line reporting:\nstandards, careers', fontsize=8.2, color=GREY, ha='center', va='center', style='italic')

fig.suptitle('Delivery model | from four separate lines to one dedicated trio', x=.03, y=.995, ha='left', fontsize=17, fontweight='bold', color=NAVY)
fig.add_artist(plt.Line2D([.505, .505], [.1, .9], color='#DCE5EB', lw=1))
fig.subplots_adjust(left=.03, right=.98, top=.89, bottom=.13, wspace=.12)
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
# Base case (the plan): rows per project are [benefit, operating cost, capex, cash tax, net cash].
GREEN, TAX = '#84C225', '#F4A6A9'
rows = sum(np.array(c['scenarios']['Base']['rows'], float) for c in D['projects'].values())
benefit, spend, tax = rows[:, 0], rows[:, 1] + rows[:, 2], rows[:, 3]
cum_base = np.cumsum(rows[:, 4])
assert np.allclose(rows[:, 4], D['portfolio']['Base']['cash'])
fig, ax = plt.subplots(figsize=(11.5, 6)); years = np.arange(6); w = .55
ax.bar(years, benefit, w, color=GREEN, label='Benefits (cash gains)')
ax.bar(years, -spend, w, color=RED, label='Investment and run costs')
ax.bar(years, -tax, w, bottom=-spend, color=TAX, label='Cash tax on gains')
for x, b, s, t in zip(years, benefit, spend, tax):
    # ponytail: labels sit inside the bars next to zero, clear of the J-curve line
    if b > 0: ax.text(x, .3, f'+{b:.1f}', ha='center', va='bottom', fontsize=9, weight='bold', color=NAVY)
    ax.text(x, -.3, f'-{s:.1f}', ha='center', va='top', fontsize=9, weight='bold', color='white')
ax.plot(years, cum_base, color=NAVY, marker='o', lw=2.6, zorder=4, label='Cumulative net cash (J-curve)')
ax.axhline(0, color=NAVY, lw=1)
low = int(np.argmin(cum_base))
ax.annotate(f'Trough -${-cum_base[low]:.1f}m\n(end Y{low})', (low, cum_base[low]), xytext=(low + .45, cum_base[low] - 2.3),
            fontsize=9, weight='bold', color=NAVY, bbox=dict(fc='white', ec='none', pad=1), arrowprops=dict(arrowstyle='-', color=NAVY, lw=.8))
k = int(np.argmax(cum_base > 0)); be = k - 1 + -cum_base[k - 1] / (cum_base[k] - cum_base[k - 1])
ax.scatter([be], [0], s=70, color='white', edgecolors=NAVY, linewidths=2, zorder=5)
ax.annotate(f'Break-even\nafter {be:.1f} years', (be, 0), xytext=(be - 1.0, 4.2), fontsize=9, weight='bold', color=NAVY,
            arrowprops=dict(arrowstyle='-', color=NAVY, lw=.8))
top = max(benefit.max(), cum_base.max()) + 4
for x, label in [(0.5, 'Gate 0\n~day 90'), (1.5, 'Gate 1\nmonth 12'), (2.5, 'Gate 2\nmonth 24'), (3.5, 'Review\nmonth 36')]:
    ax.axvline(x, color=GREY, ls=(0, (4, 3)), lw=1)
    ax.text(x + .04, top - .3, label, fontsize=8.5, color=GREY, va='top')
ax.text(0, top - .3, 'Tranche 1\napproved now', ha='center', va='top', fontsize=8.5, color=NAVY, weight='bold')
ax.set_xticks(years, [f'Y{i}' for i in years]); ax.set_ylim(min(cum_base.min(), -(spend + tax).max()) - 4, top)
ax.set_ylabel('USD m (base case)'); ax.set_title('Staged funding | costs first, gains from Y2, gates at each release', loc='left', pad=14)
finish(ax); ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(0, -.08), ncol=4, fontsize=9)
wc = np.cumsum(D['portfolio']['Weighted']['cash'])
fig.text(.07, .015, f'Base case, undiscounted, after tax. Expected value ({WLABEL}): trough -${-wc.min():.1f}m, '
         f'\nbreak-even after {D["portfolio"]["Weighted"]["payback"]:.1f} years. A failed gate stops further avoidable spend.',
         fontsize=8.5, color=GREY)
fig.subplots_adjust(bottom=.2, top=.88)
export(fig, 'v3_funding_gates')
print('V3 charts exported')
