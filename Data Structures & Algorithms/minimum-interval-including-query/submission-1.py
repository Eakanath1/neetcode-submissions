import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        sorted_q = sorted(enumerate(queries), key=lambda x:(x[1], x[0]))
        res = [-1]*len(queries)
        i = 0
        heap = []
        for (j, q) in sorted_q:
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[j] = heap[0][0]
        return res