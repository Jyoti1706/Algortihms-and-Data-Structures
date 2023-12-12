import math


class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex S
    def dijkstra(self, V, adj, S):
        process = set()
        result = [math.inf for _ in range(V)]
        result[S] = 0
        process.add((0, S))
        while process:
            #dis, node = -1,-1
            for i in iter(process):
                dis = i[0]
                node = i[1]
                break
            process.remove((dis, node))
            for neihbour in adj[node]:
                nei = neihbour[0]
                d = neihbour[1]
                tdis = dis + d
                if tdis < result[nei]:
                    process.discard((result[nei], nei))
                    process.add((tdis, nei))
                    result[nei] = tdis

        return result


obj = Solution()
V = 3
S = 2
aj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
print(obj.dijkstra(V, aj, S))

V = 2
adj = [[[1, 9]], [[0, 9]]]
S = 0
print(obj.dijkstra(V, adj, S))
