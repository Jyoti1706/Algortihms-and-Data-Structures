# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, sum=0, results=[]):
    if root is None:
        return

    sum=sum+root.value
    if root.left is None and root.right is None:
        results.append(sum)
        return
    branchSums(root.left, sum, results)
    branchSums(root.right, sum, results)
    return results