import heapq
import math
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        i = 0
        j = len(costs)-1
        pq1 = []
        heapq.heapify(pq1)
        pq2 = []
        heapq.heapify(pq2)
        hire = 1
        while hire <= k:
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1,costs[i])
                i += 1
            while len(pq2) < candidates and j >= i:
                heapq.heappush(pq2,costs[j])
                j -= 1
            min_pq1 = pq1[0] if pq1 else math.inf
            min_pq2 = pq2[0] if pq2 else math.inf
            if min_pq1 <= min_pq2:
                total_cost += min_pq1
                heapq.heappop(pq1)
            else:
                total_cost += min_pq2
                heapq.heappop(pq2)
            hire += 1
        return total_cost


if __name__ == "__main__":
    obj = Solution()
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    print(obj.totalCost(costs,k,candidates))
    costs = [1, 2, 4, 1]
    k = 3
    candidates = 3
    print(obj.totalCost(costs,k,candidates))