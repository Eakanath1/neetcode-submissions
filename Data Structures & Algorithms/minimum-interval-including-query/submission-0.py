class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = [-1]*len(queries)
        for interval in (intervals):
            len_int = interval[1] - interval[0] + 1
            for j in range(len(queries)):
                if interval[0] <= queries[j] and queries[j] <= interval[1]:
                    if res[j] == -1:
                        res[j] = len_int
                    else:
                        res[j] = min(len_int, res[j])
        return res