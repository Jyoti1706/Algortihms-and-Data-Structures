import heapq
import math


class Solution:
    def minIntervalbruteforce(self, intervals, queries):
        intervals.sort()
        queries.sort()
        res = []
        j = 0
        for q in queries:
            val = math.inf
            while j < len(intervals):
                st = intervals[j][0]
                end = intervals[j][1]
                if st <= q <= end:
                    val = min(val, end - st + 1)
                    j = j + 1
                elif st > q:
                    break
            if val == math.inf:
                res.append(-1)
            else:
                res.append(val)
        return res

    def minInterval(self, intervals, queries):
        intervals.sort()
        minheap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            res[q] = minheap[0][0] if minheap else -1

        return [res[q] for q in queries]


obj = Solution()
intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
print(obj.minInterval(intervals, queries))
intervals = [[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]]
queries = [7, 9, 3, 9, 3]
print(obj.minInterval(intervals, queries))
