import attr
from typing import List
from __future__ import annotations


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
