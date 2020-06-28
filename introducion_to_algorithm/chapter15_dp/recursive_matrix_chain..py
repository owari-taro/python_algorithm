import math
from typing import List
Matrix = List[List]


def recursive_matrix_chain(p: List, st, ed):
    """[summary]
    return caluculation amount needed to multiply A[St]*....A[ed]

    Parameters
    ----------
    p : List
        [description]
    st : [type]
        [description]
    ed : [type]
        [description]
    """
    memo = [[None]*]
    if st == ed:
        return 0
    tmp = math.inf
    for i in range(st, ed):
        current = recursive_matrix_chain(
            p, st, i)+recursive_matrix_chain(p, i+1, ed)+p[st-1]*p[i]*p[ed]
        if current < tmp:
            tmp = current
    return current
