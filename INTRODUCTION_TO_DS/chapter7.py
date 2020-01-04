from collections import namedtuple
import random

Item = namedtuple("Item", ("name", "weight", "price"))


class Knapsack:
    def __init__(self, size: int):
        self.size = size
        self.weight = 0
        self.value = 0
        self.items = []

    def append(self, item: Item):
        if not self.has_room_for(item):
            raise ValueError("too many items,over weight!!")
        self.items.append(item)
        self.weight += item.weight
        self.value += item.price

    def has_room_for(self, item: Item) -> bool:
        """check enough room for appending new item. """
        return self.size >= self.weight+item.weight

    def __str__(self):
        val = f"weight:{self.weight}kg value:\\{self.value}thousand yen"
        return val

def greedy(items:List[Item],size_limit:int):
    sorted_item_list=sorted(items,key:lamda x:x.price/x.weight,reverse=True)
    my_knapsack=Knapsack(size_limit)
    for v in sorted_items_list:
        try:
            my_knapsack.append(v)
        except ValueError:
            coutinue
    return my_knapsack
