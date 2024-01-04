import collections
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)  ### Indegree map
        for src, dest in edges:
            adj[dest].append(src)
        res = []
        for i in range(n):
            if not adj[i]:
                res.append(i)
        return res
