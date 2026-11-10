"""Compare two complete cash-flow paths without adding their gap twice.

Both paths must describe the same entity, ownership share, currency, period,
tax treatment and opportunity set. Values may be absolute cash flow or change
from the same reference; mixing the two bases is invalid.
"""
from math import isfinite


def incremental_path(program, continuing_baseline):
    program = tuple(program)
    continuing_baseline = tuple(continuing_baseline)
    if not program or len(program) != len(continuing_baseline):
        raise ValueError('Paths must be non-empty and cover identical periods')
    if any(not isfinite(x) for x in program + continuing_baseline):
        raise ValueError('Cash flows must be finite')
    return tuple(a - b for a, b in zip(program, continuing_baseline))


def waiting_gap(early, delayed):
    """Compare two complete paths; cost of waiting is not an extra benefit."""
    return incremental_path(early, delayed)
