class Solution:
    @staticmethod
    def isMatch( s: str, p: str) -> int:
        i, j = 0, 0
        while j < len(p) and p[j] == '*':
            j += 1
            i += 1

        start = j
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '*'):
                i += 1
                j += 1
            elif j == len(p):
                return i-j
            else:
                i += 1
                j = start

        if j < len(p) - 1:
            return -1
        else:
            if i < 0:
                return i
            return i - j


print(Solution.isMatch("juliasamanthantjulia","ant*as"))
print(Solution.isMatch("juliasamanthantjulia","ant*a"))
print(Solution.isMatch("juliasamanthantjulia","a***a"))
print(Solution.isMatch("juliasamanthantjulia","*********"))