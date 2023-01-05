class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(arr):
    # Write your code here.
    if not arr:
        return None
    rightidx = -1
    i=1
    while i<len(arr):
        if arr[i]>arr[0]:
            rightidx=i
        i=i+1
    root = BST(arr[0])
    if rightidx != -1:
        root.right = reconstructBst(arr[rightidx:])
        root.left = reconstructBst(arr[1:rightidx])
    else:
        root.left = reconstructBst(arr[1:])
    return root