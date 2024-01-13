"""
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/

"""
from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        The solution creates a graph representation of the tree using a default dictionary g of lists in the dfs
        (Depth-First Search) function.
        BFS Algorithm:

        The solution sets up a while loop that continues until the queue q is empty,
        signifying that there are no more nodes to be infected.
        :param root:
        :param start:
        :return:
        Return Value:

            By the end of the BFS loop, ans holds the number of minutes it took to infect the entire tree since each
            loop iteration represents one minute of infection time passing.
            The return value ans represents the required number of minutes for the infection to spread through the
            entire tree, as determined by our BFS algorithm.
        """
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time


node1 = TreeNode(1)
node5 = TreeNode(5)
node3 = TreeNode(3)
node4 = TreeNode(4)
node10 = TreeNode(10)
node6 = TreeNode(6)
node9 = TreeNode(9)
node2 = TreeNode(2)
root = [1, 5, 3, None, 4, 10, 6, 9, 2]
node1.left = node5
node1.right = node3
node5.right = node4
node4.left = node9
node4.right = node2
node3.left = node10
node3.right = node6
start = 3

obj = Solution()
print(obj.amountOfTime(node1, node3))
