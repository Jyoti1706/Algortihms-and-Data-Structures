"""
https://leetcode.com/problems/break-a-palindrome/
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i]+'a'+palindrome[i+1:]
                return palindrome
        palindrome = palindrome[:n-1]+'b'
        return palindrome


if __name__ == "__main__":
    obj = Solution()
    palindrome = "abccba"
    print(obj.breakPalindrome(palindrome))
