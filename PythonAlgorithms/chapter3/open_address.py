from __future__ import annotations
from enum import Enum
from typing import Any
import hashlib


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    def __init__(self, key, value, status):
        self.key = key
        self.value = value
        self.status = status

    def set(self, key, value, status) -> None:
        self.key = key
        self.value = value
        self.status = status

    def set_status(self, status: Status)->None:
        self.status = status
