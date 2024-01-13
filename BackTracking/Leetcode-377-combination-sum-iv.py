"""
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:
------------------
Input: nums = [9], target = 3
Output: 0

"""
from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4_Method1(self, nums: List[int], target: int) -> int:
        """
        using Backtracking with take and skip concept
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        dp = {}

        def solve(idx, target):
            if idx >= n or target <= 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if (idx, target) in dp:
                return dp[(idx, target)]
            take = solve(0, target - nums[idx])
            skip = solve(idx + 1, target)
            dp[(idx, target)] = take + skip
            return dp[(idx, target)]

        return solve(0, target)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        using Backtracking with take and skip concept
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        dp = {}

        def solve(idx, target):
            if idx >= n or target <= 0:
                if target == 0:
                    return 1
                else:
                    return 0
            if (idx, target) in dp:
                return dp[(idx, target)]
            result = 0
            for idx in range(n):
                take_i = solve(idx, target - nums[idx])
                result += take_i
            dp[(idx, target)] = result
            return dp[(idx, target)]

        return solve(0, target)


class Solution_2:
    def combinationSum4(self, nums: list[int], target: int) -> int:

        @lru_cache(None)
        def dp(target: int, res=0) -> int:

            for n in nums:

                if n == target: res += 1
                if n < target: res += dp(target - n)

            return res

        return dp(target)


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3]
    target = 4
    print(obj.combinationSum4(nums, target))

    nums = [9]
    target = 3
    print(obj.combinationSum4(nums, target))
