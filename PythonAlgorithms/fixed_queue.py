from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None]*capacity

    def __len__(self) -> int:
        return self.no

    def is_empty(self)->bool:
        return self.no<=0