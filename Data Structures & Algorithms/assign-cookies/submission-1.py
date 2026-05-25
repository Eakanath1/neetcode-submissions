class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        kid, cookie = 0, 0
        while kid < len(g) and cookie < len(s):
            if s[cookie] >= g[kid]:
                kid += 1
            cookie += 1
        return kid
# Time: O(n*log(n) + m*log(m)), sorting arrays & 2 pointers
# Space: O(1)