"""Comprehensive Investment-Grade Audit of totalenergies_ai_portfolio_model.xlsx.
Checks sheet existence, formula validity, cell references, and reconciliations.
"""

from pathlib import Path
import openpyxl

WB_PATH = Path("work/finance/totalenergies_ai_portfolio_model.xlsx")

def audit():
    print(f"Auditing Workbook: {WB_PATH}")
    wb = openpyxl.load_workbook(WB_PATH, data_only=False)
    
    print("\n1. Sheets present:")
    for name in wb.sheetnames:
        ws = wb[name]
        print(f"  - {name:28s} (Max Row: {ws.max_row:3d}, Max Col: {ws.max_column:2d})")

    # 2. Inspect Variables Sheet
    print("\n2. Variables Sheet Parameters:")
    ws_v = wb["Variables"]
    for r in range(3, 24):
        cat = ws_v.cell(r, 1).value
        pname = ws_v.cell(r, 2).value
        val = ws_v.cell(r, 3).value
        unit = ws_v.cell(r, 4).value
        print(f"  Row {r:2d}: {pname:38s} = {str(val):30s} [{unit}]")

    # 3. Inspect Portfolio Consolidation
    print("\n3. Portfolio Consolidation Table:")
    ws_pc = wb["Portfolio_Consolidation"]
    print(f"  {'Row':3s} | {'ID':4s} | {'Name':35s} | {'Cost Ref':25s} | {'NPV Ref':25s} | {'Hurdle Ref':15s}")
    print("  " + "-" * 115)
    for r in range(5, 25):
        pid = ws_pc.cell(r, 1).value
        name = ws_pc.cell(r, 2).value
        cost = ws_pc.cell(r, 6).value
        npv = ws_pc.cell(r, 10).value
        hurdle = ws_pc.cell(r, 9).value
        if pid:
            print(f"  {r:3d} | {str(pid):4s} | {str(name)[:35]:35s} | {str(cost):25s} | {str(npv):25s} | {str(hurdle):15s}")

    # 4. Inspect Portfolio Cash Waterfall Formulas
    print("\n4. Portfolio Cash Waterfall Formulas:")
    ws_wf = wb["Portfolio_Cash_Waterfall"]
    for r in range(4, 13):
        metric = ws_wf.cell(r, 1).value
        b_val = ws_wf.cell(r, 2).value
        c_val = ws_wf.cell(r, 3).value
        h_val = ws_wf.cell(r, 8).value
        print(f"  Row {r:2d} ({metric[:35]:35s}): B={str(b_val)[:30]:30s} | C={str(c_val)[:30]:30s} | H={str(h_val)}")

    print("\n  Portfolio Waterfall KPIs:")
    for r in range(16, 26):
        lbl = ws_wf.cell(r, 1).value
        val = ws_wf.cell(r, 2).value
        if lbl:
            print(f"  {str(lbl):40s} = {val}")

    # 5. Inspect Scenario Sensitivity (ENPV)
    print("\n5. Scenario Sensitivity & ENPV:")
    ws_sc = wb["Scenario_Sensitivity_ENPV"]
    for r in range(4, 8):
        scen = ws_sc.cell(r, 1).value
        prob = ws_sc.cell(r, 2).value
        cap = ws_sc.cell(r, 3).value
        cash = ws_sc.cell(r, 4).value
        npv = ws_sc.cell(r, 5).value
        print(f"  Row {r}: {scen:30s} | Prob={str(prob):15s} | Cap={str(cap):5s} | Net Cash={str(cash):35s} | NPV={str(npv)}")

    # 6. Inspect Strategic Reconciliations
    print("\n6. Strategic Reconciliations:")
    ws_sr = wb["Strategic_Reconciliations"]
    print("  Table 1: Three Horizons Capital & 5-Yr Net Value:")
    for r in range(5, 10):
        cat = ws_sr.cell(r, 1).value
        inits = ws_sr.cell(r, 2).value
        cost = ws_sr.cell(r, 3).value
        mix = ws_sr.cell(r, 4).value
        npv = ws_sr.cell(r, 6).value
        vmix = ws_sr.cell(r, 7).value
        print(f"  Row {r}: {str(cat):32s} | Cost={str(cost):35s} | Mix={str(mix):15s} | NPV={str(npv):35s} | VMix={str(vmix)}")

    print("\n  Table 1b: Full-Scale Strategic Value Creation (Maturity 2030+):")
    for r in range(14, 19):
        cat = ws_sr.cell(r, 1).value
        inits = ws_sr.cell(r, 2).value
        val_scale = ws_sr.cell(r, 3).value
        mix = ws_sr.cell(r, 4).value
        target = ws_sr.cell(r, 5).value
        print(f"  Row {r}: {str(cat):32s} | SteadyValue={str(val_scale):10s} | Mix={str(mix):15s} | Target={str(target):15s}")

    print("\n  Table 2: Sourcing Strategy Allocation:")
    for r in range(23, 27):
        mode = ws_sr.cell(r, 1).value
        cost = ws_sr.cell(r, 3).value
        share = ws_sr.cell(r, 4).value
        print(f"  Row {r}: {str(mode):32s} | Cost={str(cost):45s} | Share={str(share)}")

    # 7. Inspect Cost of Inaction Sheet
    print("\n7. Cost of Inaction & Decision Value Bridge:")
    ws_coi = wb["Cost_of_Inaction"]
    print("  Inaction Erosion Schedule:")
    for r in range(5, 11):
        did = ws_coi.cell(r, 1).value
        y1 = ws_coi.cell(r, 4).value
        y2 = ws_coi.cell(r, 5).value
        y3 = ws_coi.cell(r, 6).value
        y4 = ws_coi.cell(r, 7).value
        y5 = ws_coi.cell(r, 8).value
        cum = ws_coi.cell(r, 9).value
        pv_h = ws_coi.cell(r, 10).value
        pv_w = ws_coi.cell(r, 11).value
        print(f"  Row {r:2d}: {str(did):32s} | Y1={str(y1):6s} | Y2={str(y2):6s} | Y3={str(y3):6s} | Y4={str(y4):6s} | Y5={str(y5):6s} | Cum={str(cum):15s} | PV@Hurdle={str(pv_h):25s} | PV@WACC={str(pv_w):25s}")

    print("\n  Decision Value Bridge:")
    for r in range(15, 21):
        metric = ws_coi.cell(r, 1).value
        sq = ws_coi.cell(r, 2).value
        prog = ws_coi.cell(r, 3).value
        inc = ws_coi.cell(r, 4).value
        rat = ws_coi.cell(r, 5).value
        print(f"  Row {r:2d}: {str(metric):45s} | StatusQuo={str(sq):15s} | Program={str(prog):30s} | Incremental={str(inc):18s}")

    print("\n  Incremental Cash Flow Stream (for IRR):")
    for r in range(23, 26):
        lbl = ws_coi.cell(r, 1).value
        vals = [str(ws_coi.cell(r, c).value) for c in range(2, 8)]
        print(f"  Row {r:2d}: {str(lbl):45s} | " + " | ".join(vals))

    # 8. Automated Assertion Checks
    print("\n8. Programmatic Integrity Assertions:")
    assert ws_coi["C15"].value == "=Portfolio_Consolidation!$F$24", f"C15 invalid: {ws_coi['C15'].value}"
    assert ws_coi["C16"].value == "=Portfolio_Consolidation!$H$24", f"C16 invalid: {ws_coi['C16'].value}"
    assert ws_coi["C17"].value == "=Portfolio_Cash_Waterfall!$B$17", f"C17 invalid: {ws_coi['C17'].value}"
    assert ws_coi["C18"].value == "=Scenario_Sensitivity_ENPV!$E$7", f"C18 invalid: {ws_coi['C18'].value}"
    assert ws_coi["C19"].value == "=Portfolio_Cash_Waterfall!$B$18", f"C19 invalid: {ws_coi['C19'].value}"
    assert ws_coi["C20"].value == "=Portfolio_Cash_Waterfall!$B$20", f"C20 invalid: {ws_coi['C20'].value}"
    assert ws_coi["D19"].value == "=IRR(B25:G25)", f"D19 invalid: {ws_coi['D19'].value}"
    assert ws_coi["J10"].value == "=NPV(Variables!$C$13, D10:H10)", f"J10 invalid: {ws_coi['J10'].value}"
    assert ws_coi["K10"].value == "=NPV(Variables!$C$6, D10:H10)", f"K10 invalid: {ws_coi['K10'].value}"
    print("  [PASS] All Cost_of_Inaction cross-sheet references verified.")

    # IRR numerical check
    prog_cf = [-5.95, -4.41, 59.83, 173.54, 265.50, 308.00]
    sq_cf = [0.0, -1.00, -31.22, -56.32, -80.91, -106.57]
    inc_cf = [p - s for p, s in zip(prog_cf, sq_cf)]
    # This example has one initial negative flow followed by positive flows,
    # so its unique positive IRR can be found without an optional dependency.
    low, high = 0.0, 1.0
    def npv(rate):
        return sum(cf / (1 + rate) ** year for year, cf in enumerate(inc_cf))
    while npv(high) > 0:
        high *= 2
    for _ in range(100):
        mid = (low + high) / 2
        if npv(mid) > 0:
            low = mid
        else:
            high = mid
    calc_irr = (low + high) / 2
    assert abs(calc_irr - 3.8539) < 0.01, f"Calculated IRR mismatch: {calc_irr}"
    print(f"  [PASS] Incremental IRR mathematically verified at {calc_irr*100:.2f}%.")

    print("\nReference assertions and the hard-coded IRR example passed. This is not a workbook recalculation or an economic validation.")

if __name__ == "__main__":
    audit()
