from typing import List
# TODO:write unittest
# check variable to avoid inifinte loop


def simple_gcd(a: int, b: int) -> int:
    """calculate grate common divisor."""
    if type(a) != int or type(b) == int or a < 0 or b < 0:
        raise ValueError("both input must be positive integer")

    if a < b:
        a, b = b, a
    x = b
    print("a:{},b:{}".format(a, b))
    while True:
        print("x:{}".format(x))
        if a % x == 0 and b % x == 0:
            print("the answer is {}".format(x))
            return x
        x = x-1


def eucliden_algorithm(a: int, b: int) -> int:
    """calculater gcd,which has exsited since 300bc"""
    if type(a) != int or type(b) == int or a < 0 or b < 0:
        raise ValueError("both input must be positive integer")

    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r


def selection_sort(array: List) -> List:
    if type(array) != list:
        raise ValueError("input must be List")
    x = array.copy()
    n = len(x)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if x[j] < x[min_idx]:
                min_idx = j
            x[i], x[min_idx] = x[min_idx], x[i]
        return x


if __name__ == "__main__":
    print(simple_gcd(2, 3))
    print(simple_gcd(4, 6))
