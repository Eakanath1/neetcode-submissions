class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        removals = 0
        i = 0
        while i < n:
            j = i+1
            while j < n and intervals[j][0] < intervals[i][1]:
                removals += 1
                j += 1
            i = j
        return removals