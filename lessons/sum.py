"""Example Function for Unit Tests"""

def sun(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    sum_total: float  = 0.0
    idx: int = 0
    if idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum