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


class TestStack:
    def setup_method(self, method):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print("setup:{}")
        self.size = 5
        self.stack: Stack = Stack(self.size)
        self.input_list = [3, 2, 4, 1, 2]

    def teardown_method(self, method):
        print("finish############################################################")

    def test_stack(self):

        for ele in self.input_list:
            self.stack.push(ele)
        print(self.stack.queue_push.queue)
        for i in range(self.size-1, -1, -1):
            print(i)
            print(self.stack.queue_push.queue)
            assert self.stack.pop() == self.input_list[i]

    def test_exception(self):
        # emtpy
        print(self.stack.print_elements)
        with pytest.raises(Stack.Empty):
            self.stack.pop()
        with pytest.raises(Stack.Full):
            for i in range(100):
                self.stack.push(i)
.