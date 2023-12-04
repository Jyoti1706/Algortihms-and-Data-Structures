"""  ********** Not Solved ********************** #Todo
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The
added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is
represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai
and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
return the answer that occurs last in the input.

"""
from collections import defaultdict

"""https://www.geeksforgeeks.org/problems/detect-cycle-using-dsu/1"""


class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u = self.find(u)
        ulp_v = self.find(v)
        if ulp_v == ulp_u:
            return
        if self.rank[ulp_v] > self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1


class Solution:

    # Function to detect cycle using DSU in an undirected graph.
    def findRedundantConnection(self, edges):
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        res=[]
        print(adj)
        V = len(adj.keys())
        ds = DisjointSet(V)
        for u in range(1,V):
            for v in adj[u]:
                if u<v:
                    parentU=ds.find(u)
                    parentV = ds.find(v)
                    if parentV == parentU:
                        res.append([u,v])
                    ds.union(u,v)
        return res


if __name__ == "__main__":
    obj = Solution()
    edges = [[1, 2], [1, 3], [2, 3]]
    print(obj.findRedundantConnection(edges))
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(obj.findRedundantConnection(edges))
    edges = [[1, 2], [2, 3], [3, 4], [1, 5]]
    print(obj.findRedundantConnection(edges))



