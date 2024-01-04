'''
https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=dynamic-programming
'''
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [-1 for _ in range(n)]

        # memo[0]=nums[0]
        # memo[1]=nums[1]

        def solve(idx):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]
            steal = nums[idx] + solve(idx + 2)
            skip = solve(idx + 1)
            memo[idx] = max(steal, skip)
            return memo[idx]

        solve(0)
        print(memo)
        return max(memo[0], memo[1])

    def rob_tabulation(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        memo = [0 for _ in range(n + 1)]
        memo[0]=0
        memo[1] = nums[0]
        for i in range(2,n+1):
            steal = nums[i-1]+memo[i-2]
            skip = memo[i-1]
            memo[i] = max(steal,skip)
        return memo[-1]


if __name__=="__main__":
    obj = Solution()
    nums = [1, 2, 3, 1]
    print(obj.rob(nums))