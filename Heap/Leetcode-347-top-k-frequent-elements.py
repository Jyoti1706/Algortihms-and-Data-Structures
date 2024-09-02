import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        frequency = Counter(nums)
        frequency = [(value, key) for key, value in frequency.items()]
        heap = []
        heapq.heapify(heap)
        for i in range(len(frequency)):
            heapq.heappush(heap, (-frequency[i][0],frequency[i][1]))
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        return result


if __name__ == "__main__":
    obj = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(obj.topKFrequent(nums,k))
    # nums = [1]
    # k = 1
    # print(obj.topKFrequent(nums,k))
