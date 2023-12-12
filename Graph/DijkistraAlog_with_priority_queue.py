"""
https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
"""
import heapq
import math


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S
    def dijkstra(self, V, adj, S):
        res = [math.inf for _ in range(V)]
        res[S] = 0
        minheap = [[0,S]]
        heapq.heapify(minheap)
        while minheap:
            dis, node = heapq.heappop(minheap)
            for neihbour in adj[node]:
                nei = neihbour[0]
                d = neihbour[1]
                tdis = dis+d
                if tdis < res[nei]:
                    heapq.heappush(minheap,[tdis, nei])
                    res[nei] = tdis
        return res


obj = Solution()
V = 3
S = 2
aj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
print(obj.dijkstra(V, aj, S))

V = 2
adj = [[[1, 9]], [[0, 9]]]
S = 0
print(obj.dijkstra(V, adj, S))