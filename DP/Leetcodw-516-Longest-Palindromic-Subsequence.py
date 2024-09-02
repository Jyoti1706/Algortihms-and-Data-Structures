"""
https://leetcode.com/problems/longest-palindromic-subsequence/description/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

"""
from functools import lru_cache

"""
Approach 1

S1 = bbbab
s2 = S1[::-1].copy()
Find longest Common Subsequence

Approach-2

"""


class Solution:
    #@lru_cache(None)
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def solve(s, i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == s[j]:
                dp[(i, j)] =  2 + solve(s, i + 1, j - 1)
            else:
                dp[(i,j)] = max(solve(s, i + 1, j), solve(s, i, j - 1))
            return dp[(i,j)]
        return solve(s, 0, len(s)-1)


s = "bbbab"
obj = Solution()
print(obj.longestPalindromeSubseq(s))