
from typing import List
Matrix = List[List[float]]


def transponse_adjancy_matrix(matrix: Matrix) -> Matrix:
    nrow = len(matrix)
    ncol = len(matrix[0])
    transposed: Matrix = [[0]*ncol for i in range(nrow)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                transposed[j][i] = 1
    return transposed
