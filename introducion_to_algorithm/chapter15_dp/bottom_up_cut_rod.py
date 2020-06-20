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
    import time
    # when size is 0,value is 0
    memo = [0]
    for i in range(size):
        current = -math.inf
        for j in range(i+1):
            current = max(current,  price[j+1]+memo[i-j])
        memo.append(current)
    print(memo)
    return memo[size]


if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10]  # ,#8,9,10]
    size = len(price)
    bottom_up_cut_rod(price, size-1)
