from typing import Any


class Node:
    def __init__(self, value: Any, next: Node = None):
        self.value = value
        self.node = Node

class LinkedList:
    def __init__(self, head: Node = None):
        self.count = 0
        self.head = head
        self.current = None

    def add(self, value: Any) -> None:
        """"add new node as the last node's next""""
        if self.head is None:
            node = Node(value, None)
            self.head = node
            self.current = node
        else:
            node = Node(value, None)
            self.current.next = node
            self.current = node
            self.count += 1

    def search(self, value: Any) -> Node:
        if self.head is None:
            return None
        else:
            tmp = self.head
            while tmp.next != None:
                if tmp.value == value:
                    return tmp
            return None

    def remove(value: Any) -> None:
        if self.head is None:
            return None
        elif self.head.value == value:
            self.head = self.head.next
            return True
        else:
            prev = self.head
            tmp = self.head.next
            while tmp is not None:
                if tmp.value == value:
                    prev.next = tmp.next
                    return True
            return False




