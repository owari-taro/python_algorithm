from typing import List,Set
from recursive_activity_selector import Element

def greedy_activity_selector(started_at:List,finished_at:List)->Set:
    n=len(started_at)
    answer=set([1])
    k=1
    for m in range(2,n+1):
        if 
\