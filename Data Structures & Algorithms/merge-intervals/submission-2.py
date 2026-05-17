class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = []
        prev = intervals[0]
        for j in range(1, n):
            cur = intervals[j]
            if prev[1] < cur[0]:
                res.append(prev)
                prev = cur
            else:
                prev = [min(prev[0], cur[0]), max(prev[1], cur[1])]
        res.append(prev)
        return res