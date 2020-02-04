from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        self.key = key
        self.value = value
        self.right = right


class BinarySearchTree:

    def __init__(self):
        #
        self.root = None

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
