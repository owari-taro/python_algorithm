from __future__ import annotations
from typing import Any, List

from dataclasses import dataclass


@dataclass
class Node:
    key: Any
    left: Node
    right: Node
    value: Any = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def search(self, key: Any):
        node = self.root
        while True:
            if node is None:
                return None
            elif node.key == key:
                return node.value
            elif node.key < key:
                node = node.right

            else:
                node = node.right

    def add(self, key: Any, value: Any) -> bool:
        def add_node(node: Node, key: Any, value: Any):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    add_node(node.right, key, value)
            return True
            
        if self.root is None:
            self.root = Node(key, value)
            return True
        else:
            return add_node(self.root, key, value)
