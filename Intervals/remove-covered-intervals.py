class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda i:(i[0],-i[1]))
        res = [intervals[0],]
        for l, r in intervals:
            prevL, prevR = res[-1]
            if prevL <= l and prevR >= r:
                continue
            res.append([l,r])
        return len(res)

obj = Solution()
# intervals = [[1,4],[3,6],[2,8]]
# print(obj.removeCoveredIntervals(intervals))
intervals = [[3,10],[4,10],[5,11]] #[[1,4],[2,3]]
print(obj.removeCoveredIntervals(intervals))
