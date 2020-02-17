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
    return [ele.value for ele in ele_list]


def randomize_in_place(input_list: List) -> List:
    n = len(input_list)
    for i in range(n):
        tmp = input_list[i]
        random_index = int(uniform(0, n))
        input_list[i] = input_list[random_index]
        input_list[random_index] = tmp
    return input_list


def permute_by_cyclic(input_list: List):
    print(f"{len(input_list)}")
    n = len(input_list)
    output_list = [None]*n
    offset = int(uniform(0, n))
    print(offset)
    for i in range(n):
        dest = i+offset
        if dest >= n:
            print(f"{dest} > {n}")
            dest -= n
        output_list[dest] = input_list[i]

    return output_list


def random_sample(m: int, n: int):
    # TODO check appropriate data type for variable s
    if m == 0:
        return 0
    else:
        s = random_sample(m-1, n-1)
        i = random_sample(1, n)
        if i in s:
            s = s.appned(n)
        else:
            s = s.appned(i)
    return s



if __name__ == "__main__":
    print(permute_by_cyclic([1,3,4,5,10,12,3,4]))
    
    #print(permute_by_sort([3, 4, 2, 1, 6, 7, 76]))
    
    #for i in range(100):
     #   print(randomize_in_place([3, 4, 5, 6, 7, 3, 2, 11, 33, 44, 123]))
