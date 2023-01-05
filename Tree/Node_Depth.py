class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
    if root is None:
        return depth
    #depth=depth+1
    if root.left is None and root.right is None:
        return depth
    return max(nodeDepths(root.left,depth+1), nodeDepths(root.right,depth+1))


a=BinaryTree(1)
b=BinaryTree(2)
c=BinaryTree(3)
d=BinaryTree(4)
e=BinaryTree(5)
f=BinaryTree(6)
g=BinaryTree(7)
h=BinaryTree(8)
i=BinaryTree(9)
j=BinaryTree(10)
k=BinaryTree(11)
l=BinaryTree(12)
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
d.right=i
i.right=j
j.left=k
j.right=l
print(nodeDepths(a))