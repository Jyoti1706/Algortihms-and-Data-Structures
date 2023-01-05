import math


def minHeightBst(arr):
    if not arr:
        return None
    mid = (len(arr)) // 2
    root = BST(arr[mid])
    root.left = minHeightBst(arr[:mid])
    root.right = minHeightBst(arr[mid + 1:])
    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array=[1, 2, 5, 7, 10, 13, 14, 15, 22]
print(minHeightBst(array))
