"""
Split the Binary Tree by removing an edge such that sum of 2 sub-tree are equal.
Date : 15-11-2023
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getTreeSum(tree):
    if not tree:
        return 0
    return getTreeSum(tree.left)+getTreeSum(tree.right)+tree.value


def trysubtree(tree, desired_sum):
    if not tree:
        return 0, False
    leftSum, leftCanBeSplit = trysubtree(tree.left, desired_sum)
    rightSum, rightCanBeSplit = trysubtree(tree.right, desired_sum)
    currentSum = tree.value + leftSum + rightSum
    canBeSplit = leftCanBeSplit or rightCanBeSplit or (currentSum == desired_sum)
    return currentSum, canBeSplit


def splitBinaryTree(tree):
    # Write your code here.
    desired_sum = getTreeSum(tree)/2
    canBeSplit = trysubtree(tree, desired_sum)[0]
    return desired_sum if canBeSplit else 0

