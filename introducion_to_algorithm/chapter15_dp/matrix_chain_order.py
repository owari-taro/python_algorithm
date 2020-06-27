from typing import List
import math
Matrix = List[List]
# TODO;operation check


def matrix_multiply(A: Matrix, B: Matrix) -> Matrix:
    """[summary]

    Parameters
    ----------
    A : Matrix
        [description]
    B : Matrix
        [description]

    Returns
    -------
    Matrix
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    if len(A[0]) != len(B):
        raise ValueError("incompatible matrixes!")
    C: Matrix = [[None]*len(B[0]) for i in range(A)]
    for i in range(len(A)):
        for j in range(len(B[0])):
            C[i][j] = 0
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C


def matrix_chain_order(p: List):
    """[summary]

    Parameters
    ----------
    p : List
        containing each matrix size 
    Returns
    -------
    [type]
        [description]
    """
    size = len(p)-1
    calc_cost = [[None]*size]*size
    split_points = []
    for i in range(size):
        calc_cost[i][i] = 0
    for length in range(2, n+1):
        for st in range(size-length+1):
            ed = st+length-1
            calc_cost[i][j] = math.inf
            for k in range(st, ed):
                current = calc_cost[st][k] + calc_cost[k+1][ed] +
                p[st]*p[k]*p[ed]

                if　current < calc_cost[st][ed]:
                    calc_cost[st][ed] = current
                    split_points[st][ed] = k
    return calc_cost, split_points


def matrix_chain_multiply(A: List[Matrix], split_points: Matrix, i: int, j: int)->Matrix:
    while True:
        if j == i+1:
            # TODO:rewrite below to matrix multiplication
            return matrix_multiply(A[i], A[j])

        else:
            split = split_points[i][j]
            first = matrix_chain_multiply(A, split_points, i, split)
            secont = matrix_chain_multiply(A, split_points, split+1, j)
            # TODO:rewrite below to matrix multiplication
            return matrix_multiply(first, second)
