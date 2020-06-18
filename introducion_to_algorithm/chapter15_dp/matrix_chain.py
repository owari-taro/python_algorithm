from typing import List
import math

def matrix_chain_order(p: List[int]) -> int:
    n = len(p)-1
    m = [[0]*n for _ in range(n)]
    s = [[0]*n for _ in range(n)]
    for i in range(n):
        m[i][i]=0
    for l in range(2,n+1):
        for i in range(n-l):
            j=i+l-1
            m[i,j]=math.inf
            