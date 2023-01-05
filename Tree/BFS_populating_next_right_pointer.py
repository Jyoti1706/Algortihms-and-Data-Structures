class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def BFS_populating_next_right_pointers_in_each_node_ii(root):

    if root == [] or root is None:
        return []
    queue = [root]
    level_node_count = len(queue)
    view_results=[]
    results = []
    counter = 0
    while len(queue) > 0:
        curr_node = queue.pop(0)
        counter += 1

        results.append(curr_node)
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)
        if counter == level_node_count:
            level_node_count = len(queue)
            counter = 0
            try:
                for i in range(len(results)):
                    view_results.append(results[i].val)
                    results[i].right = results[i+1]
            except:
                results[-1].right=None
                view_results.append("#")
            results = []
    return view_results


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(7)

a.left=b
a.right=c
b.left=d
b.right=e
c.right=f


print(BFS_populating_next_right_pointers_in_each_node_ii(a))
a1=Node()
print(BFS_populating_next_right_pointers_in_each_node_ii([]))