from typing import Optional

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_unival_subtrees(root: Node) -> int:
    def num_subtrees_node(node: Optional[Node]) -> int:
        if node is None:
            return 0

        left_subtrees = num_subtrees_node(node.left)
        right_subtrees = num_subtrees_node(node.right)

        subtrees = left_subtrees + right_subtrees

        # A node has one subtree if it has no nodes
        # If it has any number of nodes, it is only a subtree IF all children have (the same value AND more than one subtree)
        children = [n for n in [node.left, node.right] if n]
        if all([n.val == node.val for n in children]):
            subtrees += 1

        return subtrees

    return num_subtrees_node(root)
