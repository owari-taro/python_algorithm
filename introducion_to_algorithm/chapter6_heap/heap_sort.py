from typing import Any, List


class Node:
    def __init__(self, value: Any, index: int):
        self.index = index
        self.value = value

    def parent(self):
        return int(self.index/2)

    def left(self):
        return 2*self.index

    def right(self):
        return 2*self.index+1


def left(i: int) -> int:
    """
    return left child's index

    Parameters
    ----------
    i : int
        [description]

    Returns
    -------
    int
        [description]
    """
    return 2*i


def right(i: int) -> int:
    """
    return right child's index
    Parameters
    ----------
    i : int
        [description]

    Returns
    -------
    int
        [description]
    """
    return 2*i+1


def parent(i: int):
    return int(i/2)


class Heap:
    def __init__(self):
        self.data = []
        # self.size = len(self.data)while expression:

    def size(self) -> int:
        """
        return length of data

        Returns
        -------
        int
            [description]
        """
        return len(self.data)


def min_heaptify():
    NotImplemented


def max_heaptify(heap: Heap, i: int) -> None:
    l = left(i)
    r = right(i)
    largest = i
    if l < heap.size() and heap.data[l] > heap.data[i]:
        largest = l
    elif r < heap.size() and heap.data[r] > heap.data[i]:
        largest = r
    if largest != i:
        heap.data[i], heap.data[largest] = heap.data[largest], heap.data[i]
        max_heaptify(heap, largest)


def min_heaptify(heap: Heap, i: int) -> None:
    l = left(i)
    r = right(i)
    smallest = i
    if l < heap.siz() and heap.data[l] < heap.data[i]:
        smallest = l
    elif r < heap.size() and heap.data[r] < heap.data[i]:
        smallest = r
    if smallest != i:
        heap.data[i], heap.data[smallest] = heap.data[smallest], heap.data[i]
        min_heaptify(heap, smallest)


def build_max_heap(heap: Heap) -> None:
    
    size = heap.size()
    #start with the parent having the largest index
    for i in range(int(size/2), 1, -1):
        max_heaptify(heap, i)


