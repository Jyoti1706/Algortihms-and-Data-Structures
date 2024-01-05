from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if pairs[i][0]>pairs[j][1]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)