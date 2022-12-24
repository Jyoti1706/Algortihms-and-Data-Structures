# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    res = []

    def inorder(tree):
        if tree:
            inorder(tree.left)
            print(tree.value)
            res.append(tree.value)
            inorder(tree.right)
        else:
            return None

    inorder(tree)
    print(res)
    op = None
    print(node)
    print("------------")
    data = 5
    for i in range(len(res)):

        print(data)
        print(res[i] == data)
        if res[i] == data:
            op = i + 1
            break
    if op < len(res):
        return res[op]
    return None
