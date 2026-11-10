# Workbook recalculation review

**Review date:** 10 November 2026. **Scope:** verify cached workbook outputs, not business assumptions or Excel-specific compatibility.

Source: `work/finance/portfolio_model_14_revised.xlsx`, SHA-256 `1B55285D093FCF3B1CC133ADF2D232D09AFC61C03B003DB15466CB4FBDE7D3B1`. Excel COM could not start in this environment (Windows error `0x80070520`), so no Excel recalculation occurred.

LibreOffice was run headlessly with an isolated profile to open and convert the source to a separate temporary XLSX; the original was not saved or changed. The three Portfolio scenario cumulative cash series, Y0–Y5 (18 cells), matched the source caches. Across nine worksheet XML files, **2,906 comparable numeric formula cache values** matched with tolerance `1e-7 × max(1, |original|)`, and no recalculated errors were detected among the compared original formula cells. Breakdown by worksheet index: 34, 72, 0, 384, 4, 4, 280, 2,128 and 0. This only covers cells present as numeric formula caches in both XLSX files; it does not audit all formulas, charts, scenario quality, financial attribution, missing values or Excel-specific features. LibreOffice may rewrite spreadsheet features, so the converted file is a disposable review copy, not the deliverable.

The separate inaction overlay is not in the spreadsheet. `work/finance/verify_inaction.ps1` independently reads the original cached Portfolio series, adds the documented overlay and verifies the four NPV results. It does not establish that the overlay's exposure, causality, cost coverage or non-overlap is true. Reopen and recalculate in Excel when available for a native-engine check, saving any recalculated copy separately and comparing it before changing the active model.


The existing financial test suite was run from work/finance with the bundled Python runtime: **34 tests passed**, including the independent workbook cash-flow reconciliation, featured-case calculations and notebook dataset checks. These tests verify the documented calculations and cached dataset, not the truth of business assumptions or a native Excel recalculation.

