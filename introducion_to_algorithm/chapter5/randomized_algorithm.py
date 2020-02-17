from typing import Any, List
from random import uniform


class Element:
    def __init__(self, value: Any, priority: int):
        self.value = value
        self.priority = priority

    def __str__(self):
        return f"value:{self.value},priotiry:{self.priority}"


def permute_by_sort(input_list: List) -> List:
    n = len(input_list)
    ele_list: List[Element] = []
    for value in input_list:
        ele_list.append(Element(value, int(uniform(0, n**3))))
    print(ele_list)
    ele_list = sorted(ele_list, key=lambda u: u.priority)
    return [ele.value for ele in tmp_list]


def randomlize_in_place(input_list: List) -> List:
    n = len(input_list)
    for i in range(n):
        tmp = input_list[i]
        random_index=int(unifrom(0,n))
        input_list[i] = input_list[random_index]
        input_list[random_index]=tmp
    return input_list



if __name__ == "__main__":
    print(permute_by_sort([3, 4, 2, 1, 6, 7, 76]))
