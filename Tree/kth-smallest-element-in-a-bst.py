class Solution:
    def kthSmallest(self, root,k ):
        flattened = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            flattened.append(node.val)
            dfs(node.right)

        dfs(root)

        return flattened[k-1]