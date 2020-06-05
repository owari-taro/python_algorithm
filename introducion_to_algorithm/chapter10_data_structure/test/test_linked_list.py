import pytest
from ..linked_list import LinkedList, Node


class TestLinkedList:
    def setup_method(self, method):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print("setup:{}".format(LinkedList.__class__.__name__))
        head = Node(3)
        self.linked_list = LinkedList(head)

    def test_eq(self):
        """test __eq__ method"""
        # list has only head
        other = LinkedList(Node(3))
        assert self.linked_list == other
        # 2 elements
        self.linked_list.add(5)
        other.add(5)
        assert self.linked_list == other
        #not equal
        self.linked_list.add(4)
        assert self.linked_list != other
