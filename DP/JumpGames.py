'''
PS ::: https://leetcode.com/problems/jump-game/?envType=study-plan&id=dynamic-programming-i
'''

class Solution(object):
    def canJump_basic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps = 0
        goal =len(nums)-1
        if goal == 0:
            return True
        while steps < len(nums):
            if nums[steps] == 0:
                return False
            steps = steps + nums[steps]
            if steps >= goal :
                return True
        return False

    def canJump(self, nums):
        goal = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal = i
        return True if goal == 0 else False

ob = Solution()
nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]

nums3 =[2,5,0,0] #[2,0]
#print(ob.canJump(nums1))
#print(ob.canJump(nums2))
print(ob.canJump(nums3))