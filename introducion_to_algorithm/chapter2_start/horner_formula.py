from typing import List


def horner(coef_list: List, x: float):
    y = 0
    n = len(coef_list)
    for i in range(n-1, -1, -1):
        y += a[i]+x*y
    return y


def horner_alt(coef_list: List, x: float):
    y = 0
    for i in range(len(coef_list)):
        coef = coef_list[i]
        tmp = coef
        for j in range(i):
            tmp = tmp*x
        y += tmp
    return y

if __name__ == "__main__":
    for i in range(10, -1, -1):
        print(i)
