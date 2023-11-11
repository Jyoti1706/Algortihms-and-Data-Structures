class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanced_tree(root):
    return check_balanced(root, height = 1)

def check_balanced(root, height = 0):
    if root is None:
        return (True, height)
    # if root.left is None and root.right is None:
    #     return (True, height)
    left_balanced, left_height = check_balanced(root.left, height+1)
    right_balanced, right_height = check_balanced(root.right, height + 1)
    height_diff = abs(left_height-right_height)
    if (left_balanced and right_balanced) and height_diff<=1:
        return True, max(right_height, left_height)
    else:
        return False, max(right_height, left_height)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node4.left = node6
node4.right = node7

print(balanced_tree(node1))