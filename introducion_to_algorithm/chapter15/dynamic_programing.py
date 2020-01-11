
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

def fibonach(n: int) -> int:
    """problem15.1-5"""
    if n < 0:
        raise ValueError("n must be positive")
    f: List[int] = [0, 1]
    if n == 0 or n == 1:
        return f[n]
    for i in range(2, n):
        f.append(f[i-1]+f[i-2])

    return f[-1]

if __name__=="__main__":
    prnt("aaaas")
    print(fibonach(1000))    
