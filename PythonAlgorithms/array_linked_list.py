from typing import Any
Null=-1
class Node:

    def __init__(self,data=Null,next=null,dnext=null):
        self.data=data
        self.next=next
        self.dnext=dnext
    

class ArrayLinkedList:

    def __init__(self,capacity:int):
        self.head=Null
        self.current=Null
        self.max=Null
        self.deleted=Null
        self.capacity=capacity
        self.n=[Node()]*self.capacity
        self.no=0

    def __len__(self)->int:
        return self.no
    
    def get_insert_index(self):
        if self.deleted==Null:
            if self.max<self.capacity:
                self.max+=1
                return self.max
            else:
                return Null
        else:
            rec=self.deleted
            self.deleted=self.n[rec].dnext
            return rec