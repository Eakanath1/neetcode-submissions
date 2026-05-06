class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur = nums[0]
        cur_min = nums[0]
        for num in nums[1:]:
            if num < 0:
                cur, cur_min = cur_min, cur
            cur = max(num, cur * num)
            cur_min = min(num, cur_min * num)
            res = max(res, cur)
        return res