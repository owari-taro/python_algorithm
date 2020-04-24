from typing import Any


class Stack:
    class Empty(Exception):
        pass

    class Full(Exception):
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
            raise Stack.Full
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
            raise Stack.Empty
        else:
            self.head -= 1
            self.count -= 1
            return self.stack[self.head]


class Queue:
    """queue made from two stacks"""
    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self, size_limit: int):
        self.stack_enque = Stack(size_limit)
        self.stack_deque = Stack(size_limit)
        self.size_limit = size_limit

    def is_full(self):
        return self.stack_enque.is_full()

    def is_empty(self):
        return self.stack_enque.is_empty()

    def enque(self, x: Any) -> None:
        if not self.is_full():
            self.stack_enque.push(x)
        else:
            raise Stack.Full
           # return self.stack_first.OverFlow

    def deque(self):
        if self.stack_enque.is_empty():
            print("cannot deque from empty queue")
            raise Queue.Empty
        else:
            self.exchange(self.stack_enque, self.stack_deque)
            out = self.stack_deque.pop()
            # restore the rest of elements
            self.exchange(self.stack_deque, self.stack_enque)
            return out

    def exchange(self, stack1, stack2):
        """exchange contents between two stacks"""
        while not stack1.is_empty():
            tmp = stack1.pop()
            stack2.push(tmp)


if __name__ == "__main__":
    queue = Queue(5)
    queue.enque(3)
    queue.enque(2)
    queue.enque(1)
    for i in range(3):
        print(queue.deque())
