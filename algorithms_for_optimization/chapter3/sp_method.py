from __future__ import annotations
from dataclasses import dataclass
from  typing import Callable

@dataclass
class Point:
    x: float
    y: float

    @classmethod
    def get_sp_intersection(self, A: Point, b: Point, slope: float) -> Point:
        intersection = ((A.y-B.y)-slope*(A.x-B.x))/2*slope
        return Point(A.x+intersection, A.y+intersection*slope)  
    
    def shubert_piyavskii(self,f:Callable,a:Point,b:Point,slope:float,eps:float,delat:float=0.01):
        """
        [summary]

        Parameters
        ----------
        f : Callable
            [description]
        a : Point
            [description]
        b : Point
            [description]
        slope : float
            [description]
        eps : float
            [description]
        delat : float, optionalxz
            [description], by default 0.01
        """        
        m=(a+b)/2
        A,B,M=Point(a,f(a)),Point(b,f(b)),Point(m,f(m))
        #TODO:implement below