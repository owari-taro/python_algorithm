from __future__ import annotations
from enum import Enum
from typing import Any
import hashlib
from dataclasses import dataclass


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


@dataclass
class Bucket:
    key: Any
    value: Any
    status: Status = Status.EMPTY

    def set(self, key, value, status) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status) -> None:
        self.status = status


class OpenHash:
    def __init__(self, capacity: int):
        self.capcity = capacity
        self.table = [Bucket()]*self.capacity

    def hash_value(self, key: Any):
        if isinstance(key, int):
            return key % self.capcity
        else:
            hash_ = hashlib.sha256(str(key).encode("utf-8"))
            hex_ = int(hash_, 16)
            return hex_ % self.capacity

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key)+1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """
        return value if exist

        Parameters
        ----------
        key : Any
            [description]

        Returns
        -------
        Any
            [description]
        """
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any):
        if self.search(key)is not None:
            return False
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> bool:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
