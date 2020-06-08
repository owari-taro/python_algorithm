from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, value: Any, next: Node = None):
        """"
        Node is used as each elment of linked_list
        value:Any
        next:Node
        """
        self.value = value
        self.next = next

    def __eq__(self, other: Node) -> bool:
        return self.value == other.value

    def __str__(self):
        return f"value:{self.value} Node:{self.next}"

    def __repr__(self):
        return f"value:{self.value} Node:{self.next}"


class LinkedList:
    def __init__(self, head: Node = None):
        """"

        head:Node
        """
        if head is None:
            self.cont = 0
        else:
            self.count = 1
        self.head = head
        self.current = head

    def __len__(self) -> int:
        return self.count

    def __eq__(self, other):
        def eq_helper():
            if self.count != other.count:
                return False
            tmp = self.head
            tmp_other = other.head
            while True:
                print(tmp)
                print(tmp_other)
                if tmp is None and tmp_other is None:
                    return True
                elif not tmp == tmp_other:
                    return False
                tmp, tmp_other = tmp.next, tmp_other.next
            else:
                return False
        return eq_helper()

    def add(self, value: Any) -> None:
        """add new node as the last node's next"""
        if self.head is None:
            node = Node(value, None)
            self.head = node
            self.current = node
            self.count += 1
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

    def remove_current(self) -> None:
        """remove the latest added node"""
        if self.head is None:
            return None
        count = 1
        tmp = self.head
        if self.count == 1:
            self.count -= 1
            self.current = None
            self.head = None
        else:
            while count < (self.count-1):
                tmp = tmp.next
                count += 1
            self.count -= 1
            tmp.next = None
            self.current = tmp

    def remove(self, value: Any) -> None:
        if self.head is None:
            return None
        elif self.head.value == value:
            self.head = self.head.next
            self.count -= 1
            return True
        else:
            prev = self.head
            tmp = self.head.next
            while tmp is not None:
                if tmp.value == value:
                    prev.next = tmp.next
                    self.count -= 1
                    return True
            return False

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.head.next
            self.count -= 1

    def print_current(self):
        if self.current is not None:
            print(self.current.value)
        else:
            print("current is None")

    def add_first(self, value: Any) -> None:
        node = Node(value, None)
        if self.head:
            node.next = self.head
        self.head = node

    def extend(self, linked_list: LinkedList) -> None:
        """merge two linked_list"""
        if linked_list.count == 0:
            print("extendされませんでした")
        else:
            self.count += linked_list.count
            self.current.next = linked_list.head
            self.current = linked_list.current

    def reverse(self) -> None:
        if self.count >= 2:
            self.current = self.head
            prev = self.head
            next = prev.next
            while True:
                tmp = next.next
                if tmp is None:
                    next.next = prev
                    self.head = next
                    break

                next.next = prev
                prev = next
                next = tmp

            # Todo
            self.head = None
            self.current = None


class Stack:

    def __init__(self):
        """stack using linked list"""
        self.stack = LinkedList()

    def pop(self) -> Any:
        """return current value and make prev's nodes valu"""
        if self.stack.head is None:
            return None
        output = self.stack.current.value
        self.stack.remove_current()
        return output

    def add(self, value: Any) -> None:
        self.stack.add(value)

# is inheriteance  a better way to impolement?


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def dequeue(self) -> Any:
        if len(self.queue) == 0:
            return None
        out = self.queue.head.value
        self.queue.remove_current()
        return out

    def enque(self, value: Any) -> None:
        self.queue.add(value)


if __name__ == "__main__":
    stack = Stack()
    stack.add(3)
    stack.add(4)
    print(len(stack.stack))
    print("##############################")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("###############################")
    stack.stack.print_current()
    print(len(stack.stack))
