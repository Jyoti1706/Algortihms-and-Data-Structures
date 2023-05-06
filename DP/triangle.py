'''
https://leetcode.com/problems/triangle/?envType=study-plan-v2&id=dynamic-programming
'''
from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        sumation = sum(triangle[0])
        n = len(triangle)
        idx = 0
        for i in range(1,n):
            try:
                if triangle[i][idx] <= triangle[i][idx+1]:
                    sumation = sumation+triangle[i][idx]
                else:
                    sumation = sumation+triangle[i][idx+1]
                    idx = idx+1
            except:
                sumation = sumation + triangle[i][idx]
        return sumation

    def minimumTotal(self, triangle):
        dp = [0]*(len(triangle)+1)
        for row in triangle[::-1]:
            print(row)
            for i,n in enumerate(row):
                dp[i] = n+min(dp[i], dp[i+1])
        return dp[0]

triangle = [[-10]] #[[2],[3,4],[6,5,7],[4,1,8,3]]
ob = Solution()
print(ob.minimumTotal(triangle))