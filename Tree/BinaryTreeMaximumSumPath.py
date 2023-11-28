import math

from Tree.Tree_DS import Node


class Solution:
    def maxPathSum(self, root) -> int:
        res = [root.val]

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            leftmax = max(left,0)
            right = helper(root.right)
            rightmax = max(right,0)
            res[0] = max(leftmax + rightmax + root.val, leftmax + root.val, rightmax + root.val, res[0])
            return root.val+max(leftmax, rightmax)

        res = helper(root)
        return res


a = Node(3)
b = Node(11)
c = Node(-24)
d = Node(4)
e = Node(2)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

obj = Solution()

print(obj.maxPathSum(a))
