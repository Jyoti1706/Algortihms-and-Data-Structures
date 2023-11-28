# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

from Tree.Tree_DS import Node


class Solution:
    def levelOrder(self, root):
        queue = [[root],]
        res=[]
        temp = [root]
        while len(queue[0])>0:
            res.append([t.val for t in temp.copy()])
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
            #res.append(temp.copy())

        return res

    def levelOrderdequeu(self, root):
        dqueue = collections.deque()
        res=[]
        if root:
            dqueue.append(root)
        while dqueue:
            temp = []
            for i in range(len(dqueue)):
                node = dqueue.popleft()
                temp.append(node.val)
                #print(node.val)
                if node.left:
                    dqueue.append(node.left)
                if node.right:
                    dqueue.append(node.right)
            res.append(temp.copy())
        return res



a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
# h = Node('h')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f


obj = Solution()
print(obj.levelOrderdequeu(a))


