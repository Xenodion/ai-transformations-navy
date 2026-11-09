# Adversarial Investment-Grade Financial Audit: Roadmap Step 18

**Deliverables Audited:**
- `work/finance/portfolio_economics.md` (Portfolio Financial Economics and Investment Model Report)
- `work/finance/totalenergies_ai_portfolio_model.xlsx` (Master Investment-Grade Excel Model)
- `work/finance/build_financial_model.py` (Model Generation Script)

**Audit Date:** 9 November 2026  
**Auditor:** Quality & Financial Review Gate (`review-expert`)  
**Acceptance Criterion Audited:**
> *"CAPEX/OPEX, year 0–5 flows, NPV, IRR, payback, justified hurdle, downside/base/upside, sensitivities, and double-counting check."*

**Audit Verdict:** 🔴 **REQUEST CHANGES (FAIL)**  
**Confidence Rating:** High (100% verified via automated cell extraction, formula parsing, and independent DCF modeling)

---

## Executive Summary & Scorecard

| Audit Verification Dimension | Status | Key Audit Finding |
| :--- | :---: | :--- |
| **1. Markdown vs Excel 100% Reconciliation** | 🔴 **FAIL** | 6 numerical discrepancies identified: Subtotal hurdles (I10/I22), subtotal IRRs (K10/K22), consolidated IRR (K24), scenario NPVs (E4/E6/E7), and the 25-cell 2D sensitivity matrix. |
| **2. Formula Integrity & Dynamic Referencing** | ⚠️ **PARTIAL** | 860 live formulas, 0 broken sheet references (`#REF!`), but algebraic bugs in `Portfolio_Consolidation!K24` (averaging IRRs) and `Scenario_Sensitivity_ENPV` (mixing nominal cash with discounted dollars). |
| **3. Three Horizons & Sourcing Allocations** | 🟢 **PASS** | Exact 100.0% sum to $38.79M across both dimensions: Sourcing (Blend 55.2%, Buy 25.5%, Build 19.3%) and Horizons (H0 4.2%, H1 60.7%, H2 19.1%, H3 16.0%). |
| **4. Hurdle Rates & WACC Justification** | 🟢 **PASS** | Methodologically sound CAPM derivation (7.5% WACC) with transparent branch operational risk premiums (9.0%–15.0%) and exact capital-weighted hurdle (10.98%). |
| **5. Anti-Double Counting Safeguards** | 🟢 **PASS** | Clean demarcation against TotalEnergies' $12.5bn corporate savings plan (`CLM-007`) and rock-solid technical boundary between P01 and P10 on steam crackers. |
| **6. Course Requirements & AGENTS.md Rules** | 🔴 **FAIL** | Violates AGENTS.md Rule 3 and Rule 6 due to conflicts between markdown narrative numbers and the Excel single source of truth. |

---

## Detailed Audit Findings

### 🚨 Blocker 1: Portfolio Consolidated IRR in `Portfolio_Consolidation!K24`
- **Location:** `Portfolio_Consolidation` sheet, cell `K24` vs `Portfolio_Cash_Waterfall!B16` vs `portfolio_economics.md` line 178.
- **Defect:** In `Portfolio_Consolidation`, cell `K24` calculates:
  ```excel
  =(K10*F10+K22*F22)/F24
  ```
  This is a capital-weighted average of the Tier 1 and Tier 2 IRRs, evaluating to **952.2%**.
- **Financial Rule:** In corporate finance (Session 3), portfolio IRR is defined as the internal rate of return of the consolidated net cash flow stream. A weighted average of IRRs is mathematically invalid because timing and cash scale differ across projects.
- **Discrepancy:**
  - `Portfolio_Cash_Waterfall!B16` calculates `=IRR(B8:G8)` = **784.9%** (the true portfolio IRR).
  - `portfolio_economics.md` Table 5, row 178 displays **784.9%**.
  - But `Portfolio_Consolidation!K24` displays **952.2%**.
- **Required Fix:** Change `Portfolio_Consolidation!K24` to reference `=Portfolio_Cash_Waterfall!$B$16`.

---

