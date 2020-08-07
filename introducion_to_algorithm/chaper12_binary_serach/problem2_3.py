from binary_search_tree import Node, tree_maximum



def tree_predecessor(node: Node)->Node:
    """
    find max node from nodes smaller than input node

    Parameters
    ----------
    node : Node
        [description]

    Returns
    -------
    Node
        [description]
    """
    if current := node.left:
        # extract subtree maximum
        while current.right:
            current = current.right
        return current
    parent = node.parent
    while parent and node == parent.left:
        node = parent
        parent = parnet.parent
    return parent
