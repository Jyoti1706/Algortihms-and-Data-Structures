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
    def detectCycle(self, V, adj):
        ds = DisjointSet(V)
        for u in range(0,V):
            for v in adj[u]:
                if u<v:
                    parentU=ds.find(u)
                    parentV = ds.find(v)
                    if parentV == parentU:
                        return True
                    ds.union(u,v)
        return False


