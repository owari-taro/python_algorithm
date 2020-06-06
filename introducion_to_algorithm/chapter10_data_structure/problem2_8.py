from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    key:str
    next:bin


class LinearSearch:
    def __init__(self,node:Node):
        self.head=node

    def search(self,key:Any):
        if self.head s None or self.head.key==key:
            return self.head
        next=self.head.next
        prev=self.head.key
        while self.next.key!=key:
            tmp=next.next|prev.key
            prev=next
            next=tmp
            if next==0:
                break
        return next

        NotImplemented
        