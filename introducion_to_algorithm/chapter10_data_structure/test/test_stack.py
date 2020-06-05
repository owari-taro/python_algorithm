import pytest
from ..stack import Stack, Queue


@pytest.mark.skip
class TestStack:
    def setup_method(self, method):
        print("setup:{}".format(self.__class__.__name__))
        self.size = 5
        self.stack: Stack = Stack(self.size)
        self.input_list = [3, 2, 4, 1, 2]

    def test_normal(self):
        """test by normal usage"""
        assert self.stack.is_empty() == True

        for ele in self.input_list:
            self.stack.push(ele)
        assert self.stack.is_full() == True
        for i in range(self.size-1, -1, -1):
            print(i)
            assert self.stack.pop() == self.input_list[i]

    def test_exception(self):
        with pytest.raises(Stack.Empty):
            self.stack.pop()
        with pytest.raises(Stack.Full):
            for _ in range(self.size+1):
                self.stack.push(1)


class TestQueue:
    def setup_method(self, method):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print("setup:{}".format(self.__class__.__name__))
        self.size = 5
        self.queue = Queue(self.size)
        self.input_list = [3, 2, 4, 1, 2]

    def test_normal(self):
        assert self.queue.is_empty() == True
        for ele in self.input_list:
            self.queue.enque(ele)
        assert self.queue.is_full() == True
        for ele in self.input_list:
            assert self.queue.deque() == ele
