"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/
"""


class Solution:
    def maxValueOfCoinsKT(self, piles, k):
        """
        Khandani Tarika :: Recursion and Memoization
        :param piles: 
        :param k: 
        :return: 
        """
        n = len(piles)
        dp = {}

        def solve(piles, i, k):
            if i >= n:
                return 0

            if (i, k) in dp:
                return dp[(i, k)]
            notTaken = solve(piles, i + 1, k)
            summation = 0
            taken = 0
            for j in range(min(len(piles[i]), k)):
                summation += piles[i][j]
                taken = max(taken, summation + solve(piles, i + 1, k - (j + 1)))
            dp[(i, k)] = max(taken, notTaken)
            return dp[(i, k)]

        return solve(piles, 0, k)

    def maxValueOfCoins(self, piles, k):
        """
        Bottoms Up Approach
        :param piles:
        :param k:
        :return:
        """
        n = len(piles)
        t = [[0 for _ in range(k+1)] for _ in range(n+1)]
        # t[i][coins] = max value when we have i piles and max coins that we can take is 'coins'
        for i in range(1, n + 1):
            for coins in range(k + 1):
                money = 0
                for currCoins in range(min(len(piles[i - 1]), coins)+1):
                    if currCoins > 0:
                        money += piles[i - 1][currCoins - 1]
                    t[i][coins] = max(t[i][coins], money + t[i - 1][coins - currCoins])
        print(t)
        return t[n][k]


if __name__ == "__main__":
    obj = Solution()
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    print(obj.maxValueOfCoins(piles, k))
    piles = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
    k = 7
    print(obj.maxValueOfCoins(piles, k))
