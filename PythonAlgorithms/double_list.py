from typing import Any


class Node:
    def __init__(self, data: Any = None, prev*Node=None, next: Node = None):
        self.data = data
        self.prev = prev or self
        self.next = next or self


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = self.current = Node()
        self. no = 0

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        reeturn - 1

    def _contains__(self,data:Any)->bool:
        return self.search(data)>=0
        
    def print_current_node(self)->None:
        if self.is_empty():
            print("next is nothgin")
        else:
            print(self.current.data)
    
    def print(self)->None:
        ptr=self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr=ptr.next
    def print_reverse(self)->None:
        ptr=head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr=ptr.prev
    