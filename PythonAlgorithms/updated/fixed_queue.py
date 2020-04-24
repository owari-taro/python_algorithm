from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, size):
        # number of emenet in queue
        self.count = 0
        self.front = 0
        self.rear = 0
        self.size = size
        self.que = [None]*self.size
        # used for iterator
        self.__iter_count = 0

    def __len__(self):
        return self.count

    def is_empty(self) -> bool:
        return self.count <= 0

    def is_full(self) -> bool:
        return self.count == self.size

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.count = 0
        if self.rear == self.size:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        res = self.que[self.front]
        self.front += 1
        self.count -= 1
        if self.front == self.size:
            self.front = 0
        return res

    def __iter__(self):
        return self
        # return iter(self.que)

    def __next__(self):
        pass
