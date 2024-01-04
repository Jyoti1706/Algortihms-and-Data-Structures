class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbStairsmemo(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in memo.keys():
                return memo[n]
            memo[n] = climbStairsmemo(n - 1) + climbStairsmemo(n - 2)
            return memo[n]

        return climbStairsmemo(n)


obj = Solution()
n = 5
print(obj.climbStairs(n))
