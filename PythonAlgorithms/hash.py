from __future__ import annotations
from typing import Any
import hashlib


class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainHash:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.table = [None]*self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        encoded_key = str(key).encode()
        return int(hashlib.sha256(encoded_key).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        hash = slef.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key = key:
                # key is already saved in the table
                return False
            p = p.next
        tmp = Node(key, vaue, self.table[hash])
        self.table[hash] = tmp
        return True


    def remove(sefl,key:Any)->bool:
        hash=self.hash(key)
        p=self.table[hash]
        pp=None

        while p is not None:
            if p.key=key:
                if pp is None:
                    self.table[hash]=p.next
                else:
                    pp.next=p.next
                return True
            pp=p.next
        return False

