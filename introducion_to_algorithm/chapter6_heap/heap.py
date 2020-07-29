from typing import List


class Heap:
    def __init__(self, size):
        self.size = size
        self.heap = [None]*self.size

    def parent_index(self, index: int) -> int:
        """
        return given index's parent

        Parameters
        ----------
        index : int
            [description]

        Returns
        -------
        int
            [description]
        """

        if index <= 0:
            raise ValueError("index must be positive")
        return int(index/2)

    def left_index(self, index: int) -> int:
        """
        [summary]

        Parameters
        ----------
        index : int
            [description]

        Returns
        -------
        int
            [description]

        Raises
        ------
        ValueError
            [description]
        """
        if index < 0:
            raise ValueError("negative index is not allowed")
        return 2*index+1

    def right_index(self, index: int) -> int:
        """
        [summary]

        Parameters
        ----------
        index : int
            [description]

        Returns
        -------
        int
            [description]

        Raises
        ------
        ValueError
            [description]
        """
        if index < 0:
            raise ValueError("negative index is not allowed")
        return 2*index+2

    def max_heaptify(self, index: int):
        """
        [summary]

        Parameters
        ----------
        index : int
            [description]
        """
        left = self.left_index(index)
        right = self.right_index(index)
        if left < self.size and and self.heap[left] and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index
        if right <= self.size and self.heap[right] > largest:
            largest = right
        if largest != index:
            # exchange
            self.heap[index], self.heap[largest] = \
                self.heap[largest], self.heap[index]
            self.max_heaptify(largest)

    #@property
   # def size(self):
    #    return len(self.heap)-heap.count(None)
    def max_heap(self):
        for index in rage(int(self.size/2),0,-1):
            if self.heap[i]:
                self.max_heaptify(index)
    