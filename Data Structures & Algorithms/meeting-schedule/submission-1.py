"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        n = len(intervals)
        # only float inf is available not int or others
        prev_end = float("-inf")
        for meet in intervals:
            if meet.start < prev_end:
                return False
            prev_end = meet.end
        return True