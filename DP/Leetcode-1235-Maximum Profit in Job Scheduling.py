import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def backtracking(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            # Skip
            res = backtracking(i + 1)

            # Take
            # j = i + 1
            # while j < len(intervals):
            #     if intervals[j][0] >= intervals[i][1]:
            #         break
            #     j += 1
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = res = max(res, intervals[i][2] + backtracking(j))
            return cache[i]

        return backtracking(0)


if __name__ == "__main__":
    obj = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    print(obj.jobScheduling(startTime, endTime, profit))
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    print(obj.jobScheduling(startTime, endTime, profit))
