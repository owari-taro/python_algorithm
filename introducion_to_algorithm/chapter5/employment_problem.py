from typing import List


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
