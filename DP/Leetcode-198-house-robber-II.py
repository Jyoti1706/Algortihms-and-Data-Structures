class Solution:
    def rob(self, nums):

        def houseRobberI(arr):
            n = len(arr)
            memo = [-1 for _ in range(n + 1)]

            def recursion(idx):
                if idx >= n:
                    return 0
                if memo[idx] != -1:
                    return memo[idx]
                steal = arr[idx] + recursion(idx + 2)
                skip = recursion(idx + 1)
                memo[idx] = max(steal, skip)
                print(memo)
                return memo[idx]

            recursion(0)
            return max(memo[0], memo[1])

        return max(houseRobberI(nums[1:]), houseRobberI(nums[:-1]))

    def rob2_Tabulation(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        t = [0 for _ in range(n+1)]

        for i in range(1,n):
            skip = t[i-1]
            steal = nums[i-1]+t[i-2] if (i-2)>=0 else 0
            t[i] = max(skip,steal)
        result1 = t[n-1]
        t = [0 for _ in range(n+1)]
        for i in range(2, n+1):
            skip = t[i - 1]
            steal = nums[i - 1] + t[i - 2] if (i - 2) >= 0 else 0
            t[i] = max(skip, steal)
        result2 = t[n]
        return max(result1, result2)

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3, 1, 4]
    #print(obj.rob2_Tabulation(nums))
    # nums = [2, 3, 2]
    # print(obj.rob2_Tabulation(nums))
    nums = [1, 2, 3]
    print(obj.rob2_Tabulation(nums))
