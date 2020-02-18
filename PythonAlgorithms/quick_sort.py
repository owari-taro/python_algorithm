from typing import MutableSequence


def partition(input_list: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n-1
    x = a[n//2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
