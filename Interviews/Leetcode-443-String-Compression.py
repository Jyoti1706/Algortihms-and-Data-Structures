"""
https://leetcode.com/problems/string-compression/
"""


class Solution:
    def compress(self, chars):
        #chars = list(chars)
        idx = 0
        i = 0
        n = len(chars)
        while i < n:
            count = 0
            current_char = chars[i]
            while i < len(chars) and chars[i] == current_char:
                count += 1
                i += 1
            #print(chars[idx])
            chars[idx] = current_char
            idx += 1
            if count > 1:
                count_str = str(count)
                for ch in count_str:
                    chars[idx] = ch
                    idx += 1
        return idx


obj = Solution()
chars = ["a","a","b","b","c","c","c"]
print(obj.compress(chars))
