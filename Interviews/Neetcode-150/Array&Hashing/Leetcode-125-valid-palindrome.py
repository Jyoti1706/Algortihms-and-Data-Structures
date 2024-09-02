class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(',',"")
        s = s.replace(':', "")
        s = s.strip()
        print(s)
        return s == s[::-1]

obj = Solution()