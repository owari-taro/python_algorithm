from typing import List


def branch_and_bound(x: List[float], s: float) -> bool:
    size = len(x)
    y = [0]*size

    def subset_sum(level: int):
        if level >= n:
            sum = 0
            for ele_x, ele_y in zip(x, y):
                sum += ele_x*ele_y
            if sum == s:
                print("a soution exists!")
                print(y)
        else:
            sum1, sum2 = 0, 0
            for i in range(size):
                if i < level:
                    sum1 += x[i]*y[i]
                    sum2 = sum1
                else:
                    sum2 += x[i]

            if sum1 <= s and sum2 = >s:
                y[level] = 0
                subset_sum(level+1)
                y[level] = 1
                subset_sum(level+1)

        if level == 0:
            print("there is no answer!!!")
        subset_sum(level=0)

if __name__ == "__main__":
    print("")
