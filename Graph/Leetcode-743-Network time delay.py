import heapq
import math


class Solution:
    def networkDelayTime(self, times, n, k):
        res = [math.inf for _ in range(n+1)]
        res[0] = -1
        adj = {node:[] for node in range(n+1)}
        for t in times:
            u, v, w = t
            adj[u].append([v,w])
        res[k] = 0
        minheap = [[0, k]]
        heapq.heapify(minheap)
        while minheap:
            dis, node = heapq.heappop(minheap)
            for neihbour in adj[node]:
                nei = neihbour[0]
                d = neihbour[1]
                tdis = dis + d
                if tdis < res[nei]:
                    heapq.heappush(minheap, [tdis, nei])
                    res[nei] = tdis
        result = max(res)
        return -1 if result == math.inf else result


obj = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(obj.networkDelayTime(times,n,k))