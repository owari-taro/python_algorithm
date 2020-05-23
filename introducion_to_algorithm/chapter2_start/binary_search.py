from typing import List


def binary_serach(sorted_list: List, target: float):
    st, ed = 0, len(sorted_list)
    middle = len(sorted_list)//2
    while st <= ed:
        middle = (st+ed)//2
        if sorted_list[middle] == target:
            return middle
        if sorted_list[middle] < target:
            st = middle-1
        if sorted_list[middle] > target:
            ed = middle-1

    return None
