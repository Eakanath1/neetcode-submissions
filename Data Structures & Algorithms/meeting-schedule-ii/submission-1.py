from heapq import heappush, heappop
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        sorted_intervals = sorted(intervals, key=lambda x: (x.start, -x.end))
        # min-heap of end times
        heap = []
        for interval in sorted_intervals:
            if heap and interval.start >= heap[0]:
                heappop(heap)
            heappush(heap, interval.end)
        return len(heap)