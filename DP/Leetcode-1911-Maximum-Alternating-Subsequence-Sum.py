class Solution:

    def maxAlternatingSum(self, nums):
        # t = {(-1, -1): 0 for _ in range(1000001)}
        t = {}
        n = len(nums)

        def solve(idx, nums, flag):
            if idx >= n:
                return 0
            if (idx, flag) in t:
                return t[(idx, flag)]
            skip = solve(idx + 1, nums, flag)
            val = nums[idx]
            if not flag:
                val = -1 * val
            take = solve(idx + 1, nums, not (flag)) + val
            t[(idx, flag)] = max(skip, take)
            return t[(idx, flag)]

        return solve(0, nums, True)

    def maxAlternatingSumArray(self, nums):
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ans += nums[i] - nums[i + 1]
        ans += nums[-1]
        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [4, 2, 5, 3]
    print(obj.maxAlternatingSum(nums))
    nums = [51, 32, 207, 373, 174, 56, 128, 99, 98, 275, 230, 72, 217, 94, 143, 237, 128, 39, 227, 282, 51, 26, 334,
            277, 8, 48, 386, 122, 86, 209, 249, 247, 110, 206, 31, 85, 195, 2, 200, 136, 233, 147, 217, 357, 375, 285,
            339, 368, 250, 80, 98, 152, 112, 30, 297, 377, 278, 32, 383, 161, 30, 26, 300, 245, 258, 272, 81, 30, 261,
            42, 96, 36, 305, 35, 346, 121, 207, 62, 292, 127, 297, 305, 21, 318, 42, 215, 337, 299, 290, 268, 162, 134,
            105, 343, 367, 161, 123, 136, 203, 68]
    print(obj.maxAlternatingSum(nums))
