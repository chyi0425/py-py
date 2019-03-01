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


def diameter(root):
    if root is None:
        return 0

    # Get the height of left and right sub-trees
    lheight = height(root.left)
    rheight = height(root.right)

    # Get the diameter of left and right sub-trees
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    # 1) Diameter of left tree
    # 2) Diameter of right tree
    # 3) Height of left subtree + height of right subtree +1
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))
