from typing import Any
from enum import Enum


class Mode(Enum):
    RIGHT = 0
    LEFT = 1


class DoubleStack:
    """# problems10.1-2 written in introducion to algorithm """

    class Empty(Exception):
        pass

    class OverFlow(Exception):
        pass

    def __init__(self, size_limit: int):
        """contain two stack in one list"""
        self.size_limit = size_limit
        self.stack = [None]*self.size_limit
        self.head_left = 0
        self.head_right = size_limit-1
        self.count_right = 0
        self.count_left = 0

    def is_empty(self, mode=None):

        if mode is None and (self.count_right+self.count_left == 0):
            # count entire list used by both stack
            return True
        elif mode == Mode.RIGHT and self.count_right == 0:
            return True
        elif mode == Mode.LEFT and self.count_left == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.count_right+self.count_left >= self.size_limit:
            return True
        else:
            return False

    def push(self, value: Any, mode: Mode) -> None:
        if self.is_full():
            raise DoubleStack.OverFlow()
        if mode == Mode.RIGHT:
            self.stack[self.head_right] = value
            self.count_right += 1
            self.head_right -= 1
        else:
            self.stack[self.head_left] = value
            self.count_left += 1
            self.head_left += 1

    def pop(self, mode: Mode) -> Any:
        if self.is_empty(mode):
            raise DoubleStack.Empty()
        if mode == Mode.RIGHT:
            self.head_right += 1
            out = self.stack[self.head_right]
            self.count_right -= 1
            return out
        else:
            self.head_left -= 1
            self.count_left -= 1
            return self.stack[self.head_left]


if __name__=="__main__":
