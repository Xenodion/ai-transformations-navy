"""Scope-matched benefit drivers; amounts are assumptions, not evidence.

These functions require a documented counterfactual and consistent units. Their
outputs are not post-tax cash flows until scope, ownership and timing have been
validated by the case owner and finance.
"""
from math import isfinite


def _nonnegative(**values):
    if any(not isfinite(value) or value < 0 for value in values.values()):
        raise ValueError('Inputs must be finite and non-negative')


def _fraction(**values):
    _nonnegative(**values)
    if any(value > 1 for value in values.values()):
        raise ValueError('Fractions must be between zero and one')


def retail_writeoff_reduction(stores, cost_basis_per_store, loss_rate, reduction, adoption):
    """Annual incremental avoided inventory expense on a cost basis.

    The loss reduction must exclude goods also claimed as markdown recovery.
    Store scope and adoption must match the budget and counterfactual.
    """
    _nonnegative(stores=stores, cost_basis_per_store=cost_basis_per_store)
    _fraction(loss_rate=loss_rate, reduction=reduction, adoption=adoption)
    return stores * cost_basis_per_store * loss_rate * reduction * adoption


def drilling_cash_saving(days_avoided, avoidable_cash_per_day, entitled_share, implementation_cost=0):
    """Incremental cash retained by the company, after incremental incentives.

    Days alone do not prove cash: use zero avoidable cost where invoices or
    contractual outflows remain fixed; entitlement is contract-specific.
    """
    _nonnegative(days_avoided=days_avoided, avoidable_cash_per_day=avoidable_cash_per_day,
                 implementation_cost=implementation_cost)
    _fraction(entitled_share=entitled_share)
    return days_avoided * avoidable_cash_per_day * entitled_share - implementation_cost


def refinery_margin(eligible_barrels, incremental_availability, realized_share, contribution_margin):
    """Annual extra contribution, with volumes and margin on matching scope."""
    _nonnegative(eligible_barrels=eligible_barrels, contribution_margin=contribution_margin)
    _fraction(incremental_availability=incremental_availability, realized_share=realized_share)
    return eligible_barrels * incremental_availability * realized_share * contribution_margin
