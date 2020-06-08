from __future__ import annotations
import attr
from typing import Any


@attr.s
class Node:
    key: Any = attr.ib()
    next: Node = attr.ib()
    #prev: Node = attr.ib()


class LinkedList:
    def __init__(self, node: Node):
        self.head = node

    def inverse(self):
        next = self.head.next
        self.head.next = None
        current = self.head
        while next:
            tmp = next.next
            next.next = current
            current = next
            next = tmp
        self.head = current
