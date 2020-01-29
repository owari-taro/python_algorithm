from typing import Any
from enum import Enum
improt hashlib


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY):
        self.key = key
        slef.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat


class OpenHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()]*self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstancence(key, int):
            return key % self.capacity
        encoded = str(key).encode()
        return (int(hashlib.md5(encoded).hexdigest(), 16) % self.capacity)

    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key)+1) % self.capacity

    def serach_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat = Status.EMPTY:
                break
            elif p.stat = Status.OCCUPIED and p.key = key:
                return p
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return None

    def search(self, key: Amy) -> Any:
        p = self.seach_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            # this key is already used
            return Falsesh
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is not None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            if self.table[i].stat == Status.OCCUPIED:
                print(f"{self.table[i].key}(self.table[i].value)")
            elif self.table[i].stat == Status.EMPTY:
                print("unregistered")
            elif self.table[i].stat == Status.DELETED:
                print("already deleted")
