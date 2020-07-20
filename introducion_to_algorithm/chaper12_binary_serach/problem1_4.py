from binary_search_tree import Node




def pre_order_tree_walk_simple(node:NOde)->None:
    if node:
        print(node.value)
        pre_order_tree_walk_simple(node.left)
        pre_order_tree_walk_simple(node.right)


def post_order_tree_walk_simple(node:Node)->None:
    """
    each node's is printed after both childs are checked 

    Parameters
    ----------
    node : Node
        [description]
    """    
    if node:
        post_order_tree_walk_simple(node.left)
        post_order_tree_walk_simple(node.right)
        print(node.value)

def preorder_tree_walk(node: Node) -> Node:
    """
    each nodes' parent are printed bfore their children

    Parameters
    ----------
    node : Node
        [description]

    Returns
    -------
    Node
        [description]
    """
    print("start")
    current = node
    stack = [current]
    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            # putting  priority on left child
            stack.append(current.left)
        print(current.key)
        # current = stack.pop()
    print("end")


def postorder_tree_walk(node: Node) -> None:
    """[summary]

    Parameters
    ----------
    node : Node
        [description]
    """
    current = node
    stack = [current]
    while stack:
        if current.left and current.left.not_printed:
            current = current.left
            stack.append(current)
        elif current.right and current.right.not_printed:
            current = current.right
            stack.append(current)
        else:
            print(current.key)
            current.not_printed = False
            current = stack.pop()
