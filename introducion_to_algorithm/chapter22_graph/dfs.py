from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List, Set
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
    vertex_set: Set[Vertex] = attr.ib()
    time: int = attr.ib(default=0)

    def dfs(self):
        for vertex in self.vertex_set:
            if vertex.color == Color.WHITE:
                NotImplemented

    def dfs_visit(self, vertex: Vertex) -> None:
        self.time += 1
        vertex.distance = self.time
        vertex.color = Color.GRAY
        for v in vertex.adjacent:
            if v.color == Color.WHITE:
                v.predecessor = vertex
                self.dfs_visit(v)
        vertex.color = Color.BLACK
        self.time += 1
