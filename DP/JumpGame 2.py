class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps =0
        l = r=0
        while r < len(nums)-1:
            far = 0
            for i in range(l,r+1):
                far = max(far,i+nums[i])
            l=r+1
            r=far
            steps += 1
        return steps