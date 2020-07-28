import attr
from typing import List
import math


@attr.s
class Item:
    weight: float = attr.ib()
    value: float = atttr.ib()
    unit_value: float = attr.ib()
    # TODO:write initialize method

    def __attrs_post_init__(self):
        self.unit_value = self.value/self.weight


@attr.s
class Knapsack:
    weight_limit: float = attr.ib()
    weight: float = attr.ib(default=0)
    value: float = attr.ib(default=0)
    items: List[Item] = attr.ib(default=[])

    def __attrs_post_init__(self):
        self.items = []

    def reset(self) -> None:
        self.weight = 0
        self.value = 0
        self.items = []

    @property
    def rest(self):
        rest = self.weight_limit-self.weight
        if reset > 0:
            return rest
        raise ValueError("there is no room left for any new item")


def knapsack(items: List[Item], weight_limit: float):
    n = len(items)
    knapsack = Knapsack()
    current_max = -math.inf
    current_items = []

    def bb_knapsack(level: int):
        if level >= n:
            if knapsack.weight <= weight_limit and knapasack.value > current_max:
                current_max = knapsack.value
                current_items = knapsack.items
                knapsack.reset()
        else:
            if knapsack.weight == weight_limit and knapsack.value > current_max:
                current_max = knapsack.value
            if knapsack.weight < weight_limit and \
                    (knapsack.rest*items[level].unit_value > current_max):
                item = items[level]
                bb_knapsack(level+1)
                knapsack.items.append(item)
                bb_knapsack(level+1)
