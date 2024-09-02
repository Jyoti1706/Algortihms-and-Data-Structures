from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    elif dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
        max_seq = max(dp)
        resultant_index = 0
        for i, seq in enumerate(dp):
            if seq == max_seq:
                resultant_index += count[i]
        return resultant_index


if __name__=="__main__":
    obj = Solution()
    nums = [1, 3, 5, 4, 7]
    print(obj.findNumberOfLIS(nums))
    nums = [2, 2, 2, 2, 2]
    print(obj.findNumberOfLIS(nums))