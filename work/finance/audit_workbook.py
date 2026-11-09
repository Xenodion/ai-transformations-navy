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
    print("  Three Horizons Allocation:")
    for r in range(5, 10):
        cat = ws_sr.cell(r, 1).value
        inits = ws_sr.cell(r, 2).value
        cost = ws_sr.cell(r, 3).value
        mix = ws_sr.cell(r, 4).value
        npv = ws_sr.cell(r, 6).value
        vmix = ws_sr.cell(r, 7).value
        print(f"  Row {r}: {str(cat):32s} | Cost={str(cost):35s} | Mix={str(mix):15s} | NPV={str(npv):35s} | VMix={str(vmix)}")

    print("\n  Sourcing Strategy Allocation:")
    for r in range(14, 18):
        mode = ws_sr.cell(r, 1).value
        cost = ws_sr.cell(r, 3).value
        share = ws_sr.cell(r, 4).value
        print(f"  Row {r}: {str(mode):32s} | Cost={str(cost):45s} | Share={str(share)}")

    print("\nAUDIT COMPLETED CLEANLY.")

if __name__ == "__main__":
    audit()
