"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

"""
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {node: [] for node in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(adj, curr, parent, hasApple):
            time = 0
            for child in adj[curr]:
                if child == parent:
                    continue
                time_from_child = dfs(adj, child, curr, hasApple)
                if time_from_child>0 or hasApple[child]:
                    time += time_from_child+2
            return time
        return dfs(adj, 0, -1, hasApple)