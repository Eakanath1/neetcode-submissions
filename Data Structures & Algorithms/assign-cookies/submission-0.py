class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookies = list(Counter(s).items())
        heapq.heapify(cookies)
        g.sort()
        res = 0
        for kid in g:
            while cookies:
                size, count = heapq.heappop(cookies)
                if size >= kid:
                    res += 1
                    count -= 1
                    if count > 0:
                        heapq.heappush(cookies, (size, count))
                    break
        return res
# Time: O(n*log(n) + (n+m)*log(m)), heap push O(log k) each time, worst k is m so loop isn't linear time
# Space: O(m), heap/counter extra