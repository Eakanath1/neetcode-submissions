class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        l = 0
        zeros = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if r-l+1 > res:
                res = r-l+1
        return res