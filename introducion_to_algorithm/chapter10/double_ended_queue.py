from tynping import Any


class DoubleEndedQueue:
    class Empty(Exception):
        pass

    def __init__(self, size_limit: int):
        self.queue = [None]*size_limit
        self.head_left = self.tail_left = 0
        self.head_right = self.tail_right = size_limit-1
        self.count = 0
        self.size_limit = size_limit

    def is_full(self) -> bool:
        if self.count == self.size_limit:
            return True
        else:
            return False

    def enque_left(self, value: Any) -> None:
        # if self.tail_left<=self.tail_right:
        self.queue[self.tail_left] = value
        self.count += 1
        self.tail_left += 1

    def deque_right(self, value: Any) -> None:
        self.queue[self.tail_left] = value
        self.count += 1
        self.tail_right -= 1

    def deque_left(self):
        if self.head_left == self.tail_left:
            raise DoubleEndedQueue.Empty()
        out = self.queue[self.head_left]
        self.head_left += 1
        self.count -= 1
        return out

    def deque_right(self):
        if self.head_right == self.tail_left:
            raise DoubleEndedQueue.Empty()
        out = self.queue[self.head_right]
        self.head_right -= 1
        self.count -= 1
        return out
