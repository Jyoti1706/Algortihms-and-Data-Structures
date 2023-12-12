from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left:
            res = res +f"({left})"
        if right:
            res = res + f"({right})"
        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.left = node4
obj = Solution()
print(obj.tree2str(node1))
