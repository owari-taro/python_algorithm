from typing List


def depth_first_search(start: int, W: List[List]):
    work_stack = []
    visited = set()
    work_stack.append(start)
    visited.add(start)
    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_stack.appen(i)
                visited.add(i)
    return visited
