from typing import List


class Solution:
    def lengthOfLISMethod1(self, nums: List[int]) -> int:
        """
        Top-Down Approach + memoization , This leads to time exceed error in Leetcode.
        Base Case: idx>len(nums) return 0
        1. we have 2 option. either to take that idx or leave that idx
        2. we will take only when nums[idx]<nums[prev] and add 1 to it as we add that element to subsequence
        3. return max(take, skip)

        :param nums:
        :return:
        """
        n = len(nums)
        previous = -1
        dp = [[-1 for _ in range(2501)] for _ in range(2501)]

        def solve(idx, prev):
            take = -1
            if idx >= n:
                return 0
            if dp[idx][prev] != -1:
                return dp[idx][prev]
            if prev == -1 or nums[prev] < nums[idx]:
                take = 1+solve(idx+1, idx)
            skip = solve(idx+1, prev)
            dp[idx][prev] = max(take, skip)
            return dp[idx][prev]
        return solve(0, previous)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)

if __name__ == "__main__":
    obj = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(obj.lengthOfLIS(nums))
    nums = [0, 1, 0, 3, 2, 3]
    print(obj.lengthOfLIS(nums))
    nums = [7, 7, 7, 7, 7, 7, 7]
    print(obj.lengthOfLIS(nums))