### 🚨 Blocker 2: Tier 1 and Tier 2 Subtotal Hurdle Rates in Table 5
- **Location:** `portfolio_economics.md` Table 5 (lines 167 & 177) vs `Portfolio_Consolidation!I10` and `I22`.
- **Defect:**
  - In `Portfolio_Consolidation!I10`, the formula `=SUMPRODUCT(F5:F9,I5:I9)/F10` evaluates to **11.17%** (or 11.2%). In markdown line 167, the table reports **11.41%** (which appears to be an unweighted arithmetic average of branch hurdles: `57/5 = 11.4%`).
  - In `Portfolio_Consolidation!I22`, the formula `=SUMPRODUCT(F13:F21,I13:I21)/F22` evaluates to **10.85%** (or 10.8%). In markdown line 177, the table reports **10.67%**.
- **Required Fix:** Update Table 5 lines 167 and 177 in `portfolio_economics.md` to **11.17%** and **10.85%** respectively, matching the Excel dynamic calculations.

---

### 🚨 Blocker 3: Tier 1 and Tier 2 Subtotal IRRs in Table 5
- **Location:** `portfolio_economics.md` Table 5 (lines 167 & 177) vs `Portfolio_Consolidation!K10` and `K22`.
- **Defect:**
  - In `Portfolio_Consolidation!K10`, `=SUMPRODUCT(F5:F9,K5:K9)/F10` evaluates to **562.2%**, but markdown line 167 reports **512.9%**.
  - In `Portfolio_Consolidation!K22`, `=SUMPRODUCT(F13:F21,K13:K21)/F22` evaluates to **1228.6%**, but markdown line 177 reports **1312.5%**.
  *(Note: If calculated as consolidated cash flow IRRs from the net cash flows of each tier, Tier 1 IRR is 311.7% and Tier 2 IRR is 1154.3%).*
- **Required Fix:** Reconcile `K10` and `K22` with the markdown document, clearly identifying whether the metric is a weighted average IRR or a consolidated cash flow IRR.

---

### 🚨 Blocker 4: Scenario Sensitivity (Downside, Upside, ENPV) Formulation and Values
- **Location:** `Scenario_Sensitivity_ENPV!E4:E7` vs `portfolio_economics.md` Section 6 (lines 44, 189–205, 298–300).
- **Defect:**
  1. **Dimensional Mismatch in Excel Formula:** In `Scenario_Sensitivity_ENPV`, cell `E4` uses:
     ```excel
     =(Portfolio_Cash_Waterfall!H10+Portfolio_Cash_Waterfall!H6)*C4-Portfolio_Cash_Waterfall!H6
     ```
     `H10` is Discounted Net Present Value ($675.57M), while `H6` is the *undiscounted* sum of nominal outflows ($50.79M). Adding undiscounted dollars to discounted dollars produces a dimensional mismatch.
  2. **Numerical Discrepancy:**
     - Downside NPV: Excel `E4` evaluates to **+$385.02M**, but markdown claims **+$387.82M**.
     - Upside NPV: Excel `E6` evaluates to **+$893.47M**, but markdown claims **+$891.39M**.
     - ENPV: Excel `E7` evaluates to **+$657.41M**, but markdown claims **+$657.59M**.
  3. **Rigorous Discounted Cash Flow Valuation:**
     Discounting the flows year-by-year (or discounting PV of Gross Benefits: $715.71M and PV of Outflows: $40.14M):
     - True Downside NPV (60% benefits, 100% costs) = `0.60 * $715.71M - $40.14M` = **+$389.28M**.
     - True Upside NPV (130% benefits, 100% costs) = `1.30 * $715.71M - $40.14M` = **+$890.28M**.
     - True ENPV (25% / 50% / 25%) = **+$657.67M**.
- **Required Fix:**
  - Either upgrade `Scenario_Sensitivity_ENPV` to discount the flows properly using `SUMPRODUCT` with the discount factor row, OR align the markdown document precisely with the exact output of the Excel cells.

---

