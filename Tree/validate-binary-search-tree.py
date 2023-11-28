class Solution:
    def isValidBST(self, root):
        node = root.val
        def helper(root):
            if not root:
                return True
            if root.left:
                if root.val < root.left.val or root.val>node:
                    return False
            if root.right:
                if root.val > root.right.val or root.val<node:
                    return False
            return helper(root.left) and helper(root.right)
        return helper(root)

    def isValidBST(self, root):
        def helper(root, left, right):
            if not root:
                return True
            if not(root.val < right and root.val>left):
                return False
            return helper(root.left, left, root.val) and helper(root.right,root.val, right)
        return helper(root, float("-inf"), float("inf"))
