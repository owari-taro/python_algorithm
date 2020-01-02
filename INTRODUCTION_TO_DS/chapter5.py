from typing import List


def linear_search(array: List, target: int) -> bool:
    for ele in array:
        if ele == target:
            return True
    return False
