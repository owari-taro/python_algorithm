import random
from typing import List, Set, Tuple
from collections import deque
import math
import heapq


def generate_graph(n: int, m: int) -> Tuple[List, Set]:
    """generate graph search"""
    if m > (n**2-n)/2:
        raise ValueError(
            f"m is too big!m must be equtl or less than (n*2-n)/2.")
    graph_data: List[int] = [[0]*n for i in range(n)]
    edge_set: Set[Tuple[int, int]] = set()
    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j:
            i, j = j, i
        edge_set.add((i, j))
        graph_data[i][j] = graph_data[j][i] = 1
    return graph_data, edge_set


def breadth_first_search(start: int, W: List[List[int]]) -> Set:
    work_queue: deque = deque([])
    visited: Set[int] = set()
    work_queue.append(start)
    visited.add(start)
    while work_queue:
        here = work_queue.popleft()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                visited.add(i)
                work_queue.append(i)
    return visited


def depth_fist_search(start: int, W: List[List[int]]) -> Set:
    work_stack = []
    visited: Set[int] = set()
    work_stack.append(start)
    visited.add(start)
    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                visited.add(i)
                work_stack.append(i)

    return visited


def dijkstra(start: int, W: List[List[int]]) -> List:
    """return distance list,element of which  
    is minum distance from start point."""
    distance_list = [math.inf]*len(W)
    distance_list[start] = 0
    done_list = []
    wait_heap = []

    for i, d in enumerate(distance_list):
        heapq.heappush(wait_heap, (d, i))
    while wait_heap:
        p = heapq.heappop(wait_heap)
        i = p[1]
        if i in done_list:
            continue
        done_list.append(i)
        forj, x in enumerate(W[i]):
            if x == 1 and j not in done_list:
                if x == 1 and j not in done_list:
                    d = min(distance_list[j], distance_list[i]+x)
                    distance_list[j] = d
                    heapq.heappush(wait_heap, (d, j))

    return distance_list


def all_pairs_shortest_patsh(W: List[List]) -> List[List]:
    for i in range(n):
        for j in range(j, n):
            if i == j:
                val = 0
            elif W[i][j]:
                val = W[i][j]
            else:
                val = math.inf
            res[i][j] = res[j][i] = val
    for k in range(n):
        for u in range(n):
            for v in range(n):
                res[u][v] = min(res[u][v], res[u][k]+res[k][v])

    .return res


if __name__ == "__main__":
    n = 150
    m = 30
    graph, edge = generate_graph(n, m)
    print(breadth_first_search(3, graph))
    print(depth_fist_search(3, graph))
