from typing import Any

class Node:
    def __init__(self,data:Any=None,prev*Node=None,next:Node=None):
        self.data=data
        self.prev=prev or self
        self.next=next or self
    
    
class DoubleLinkedList:
    def __init__(self)->None:
        self.head=self.current=Node()
        self. no=0
    
    def __len__(self)->int:
        return self.no
    
    def is_empty(self)->bool:   
        return self.head.next is self.head
    