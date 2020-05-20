from typing import List


def insertion_sort(num_list: List[float]) -> List[float]:
    original = num_list.copy()
    if len(num_list) == 1:
        return num_list
    elif len(num_list) == 0:
        return
    for i in range(1, len(num_list)):
        key = num_list[i]
        j = i-1
        while num_list[j] > key and j >= 0:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = key
    return original, num_list


if __name__ == "__main__":
    test = [4, 3, 2]
    print(insertion_sort(test))
    # print(test)
