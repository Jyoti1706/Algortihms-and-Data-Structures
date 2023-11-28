"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        dqueue = collections.deque()
        res = [root]
        count = 1
        if root:
            dqueue.append(root)
        while dqueue:
            temp = []
            for i in range(len(dqueue)):
                node = dqueue.popleft()
                temp.append(node.val)
                if node.left:
                    dqueue.append(node.left)
                if node.right:
                    dqueue.append(node.right)
                temp.append(node.val)
            if count%2 == 0:
                res.append(temp[::-1].copy())
            else:
                res.append(temp.copy())
            count += 1
        return res

