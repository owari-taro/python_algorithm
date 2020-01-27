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
