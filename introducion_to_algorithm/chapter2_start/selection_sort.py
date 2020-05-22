from typing import MutableSequence


def selection_sort(input_list: MutableSequence):
    original = input_list.copy()
    n = len(input_list)
    for j in range(i+1, n):
        if input_list[j] < input_list[min]:
            min = j
    input_list[i], input_list[min] = input_list[min], input_list[i]
