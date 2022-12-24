import math

from Tree.Tree_DS import Node


def max_sum_path(root):
    if root is None:
        return (math.inf) * -1
    if root.left is None and root.right is None:
        return root.val
    max_child = max(max_sum_path(root.left), max_sum_path(root.right))
    return root.val + max_child

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(max_sum_path(a))