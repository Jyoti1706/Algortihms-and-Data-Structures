# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Tree.Tree_DS import Node


class Solution:
    def rightSideView(self, root):
        queue = [[root],]
        res=[[root][-1],]
        while len(queue[0])>0:
            temp = []
            curr = queue.pop(0)
            while len(curr)>0:
                node = curr.pop(0)
                #print(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue.append(temp)
            res.append(temp.copy()[-1])

        return res[:-1]


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
# g = Node('g')
# h = Node('h')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f


obj = Solution()
print(obj.levelOrder(a))


