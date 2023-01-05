from Tree import Node_Depth

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printNode(root, level, results):
    if root is None:
        return
    if level==0:
        results.append(root.val)
        return
    else:
        printNode(root.left, level-1, results)
        printNode(root.right, level-1, results)
    return results


def level_order_traversal_recursion(root):
    height = Node_Depth.nodeDepths(root)
    results = []
    for level in range(height):
        printNode(root,level, results)
        results.append("#")
    return results

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f
f.right=g
g.left=h

print(level_order_traversal_recursion(a))
