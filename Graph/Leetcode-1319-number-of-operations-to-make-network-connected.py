"""

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer
directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected
computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not
possible, return -1.


"""


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


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        if len(connections) < n - 1:
            return -1
        ds = DisjointSet(n)
        component = n
        for edge in connections:
            u = edge[0]
            v = edge[1]
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                component -= 1
        return component - 1


if __name__ == "__main__":
    obj = Solution()
    n = 4
    connections = [[0, 1], [0, 2], [1, 2]]
    print(obj.makeConnected(n, connections) == 1)

    n = 6
    connections = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print(obj.makeConnected(n, connections) == 2)
