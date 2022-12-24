

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
    if root is None:
        return
    depth=depth+1
    if root.left is None and root.right is None:
        return depth
