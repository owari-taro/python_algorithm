import random


def genereate_graph(n: int, m: int):
    """[summary]

    Parameters
    ----------
    n : int
        [description]
    m : int
        [description]

    Returns
    -------
    [type]
        [description]
    """
    graph_data = [[0]*n for i in range(n)]
    edge_set = set()
    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j:
            i, j = j, i
        edge_set.add((i, j))
        graph_data[i][j] = graph_data[j][i] = 1

    return graph_data, edge_set
