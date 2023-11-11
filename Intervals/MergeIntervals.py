from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        st = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if end < intervals[i][0]:
                res.append([st,end])
                st = intervals[i][0]
                end = intervals[i][1]
            else:
                st = min(st,intervals[i][0])
                end = max(end,intervals[i][1])
        res.append([st,end])
        return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals=[[1,4],[4,5]]
obj = Solution()
print(obj.merge(intervals))