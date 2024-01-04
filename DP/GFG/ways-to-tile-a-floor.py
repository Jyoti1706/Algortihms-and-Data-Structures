class Solution:
    def numberOfWays(self, N):
        # code here
        memo = {}

        def recursion(N):
            res = memo.get(N,-1)
            if res == -1:
                if N < 2:
                    memo[N]=1
                    return 1
                memo[N] = recursion(N-1)+recursion(N-4)
                res = memo[N]
            return res
        return recursion(N)


if __name__=="__main__":
    obj = Solution()
    N = 24151
    print(obj.numberOfWays(N))