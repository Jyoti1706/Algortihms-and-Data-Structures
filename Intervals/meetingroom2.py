class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals):
        res = 0
        while len(intervals)>0:
            j = 0
            end = intervals[0][1]
            intervals.pop(0)
            while j < len(intervals):
                if end > intervals[j][1]:
                    j = j+1
                else:
                    intervals.pop(j)
            res += 1
        return res

obj = Solution()
intervals = [(0,30),(5,10),(15,20)]
print(obj.min_meeting_rooms(intervals))
intervals =[(2,7)]
print(obj.min_meeting_rooms(intervals))