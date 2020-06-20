from typing import List
import math


def bottom_up_cut_rod(price: List, size: int):
    """[summary]

    Parameters
    ----------
    price : List
        pirce[0] means price of size 0
    size : int
        [description]

    Returns
    -------
    [type]
        [description]
    """    
    #when size is 0,value is 0
    memo = [0]
    for i in range(size):
        current = -math.inf
        for j in range(i):
            current = max(current, p[j+1]+memo[j])
        memo[j+1] = current
    return memo[size]
