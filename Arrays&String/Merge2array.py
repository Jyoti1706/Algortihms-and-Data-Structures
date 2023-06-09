'''
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

'''
import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        data = math.inf
        for k in range(m,len(nums1)):
            nums1[k] = data
        counter = 0
        i = 0
        j = 0
        while i < m+counter:
            while j <n:
                if nums1[i]<nums2[j]:
                    i=i+1
                else:
                    nums1 = shift(nums1, i, m+counter, nums2[j])
                    i=i+1
                    j=j+1
                    counter=counter+1
        return nums1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()
def shift(nums, i , length, element):
    j=length
    while j > i:
        print(j,i)
        print(nums[j-1],nums[j])
        nums[j]=nums[j-1]
        j-=1
    #nums[j] = nums[i]
    nums[i]=element
    return nums

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

obj = Solution()
print(obj.merge(nums1, m, nums2, n))
