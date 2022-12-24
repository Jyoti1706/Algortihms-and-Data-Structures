## Creating a Tree

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

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

def depth_search_tree_iterative(root):
    if root == []  or root==None:
        return []
    stack = [root]
    results =[]
    while len(stack)>0:
        curr_node=stack.pop()
        results.append(curr_node.val)
        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left is not None:
            stack.append(curr_node.left)
    return results

#print(depth_search_tree_iterative(a))

def depth_search_tree_recursive(root):
    if root ==[] or root is None:
        return []
    left = depth_search_tree_recursive(root.left)
    right = depth_search_tree_recursive(root.right)
    return [root.val, *left, *right]

print(depth_search_tree_recursive(a))