# This is the class of the input tree. Do not edit.

import math
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    # Write your code here.
    diff = math.inf
    if tree.value == target:
        return target
    if target > tree.value :
        findClosestValueInBst(tree.right, target)