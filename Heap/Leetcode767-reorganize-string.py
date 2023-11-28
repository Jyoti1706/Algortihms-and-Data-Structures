"""
767. Reorganize String
Medium
8.1K
237
Companies
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

"""
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s):
        cnt = Counter(s)
        # Extract keys and values using items() method
        maxheap = [(-b,a) for a,b in cnt.items()]
        heapq.heapify(maxheap)
        prev = None

        res=""
        while maxheap or prev:
            print(prev)
            if not maxheap and prev:
                return ""
            cnt, chr = heapq.heappop(maxheap)
            res += chr
            cnt += 1
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if cnt != 0:
                prev = (cnt, chr)
        return res








s = "aaabb"


obj = Solution()
print(obj.reorganizeString(s))
