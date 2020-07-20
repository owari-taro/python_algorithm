from typing import List
Matrix = List[List]


def print_lcs(c: Matrix, x: List, y: List):
    """[summary]

    Parameters
    ----------
    c : Matrix
        [description]
    x : List
        [description]
    y : List
        [description]
    """

    n = c[len(x), len(y)]
    s = [None]*(n+1)
    i, j = len(x), len(y)
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            s[n] = x[i]
            n -= 1
            i -= 1
            j -= 1
        elif c[i-1, j] >= c[i, j-1]:
            i -= 1
        else:
            j -= 1
    print(s)
    return s
