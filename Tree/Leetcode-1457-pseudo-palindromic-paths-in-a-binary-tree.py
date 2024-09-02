# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root):
        arr = [0 for _ in range(10)]
        result = [0]

        def solve(root):
            if root is None:
                return
            arr[root.val] += 1
            if root.left is None and root.right is None:
                oddFrequency = 0
                for node in arr:
                    # print(node, arr)
                    if not (node % 2 == 0):
                        oddFrequency += 1
                if oddFrequency <= 1:
                    result[0] = result[0] + 1
            # arr[root.val] -= 1
            solve(root.left)
            solve(root.right)
            arr[root.val] -= 1

        solve(root)
        return result[0]


class BitSolution:
    def pseudoPalindromicPaths(self, root, cnt=0):
        if not root: return 0
        cnt ^= 1 << (root.val - 1)
        if root.left is None and root.right is None:
            return 1 if cnt & (cnt - 1) == 0 else 0
        return self.pseudoPalindromicPaths(root.left, cnt) + self.pseudoPalindromicPaths(root.right, cnt)


if __name__ == "__main__":
    nodea = TreeNode(2)
    nodeb = TreeNode(3)
    nodec = TreeNode(1)
