from typing import Any


class Node:
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None):
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

    def _contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        if self.is_empty():
            print("next is nothgin")
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        ptr = head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """move current node to next"""
        if self.is_empty()or self.current.next is self.head:
            #next is emtpy
            return False
        self.current = self.current.next
        return current

    def prev(self) -> bool:
        if slef.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        """add new node to current&'s next"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """add new node as first"""
        self.current = self.head
        self.add(data)

    def add_last(self, data: Any) -> None:
        """add new node to last"""
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """remove node p"""
        ptr = self.head.next
        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
                ptr = ptr.next

    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()
