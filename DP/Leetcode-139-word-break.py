"""
https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=dynamic-programming

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str], ):

        memo = {}

        def memoize(target, wordDict):
            if target == "":
                return True
            if target in memo:
                return memo[target]

            for word in wordDict:
                if target[:len(word)] == word and memoize(target[len(word):], wordDict):
                    memo[target] = True
                    return memo[target]
            memo[target] = False
            return memo[target]

        return memoize(s, wordDict)


obj = Solution()
s = "leetcode"
wordDict = ["leet","code"]
print(obj.wordBreak(s,wordDict))
s = "applepenapple"
wordDict = ["apple","pen"]
print(obj.wordBreak(s,wordDict))