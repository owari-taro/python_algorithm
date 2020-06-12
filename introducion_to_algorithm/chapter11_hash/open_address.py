from __future__ import annotations
import attr
from typing import List, Callable, Any
from enum import Enum


class Status(Enum):
    DELETED = 0


@attr.s
class Node:
    key: int
    value: Any


@attr.s
class OpeneAdress:
    size: int = attr.ib()
    hash_func: Callable = attr.ib()
    table: List[Node] = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.table = [None]*self.size

    def insert(self, node: Node) -> int:
        i = 0
        while i < self.size:
            j = self.hash_func(node.value, i)
            if self.table[j] == None or self.table[j] == Status.DELETED:
                self.table[j] = node
                return j
            i += 1
        raise OverflowError("no space left for a new node")

    def hash_search(self, key: int) -> int:
        i = 0
        while i < self.size:
            j = self.hash_func(key, i)
            if self.table[j]:
                return j
            if self.table[j] == Status.DELETED
            continue
            if self.table[j] is None:
                break
            i += 1
        return None

    def delete(self, key):
        key = self.hash_search(key)
        if key:
            self.table[key] = Status.DELETED
            return True
        return None
