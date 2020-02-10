from typing import Any


class Node:
    def __init__(self, key: str, value: Any) -> None:
        self.key = key
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key: str, value: Any) -> None:
        if self.root is None:
            self.root = Node(key, value)
        else:
            print()