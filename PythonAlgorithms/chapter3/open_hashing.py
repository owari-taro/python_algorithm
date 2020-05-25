from __future__ import annotations
from typing import List, Any
import hashlib


class Node:
    def __init__(self, key: Any, value: Any, next: Node):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table: List[Node] = [None]*self.capacity

    def hash_value(self, key: Any):
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
