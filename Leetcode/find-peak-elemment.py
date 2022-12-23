'''
https://leetcode.com/problems/find-peak-element/description/
Approach, Divide and Conqure similar to Binary Searc
'''
from typing import List


def findPeakElement_Recursion(nums, lo, hi):
    mid = (lo + hi) // 2
    if len(nums) <= 2:
        if len(nums)==2:
            if nums[1]> nums[0]:
                return 1
        return lo
    elif nums[mid - 1] < nums[mid] > nums[mid + 1]:
        return mid
    elif nums[mid - 1] > nums[mid]:
        return findPeakElement_Recursion(nums, lo, mid - 1)
    elif nums[mid + 1] > nums[mid]:
        return findPeakElement_Recursion(nums, mid + 1, hi)
    else:
        print(f"Debug, edge case missing array: {nums}, low : {lo}, high : {hi}")


nums = [1, 2]
print(findPeakElement_Recursion(nums, 0, len(nums)))


def findPeakElement_Iteration(nums):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid - 1 >= lo and mid + 1 <= hi and nums[mid - 1] <= nums[mid] >= nums[mid + 1]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            hi = mid - 1
        elif nums[mid + 1] > nums[mid]:
            lo = mid + 1
        else:
            return mid



nums=[1,2]
print(findPeakElement_Iteration(nums))
