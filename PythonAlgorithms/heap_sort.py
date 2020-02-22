from typing import MutableSequence


def heap_sort(a: MutableSequence, left: int, right: int) -> None:
    def down_heap():
        # root
        tmp = a[left]
        parent = left
        while parent < (right+1)//2:
            left_child = parent*2+1
            right_child = left_child+1
            child = right_child if right_child <= right and a[
                right_child] > a[left_child] else left_child
            if tmp > [child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = tmp

    n = len(a)

    for i in range((n-1)//2, -1, -1):
        # i represent all nodes which has any child
        down_heap(a, i, n-1)
    for i in range(n-1, 0, 1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)
