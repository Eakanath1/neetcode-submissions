class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n-2
        # Start looking for the breakpoint (the point till which eveything is lexically sorted)
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # For the last permuation (Ex: 4,2,1,1) i would be at -1. For others (like 3,4,2,1,1)
        if i >= 0:
            j = n-1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # This would get the highest possible permutation for the next round(Ex: 4, 3, 2, 1, 1)
            nums[i], nums[j] = nums[j], nums[i]
        # Reverse the current permuation window (size 2 or more) to get the next lowest permutation
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return None