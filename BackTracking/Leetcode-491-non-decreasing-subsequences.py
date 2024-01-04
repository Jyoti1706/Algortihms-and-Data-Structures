"""
https://leetcode.com/problems/non-decreasing-subsequences/description/

DESCRIPTION:
-------------

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at
least two elements. You may return the answer in any order.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = set()

        def backtrack(nums, idx, curr):
            if len(curr) > 1:
                results.add(tuple(curr))
            st = set()
            for i in range(idx, n):
                if (len(curr) == 0 or nums[i] >= curr[-1]) or (len(st)>0 and list(st)[-1] == nums[i]):
                    curr.append(nums[i])
                    backtrack(nums, i + 1, curr)
                    curr.pop(-1)
                    st.add(nums[i])

        curr = []
        backtrack(nums, 0, curr)
        return list(results)


if __name__ == "__main__":
    obj = Solution()
    nums = [4, 6, 7, 7]
    print(obj.findSubsequences(nums))
    nums = [4, 4, 3, 2, 1]
    print(obj.findSubsequences(nums))
