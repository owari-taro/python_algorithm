from typing import List


def selection_sort(input_list: List[float]):
    original = input_list.copy()
    for i in range(0, len(input_list)-1):
        tmp = input_list[i]
        index_ = i
        for j in range(i+1, len(input_list)):
            if tmp > input_list[j]:
                tmp = input_list[j]
                index_ = j
            input_list[index_] = input_list[i]
            input_list[i] = tmp
