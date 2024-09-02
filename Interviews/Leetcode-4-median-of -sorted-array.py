"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:
    def findMedianSortedArrays_Solution1(self, nums1, nums2):
        i = 0
        j = 0
        nums = []
        n = len(nums1)
        m = len(nums2)
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < n:
            nums.append(nums1[i])
            i += 1
        while j < m:
            nums.append(nums2[j])
            j += 1

        if (n + m) % 2 == 1:
            return nums[(n + m) // 2]
        else:
            return (nums[(n + m) // 2] + nums[((n + m) // 2) - 1]) / 2

    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        size = m + n

        idx1 = size // 2
        ele1 = -1
        idx2 = size // 2 - 1
        ele2 = -1
        i = 0
        j = 0
        k = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if k == idx1:
                    ele1 = nums1[i]
                if k == idx2:
                    ele2 = nums1[i]
                i += 1
            else:
                if k == idx1:
                    ele1 = nums2[j]
                if k == idx2:
                    ele2 = nums2[j]
                j += 1
            k += 1
        while i < n:
            if k == idx1:
                ele1 = nums1[i]
            if k == idx2:
                ele2 = nums1[i]
            i += 1
            k += 1
        while j < m:
            if k == idx1:
                ele1 = nums2[j]
            if k == idx2:
                ele2 = nums2[j]
            j += 1
            k += 1
        if size % 2 == 1:
            return ele1
        return (ele1 + ele2) / 2


nums1 = [1, 2]
nums2 = [3, 4]
obj = Solution()
print(obj.findMedianSortedArrays(nums1, nums2))
