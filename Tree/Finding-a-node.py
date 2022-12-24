from Tree.Tree_DS import *
def BFS_Finding_Element(root, target):
    queue = [root]
    if root ==[] or root is None:
        return False
    while len(queue)>0:
        curr_node = queue.pop(0)
        if (curr_node.val==target):
            return True
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
    return False

#print(BFS_Finding_Element(a,'k'))

def DFS_Search_Tree(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    left_res = DFS_Search_Tree(root.left,target)
    right_res = DFS_Search_Tree(root.right, target)
    return left_res or right_res


print(DFS_Search_Tree(a,'e'))
print(DFS_Search_Tree(a,'f'))
print(DFS_Search_Tree(a,'k'))
print(DFS_Search_Tree(a,'c'))
