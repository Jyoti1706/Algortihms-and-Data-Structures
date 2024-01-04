"""
https://leetcode.com/problems/palindromic-substrings/description/
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r= i
            while l>=r and s[l]==s[r]:
                res += 1
                l +=1
                r +=1
            l = i
            r = i+1
            while l>=r and s[l]==s[r]:
                res += 1
                l +=1
                r +=1
        return res