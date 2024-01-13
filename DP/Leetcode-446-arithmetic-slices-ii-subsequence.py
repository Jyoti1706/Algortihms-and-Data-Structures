"""
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.


Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        mp = [{} for _ in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                dif = nums[i] - nums[j]
                count = mp[j].get(dif, 0)

                mp[i][dif] = mp[i].get(dif, 0)+count+1

                result += count
        return result


if __name__ == "__main__":
    obj = Solution()
    nums = [2, 4, 6, 8, 10]
    print(obj.numberOfArithmeticSlices(nums))
    nums = [7,7,7,7,7]
    print(obj.numberOfArithmeticSlices(nums))
