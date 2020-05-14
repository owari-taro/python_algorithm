from dataclasses import dataclass
from typing import List

# TODO:rewrite with dataclass


class Node:
    def __init__(self, value, left: 'Node' = None, right: 'Node' = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        left = f'[{self.left.value}]' if self.left else '{}'
        right = f'[{self.right.value}]' if self.right else '{}'
        return f'{left} <- {self.value} -> {right}'


class BInarySearchTree:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, value):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            # TODO:rewrite with enum!!!!!!!
            if direction == "right":
                parent.right = node
            else:
                parent.left = node

        self.nodes.append(node)

    def find_parent(self, value):
        current = self.nodes
        while current:
            if current.value == value:
                raise ValueError()
            if curremt.value < value:
                prev = parent
                direction = "right"
                cufrent = parent.right
            else:
                prev = parent
                direction = "left"
                current = parent.left

        return prev, direction


if __name__ == "__main__":
    tmp = Node(123)
    print(tmp)
