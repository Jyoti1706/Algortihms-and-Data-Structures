from typing import List


class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum(self, nums: List[int], target: int):
        """
        using Backtracking with take and skip concept
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        result = set([])

        def solve(idx, target, temp):
            if idx >= n or target <= 0:
                if target == 0:
                    result.add(tuple(temp))
                    return
                else:
                    return
            curr = temp.copy()
            curr.append(nums[idx])
            solve(idx, target - nums[idx], curr)
            solve(idx + 1, target, temp)

        solve(0, target, [])
        return list(result)

    def combinationSum2(self, nums: List[int], target: int):
        """
        using Backtracking with take and skip concept
        :param nums:
        :param target:
        :return:
        """
        n = len(nums)
        result = set([])

        def solve(idx, target, temp):
            if idx >= n or target <= 0:
                if target == 0:
                    result.add(tuple(temp))
                    return
                else:
                    return
            curr = temp.copy()
            if nums[idx] not in temp:
                curr.add(nums[idx])
                solve(idx, target - nums[idx], curr)
                solve(idx + 1, target, temp)
            else:
                return

        solve(0, target, set([]))
        return list(result)


if __name__ == "__main__":
    obj = Solution()
    # nums = [2, 3, 6, 7]
    # target = 7
    # print(obj.combinationSum(nums, target))
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(obj.combinationSum2(candidates, target))
