"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
"""
import heapq


class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []

        heap = []
        c = 0
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if c < k:
                    heapq.heappush(heap, (-1 * (nums1[i] + nums2[j]), nums1[i], nums2[j]))
                else:
                    if heap[0][0] < -1 * (nums1[i] + nums2[j]):
                        item = (-1 * (nums1[i] + nums2[j]), nums1[i], nums2[j])
                        heapq.heappushpop(heap, item)
                c += 1

        result = []
        while heap and len(result) < k:
            _, num1, num2 = heapq.heappop(heap)
            result.append([num1, num2])

        return result


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
obj = Solution()
print(obj.kSmallestPairs(nums1, nums2, 3))
