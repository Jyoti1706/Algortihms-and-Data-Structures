'''https://leetcode.com/problems/delete-and-earn/?envType=study-plan&id=dynamic-programming-i'''
from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1,earn2 =0,0

        for i in range(len(nums)):
            curr = nums[i]*count[nums[i]]
            if i > 0 and nums[i] == nums[i-1]+1:
                temp = max(earn1+curr, earn2)
                earn1 = earn2
                earn2=temp
            else:
                temp = curr+earn2
                earn1=earn2
                earn2=temp
        return earn2

ob = Solution()
nums = [2,2,3,3,3,4]
print(ob.deleteAndEarn(nums))