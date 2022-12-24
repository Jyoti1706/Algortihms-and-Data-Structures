class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def invertBinaryTree(tree):
    # Write your code here.
    if tree.left is None and tree.right is None:
        return
    if tree is None:
        return None
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


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

print(invertBinaryTree(a))

