# improve sort algorithm
from typing import List
import time
from collections import Callable
import random

def merge_arrays(left: List, right: List = []) -> List:
    """wargning:both arguments are  sorted in advance"""
    res: List = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res+left[i:]+right[j:]


def step(array: List[List]) -> List:
    res: List = []
    for i in range(0, len(array), 2):
        res.append(merge_arrays(*array[i:i+2]))


def merge_sort(array: List) -> List:
    res = [[v] for v in array]
    while len(res[0]) != len(array):
        res = step(res)
    return res[0]


def merge_sort2(array: List) -> List:
    if len(array) <= 1:
        return array
    mid_idx = len(array)//2
    left = array[:mid_idx]
    right = array[mid_idx:]
    return merge_arrays(merge_sort2(left), merge_sort2(right))


def quick_sort(array: List) -> List:
    if array == []:
        return array
    pivot = random.choice(array)#"""array[-1]
    left = []
    right = []
    pivots = []
    for v in array:
        if v < pivot:
            left.append(v)
        elif v == pivot:
            pivots.append(v)
        else:
            right.append(v)
    return quick_sort(left)+pivots+quick_sort(right)


def performance(method: Callable, data: List, num=3; int):
    s = time.time()
    for i in range(num):
        for v in data:
            method(v)
    e = time.time()
    return e-s


if __name__ == "__main__":
    print("test")
