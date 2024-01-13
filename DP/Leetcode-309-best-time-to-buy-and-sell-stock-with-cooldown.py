"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
-------------------
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
------------------
Input: prices = [1]
Output: 0

"""
from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        """
        Top-Down Approach (Dynamic Programing)
        :param prices:
        :return:
        """
        n = len(prices)
        memo = {}

        def solve(day, buy):
            if day >= n:
                return 0

            if (day, buy) in memo:
                return memo[(day, buy)]
            profit = 0
            if buy:
                take = solve(day + 1, False) - prices[day]
                not_take = solve(day + 1, True)
                profit = max(take, not_take)
            else:
                sell = prices[day] + solve(day + 2, True)
                not_sell = solve(day + 1, False)
                profit = max(sell, not_sell)
            memo[(day, buy)] = profit
            return memo[(day, buy)]

        return solve(0, True)

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        dp = [0 for _ in range(len(prices))]
        dp[1] = max(prices[1]-prices[0],0)

        for i in range(2,n):
            dp[i] = dp[i - 1]
            for j in range(i):
                prev_profit = dp[j-2] if j >= 2 else 0
                dp[i] = max(dp[i], prices[i]-prices[j]+prev_profit)
        return dp[n-1]


if __name__ == "__main__":
    obj = Solution()
    prices = [1, 2, 3, 0, 2]
    print(obj.maxProfit(prices))
