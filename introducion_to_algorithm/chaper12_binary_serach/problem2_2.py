from binary_search_tree import Node,tree_maximum
# recursive version


def tree_min(node: Node) -> Node:
    if node.left:
        return tree_min(node.left)
    return node


def tree_max(node: Node) -> Node:
    if node.right:
        return tree_max(node.right)
    return node
