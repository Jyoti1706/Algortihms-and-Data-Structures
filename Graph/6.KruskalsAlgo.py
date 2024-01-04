


class Solution:
    def __init__(self, n):
        # self.rank = [0 for _ in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.parent = [i for i in range(n + 1)]

    def spanningTree(self, V, adj):
        edgelist = adj  # []
        # for u in range(V):
        #     for v, wt in adj[u]:
        #         edgelist.append([wt, u, v])
        edgelist.sort()
        print(edgelist)
        return self.kruskal(edgelist)

    def kruskal(self, edgelist):
        path_sum = 0
        for edge in edgelist:
            wt, u, v = edge
            parent_u = self.find(u)
            parent_v = self.find(v)
            if parent_v != parent_u:
                self.union(u, v)
                print(f"edge considered [weight, u, v] :: {edge} ")
                path_sum += wt
        return path_sum

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_v == parent_u:
            return
        if self.size[parent_u] <= self.size[parent_v]:
            self.parent[u] = parent_v
            self.size[parent_v] += self.parent[parent_u]
        else:
            self.parent[parent_v] = parent_u
            self.size[parent_u] += self.size[parent_v]


V = 7
edgeList = [[5, 0, 1], [20, 0, 3], [1, 1, 2], [5, 2, 3], [1, 3, 4], [2, 4, 5], [2, 5, 6], [4, 4, 6]]
obj = Solution(V)
print(obj.spanningTree(V, edgeList))
