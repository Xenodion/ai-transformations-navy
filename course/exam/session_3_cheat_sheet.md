# AI Transformations — Session 3 Cheat Sheet: Investment allocation

As of 31 Oct 2026 · Session of 19 Oct

The course logic runs in order: diagnose readiness → pick the operating model → sequence the portfolio → prove it financially → manage the change. This session covers the fourth step; see [session_1_cheat_sheet.md](session_1_cheat_sheet.md) for the exam format.

## 1. Investment allocation: the financial toolkit

**NPV is the headline metric.** It measures value created in today's euros after paying the cost of capital. ROI and simple payback ignore when the money arrives, so a project can show a positive ROI and still destroy value.

### Formulas

Present value of one cash flow at year t, discounted at rate r (cost of capital or required return, not just inflation):

$$
PV = \frac{CF_t}{(1+r)^t}
$$

$$
ROI = \frac{\text{total benefits} - \text{total costs}}{\text{total costs}}
$$

NPV = discounted inflows minus the initial investment I0. I0 is paid at t = 0, so it is **not discounted**:

$$
NPV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - I_0
$$

IRR is the rate that makes NPV = 0. It has no closed form; solve it numerically.

$$
\sum_{t=0}^{n} \frac{CF_t}{(1+IRR)^t} = 0
$$

- **Payback** = years until cumulative cash turns positive. **Discounted payback** = the same on cumulative PV.
- Excel: `=NPV(r, CF1:CFn) + CF0`, because NPV() treats its first value as year 1. `=IRR(CF0:CFn)`.
- Discount factor at 10%: year 1 = 0.909, year 2 = 0.826, year 3 = 0.751, year 4 = 0.683.

### Worked example: EUR 100M project, r = 10% (EUR M)

| Year | Cash flow | Cumulative | DF at 10% | PV | Cumulative PV |
| --- | --- | --- | --- | --- | --- |
| 0 | −100.0 | −100.0 | 1.000 | −100.0 | −100.0 |
| 1 | 30.0 | −70.0 | 0.909 | 27.3 | −72.7 |
| 2 | 40.0 | −30.0 | 0.826 | 33.1 | −39.7 |
| 3 | 50.0 | +20.0 | 0.751 | 37.6 | −2.1 |
| 4 | 40.0 | +60.0 | 0.683 | 27.3 | +25.2 |

| Metric | Result | How |
| --- | --- | --- |
| ROI | 60% | 60 ÷ 100 |
| Payback | 2.6 years | 2 + 30 ÷ 50 |
| Discounted payback | about 3.1 years | 3 + 2.1 ÷ 27.3 |
| NPV at 10% | EUR 25.2M | 125.2 − 100 |
| IRR | 20.5% | Rate where NPV = 0 |

Decision: **accept**, since NPV > 0 and IRR 20.5% > 10%. Discounting delays payback from 2.6 to 3.1 years. NPV falls as r rises: +60 at 0%, +25.2 at 10%, +1.0 at 20%, 0 at 20.5% (the IRR), −8.4 at 25%. NPV at 0% equals total net cash, the ROI numerator.

### Decision rules

- **NPV < 0 → no go. NPV ≥ 0 → go.** NPV = 0 means the project earns exactly the required return.
- **IRR > hurdle rate → go.** IRR is the break-even cost of capital.
- **Hurdle rate** = minimum required return = the r used in NPV. It must rise with risk: an H3 bet needs a higher hurdle than an H1 rollout.

### NPV vs IRR pitfalls

- **Scale**: IRR is a %, blind to size. EUR 1M at 50% IRR creates less value than EUR 100M at 20%. To rank mutually exclusive projects, trust NPV.
- **Sign changes**: if cash flows change sign more than once (for example a late decommissioning cost), there can be several IRRs or none.
- **Reinvestment**: IRR assumes interim cash is reinvested at the IRR; NPV assumes r, which is more realistic.
- **Additivity**: NPVs of projects add up; IRRs don't.

### Defending the numbers

Every number needs a method you can explain. Assumptions are fine if the method is strong. Always compare **worst, base and best scenarios**, and calculate the **cost of doing nothing**.

## 2. Spotting planted flaws in a strategy memo

For each claim in the memo, ask which course rule it breaks, then name the rule in your answer. This checklist is built from the course rules above. It is not an official list.

| Flaw you might see | Why it is wrong | Rule to cite |
| --- | --- | --- |
| Investment justified by ROI or IRR alone | Ignores timing (ROI) or scale (IRR) | NPV is the headline metric |
| I0 discounted, or CF0 put inside Excel NPV() | Year-0 cash is not discounted | NPV formula |
| One hurdle rate for all projects, or the hurdle set at WACC | Ignores AI execution risk | Hurdle rate rises with risk |
| One scenario only, no baseline | No downside view | Worst, base, best + cost of doing nothing |

## 3. Practice questions with answers

Answers to Q1 and Q3 come from your notes. Q2 is a suggested answer that applies the course frameworks.

1. **A project costs EUR 50M and returns EUR 20M a year for 3 years. What is its ROI, and why might it still destroy value at 10%?**
    - ROI = (60 − 50) / 50 = 20%. NPV = 20/1.1 + 20/1.1² + 20/1.1³ − 50 = 49.74 − 50 = −0.26M. **No go.** ROI ignores the time value of money; IRR is about 9.7%, below the 10% hurdle.
2. **Project A: 35% IRR on EUR 2M. Project B: 18% IRR on EUR 40M. Hurdle 13%. Which do you prefer, and what do you need to know?**
    - Both clear the hurdle. If capital allows, do both. If they are mutually exclusive, rank by **NPV, not IRR**: B likely creates far more absolute value because of scale. You need the cash-flow timing and duration, whether they are exclusive, the capital limit, each project's risk (and so its own hurdle), and whether cash flows change sign.
3. **Why test an AI programme against a hurdle rate above WACC, and what is the risk of setting it too high?**
    - WACC does not price the extra execution, adoption and tech risk that AI programmes carry. Set too high, the hurdle kills good H2 and H3 bets, pushes the portfolio toward H1 (failing strategically), and tempts teams to inflate forecasts.
