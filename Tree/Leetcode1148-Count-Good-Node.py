"""

https://leetcode.com/problems/count-good-nodes-in-binary-tree/

"""

class Solution:
    def goodNodes(self, root):
        count = 0
        maxval = root.val
        def dfs(root,maxval):
            nonlocal count
            if not root:
                return 0
            res = 1 if root.val>=maxval else 0
            count += res
            maxval = max(maxval, root.val)
            res += dfs(root.left, maxval)
            res += dfs(root.right, maxval)
            return res
        return count
