import attr
from typing import List
import math


@attr.s
class Item:
    weight: float = attr.ib()
    value: float = attr.ib()
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
    def space(self) -> float:
        """
        return space left for another item,if there is no space raise value Error

        Returns
        -------
        float
            [description]

        Raises
        ------
        ValueError
            [description]
        """
        rest = self.weight_limit-self.weight
        if reset > 0:
            return rest
        raise ValueError("there is no room left for any new item")


def knapsack(items: List[Item], weight_limit: float):
    n = len(items)
    knapsack = Knapsack(weight_limit)
    current_max = -math.inf
    current_items = []

    def bb_knapsack(level: int) -> None:
        nonlocal current_items
        nonlocal current_max
        if level >= n:
            if knapsack.weight <= weight_limit and knapasack.value > current_max:
                current_max = knapsack.value
                current_items = knapsack.items
                # knapsack.reset()
        else:
            if knapsack.weight == weight_limit and knapsack.value > current_max:
                current_max = knapsack.value
            if knapsack.weight < weight_limit and \
                    (knapsack.room*items[level].unit_value > current_max):
                item = items[level]
                bb_knapsack(level+1)
                knapsack.items.append(item)
                bb_knapsack(level+1)
