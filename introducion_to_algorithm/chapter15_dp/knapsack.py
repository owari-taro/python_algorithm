import attr
from typing import List


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
