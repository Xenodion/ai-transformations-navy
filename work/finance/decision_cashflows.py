"""Dated, gate-aware cash-flow calculations for the rebuilt decision case.

All amounts are in the same currency and nominal units. Inputs represent the
incremental program against a specified counterfactual. This module deliberately
contains no project forecasts: source-supported values must be supplied by the
case owners. Periods are year-end, with period zero at decision time.
"""
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Period:
    benefit: float = 0.0
    operating_cost: float = 0.0
    capital_cost: float = 0.0
    tax_cash: float = 0.0
    working_capital: float = 0.0
    exit_cost: float = 0.0
    # Committed payments after a stop cannot be cancelled. Sunk payments in
    # earlier periods remain in the stream automatically.
    unavoidable_cost: float = 0.0

    def __post_init__(self):
        values = vars(self)
        if any(not isfinite(v) for v in values.values()):
            raise ValueError('Cash amounts must be finite')
        if any(values[k] < 0 for k in ('benefit', 'operating_cost', 'capital_cost', 'exit_cost', 'unavoidable_cost')):
            raise ValueError('Benefits and named costs must be non-negative')
        # Signed tax and working-capital changes permit refunds and releases.


@dataclass(frozen=True)
class Project:
    name: str
    periods: tuple[Period, ...]
    # False is an unapproved reserve: no cost or benefit in the base case.
    approved: bool = True
    # Stop takes effect at the beginning of this period. Earlier costs are sunk.
    stop_at: int | None = None

    def cash(self):
        if self.stop_at is not None and not 0 <= self.stop_at < len(self.periods):
            raise ValueError('Stop period outside project schedule')
        if not self.approved:
            return tuple(0.0 for _ in self.periods)
        result = []
        for t, p in enumerate(self.periods):
            stopped = self.stop_at is not None and t >= self.stop_at
            if stopped:
                exit_charge = p.exit_cost if t == self.stop_at else 0.0
                result.append(-p.unavoidable_cost - exit_charge)
            else:
                result.append(p.benefit - p.operating_cost - p.capital_cost
                              - p.tax_cash - p.working_capital - p.unavoidable_cost)
        return tuple(result)


def aggregate(projects):
    projects = tuple(projects)
    if not projects:
        raise ValueError('At least one project is required')
    lengths = {len(p.periods) for p in projects}
    if len(lengths) != 1:
        raise ValueError('All schedules must use the same periods')
    return tuple(sum(values) for values in zip(*(p.cash() for p in projects)))


def npv(rate, flows):
    if not isfinite(rate) or rate <= -1:
        raise ValueError('Rate must be finite and greater than -100%')
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(flows))


def payback(flows, rate=0.0):
    """Interpolated payback in periods; None if cumulative cash never recovers.

    Interpolation assumes cash is spread uniformly inside the recovery period;
    annual inputs alone do not establish an actual month of receipt.
    """
    flows = tuple(flows)
    if not flows:
        raise ValueError('At least one cash flow is required')
    if not isfinite(rate) or rate <= -1:
        raise ValueError('Rate must be finite and greater than -100%')
    cumulative = flows[0]
    if cumulative >= 0:
        return 0.0
    for t, flow in enumerate(flows[1:], start=1):
        discounted = flow / (1 + rate) ** t
        next_cumulative = cumulative + discounted
        tolerance = 1e-10 * max(1.0, abs(cumulative), abs(discounted))
        if next_cumulative >= -tolerance and discounted > 0:
            return (t - 1) + min(1.0, -cumulative / discounted)
        cumulative = next_cumulative
    return None


def conventional_irr(flows):
    """IRR for a negative initial flow followed by one sign change only.

    Returns None for no positive inflow. Non-conventional streams are rejected
    because a single reported IRR can be ambiguous or misleading.
    """
    flows = tuple(flows)
    if not flows or any(not isfinite(x) for x in flows) or flows[0] >= 0:
        raise ValueError('A finite, negative initial flow is required')
    signs = [1 if x > 0 else -1 for x in flows if x != 0]
    changes = sum(a != b for a, b in zip(signs, signs[1:]))
    if changes == 0:
        return None
    if changes != 1 or signs[-1] != 1:
        raise ValueError('Non-conventional cash flows can have multiple IRRs')
    low, high = -0.999999, 1.0
    while npv(high, flows) > 0:
        high *= 2
    for _ in range(100):
        mid = (low + high) / 2
        if npv(mid, flows) > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def expected_value(scenarios):
    """Probability-weighted value; scenarios contain (probability, value)."""
    scenarios = tuple(scenarios)
    if not scenarios or any(not isfinite(p) or p < 0 or not isfinite(v) for p, v in scenarios):
        raise ValueError('Probabilities and values must be finite and probabilities non-negative')
    if abs(sum(p for p, _ in scenarios) - 1.0) > 1e-9:
        raise ValueError('Scenario probabilities must sum to one')
    return sum(p * value for p, value in scenarios)
