from dataclasses import dataclass
from enum import Enum
from typing import List
import math
from __future__ import annotations


class Color(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"
    GRAY = "GRAY"


@dataclass
class Vertex:
    color: Color
    # represeting distance from root
    predecessor: Vertex = None
    distance: float = math.inf

    def __eq__(self,other):
        return self.color
    
class Graph:
    def __init__(self,root,vertex_list):
        self.root=root
        self.vertex_list=vertex_list
    