def balanced_tree(root):
    return check_balanced(root, height = 1)

def check_balanced(root, height = 0):
    if root is None:
        return (True, height)
    if root.left is None and root.right is None:
        return (True, height)
    left_balanced, left_height = check_balanced(root.left, height+1)
    right_balanced, right_height = check_balanced(root.right, height + 1)
    height_diff = abs(left_height-right_height)
    if (left_balanced and right_balanced) and height_diff<=1:
        return True, max(right_height, left_height)
    else:
        return False, max(right_height, left_height)
