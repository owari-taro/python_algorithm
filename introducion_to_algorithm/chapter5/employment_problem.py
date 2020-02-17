from typing import List
import random


class Person:
    def __init__(name: str, score: int):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}:{self.score}"


def fire_assistant(candidate_list: List[Person]) -> None:
    best = 0
    hired = set()
    for ele in candidate_list:
        if ele.score > best:
            hired.add(ele)
            best = ele.score


def biased_generator(prob: float = 0.3) -> float:
    num = random.uniform(0, 1)
    # print(num)
    if prob > num:
        return 1
    else:
        return 0


def unbiased_generator():
    tmp = [biased_generator() for i in range(10000)]
    # TODO:make this calculation more accurate,see effective python 2nd
    estimate = sum(tmp)/len(tmp)

    def helper(estimate):
        result = []
        for i in range(100):
            result.append(biased_generator())
        tmp = float(sum(result))/float(estimate*2*100)
       # print(tmp)
        if tmp > 0.5:
            return 1
        else:
            return 0
    
    return helper(estimate)


if __name__ == "__main__":
    # print(unbiased_generator(0.3))
    print(unbiased_generator())
    for i in range(1000):
        test=[unbiased_generator() for i in range(100)]
        print(float(sum(test)/len(test)))