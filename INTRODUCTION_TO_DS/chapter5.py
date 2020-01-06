from typing import List, Tuple
import heapq


def linear_search(array: List, target: int) -> bool:
    for ele in array:
        if ele == target:
            return True
    return False


class Node:
    """class for binary search tree"""

    def __init__(self, value):
        # int or float?
        self.value = value
        self.left: Node = None
        self.right: Node = None

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


def heap_sort(array: List) -> List:
    heap = []
    for v in array:
        heapq.heappush(heap, v)
    print(heap)
    print("########")
    return [heapq.heappop(heap)]


class HashTable:
    def __init__(self, table_size: int = 100):
        self.data: List[List] = [[] for _ in range(table_size)]
        self.n: int = table_size

    def get_hash(self, v) -> int:
        return hash(v) % self.n

    def search(self, key) -> Tuple:
        i: int = self.get_hash(key)
        for j, v in enumerate(self.data[i]):
            if v[0] == key:
                return(i, j)
        return (i, -1)

    def set(self, key, value) -> None:
        i, j = self.search(key)
        if j != -1:
            self.data[i][j][1] = value
        else:
            self.data[i].append([key, value])

    def get(self, key):
        i, j = self.search(key)
        if j != -1:
            return self.data[i][j][1]
        raise KeyError(f"{key} sas not found in this hash table")


if __name__ == "__main__":
    import random
    test = [random.randint(0, 100) for i in range(15)]
    heap_sort(test)
    my_hash_table = HashTable()
    my_hash_table.set("taro", 123123)
    
    