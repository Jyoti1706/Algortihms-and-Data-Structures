class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def breadth_First_Traversal_Right_View(root):

    if root == [] or root is None:
        return []
    queue = [root]
    level_node_count = len(queue)
    right_view_results=[]
    results = []
    counter = 0
    while len(queue) > 0:
        curr_node = queue.pop(0)
        counter += 1

        results.append(curr_node.val)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
        if counter == level_node_count:
            level_node_count = len(queue)
            counter = 0
            right_view_results.append(results[-1])
            results = []
    return right_view_results

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

print(breadth_First_Traversal_Right_View(a))
