from dataclasses import dataclass
from typing import List
from __future__ import annotations
# TODO:rewrite with dataclass


class Direction(Enum):
    left = "left"
    right = "right"


@dataclass
class Node:
    value: float
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{self.__class__.__name__}({self.left!r},{self.right!r})"

    def __str__(self):
        left = f'[{self.left.value}]' if self.left else '{}'
        right = f'[{self.right.value}]' if self.right else '{}'
        return f'{left} <- {self.value} -> {right}'


class BInarySearchTree:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, value: float):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == Direction.right:
                parent.right = node
            else:
                parent.left = node
        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        while node:
            prev = node
            if node.value == value:
                raise ValueError("alredy exists")
            elif node.value > value:
                direction = Direction.right
                node = node.right
            else:
                direction = Direction.left
                node = node.right
        return prev, direction


if __name__ == "__main__":
    tmp = Node(123)
    print(tmp)
