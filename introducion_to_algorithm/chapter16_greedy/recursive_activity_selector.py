from typing import List, Set
import attr
from datetime import datetime


@attr.s
class Element:
    index: int = attr.ib()
    started_at: datetime = attr.ib()
    finished_at: datetime = attr.ib()


def recursive_activity_selector(elements: List[Element], k: int,
                                n: int) -> Set[Element]:
    """[summary]

    Parameters
    ----------
    elements : List[Element]
        [description]
    k : int
        [description]
    n : int
        [description]

    Returns
    -------
    Set[Element]
        [description]
    """
    #sorted(user_objs, key=lambda u: u.age)
    elements = sorted(elements, key=lambda ele: ele.finished_at)
    m = k+1
    while m <= n and elements[m].started_at < elements[k].finished_at:
        m += 1
    if m <= n:
        answer = set()
        answer.union(recursive_activity_selector(elements, m, n))
        answer.add(elements[m])
        return answer
    else:
        return None
