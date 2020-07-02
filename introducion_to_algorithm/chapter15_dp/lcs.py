from enum import Enum
from typing import List,Tuple
Matrix=List[List]

class Direction(Enum):
    UP = "up"
    LEFT = "left"
    UPPER_LEFT = "upper_left"


def lcs_le(x: List, y: List) ->Tuple[Matrix,atrix] :
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
    #each index is a optimal solution for each subproblem
    index_matrix=[[None]*n for i in range(m)]
    # if either indecd is 0 then each element is 0
    for i n ranage(1, m+1):
        lcs_matrix[i][0]= 0
    for j in range(n+1):
        lcs_matrix[0][j]= 0
    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                lcs_matrix[i+1][j+1]= lcs_matrix[i][j]+1
                index_matrix[i][j]=(i-1,j-1)
            elif lcs_matrix[i][j+1] >= lcs_matrix[i+1][j]:
                lcs_matrix[i+1][j+1]= lcs_matrix[i][j+1]
                index_matrix[i][j]=(i-1,j)
            else:
                lcs_matrix[i+1][j+1]= lcs_matrix[i+1][j]
                index_matrix[i][j]=(i,j-1)
    return lcs_matrix,index_matrix