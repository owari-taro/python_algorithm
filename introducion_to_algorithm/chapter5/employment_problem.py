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


def biased_generator(prob: float) -> float:
    num = random.uniform(0, 1)
    #print(num)
    if prob > num:
        return 1
    else:
        return 0


def unbiased_generator(prob:float):
    tmp = [biased_generator(prob) for i in range(1000)]
    #TODO:make this calculation more accurate,see effective python 2nd
    estimate = sum(tmp)/len(tmp)
    print(estimate)

if __name__ == "__main__":
    print(unbiased_generator(0.3))