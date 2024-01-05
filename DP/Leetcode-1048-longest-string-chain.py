from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        n = len(words)
        dp = [1 for _ in range(n)]

        def checkPredecessor(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            i, j = 0, 0
            m = len(word1)
            n = len(word2)
            while i < m and j < n:
                if word1[i] == word2[j]:
                    i += 1
                j += 1
            if i == m:
                return True
            return False

        for i in range(1, n):
            for j in range(i):
                if checkPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


if __name__ == "__main__":
    obj = Solution()
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(obj.longestStrChain(words))
    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    print(obj.longestStrChain(words))
    words = ["abcd", "dbqca"]
    print(obj.longestStrChain(words))
