from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEND = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<prevEND:
                res +=1
                prevEND = min(prevEND, intervals[i][1])
            else:
                prevEND = intervals[i][1]
        return res


intervals = [[1,2],[2,3],[3,4],[1,3]]
obj = Solution()
intervals = [[1,2],[1,2],[1,2]]
print(obj.eraseOverlapIntervals(intervals))