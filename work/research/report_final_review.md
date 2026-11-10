# Final report review — 10 November 2026

**Status: prepared for team review; no claim of internal TotalEnergies or academic assessor approval.** Scope: the Markdown analytical report and its notebook-derived figures. Do not derive the executive memo or slides until the team validates the report. No PDF, original source, active workbook, project cash flow, pre-existing chart data or original portfolio notebook has been edited. A separate notebook generates four reusable case-table figures from the workbook.

## Course coverage

The report's Appendix A maps readiness and bottleneck, operating model, Three Horizons, complete portfolio canvas, investment envelope and six categories, cash-flow scenarios, IRR and hurdle, cost of inaction, liquidity, governance, change and board questions to report sections. It distinguishes the detailed report from the separate two-page memo and 15-minute pitch / five-minute defence. The teacher's slide on downside warns against an unrealistically favourable scenario; the report records the negative pre-overlay downside, scenario limitations and a separate severe stress rather than presenting the adjusted result as a loss cap.

## Arithmetic and figure review

- 34 existing finance tests passed, including independent workbook-scenario and notebook-dataset reconciliation. Both read-only portfolio and half-envelope financial scripts passed.
- A separate LibreOffice recalculation reproduced 2,906 comparable numerical formula caches and all 18 portfolio cumulative-cash values; see `work/research/workbook_recalculation_review.md`. Excel COM did not start, so no native Excel recalculation is claimed.
- Thirteen figures are embedded in the report and collected in `deliverables/report/assets/`. Their SHA-256 digests match notebook exports, including four case-table figures from `focus_financial_tables.ipynb`. They cover portfolio bubbles and mixes, four focus cases, the combined focus view, the portfolio J-curve and net contributions. Existing visuals exclude the separate inaction overlay; P13 uses EUR and other focus cases use USD. The 15-year mix and H3 bubbles are speculative.
- All local Markdown report links resolve. The active workbook retains SHA-256 `1B55285D093FCF3B1CC133ADF2D232D09AFC61C03B003DB15466CB4FBDE7D3B1`.

## Inaction compared with the course

The course's fictional MaisonRetail assumes approximately €8m of no-programme loss PV at 12%, corresponding to 23.5% of €34m five-year gross costs. The report's hypothetical $3.143m loss PV at 10% is 11.4% of $27.6371m gross costs; at 12% the same hypothetical path is $2.927m, or 10.6%. The report separately attributes $1.571m to the portion assumed avoided, not the full loss. Different businesses, timing, tax and rate conventions limit comparison. The relative scale is a teaching-example sanity check, not evidence for a particular TotalEnergies loss.

The company does identify competition for skills and innovation risks (2025 URD p. 318), but the proposed $150m customer pool, erosion, 50% avoidability and the future-offer pool lack validation. In particular, the exposure was increased to explore an adjusted positive downside; this is a scenario choice and cannot independently substantiate that outcome. Current project and HR benefits may overlap, and the extra intervention costs may be omitted. These limits and the zero-avoidance sensitivity are in the report and `work/research/overlap_and_inaction_review.md`.

## Limits for team approval

- Proposed pilots, operational baselines, owner roles, contracted rights, cash realisation, cost classification, rates and gate thresholds remain assumptions or unknowns; the academic team may use them as openly labelled scenario inputs but they are not TotalEnergies facts or approved commitments.
- The half-envelope subset is an illustrative alternative, not a replacement of the selected portfolio; safety, H3 option value, dependencies and its own inaction path need further analysis.
- The source XLSX and pre-existing chart outputs remain unchanged; four case-table figures have been added from the separate notebook. Confirm the exact report and figures in the DOCX rendering after the user has reviewed the Markdown, and keep citations and figure limitations readable.

