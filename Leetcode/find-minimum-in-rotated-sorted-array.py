class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums)-1
        mid = i + j // 2
        while i<j:
            mid = (i+j)//2
            if nums[mid-1]> nums[mid] and nums[mid+1]>nums[mid]:
                return nums[mid]
            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid-1
        return nums[i]

ob = Solution()
nums = [4,5,6,7,0,1,2]
nums = [3,4,5,1,2] #[11,13,15,17]
print(ob.findMin(nums))