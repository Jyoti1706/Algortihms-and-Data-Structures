# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(root):
    # Write your code here.
    res = [0]
    def helper(root):
        if not root:
            return -1
        left = helper(root.left)
        right = helper(root.right)

        res[0] = max(res[0],left+right+2)
        return 1 + max(left,right)
    helper(root)
    return res[0]


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

## Using Scoping concept
def binaryTreeDiameter2(root):
    # Write your code here.
    #res = [0]
    res = 0
    def helper(root):
        nonlocal res
        if not root:
            return -1
        left = helper(root.left)
        right = helper(root.right)

        res = max(res,left+right+2)
        return 1 + max(left,right)
    helper(root)
    return res
