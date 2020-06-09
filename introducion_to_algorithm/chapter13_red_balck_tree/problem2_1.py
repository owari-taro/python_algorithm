import attr
from typing import Any


@attr.s
class Node:
    key: Any = attr.ib()
    right: Node = attr.ib(default=None)
    left: Node = attr.ib(default=None)
    parent: Node = attr.ib(default=None)


@attr.s
class Tree:
    head: Node = attr.ib()

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
