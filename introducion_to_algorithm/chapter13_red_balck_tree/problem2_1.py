import attr
from typing import Any
from enum import Enum


class Color(Enum):
    """
    each node color

    Args:
        Enum ([type]): [description]
    """
    BLACK = 0
    RED = 1


@attr.s
class Node:
    key: Any = attr.ib()
    color: Color = attr.ib()
    right: Node = attr.ib(default=None)
    left: Node = attr.ib(default=None)
    parent: Node = attr.ib(default=None)


@attr.s
class Tree:
    head: Node = attr.ib()

    def left_rotate():
        NotImplemented

    def right_rotate(self, partial_tree_root Node) -> None:

        if partial_tree_root.right is None:
            raise ValueError("right child must not be None")
        child = partial_tree_root.right
        partial_tree_root.left = child.right
        if child.right:
            child.right.parent = partial_tree_root
        if partial_tree_root.parent is None:
            self.head = self.child
            child.parent = None
        elif partial_tree_root == partial_tree_root.parent.left:
            partial_tree_root.parent.left = child
        else:
            partial_tree_root.parent.right = child
        child.parent = partial_tree_root.parent
        child.right = partial_tree_root
        partial_tree_root.parent = child

    def rb_insert(self, new_node: Node) -> None:
        current = self.head
        parent = None
        while current is None:
            parent = current
            if new_node.key < current.key:
                left = True
                current = current.left
            else:
                left = False
                current = current.right
            new_node.parent = parent
            if parent is None:
                self.head = new_node
            elif left:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.right = None
            new_node.left = None
            new_node.color = Color.RED
            # rb_insertFIXUP
            NotImplementedError

    def rb_insert_fixup(self, new_node: Node):
        current = new_node
        while current.parent.color == Color.RED:
            # parent is left child
            if current.parnet = current.parent.parent.left:
                uncle = current.parent.parent.right
                if uncle.color == Color.RED:
                    current.parnet.color = Color.BLACK
                    uncle.color = Color.BLACK
                    current.parent.parent.color = Color.RED
                    current = current.parent.parent
                else:
                    if current == current.parent.right:
                        current = current.parent
                        NotImplemented
