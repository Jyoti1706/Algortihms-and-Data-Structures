import collections
import math


class Solution:
    # def minDiffInBST1(self, root):
    #     """
    #     [90,69,null,49,89,null,52]
    #     :param root:
    #     :return: 1
    #     """
    #     res = root.val
    #     dqueue = collections.deque()
    #     if root:
    #         dqueue.append(root)
    #     while dqueue:
    #         node = dqueue.popleft()
    #         if node.left:
    #             res = min(res, node.val-node.left.val)
    #             dqueue.append(node.left)
    #         if node.right:
    #             res = min(res, node.right.val - node.val)
    #             dqueue.append(node.right)
    #   return res
    def minDiffInBST(self, root):
        flattened = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            flattened.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = float("inf")
        for i in range(1, len(flattened)):
            ans = min(ans, flattened[i] - flattened[i - 1])
        return ans
