from typing import Any


class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, size: int):
        self.size = size
        self.stack = [None]*self.size
        self.current = 0

    def __len__(self) -> int:
        """[summary]len(object) return number of element store in stack

        Returns
        -------
        int
            [description]
        """
        return self.current

    def is_empty(self) -> bool:
        return self.current <= 0

    def is_full(self) -> bool:
        return self.current >= self.size

    def push(self, value: Any):
        if self.is_full():
            raise FixedStack.Full
        self.stack[self.current] = value
        self.current += 1

    def pop(self, value: Any):
        if self.is_empty():
            raise FixedStack.Empty
        self.stack.pop()
        self.current -= 1

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.size!r})"

    def __iter__(self):
        """[summary]with this method,you can use like below
            for ele in fixed_stack:
                print(ele)

        Returns
        -------
        [type]
            [description]
        """
        return iter(self.stack)

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stack[self.current-1]

    def clear(self) -> None:
        self.current = 0
        self.stack = [None]*self.size

    def find(self, value: Any) -> int:
        for i in range(self.current-1, -1, -1):
            if self.stack[i] == value:
                return i
        return -1

    def count(self, value: Any) -> bool:
        count = 0
        for ele in range(self.current):
            if ele == value:
                count += 1
        return count

    def __contains__(self, value: Any) -> bool:
        return self.find(value) >= 0
