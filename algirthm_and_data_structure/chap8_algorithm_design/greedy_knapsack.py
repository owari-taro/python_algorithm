import attr
from typing import List


@attr.s
class Item:
    value: float = attr.ib()
    weight: float = attr.ib()
    value_per_weight: float = attr.ib()

    def __attrs_post_init__(self):
        self.value_per_weight = self.value/self.weight


@attr.s
class GreedyKnapsack:
    items: List[Item] = attr.ib()
    weight_limit: float = attr.ib()
    weight: float = attr.ib(init=False)
    value: float = attr.ib(init=False)

    def __attrs_post_init(self):
        self.weight = 0
        self.value = 0
        self.items = sorted(
            itmes, key=lambda item: item.value_per_weight, reverse=True)

    def append_items(self):
        for item in self.items:
            room = self.weight_limit-self.weight
            if room <= 0:
                break
            self.append_item(item, room)

    def append_item(self, item: Item, room: float):
        diff = room-item.weight
        if diff > 0:
            # there is enough room
            self.weight += item.weight
            self.value += item.value
        else:
            self.weight += room
            self.value += item.value*(room/item.weight)
