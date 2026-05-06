class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n - 1

        # if not rotated
        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2
            # minimum is in the unsorted half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
