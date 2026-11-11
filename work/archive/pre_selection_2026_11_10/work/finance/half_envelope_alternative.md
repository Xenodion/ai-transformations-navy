# Half-envelope portfolio alternative — illustrative subset

**Purpose:** answer the course's question “why this envelope and not half?” without changing the approved working workbook. This is an alternative planning scenario, not a selected portfolio, quote, forecast or a new approval request. The user-selected 14-initiative full portfolio and four focus cases remain unchanged.

## Perimeter and cost

Half of the full gross Y0–Y5 programme cost of $27.6371m is **$13.81855m**. Illustratively retain P01 (refining), P03 (drilling), P05 (licence rationalisation), P12 (H3 research), P13 (retail), and E01 (governance). Their existing modelled base gross expenditures sum to **$13.01708m**, leaving **$0.80147m** unallocated below the half-envelope ceiling. Gross cost includes the retained projects' Y0–Y1 CAPEX, launch and Y1–Y5 operating costs; excludes tax, working capital and post-Y5 spend, exactly as the full gross ceiling does. Excluding cash tax does not mean the tax-bearing cash flows are excluded from the NPV below.

The alternative defers P02, P04, P06, P07, P08, P09, P10 and the focus case **P11** entirely. This means losing their cash contributions, commercial flexibility learning, and P07's safety-oriented test (P07 has no booked safety benefit). P12 keeps one H3 learning option; no P12 commercial return is assumed. P11 deferral does not assert its commercial option has zero value. A programme should not cancel required safety activity: the no-programme baseline still contains existing safety controls, and any additional mandatory safety spend would reduce the unused cushion. A project may not be selected purely because its modeled return looks high; feasibility, interdependencies and H3 choice remain unresolved.

## Existing model cash, no inaction overlay

The [read-only reconciliation](verify_half_envelope.ps1) checks the gross cost and weighted NPV. Cash rows sum the original workbook's `Cash flow build` cached scenario net cash for the six retained projects, in USD m. P13 is translated using the workbook's 1.1165 USD/EUR assumption. They retain each project's existing scenario timing, tax treatment, sunk/exit costs, and inclusion; no flow was proportionally scaled. On the common 10% screening rate:

| Scenario | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | NPV at 10% | IRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Downside | −1.886 | −4.076 | +0.962 | +2.449 | +3.471 | +3.471 | +1.568 | 19.0% |
| Base | −1.797 | −3.618 | +1.377 | +2.711 | +3.547 | +3.497 | +2.683 | 26.6% |
| Upside | −1.797 | −3.361 | +1.816 | +3.305 | +4.274 | +4.224 | +4.673 | 38.0% |
| Weighted 25/50/25 | −1.819 | −3.668 | +1.383 | +2.794 | +3.710 | +3.672 | +2.902 | 27.5% |

NPV and IRR use unrounded cached annual values. Weights are subjective assumptions. The downside is the same mild gated scenario, not a worst case or a loss cap; it remains positive because this subset excludes several loss-making or expenditure-heavy projects, not because losses are impossible. All retained case assumptions, eligibility, tax, FX, shared enablers and possible overlapping value remain unverified. The full $1.571m PV avoided-inaction overlay must **not** be copied into this alternative: P11 and P08 are absent, so their contribution to preventing erosion is unknown. A fair comparison would quantify distinct alternative-specific avoided losses and extra costs, or use the no-overlay comparison for both options.

Under the same common 10% rate and before any inaction overlay, the full portfolio weighted NPV is **+$3.303m**, versus **+$2.902m** here. The difference is approximately **$0.401m**, conditional on the model's cash flows and without measuring omitted safety and option value. Neither figure is the sum of project-rate NPVs. The result is not a recommendation to cut the portfolio, nor proof of a larger return per dollar once risk, value interactions or minimum safety expenditure are accounted for.

## Decision checks

Finance should recalculate the workbook in Excel, verify the subset against the selected business scopes and spending rules, test loss of common cost allocations and data dependencies, establish what mandatory safety spending is needed, and model a severe downside and a separately justified inaction exposure. Preserve the full source workbook and notebook charts until the alternative is separately authorised.

