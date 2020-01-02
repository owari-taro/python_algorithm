from typing import List


def linear_search(array: List, target: int) -> bool:
    for ele in array:
        if ele == target:
            return True
    return False


class Node:
    """class for binary search tree"""

    def __init__(self, value):
        self.value = value
        self.left:Node = None
        self.right:Node = None

    def __str__(self):
        left = f"[{self.left.value}]" if self.left else "[]"
        right = f"[{self.right.value}]" if self.right else "[]"
        return f"{left}<-{self.value}->{right}"


class BinarySearchTree:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, value):
        node = Node(value)
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == "left":
                parent.left = node
            else:
                parent.right = node
        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        while node:
            p = node
            if p.value == value:
                raise ValueError(f"{p.value} is already saved value!")
            if p.vlaue > value:
                direction = "left"
                node = p.left
            else:
                direction = "right"
                node = p.right
        return p, direction


