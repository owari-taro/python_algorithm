from binary_search_tree import Node
from typing import Any
import attr


@attr.s
class Tree:
    root: Node = attr.ib()

    def insert(self, new_node: Any, current: Node, parent: Node = None) -> None:
        if self.root is None:
            self.root = new_node
            return
        parent = current
        if current.key < new_node.key:
            current = current.right
        else:
            current = current.left
        if current:
            # recursive
            self.insert(new_node, current, parent)
        else:
            if parent.key < new_node.key:
                parent.right = new_node
            else:
                parent.left = new_node
