class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 0
        for r in range(n):
            if nums[r] == 1:
                if r-l+1 > res:
                    res = r-l+1
            else:
                l = r+1
        return res