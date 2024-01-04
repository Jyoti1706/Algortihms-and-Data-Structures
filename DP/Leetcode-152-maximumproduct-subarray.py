"""
https://leetcode.com/problems/maximum-product-subarray/
"""

class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        currMin, currMax = 1,1
        for n in nums:
            if n ==0:
                currMin, currMax = 1,1
                continue
            tmp = currMax
            currMax = max(tmp*n, currMin*n, n)
            currMin = min(tmp*n, currMin*n, n)
            res = max(res, currMax)
        return res