class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, postorder, inorder):
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(postorder[:mid], inorder[:mid])
        root.right = self.buildTree(postorder[mid + 1:-1], inorder[mid + 1:])
        return root