### 🚨 Blocker 5: 2D Sensitivity Matrix Discrepancy
- **Location:** `Scenario_Sensitivity_ENPV!A12:F17` vs `portfolio_economics.md` Table 6.3 (lines 213–219).
- **Defect:** All 25 cells in the markdown sensitivity table were manually typed approximations that differ from the values evaluated by the Excel formulas:
  - At Hurdle 8.0%: Excel computes **$435M, $581M, $726M, $871M, $1,016M**; markdown reports **$437M, $612M, $725M, $840M, $975M**.
  - At Hurdle 11.0%: Excel computes **$385M, $530M, $675M, $820M, $966M**; markdown reports **$388M, $550M, $676M, $790M, $920M**.
- **Required Fix:** Update markdown Table 6.3 so that every cell matches the corresponding cell in Excel.

---

### ⚠️ Warning 6: Abbreviated Formula in Cross-Reference Index (Line 308)
- **Location:** `portfolio_economics.md` Table 9, line 308.
- **Defect:** Markdown writes `=Portfolio_Consolidation!F5+F6+F7+F8+F13+F18+F19`, omitting sheet qualifiers on cells `F6:F19`. In live Excel, the formula correctly qualifies every cell reference.
- **Required Fix:** Update the formula text in markdown line 308 to display the full, qualified Excel formula.

---

## Positive Validations & Highlights

1. **Self-Financing Cash Engine Proven:**
   - In Year 0, CAPEX is $5.95M.
   - In Year 1, Net Cash Flow turns positive at **+$34.36M** (Gross Benefits: $43.90M, OPEX: $9.54M).
   - Cumulative net cash breaks positive in Month 13.5 (under 1.2 years simple payback, under 1.4 years discounted payback).
2. **Three Horizons Allocation Integrity:**
   - Capital allocations: H0 = $1.64M (4.23%), H1 = $23.54M (60.69%), H2 = $7.42M (19.13%), H3 = $6.19M (15.96%). Sum = **$38.79M (100.00%)**.
   - Strategic alignment with Nagji & Tuff (2012) framework is well documented: near-term cash generation is anchored in H1/H2 core operations, while H3 options provide long-term asymmetric upside without fabricating premature paybacks.
3. **Sourcing Breakdown Integrity:**
   - Blend: $21.42M (55.22%).
   - Buy: $9.89M (25.50%).
   - Build: $7.48M (19.28%).
   - Sum = **$38.79M (100.00%)**.
4. **Anti-Double Counting Controls:**
   - Strict audit boundaries for P01, P03, P06, P11, and P13 against TotalEnergies' $12.5bn corporate savings plan (`CLM-007`).
   - Clean industrial boundary established between P01 (rotating machinery vibration/trips) and P10 (pyrolysis furnace cracking selectivity) on shared steam cracker assets.
5. **WACC & Hurdle Justification:**
   - CAPM parameters verified against audited 2025 financial statements (Rf: 3.0%, Beta: 0.90, MRP: 5.5%, Gearing: 14.7%, WACC: 7.5%).
   - Branch hurdle rates (9.0% to 15.0%) reflect capital intensity and risk profiles.

---

## Actionable Remediation Plan

To bring Step 18 to 🟢 **PASS**, execute the following:

1. **In `work/finance/build_financial_model.py`:**
   - In `build_portfolio_consolidation()`: change row 24 column 11 formula from `f"=(K{t1_sub_row}*F{t1_sub_row}+K{t2_sub_row}*F{t2_sub_row})/F{row_idx}"` to `"=Portfolio_Cash_Waterfall!$B$16"`.
   - In `build_scenario_sensitivity()`: refine the Downside and Upside formulas to use discounted present values, or ensure consistency with the reported metrics.
   - Re-run `python work/finance/build_financial_model.py` to regenerate `work/finance/totalenergies_ai_portfolio_model.xlsx`.
2. **In `work/finance/portfolio_economics.md`:**
   - Update Table 5 line 167: Subtotal Tier 1 Hurdle -> `11.17%`, Subtotal IRR -> `562.2%`.
   - Update Table 5 line 177: Subtotal Tier 2 Hurdle -> `10.85%`, Subtotal IRR -> `1228.6%`.
   - Update Table 5 line 178: Portfolio IRR remains `784.9%` (now matching Excel cell `K24`).
   - Reconcile Section 6 and Table 6.1 with the exact Excel formula outputs.
   - Update Table 6.3 (2D sensitivity matrix) to match the 25 exact values produced by Excel.
   - Update line 308 with the fully qualified formula string.
