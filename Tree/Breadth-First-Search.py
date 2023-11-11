class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def breadth_First_Traversal(root):
    queue = [root]
    results = []
    if root == [] or root is None:
        return []
    while len(queue) > 0:
        curr_node = queue.pop(0)
        results.append(curr_node.val)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    return results


print(breadth_First_Traversal(a))
