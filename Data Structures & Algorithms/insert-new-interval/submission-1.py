class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i < len(intervals):
            begin, end = intervals[i][0], intervals[i][1]
            if begin > newInterval[1]:
                break;
            elif end < newInterval[0]:
                res.append(intervals[i])
                i += 1
            else:
                newInterval = [min(newInterval[0], begin), max(newInterval[1], end)]
                i += 1
            print(newInterval)
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res