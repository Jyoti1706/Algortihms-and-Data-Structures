import math
from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0)+1
        result = 0
        for key in freq:
            if freq[key] == 1:
                return -1
            result += math.ceil(freq[key]/3)
        return result





if __name__ == "__main__":
    obj = Solution()
    nums = [2, 3, 3, 2, 2, 4, 2, 3, 4]
    print(obj.minOperations(nums))
    nums = [2, 1, 2, 2, 3, 3]
    print(obj.minOperations(nums))
