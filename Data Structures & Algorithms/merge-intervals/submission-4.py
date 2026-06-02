class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Constraint: 0 <= start <= end <= 1000. Small enough to maintain bucket
        MAX_VAL = 1000

        # farthest[start] = maximum end among intervals starting at `start`
        farthest = [-1] * (MAX_VAL + 1)

        for s, e in intervals:
            farthest[s] = max(farthest[s], e)

        res = []
        cur_start = -1
        cur_end = -1

        for start, end in enumerate(farthest):
            if end == -1:
                continue

            if cur_start == -1:
                cur_start, cur_end = start, end
            elif start <= cur_end:
                cur_end = max(cur_end, end)
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        res.append([cur_start, cur_end])
        return res