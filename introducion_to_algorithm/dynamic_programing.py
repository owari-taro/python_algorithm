
from typing import List
import math

# TODO:return maybe not only float but integer


def cut_rod(p: List, n: int) -> float:
    """ solve cut-rod problem.But this is ineffecient algorithm"""
    if n == 0:
        return 0
    q = math.inf*-1
    for i in range(n):
        q = max(q, cut_rod(i, n-i))
    return q


def bottom_up_cut_rod(p: List, n: int) -> float:
    r = [0]*(n+1)
    for j in range(1, n+1):
        q = -1*math.inf
        for i in range(1, j+1):
            q = max(q, p[i]+r[j-i])
        r[j] = q
    return q
