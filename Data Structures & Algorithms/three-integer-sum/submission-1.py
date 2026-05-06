class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            target = -nums[i]
            l, r = i+1, n-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    left_val, right_val = nums[l], nums[r]
                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        return res