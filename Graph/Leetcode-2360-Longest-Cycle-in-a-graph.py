
"""
https://leetcode.com/problems/longest-cycle-in-a-graph/description/

#todo

"""
from collections import defaultdict
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = defaultdict(list)

        for u, v in enumerate(edges):
            if v == -1: continue
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([node for node, indeg in enumerate(indegree) if indeg == 0])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                edges[node] = -1

                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in enumerate(edges):
            if v == -1: continue
            pu, pv = find(u), find(v)
            if pu == pv: continue
            if rank[pu] <= rank[pv]:
                parent[pv] = pu
                rank[pu] += rank[pv]
            else:
                parent[pu] = pv
                rank[pv] += rank[pu]
        mx = max(rank)
        return mx if mx != 1 else -1
