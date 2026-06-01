class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = dict()
        res = 0
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            if char in unique and unique[char] >= l:
                l = unique[char] + 1
            unique[char] = r
            if r-l+1 > res:
                res = r-l+1
            r += 1
        return res