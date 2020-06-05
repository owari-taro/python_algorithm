from binary_search_tree import Node


def inorder_tree_work_non_recursive(node: Node) -> None:
    current = node
    stack = [current]
    while stack:
        if current.left and current.left.not_printed:
            current = current.left
            stack.append(current)
        else:
            if current.left is None:
                current = curretnt.pop()
            print(current.key)
            current.is_printed = True
            if current.right:
                current = current.right
                stack.append(cunrrent)
            else:
                current = stack.pop()
