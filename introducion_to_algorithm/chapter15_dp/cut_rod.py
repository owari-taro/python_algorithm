from typing import List
import math.inf


def cut_rod(p: List, n: int):
    if n == 0:
        return 0
    current = -math.inf
    for i in range(n):
        current = max(current, p[i]+cut_rod(p, n-i-1))
    return current
