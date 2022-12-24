from Tree.Tree_DS import Node
def recursive_sum_of_node(root):
    if root == [] or root is None:
        return 0

    return root.val+recursive_sum_of_node(root.left)+recursive_sum_of_node(root.right)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(recursive_sum_of_node(a))

