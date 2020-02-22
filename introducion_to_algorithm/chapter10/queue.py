from typing import Any


class Queue:
    class Empty(Exception):
        pass

    class OverFlow(Exception):
        pass

    def __init__(self, size_limit: int):
        self.size_limit = size_limit
        self.queue = [None]*self.size_limit
        self.head = 0
        self.tail = 0
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.count >= self.size_limit:
            return True
        else:
            return False

    def deqeue(self) -> Any:
        if self.is_empty():
            return Queue.Empty
        output = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        self.count -= 1
        if self.head == self.size_limit:
            self.head = 0
        return output

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise Queue.OverFlow()
        self.queue[self.tail] = value
        self.count += 1
        self.tail += 1
        if self.tail == self.size_limit:
            self.tail = 0

    def __eq__(self, other):
        return self.count == other.count and self.queue == other.queue


class Stack:
    """stack made from queue"""
    # TODO:test

    def __init__(self, size_limit: int):
        self.queue_push = Queue(size_limit)
        self.queue_pop = Queue(size_limit)

    def push(self, value: Any):
        if self.queue_push.is_full():
            return Queue.OverFlow
        else:
            self.queue_push.enqueue(value)

    def pop(self):
        if self.queue_push.count > 0:
            self.exchange()
            value = self.queue_pop.deqeue()
            self.queue_pop, self.queue_push = self.queue_push, self.queue_pop
            return value
        else:
            return None

    def exchange(self):
        while self.queue_push.count > 0:
            self.queue_pop.enqueue(self.queue_push.deqeue())

    def print_elements(self):
        print(self.queue_push.queue)


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(3)
    stack.push(3)
    stack.print_elements()
    print(stack.pop())
    stack.print_elements()
