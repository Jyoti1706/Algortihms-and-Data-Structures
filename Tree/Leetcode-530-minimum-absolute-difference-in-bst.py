# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


def traverse(root):
    if root is None:
        return
    yield from  traverse(root.left)
    yield root.val
    yield from  traverse(root.right)

class Solution:
    def getMinimumDifference(self, root):
        seq = traverse(root)
        dif = math.inf
        prev = next(seq)
        for curr in seq:
            dif = min(curr-prev, dif)
            prev = curr

        return dif
