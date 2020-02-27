import pytest
from ..stack import Stack, Queue


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

    # def test_exception(self):
   #     size= 5
  #      queue= Queue(size)
 #       with pytest.raises(Queue.Empty):
#            queue.deqeue()

        # with pytest.raises(Queue.OverFlow):
            # for _ in range(size+1):
              #  queue.enqueue(3)


# class TestStack:
 #   def setup_method(self, method):
  #      print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
   #     print("setup:{}")
    #    self.size = 5
    #    self.stack: Stack = Stack(self.size)
    #    self.input_list = [3, 2, 4, 1, 2]

    # def teardown_method(self, method):
     #   print("finish############################################################")

    # def test_stack(self):

        # for ele in self.input_list:
        #    self.stack.push(ele)
       # print(self.stack.queue_push.queue)
       # for i in range(self.size-1, -1, -1):
       #     print(i)
      #      print(self.stack.queue_push.queue)
     #       assert self.stack.pop() == self.input_list[i]

    # def test_exception(self):
        # emtpy
     #   print(self.stack.print_elements)
    #    with pytest.raises(Stack.Empty):
   #         self.stack.pop()
  #      with pytest.raises(Stack.Full):
 #           for i in range(100):
#                self.stack.push(i)
