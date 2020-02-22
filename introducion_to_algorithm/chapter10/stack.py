from typing import Any


class Stack:
    class UnderFlow(Exception):
        pass

    class OverFlow(Exception):
        pass

    def __init__(self, size_limit):
        self.size_limit = size_limit
        self.stack = [None]*size_limit
        self.head = 0
        # countting how many elmeents exist in stack
        # count field make is_full,is_empty much simpler
        self.count = 0

    def is_full(self) -> bool:
        if self.count >= self.size_limit:
            return True
        else:
            return False

    def push(self, x: Any) -> None:
        if self.is_full():
            raise Stack.OverFlow
        self.stack[self.head] = x
        self.head += 1
        self.count += 1

    def is_empty(self) -> None:
        if self.count == 0:
            return True
        else:
            return False

    def pop(self) -> Any:
        if self.is_empty():
            raise Stack.UnderFlow
        else:
            self.head -= 1
            self.count -= 1
            return self.stack[self.head]


class Queue:
    """queue made from two stacks"""

    def __init__(self, size_limit: int):
        self.stack_first = Stack(size_limit)
        self.stack_second = Stack(size_limit)
        self.size_limit = size_limit

    def push(self, x: Any) -> None:
        if not self.stack_first.is_full():
            self.stack_first.push(x)
        else:
            return self.stack_first.OverFlow

    def pop(self):
        if self.stack_first.is_empty():
            return None
        else:
            while self.stack_first.count > 0:
                self.exchange(self.stack_first, self.stack_second)
            out = self.stack_second.pop()
            # restore the rest of elements
            self.exchange(self.stack_first, self.stack_first)
            return out

    def exchange(self, stack1, stack2):
        """exchange contents between two stacks"""
        while stack1.count > 0:
            tmp = stack1.pop()
            stack2.push(tmp)
