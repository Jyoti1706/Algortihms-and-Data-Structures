import heapq


class Solution:
    def maxScore(self, nums1, nums2, k: int) -> int:
        heap = []
        total = 0
        res = 0
        #print(sorted(list(zip(nums1,nums2)), key = lambda x: x[1], reverse=True))
        zipped_list = list(zip(nums1,nums2))
        zipped_list = sorted(zipped_list, key=lambda x: x[1], reverse=True)
        for a, b in zipped_list:
            heapq.heappush(heap,a)
            total += a
            if len(heap)>k:
                total -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res, total *b)
        return res


if __name__ == "__main__":
    obj = Solution()
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    print(obj.maxScore(nums1, nums2, k))