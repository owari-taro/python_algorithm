from typing import List
import math


def memorized_matrix_chain(p: List) -> None:
    n = len(p)-1
    m = [[None]*n for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            m[i][j] = math.inf
    return lookup_chain(m,p,1,n)

def lookup_chain(m,p,i,j):
    if m[i][j]<math.inf:
        return m[i][j]
    if i==j:
        m[i][j]=0
    else :
        NotImplemented