from dataclasses import dataclass
from __future__ import annotations
from typing import Any


@dataclass
class Node:
    key: Any
    next: Node


class LinkedList:
    def __init__(self, node: Node):
        self.head = node
        self.tail = node

    def insert(self, node: Node):
        node.next = self.head
        self.head = node
        self.tail.next = node

    def search(self, value: Any):
        node = self.head
        while node.key != value:
            node = node.next
            if node == self.tail:
                break
        return node
