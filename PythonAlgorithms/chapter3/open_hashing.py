from __future__ import annotations
from typing import List, Any
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: Node):
        self.key = key
        self.value = value
        next = next


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table: List[Node] = [None]*self.capacity

    def hash_value(self, key: Any) -> int:
        """
        create hash value for key

        Parameters
        ----------
        key : Any
            [description]

        Returns
        -------
        int
            [description]
        """
        if isinstance(key, int):
            return key % self.capacity
        hex_ = hashlib.sha256(str(key).encode("utf-8")).hexdigest()
        return int(hex_, 16) % self.capacity

    def search(self, key: Any):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
        return None

    def add(self, key: Any, value: Any):
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.value == value:
                return False
            p = p.next
        tmp = Node(key, value, self.table[hash])
        self.table[hash] = tmp
        return True

    def remove(self, key: Any) -> bool:
        """
        reomve the first bucket from the table elment with key's hash

        Parameters
        ----------
        key : Any
            [description]

        Returns
        -------
        bool
            [description]
        """
        hash = self.hash_value(key)
        current = self.table[hash]
        prev = None
        while current is not None:
            if current.key = key:
                if prev is None:
                    self.table[hash] = p.next
                else:
                    prev.next = current.next
                return True
            prev = current
            current = current.next

        return None

    def dump(self) -> None:
        """
        print table content

        """
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f"→ {p.key}:{key.value}", end="")
                p = p.next
            print()
