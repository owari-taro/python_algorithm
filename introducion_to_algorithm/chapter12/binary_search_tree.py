from typing import Any


class Node:
    def __init__(self, key: str, value: Any) -> None:
        self.key = key
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key: str, value: Any) -> bool:
        node = Node(Key, value)
        if self.root is None:
            self.root = node
            return True

        tmp = self.root
        #if  tmp is prev's left child ,then True
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
        def print_helper(node:Node):
            if node is not None:
                print_helper(node.left)
                print(f'{node.key}:{node.value} ')
                print_helper(node.right)    
        print_helper(self.root)    

            