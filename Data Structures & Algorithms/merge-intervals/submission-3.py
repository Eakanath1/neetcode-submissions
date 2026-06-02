class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            itl = intervals[i]
            if itl[0] <= end:
                end = max(itl[1], end)
            else:
                res.append([start, end])
                start, end = itl[0], itl[1]
        res.append([start, end])
        return res