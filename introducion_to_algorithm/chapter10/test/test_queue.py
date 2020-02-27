import pytest
from ..queue import Queue, Stack


class TestQueue:

    def test_queue(self):
        size = 5
        queue = Queue(size)
        assert queue.is_empty() == True
        queue.enqueue(10)
        queue.enqueue(3)
        assert queue.deqeue() == 10
        assert queue.count == 1

    def test_exception(self):
        size = 5
        queue = Queue(size)
        with pytest.raises(Queue.Empty):
            queue.deqeue()

        with pytest.raises(Queue.OverFlow):
            for _ in range(size+1):
                queue.enqueue(3)


class Stack:

    def test_stack(self):
        size = 5
        stack = Stack(5)
        input_list = [3, 2, 4, 1, 2]
        for ele in input_list:
            stack.push(ele)
        print(stack.queue_push.queue)
        for i in range(4, -1, -1):
            print(i)
            print(stack.queue_push.queue)
            assert stack.pop() == input_list[i]
