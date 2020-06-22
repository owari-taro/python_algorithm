from typing import List
import math


def memoirzed_cut_rod(price: List, size: int):
    memo = []
    for i in range(size):
        memo.append(-math.inf)
    return memorized_cut_rod_aux(price,size,memo)

def memorized_cut_rod_aux():
    NotImplemented


+
