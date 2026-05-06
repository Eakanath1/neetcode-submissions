class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = {}
        for (idx, elem) in enumerate(nums):
            if elem in idxDict:
                return [idxDict[elem], idx]
            else:
                idxDict[(target - elem)] = idx
        return [-1, -1]