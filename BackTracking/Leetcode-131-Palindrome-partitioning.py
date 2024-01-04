"""
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.



Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtracking(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.palindrome(s, i, j):
                    part.append(s[i:j + 1])
                    backtracking(j + 1)
                    part.pop()

        backtracking(0)
        return res

    def palindrome(self, arr, i, j):
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    obj = Solution()
    s = "aab"
    print(obj.partition(s))
    s = "a"
    print(obj.partition(s))
