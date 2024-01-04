import math
from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1 for _ in range(len(cost))]
        n = len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]

        def dp(n):
            if n == 0:
                return cost[0]
            if n < 0:
                return 0
            if memo[n] != -1:
                return memo[n]
            left = dp(n - 1) + cost[n]
            right = dp(n - 2) + cost[n]
            memo[n] = min(left, right)
            return memo[n]

        dp(n - 1)
        return min(memo[-1], memo[-2])

    def minCostClimbingStairs_Tabulation(self, cost: List[int]) -> int:
        memo = [-1 for _ in range(len(cost))]
        n = len(cost)
        memo[0] = cost[0]
        #memo[1] = cost[1]
        for i in range(1, n):
            fs = memo[i - 1] + cost[i - 1]
            ss = math.inf
            if i > 1:
                ss = memo[i - 2] + cost[i - 2]
            memo[i] = min(fs, ss)
        return memo[-1]


obj = Solution()
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]  # Output: 6
print(obj.minCostClimbingStairs(cost))
print(obj.minCostClimbingStairs2(cost))
cost = [10, 15, 20]  # Output: 15
print(obj.minCostClimbingStairs(cost))
print(obj.minCostClimbingStairs2(cost))
cost = [1, 100]  # Output: 1
print(obj.minCostClimbingStairs(cost))
print(obj.minCostClimbingStairs2(cost))
