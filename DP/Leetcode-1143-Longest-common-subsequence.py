from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = {}

        def solve(i, j):
            if i >= n1 or j >= n2:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + solve(i + 1, j + 1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(solve(i + 1, j), solve(i, j + 1))
                return dp[(i, j)]

        return solve(0, 0)

    # Todo Bottom Up Approach :
    #  https://www.youtube.com/watch?v=aJNu_DLyOxY&list=PLpIkg8OmuX-L_QqcKB5abYynQbonaNcq3&index=11


if __name__ == "__main__":
    obj = Solution()
    text1 = "abcde"
    text2 = "ace"
    print(obj.longestCommonSubsequence(text1, text2))
    text1 = "abc"
    text2 = "def"
    print(obj.longestCommonSubsequence(text1, text2))
