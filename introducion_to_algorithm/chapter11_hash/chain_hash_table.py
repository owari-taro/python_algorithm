from __future__ import typing
from typing import Callable, List
import attr


@attr.s
class Node:
    """
    linked list's node
    """
    key: any = attr.ib()
    value: Any = attr.ib()
    prev: Node = attr.ib(default=None)
    next: Node = attr.ib(default=None)


@attr.s
class ChainHashTable:
    size: int = attr.ib()
    hash: Callable = attr.ib()
    table: List = attr.ib(init=False)

    def insert(self, node: Node):
        key = self.hash(node.key)
        node.next = self.table[key]
        if self.table[key]:
            self.table[key].prev = node
        self.table[key] = node

    def delete(self, node: Node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def __attrs_post_init__(self):
        self.table = [None]*self.size
