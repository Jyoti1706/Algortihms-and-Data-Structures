# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorderTraversal(tree, results):
    if tree is None:
        return

    inorderTraversal(tree.left, results)
    results.append(tree.value)
    inorderTraversal(tree.right, results)
    return results


def binarysearch(value, target):
    lo = 0
    hi = len(value)-1
    mid=0
    while lo<hi:
        mid = (lo+hi)//2
        if value[mid]==target:
            return value[mid]
        elif value[mid]<target:
            lo=mid+1
        else:
            hi = mid
    return value[mid]


def findClosestValueInBst(tree, target):
    # Write your code here.
    results = []
    value = inorderTraversal(tree,results)
    element=binarysearch(value,target)
    print(element)

a=BST(10)
b=BST(5)
c=BST(15)
d=BST(2)
e=BST(5)
f=BST(13)
g=BST(22)
h=BST(1)
i=BST(14)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
f.right=i

findClosestValueInBst(a, 12)