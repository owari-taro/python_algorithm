from typing import Any


class Node:
    def __init__(self, key: str, value: Any) -> None:
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


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
                
