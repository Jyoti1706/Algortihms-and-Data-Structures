# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    if tree is None:
        return 0

    binaryTreeDiameter(tree.left)
    binaryTreeDiameter(tree.right)