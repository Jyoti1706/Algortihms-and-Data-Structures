"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

"""


class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(root, targetsum, leafsum):
            if not root:
                return False
            if not root.left and not root.right:
                return leafsum + root.val == targetsum
            return helper(root.left, targetsum, leafsum + root.val) or helper(root.right, targetsum, leafsum + root.val)

        return helper(root, targetSum, 0)
