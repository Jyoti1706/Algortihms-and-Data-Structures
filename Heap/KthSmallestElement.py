"""
https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150
"""

import heapq

# Example heap
heap = [4, 1, 7, 3, 8, 5]

k = 2

class Solution:
    def findKthLargest(self, nums, k):
        minheap=[]
        c= 0
        for n in nums:
            heapq.heappush(minheap, n)
            c += 1
            #print(minheap, c)
            if c == k+1:
                heapq.heappop(minheap)
                c -= 1
        #print(minheap)
        return minheap[0]

obj = Solution()
print(obj.findKthLargest(heap,k))