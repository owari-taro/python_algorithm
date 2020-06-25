import attr
from typing import List
from __future__ import annotations
import itertools


@attr.s
class Item:
    name = attr.ib()
    weight = attr.ib()
    price = attr.ib()


@attr.s
class Knapsack:
    size = attr.ib()
    weight = attr.ib(default=0)
    value = attr.ib(default=0)
    items: List = attr.ib(default=[])

    def append(self, item: Item) -> None:
        if not self.has_room_for(item):
            raise ValueError("theere isnt enough space for the item")
        self.items.append(item)
        self.weight += item.weight
        self.value += item.value

    def has_room_for(self, item):
        return self.size >= self.weight+item.weight

    @classmethod
    def greedy(cls, items: List[Item], size_limit: float) - >Knapsack:
        sorted_items: List[Item] = sorted(
            items, key=lambda: x.price/x.weight, reverse=True)
        knapsack = cls(size_limit)
        for item in sorted_items:
            try:
                knapsack.append(item)
            except ValueError:
                continue
        return knapsack

    @classmethod
    def brute_force(cls, items: List[Item], size_limit: int) -> Knapsack:
        max: Knapsack = None
        for pattern in itertools.product((0, 1), repeat=len(items)):
            tmp = cls(size_limit)
            try:
                for i, value in enumarate(pattern):
                    if value:
                        tmp.append(items[i])
                if max is None or max.value < tmp.value:
                    max = tmp

            except ValueError:
                continue
        return max
