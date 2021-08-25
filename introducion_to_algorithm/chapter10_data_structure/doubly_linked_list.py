from __future__ import annotations
import attr
from typing import Any



@attr.s
class Node:
    key: Any = attr.ib()
    next: Node = attr.ib()
    prev: Node = attr.ib()


class DoublyLinkedList:
    def __init__(self, head):
        self.head: Node = head

    def insert(self, node: Node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev:
            node.prev = node.next
        else:
            self.head = node
        if node.next:
            node.next.prev = node.pre

    def search(self, key: Any):
        """[summary]

        Parameters
        ----------
        key : Any
            [description]

        Returns
        -------
        [type]
            [description]
        """

        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return current



def funcname(self, parameter_list):
    pass