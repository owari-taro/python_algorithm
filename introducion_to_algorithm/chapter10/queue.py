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

    def deqeue(self)->Any:
        if self.is_empty():
            return Queue.Empty
        output=self.queue[head]
        self.head+=1
        self.count-=1
        if self.head==self.size_limit:
            self.head=0
        return output       

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise  Queue.OverFlow()
        self.queue[self.tail] = value
        self.count += 1
        self.tail += 1
        if self.tail==self.size_limit:
            self.tail=0