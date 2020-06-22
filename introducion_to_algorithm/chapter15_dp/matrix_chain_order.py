from typing import List
import math
#TODO;operation check

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
                current = calc_cost[st][k] + calc_cost[k+1][ed] + p[st]*p[k]*p[ed]

                if　current < calc_cost[st][ed]:
                    calc_cost[st][ed] = current
                    split_points[st][ed] = k
    return calc_cost, split_points
