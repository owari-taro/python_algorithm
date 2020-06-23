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
    # when size is 0,value is 0
    memo = [0]
    for length in range(1, size+1):
        current = -math.inf
        for cut_point in range(length+1):
            current = max(current,  price[cut_point]+memo[length-cut_point])
        memo.append(current)
    print(memo)
    return memo[size]


def bottom_up_cut_rod_with_cost(price: List, size: int, cost: int):
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
    # when size is 0,value is 0
    memo = [0]
    for length in range(1, size+1):
        current = -math.inf
        for cut_point in range(1,length+1)
           if length == cut_point:
                current = max(
                    current,  price[cut_point]+memo[0])
            else:
                current = max(
                    current,  price[cut_point]+memo[length-cut_point]-cost)

        memo.append(current)
    print(memo)
    return memo[size]


if __name__ == "__main__":
    price = [0, 1, 5, 8, 9, 10]  # ,#8,9,10]
    size = len(price)
    bottom_up_cut_rod(price, size-1)
