# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target):
    if target == tree.value:
        return tree.value
    if target > tree.value and tree.right is None:
        return tree.value
    if target < tree.value and tree.left is None:
        return tree.value
    if target < tree.value:
        findClosestValueInBst(tree.left, target)
    else:
        findClosestValueInBst(tree.right, target)
