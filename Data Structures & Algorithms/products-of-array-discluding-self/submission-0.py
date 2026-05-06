from itertools import accumulate
import operator as op

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1, *accumulate(nums[:-1], op.mul)]
        suffix = list(reversed([1, *accumulate(reversed(nums[1:]), op.mul)]))
        return [a * b for a, b in zip(prefix, suffix)]