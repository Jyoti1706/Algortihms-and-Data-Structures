# User function Template for python3
import heapq


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # code here
        minheap = [[0,0],]
        heapq.heapify(minheap)
        visit = [False for _ in range(V)]
        summation = 0
        heapq.heapify(minheap)
        while minheap:
            wt , currnode = heapq.heappop(minheap)
            #summation += wt
            if visit[currnode]:
                continue
            visit[currnode] = True
            summation += wt
            for tmp in adj[currnode]:

                neighbour_weight = tmp[0]
                neighbour = tmp[1]
                if not visit[neighbour]:
                    heapq.heappush(minheap, [neighbour_weight, neighbour])
        return summation
