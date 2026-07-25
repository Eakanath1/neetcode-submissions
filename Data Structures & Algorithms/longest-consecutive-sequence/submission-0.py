class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        vals = set(nums)
        res = 0
        for num in vals:
            if (num-1) not in vals:
                cnt = 0
                while cnt <= n and (num+cnt) in vals:
                    cnt += 1
                if cnt > res:
                    res = cnt
        return res