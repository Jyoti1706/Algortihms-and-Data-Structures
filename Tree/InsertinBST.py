class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val: int):
        curr = root
        val_nod = TreeNode(val)
        while curr:
            if val < curr.val and curr.left is None:
                curr.left = val_nod
                return root
            elif val > curr.val and curr.right is None:
                curr.right = val_nod
                return root
            else:
                if val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right

