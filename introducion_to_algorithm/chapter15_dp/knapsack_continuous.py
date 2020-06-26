import attr
from typing import List
from __future__ import annotations


@attr.s
class Item:
    name: str = attr.ib()
    weight: float = attr.ib()
    price: float = attr.ib()


@attr.s
class Knapsack:
    size = attr.ib()
    weight = attr.ib(default=0)
    value = attr.ib(default=0)
    items: List = attr.ib(default=[])

    def append(self, item: Item) -> None:
        percent = self.calc_room(item)
        if percent is 0:
            raise ValueError("theere isnt enough space for the item")
        self.items.append(item)
        self.weight += precent*item.weight
        self.value += percent*item.value

    def calc_room(self, item) -> float:
        room = self.size-self.weight
        if room <= 0:
            return 0
        if room >= item.weight:
            return 1
        else:
            return item.weight/room

    @classmethod
    def div_knapsack(cls, items: List[Item], size_limit: float):
        #　単位重さあたりの価値で品物を並び替える。
        sorted_item_list = sorted(
            items, key=lambda x: x.price/x.weight, reverse=True)
        knapsack = cls(size_limit)
        for v in sorted_item_list:
            try:
                # TODO:fix append to original version
                knapsack.append(v)
            except ValueError:
                break
        room = knapsack.size - knapsack.weight
        p = v.price * (room / v.weight)
        virtual_item = Item(-1, w, p)
        knapsack.append(virtual_item)
        return knapsack
