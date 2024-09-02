class Solution:
    def removeDuplicates(self, nums):
        _next = 0
        idx = 0
        length = len(nums)
        while idx < length:
            while idx < length and nums[idx] != nums[_next] :
                _next += 1
                nums[_next] = nums[idx]

            idx += 1
        return _next + 1


obj = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4]
#nums = [1]
print(obj.removeDuplicates(nums))
