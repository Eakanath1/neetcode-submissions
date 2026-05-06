"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        prev_end = None
        for itrvl in sorted_intervals:
            if prev_end is not None and itrvl.start < prev_end:
                return False
            prev_end = itrvl.end
        return True