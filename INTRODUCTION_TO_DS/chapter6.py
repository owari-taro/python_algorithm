import random
from typing import List, Set, Tuple


def generate_graph(n: int, m: int) -> Tuple[List, Set]:
    ""
    if m>(n**2-n)/2:
        raise ValueError(f"m is too big!m must be equtl or less than (n*2-n)/2.")
    graph_data: List[int] = [[0]*n for i in range(n)]
    edge_set:Set[Tuple[int,int]] = set()
    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j:
            i, j = j, i
        edge_set.add((i, j))
        graph_data[i][j] = graph_data[j][i] = 1
    return graph_data, edge_set


if __name__ == "__main__":
    n = 150
    m = 20
    graph, edge = generate_graph(n, m)
    print(edge)
