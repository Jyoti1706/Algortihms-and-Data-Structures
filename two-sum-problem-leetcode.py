'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
'''
from typing import List
#
# arr_len, target = map(int, input().split())
# n = list(map(int, input().split()))
# flag = False
# for p1 in range(arr_len):
#     for p2 in range(p1+1, arr_len):
#         if n[p2] == target-n[p1]:
#             print(f"sum is found at indexes {p1} and {p2}")
#             flag = True
#             break
#     if flag :
#         break
# if not flag:
#     print("No Solution Found")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr_len = len(nums)
        for p1 in range(arr_len):
            for p2 in range(p1 + 1, arr_len):
                if nums[p2] == target - nums[p1]:
                    return [p1,p2]
        return None

    def twoSum_Optimized(self, nums: List[int], target: int) -> List[int]:
        '''
        :param nums:
        :param target:
        :return:
        time time taken: 63 ms o(n)
        '''
        arr_len = len(nums)
        hashmap = {}
        for p1 in range(arr_len):
            ntf = target-nums[p1]
            p2 = -1
            print(ntf, hashmap)
            try:
                p2 = hashmap[nums[p1]]
                return [p1, p2] if p1<p2 else [p2,p1]
            except:
                hashmap[ntf] = p1
        return None

    def twoSum_Optimized2(self, nums: List[int], target: int) -> List[int]:
        '''
        time: 64ms o(n)
        :param nums:
        :param target:
        :return:
        '''
        arr_len = len(nums)
        hashmap = {}
        for p1 in range(arr_len):
            hashmap[nums[p1]] = p1
        for p1 in range(arr_len):
            ntf = target-nums[p1]
            try:
                p2 = hashmap[ntf]
                if p2 == p1:
                    continue
                return [p1, p2] if p1<p2 else [p2,p1]
            except:
                continue
        return None

obj = Solution()
print(obj.twoSum_Optimized2(nums = [2,3,5,2,7],target = 10))







