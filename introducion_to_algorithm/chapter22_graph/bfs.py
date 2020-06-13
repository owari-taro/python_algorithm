from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List
import math
from collections import deque
import attr


class Color(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    GRAY = "GRAY"


@attr.s
class Vertex:
    id_: int
    color: Color = attr.ib()
    # represeting distance from root
    distance: float = attr.ib(default=None)
    predecessor: Vertex = attr.ib(default=None)
    adjacent: List[Vertex] = attr.ib(default=None)

    def __eq__(self, other: Vertex):
        return self.id_ == other.id_


@attr.s
class Graph:
        root: Vertex = attr.ib()
        vertex_list: List[Vertex] = attr.ib()

    def print_path(self,start:Vertex,end:Vertex)->None:
        """[summary]
        print all the nodes on the shortest path from start to end
        Parameters
        ----------
        start : Vertex
            [description]
        end : Vertex
            [description]
        """        
        if start==end:
            print(start)
        elif end.parrent is None:
            print("there is no route to end from start")
        else:
            self.print_path(start,end.parent)
            print(end)

def bfs(graph: Graph) -> Graph:
    # initialize
    for vertex in graph.vertex_list:
        if vertex == graph.root:
            continue
        vertex.color = Color.WHITE
        vertex.distance=math.inf
        vetex.predecessor=None

    queue = deque([])
    queue.append(graph.root)
    while queue:
        current = queue.popleft()
        for adj in current.adjacent:
            # white means note visited before
            if adj.color == Color.WHITE:
                adj.color = Color.GRAY
                adj.distance = current.distance+1
                adj.parrent = current
                queue.append(adj)
        # finish
        current.color = Color.BLACK
    return graph
