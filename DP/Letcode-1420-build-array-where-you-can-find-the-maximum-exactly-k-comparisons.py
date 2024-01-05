class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = int(1e9 + 7)
        dp = {}

        def Solve(idx, sc, maximum):
            if idx == n:
                if sc == k:
                    return 1
                return 0
            res = 0
            if (idx, sc, maximum) in dp:
                return dp[(idx, sc, maximum)]
            for i in range(1, m + 1):
                if i > maximum:
                    res = (res + Solve(idx + 1, sc + 1, i)) % MOD # if i > maximum so far then search cost will increase
                else:
                    res = (res + Solve(idx + 1, sc, maximum)) % MOD
            dp[(idx, sc, maximum)] = res % MOD   # Memoization
            return dp[(idx, sc, maximum)]
            # idx, search cost, max so far

        return Solve(0, 0, -1)
