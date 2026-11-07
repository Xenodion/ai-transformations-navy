
---

## Financial Reminders

### Present Value
    PV = CF(t) / (1+r)^t

- `CF(t)`: cash flow received at year t
- `r`: discount rate = cost of capital / required return (inflation is only one component of it)
- `t`: number of years from today

A euro later is worth less than a euro today. Example with r = 5%:
- today: 100 €
- in 1 year: 100 / 1.05 = 95.24 €
- in 2 years: 100 / 1.05^2 = 90.70 €


### Return on investment
    ROI = (total benefits - total costs) / total costs

Uses raw cash: ignores *when* the money comes in.


### Discounted cash flow
    DCF = CF1 / (1+r) + CF2 / (1+r)^2 + ... + CFn / (1+r)^n

PV of the future inflows only (the investment is not included).


### Net Present Value
    NPV = DCF - I_0 = SUM(t=1..n) CF(t) / (1+r)^t - I_0

- `I_0`: initial investment, paid at t = 0 → **not discounted**
- Same thing as `SUM(t=0..n) CF(t) / (1+r)^t` with `CF(0) = -I_0`
- Excel: `=NPV(r, CF1:CFn) + CF0`. `NPV()` treats its first value as t = 1, so CF0 goes outside the function.


### Payback
- **Payback**: years until the cumulative cash flow turns positive
- **Discounted payback**: same, on the cumulative PV


### Check on the worked example below (€M, r = 10%)
    ROI     = 60 / 100 = 60%
    Payback = 2 + 30/50 = 2.6 yrs
    NPV     = 30/1.1^1 + 40/1.1^2 + 50/1.1^3 + 40/1.1^4 - 100 = 25.22


# Module 1 · Worked Example 1 — One €100M project, step by step

All figures in €M. Discount rate: **10%**. Discount factor: `DF = 1 / 1.10^t`. Figures rounded.

## Cash flow table

| Year | Cash flow | Cumulative | DF @10% | PV | Cumulative PV |
|---:|---:|---:|---:|---:|---:|
| 0 | −100.0 | −100.0 | 1.000 | −100.0 | −100.0 |
| 1 | 30.0 | −70.0 | 0.909 | 27.3 | −72.7 |
| 2 | 40.0 | −30.0 | 0.826 | 33.1 | −39.7 |
| 3 | 50.0 | +20.0 | 0.751 | 37.6 | −2.1 |
| 4 | 40.0 | **+60.0** | 0.683 | 27.3 | **+25.2** |

## Key metrics

| Metric | Result | How it's calculated |
|---|---|---|
| **ROI** | 60% | Net cumulative cash ÷ investment = 60 ÷ 100 |
| **Payback** | 2.6 yrs | Cumulative turns positive in year 3: 2 + 30 ÷ 50 |
| **Discounted payback** | ≈ 3.1 yrs | Cumulative PV turns positive in year 4: 3 + 2.1 ÷ 27.3 |
| **NPV @ 10%** | **€25.2M** | Sum of PVs of inflows − investment = 125.2 − 100 |
| **IRR** | 20.5% | Rate at which NPV = 0 |

## Decision

**Accept** — NPV > 0 and IRR (20.5%) > 10% cost of capital.

## Takeaways

- **ROI and simple payback ignore the time value of money**; they use raw cumulative cash.
- **Discounting delays payback** (2.6 → 3.1 yrs) because later cash flows are worth less today.
- **NPV is the headline metric** (boxed on the slide): it measures value created in today's euros.
- **IRR** gives the break-even discount rate — the project stays NPV-positive as long as the cost of capital is below ~20.5%.

## Financial notes — NPV & IRR

### NPV
- Value created **in today's euros**, after paying the cost of capital.
- NPV < 0 → no go
- NPV ≥ 0 → go (NPV = 0: the project earns exactly the required return, no more)
- NPV decreases as r increases: later cash flows are discounted more.

### IRR
- The discount rate that makes NPV = 0:

      SUM(t=0..n) CF(t) / (1+IRR)^t = 0

- It is the project's own annual return, i.e. the **break-even cost of capital**: the highest r at which the project is still not losing value.
- No closed form: solve numerically (Excel `=IRR(CF0:CFn)`).
- Decision: IRR > hurdle rate → go; IRR < hurdle rate → no go.
- Worst case that is still acceptable: NPV = 0 ⇔ r = IRR.

NPV as a function of r (worked example):

| r | 0% | 10% | 20% | **20.5% (IRR)** | 25% |
|---|---:|---:|---:|---:|---:|
| NPV (€M) | +60.0 | +25.2 | +1.0 | **0** | −8.4 |

NPV > 0 as long as r < IRR, NPV < 0 beyond. Note NPV at 0% = total net cash = the ROI numerator.

### Hurdle rate
- Minimum return required = the discount rate used for NPV, and the bar IRR is compared to.
- It must **not** be the same for every project: riskier project → higher hurdle rate (e.g. an H3 bet vs an H1 rollout).

### NPV vs IRR — pitfalls
- **Scale**: IRR is a %, it ignores project size. €1M at 50% IRR creates less value than €100M at 20% IRR → to rank mutually exclusive projects, trust NPV.
- **Sign changes**: if cash flows change sign more than once (e.g. a late decommissioning cost), there can be several IRRs or none.
- **Reinvestment**: IRR implicitly assumes intermediate cash is reinvested at the IRR itself; NPV assumes reinvestment at r (more realistic).
- **Additivity**: NPVs of projects add up, IRRs don't.

# Questions

Q1 : A project costs €50M and returns €20M a year for 3 years. What is its ROI - and why might it still destroy value at 10% ?

    - ROI = (3*20 - 50) / 50 = 0.2 = 20%
    - NPV@10% = 20/1.1 + 20/1.1^2 + 20/1.1^3 - 50 = 49.74 - 50 = -0.26 €M < 0

        -> no go

        ROI > 0 but NPV < 0: ROI ignores the time value of money (IRR ≈ 9.7% < 10% hurdle rate)


Q2 : Project A: IIR at 35% on €2M.
Project B: IRR 18% on €40M.
The hurdle is 13%. Which do you prefer, and what do you need to know ?

Q3 : Why should an AI programme be tested agaisnt a hurdle rate above WACC - and what is the risk of setting it too high ?

    because WACC does not embbed risk and AI programs by design cary a risk.
    
    The risk of setting it too high is that the project might never reach that point or its going to have a very low return.