class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            elem = set()
            for j in range(n):
                if i != j:
                    val = nums[i] + nums[j]
                    if (0-val) in elem:
                        res.add(tuple(sorted([nums[i], nums[j], -val])))
                    else:
                        elem.add(nums[j])
        return [list(t) for t in res]