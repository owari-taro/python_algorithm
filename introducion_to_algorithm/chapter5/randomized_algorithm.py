from typing import Any, List
from random import uniform


class Element:
    def __init__(self, value: Any, priority: int):
        self.value = value
        self.priority = priority
    def __str__(self):
        return f"value:{self.value},priotiry:{self.priority}"


def permute_by_sort(input_list: List):
    n = len(input_list)
    tmp_list: List[Element] = []
    for value in input_list:
        tmp_list.append(Element(value, uniform(1, n**3)))
    print(tmp_list)
    tmp_list=sorted(tmp_list, key=lambda u: u.priority)
    return [ele.value for ele in tmp_list]


if __name__ == "__main__":
    print(permute_by_sort([3, 4, 2, 1, 6, 7, 76]))
