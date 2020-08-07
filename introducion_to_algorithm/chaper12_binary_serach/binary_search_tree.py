from __future__ import annotations
from typing import Any
import attr


@attr.s
class Node:

    key: Any = attr.ib()
    value: Any = attr.ib()
    left: Node = attr.ib()
    right: Node = attr.ib()
    not_printed: bool = attr.ib()
    parent: Node = attr.ib()

    def __eq__(self, other):
        return self.key == other.key  # and self.value == other.value


def inorder_tree_walk(node: Node) -> None:
    # if none do  nothing
    if node:
        # prioritizing left node ,which is smaller than node.value
        inorder_tree_walk(node.left)
        print(node.key)
        inorder_tree_walk(node.right)


def tree_search(node: Node, key: Any) -> Node:
    if (node is None) or node.key == key:
        return node
    if node.key > key:
        return tree_search(x.left, key)
    else:
        return tree_search(node.right, key)


def iterative_tree_search(node: Node, key) -> Node:

    while node and node.key != key:
        if node.key < key:
            node = node.right
        else:
            node = node.left

    return node


def tree_mininum(node: Node) -> Node:
    """find minimum node

    Parameters
    ----------
    node : Node
        [description]

    Returns
    -------
    Node
        [description]
    """
    if not node:
        raise ValueError("node must notbe None")
    while node.left:
        node = node.left
    return node


def tree_maximum(node: Node) -> Node:
    """[summary]

    Parameters
    ----------
    node : Node
        [description]

    Returns
    -------
    Node
        [description]

    Raises
    ------
    ValueError
        [description]
    """
    if not node:
        raise ValueError("node must not be none")
    while node.right:
        node = node.right
    return node


def tree_successor(node: Node):
    if node.right:
        return tree_mininum(node.right)
    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = parent.parent
    return parent

    print("####")


@attr.s
class Tree:
    root: Node = attr.ib()

    def transplant(self, deleted_node: Node, moved_node: Node):
        """[summary]

        Parameters
        ----------
        deleted_node : Node
            [description]
        moved_node : Node
            [description]
        """
        if deleted_node.parent is None:
            self.root = moved_node
        elif deleted_node == deleted_node.parent.left:
            deleted_node.parent.left = moved_node
        else:
            deleted_node.parent.right = moved_node

    def delete(self, node: Node) -> Node:
        if node.left:
            NotImplemented

    def insert(self, new_node: Any) -> None:
        parent = None
        current = self.root
        if current is None:
            self.root = new_node
            return
        while current:
            prev = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = prev
        if prev.key < new_node.key:
            prev.right = new_node
        else:
            prev.left = new_node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key: str, value: Any) -> bool:
        node = Node(key, value)
        if self.root is None:
            self.root = node
            return True

        tmp = self.root
        # if  tmp is prev's left child ,then True
        left = None
        while tmp is None:
            prev = tmp
            if tmp.key == key:
                # key is alerady used
                print("key is already used")
                return False
            elif tmp.key > key:
                tmp = tmp.left
                left = True
            else:
                tmp = tmp.right
                left = False

        if left:
            prev.left = node

        else:
            prev.right = node
        return True

    def print_tree(self):
        def print_helper(node: Node):
            if node is not None:
                print_helper(node.left)
                print(f'{node.key}:{node.value} ')
                print_helper(node.right)
        print_helper(self.root)

    def seatch_min(self):
        tmp = self.root
        while tmp.left is not None:
            tmp = tmp.left
        return tmp

    def search_max(self):
        tmp = self.root
        while tmp.right is not None:
            tmp = tmp.right
        return tmp

    def search(self, key: Any) -> Node:
        """
        search node with key ,if nothing return None
        it takes O(log(h)) time
        Parameters
        ----------
        key : Any
            [description]

        Returns
        -------
        Node
            [description]
        """
        def search_helper(node: Node, key: str) -> Node:
            if node.key == key or node is None:
                return node
            if node.key < key:
                search_helper(node.right, key)
            else:
                search_helper(node.left, key)
        node = self.root
        return search_helper(node, key)

    def delete(self, key: str) -> bool:
        def transplant(root, u: Node, v: Node) -> None:
            if self.root == u:
                # root case
                self.root == v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v is not None:
                v.parent = u.parent

    def delete_tmp(self, key: str) -> bool:
        cur = self.root
        parent = None
        # find key
        while True:
            if current is None:
                return False
            if current.key == key:
                break
            elif key < parent.key:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right

        # check
        if current.left is None:
            if current == self.root:
                NotImplemented
