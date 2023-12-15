import heapq


class Solution:

    def minCostConnectPoints(self, points):
        V = len(points)
        visited = [False for _ in range(V)]
        adj = {node:[] for node in range(V)}
        for i in range(V):
            for j in range(i, V):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                dis = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([j, dis])
                adj[j].append([i, dis])

        minheap = [[0,0],]
        heapq.heapify(minheap)
        s = 0
        while minheap:
            wt, currnode = heapq.heappop(minheap)
            if visited[currnode]:
                continue
            visited[currnode]=True
            s += wt
            for neighbour in adj[currnode]:
                n_node, dis = neighbour
                if not visited[n_node]:
                    heapq.heappush(minheap, [dis, n_node])
        return s