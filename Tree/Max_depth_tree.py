from Tree.Tree_DS import *

def max_depth(root, depth=0):
    if root is None:
        return depth
    l = max_depth(root.left,depth+1)
    r = max_depth(root.right, depth+1)
    return max(l,r)

print(max_depth(a))
