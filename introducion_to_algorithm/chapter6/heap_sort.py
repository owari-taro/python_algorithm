from typing import Any


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


def left(i: int):
    return 2*i


def right(i: int):
    return 2*i+1


def parent(i: int):
    return int(i/2)


class Heap:
    def __init__(self, heap_size):
        self.data = []
        self.heap_size = heap_size


def max_heaptify(heap: Heap, i):
    #root is largest
    l = left(i)
    r = right(i)
    if l < heap.heap_size and heap.data[l] > heap.data[i]:
        largest = l
    else:
        largest = i
    if r <= heap.heap_size and heap.data[r] > heap[largest]:
        largest = r
    if largest != i:
        max_heaptify(heap, largest)
