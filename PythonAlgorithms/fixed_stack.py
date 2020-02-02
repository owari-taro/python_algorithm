from typing import Any

class FixedStack:

    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self,capacity:int=256)->None:
        self.stk=[None]*capacity
        self.capacity=capacity
        self.ptr=0
    
    def __len__(self)->int:
        return self.ptr

    def is_empty(self)->bool:
        return sefl.ptr<=0
    
    def is_full(self)->bool:
        return self.ptr>=self.capacity
        
