from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    @classmethod
    def get_sp_intersection(self, A: Point, b: Point, slope: float) -> Point:
        intersection = ((A.y-B.y)-slope*(A.x-B.x))/2*slope
        return Point(A.x+intersection, A.y+intersection*slope)
