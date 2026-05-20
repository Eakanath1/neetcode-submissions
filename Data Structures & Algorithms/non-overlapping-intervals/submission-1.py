class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        n = len(intervals)
        i = 0
        res = 0
        while i < n:
            j = i+1
            while j < n and intervals[i][1] > intervals[j][0]:
                res += 1
                j += 1
            i = j
        return res