class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isBalanced(self, root):
    #     if not root:
    #         return 0
    #     left = self.isBalanced(root.left)
    #     right = self.isBalanced(root.right)
    #     if abs(left - right) > 1:
    #         return False
    #     else:
    #         return max(left,right)+1

    def isBalanced(self, root):
        def helper(root):
            if not root:
                return [True, 0 ]
            left = helper(root.left)
            right = helper(root.right)
            balanced = (left[0] and right[0] and (abs(left[1]-right[1])<=1))
            return [balanced, max(left[1], right[1])+1]
        balanced = helper(root)
        return balanced


