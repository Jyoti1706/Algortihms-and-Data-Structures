"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.
"""


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        # Write your code here
        intervals.sort()
        end = intervals[0][1]
        for s1, e1 in intervals[1:]:
            if s1 < end:
                return False
            else:
                end = e1
        return True


intervals = [(0,30),(15,20),(5,10)]
ob = Solution()
print(ob.can_attend_meetings(intervals))

intervals = [(5,8),(9,15)]
ob = Solution()
print(ob.can_attend_meetings(intervals))

intervals = [(0,8),(8,15)]
ob = Solution()
print(ob.can_attend_meetings(intervals))