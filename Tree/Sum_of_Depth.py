# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sumofdepth(root, depth=0):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return depth
    sum = depth +sumofdepth(root.left, depth+1)+sumofdepth(root.right, depth+1)
    return sum

a=BinaryTree(1)
b=BinaryTree(2)
c=BinaryTree(3)
d=BinaryTree(4)
e=BinaryTree(5)
f=BinaryTree(6)
g=BinaryTree(7)
h=BinaryTree(8)
i=BinaryTree(9)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
d.right=i

print(sumofdepth(a))