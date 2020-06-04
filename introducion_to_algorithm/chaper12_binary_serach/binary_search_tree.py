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
    # parent: Node = attr.ib()

    def __eq__(self, other):
        return self.key == other.key  # and self.value == other.value


def inorder_tree_work(x: Node) -> None:
    if x:
        inorder_tree_work(x.left)
        print(x.key)
        inorder_tree_work(x.right)


def inorder_tree_work_non_recursive(node: Node) -> None:
    current = node
    stack = [current]
    while stack:
        if current.left and current.left.not_printed:
            current = current.left
            stack.append(current)
        else:
            if current.left is None:       
                current=curretnt.pop()
            print(current.key)
            current.is_printed = True
            if current.right:
                current = current.right
                stack.append(cunrrent)
            else:
                current=stack.pop()


def tree_search(x: Node, key) -> None:
    if (x is None) or x.key == key:
        return x
    if x.key > key:
        return tree_search(x.left, key)
    else:
        return tree_search(x.right, key)


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

    def search(self, k):
        def search_helper(node: Node, key: str) -> Node:
            if node.key == k or node is None:
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
        while True
           if current is None:
                return False
            if current.key ==key:
                break
            elif key <parent.key:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right

        # check
        if current.left is None:
            if current ==self.root:
                

