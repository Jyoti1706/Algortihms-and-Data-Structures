from collections import deque
from typing import List


def create_graph_AL(vertices, list):
    adj_list = {vertice: list[vertice] for vertice in range(vertices)}
    return adj_list


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycleDFS(self, V: int, adj: List[List[int]]):
        graph = create_graph_AL(V, adj)
        visited = [False for _ in range(V)]
        parent = -1

        def dfs(graph, node, visited, parent):
            visited[node] = True
            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if visited[neighbour]:
                    return True
                if dfs(graph, neighbour, visited, node):
                    return True
            return False
        for vertice in range(V):
            if not visited[vertice] and dfs(graph, vertice, visited, parent=-1):
                return True
        return False

    def isCycleBFS(self, V: int, adj: List[List[int]]):
        graph = create_graph_AL(V, adj)
        visited = [False for _ in range(V)]
        parent = -1

        def bfs(graph, visited, node, parent):
            visited[node] = True
            queue = deque()
            queue.append((node,parent))
            while len(queue)>0:
                curr, parent = queue.popleft()
                for neighbour in graph[curr]:
                    if neighbour == parent:
                        continue
                    elif visited[neighbour]:
                        return True
                    else:
                        visited[neighbour]=True
                        queue.append((neighbour,curr))
            return False

        for vertice in range(V):
            if not visited[vertice] and bfs(graph, visited, vertice, parent=-1):
                return True
        return False



V = 5
adj = [[2, 3, 1], [0], [0, 4], [0, 4], [2, 3]]

obj = Solution()
print(obj.isCycleBFS(V, adj))

V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(obj.isCycleBFS(V, adj))