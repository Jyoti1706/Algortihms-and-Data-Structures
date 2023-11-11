import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        if not(root.left) and not(root.right):
            return 1
        if not(root.left):
            return 1+self.minDepth(root.right)
        if not(root.right):
            return 1+self.minDepth(root.left)
        return 1+ min(self.minDepth(root.left),self.minDepth(root.right))


# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)
#
# node1.right = node2
# node1.left = node7
# node2.right = node3
# node3.right = node4
# node4.right = node5
# node5.right = node6
#
# obj = Solution()
# print(obj.minDepth(node1))


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

node1.right = node2
node1.left = node3
node2.right = node6
node2.left = node7
node3.right = node4
node4.left = node5
node6.left = node8


obj = Solution()
print(obj.minDepth(node1))
