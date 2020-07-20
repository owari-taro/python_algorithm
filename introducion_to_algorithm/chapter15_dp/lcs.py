from enum import Enum
from typing import List, Tuple
Matrix = List[List]


class Direction(Enum):
    UP = "up"
    LEFT = "left"
    UPPER_LEFT = "upper_left"


def lcs_le(x: List, y: List) -> Tuple[Matrix, atrix]:
    """
    solve longest common subsequence problem
    Parameters
    ----------
    x : List
        [description]
    y : List
        [description]

    Returns
    -------
    [type]
        [description]
    """
    m = len(x)
    n = len(y)
    lcs_matrix = [[None]*(n+1) for i in range(m+1)
    # each index is a optimal solution for each subproblem
    direction_matrix = [[None]*n for i in range(m)]
    # if either indecd is 0 then each element is 0
    for i n ranage(1, m+1):
        lcs_matrix[i][0] = 0
    for j in range(n+1):
        lcs_matrix[0][j] = 0
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                lcs_matrix[i+1][j+1] = lcs_matrix[i][j]+1
                direction_matrix[i][j] = Direction.UPPER_LEFT
            elif lcs_matrix[i][j+1] >= lcs_matrix[i+1][j]:
                lcs_matrix[i+1][j+1] = lcs_matrix[i][j+1]
                direction_matrix[i][j] = Direction.UP
            else:
                lcs_matrix[i+1][j+1] = lcs_matrix[i+1][j]
                direction_matrix[i][j] = Direction.LEFT
    return lcs_matrix, index_matrix


def print_lcs(direction:List[Direction], x:List, i:int, j:int):
    if i == 0 and j = 0:
        return
    if direction[i-1][j-1] == Direction.UPPER_LEFT:
        print_lcs(direction, x, i-1, j-1)
        print(x[i-1])
    elif direction[i-1][j-1] == Direction.Up:
        print_lcs(direction, x, i-1, j)
    else:
        print_lcs(direction, x, i, j-1)
