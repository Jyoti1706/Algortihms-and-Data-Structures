"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""
from collections import defaultdict


def create_adjacency_list(edge_list):
    adjacency_list = defaultdict(set)

    for edge in edge_list:
        node1, node2 = edge

        # Adding node2 to the adjacency list of node1
        adjacency_list[node1].add(node2)

        # Adding node1 to the adjacency list of node2 (assuming the graph is undirected)
        adjacency_list[node2].add(node1)

    return adjacency_list

class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        visited = [False for _ in range(n)]

        adj_lst = create_adjacency_list(edges)

        def dfs(adj_lst, source, visited):
            # Mark the current vertex as visited
            visited[source] = True
            print(source, end=' ')

            # Recur for all the adjacent vertices
            for neighbor in adj_lst[source]:
                if not visited[neighbor]:
                    dfs(adj_lst, neighbor, visited)
        dfs(adj_lst,source,visited)
        return visited[destination]

obj = Solution()
edges= [[0,4]]
print(obj.validPath(5, edges, 0,4))
