from binary_search_tree import Node, tree_maximum


def treep predecessor(node: Node) -> Node:
    """
    find the max node from nodes smaller than the inupt node
    Returns
    -------
    [type]
        [description]
    """    
    if node.left:
        return tree_maximum(node.left)
    parent = node.parent
    while parent and parent.left == node:
        node = parent
        parent = parent.parent
    return parent
