# coding: utf-8

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    """
    The function Compute the "height" of a tree. Height is the
    number f nodes along the longest path from the root node
    down to the farthest leaf node.
    """
def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))



