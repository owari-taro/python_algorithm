from typing import List


def binary_search(a: List, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError()
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (hi+lo)//2
        if x < a[mid]:
            hi = mid
            
