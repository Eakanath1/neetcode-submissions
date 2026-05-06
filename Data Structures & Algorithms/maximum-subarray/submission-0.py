class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for x in nums[1:]:
            # either extend the current subarray or start new at x
            curr = max(x, curr + x)
            best = max(best, curr)
        return best