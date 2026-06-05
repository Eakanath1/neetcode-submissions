class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Logic, always sort the numbers when duplicates are allowed, so as to skip them
        nums.sort()
        n = len(nums)
        res = []
        def traverse(perm, picked):
            if len(perm) == n:
                res.append(perm[:])
                return
            for i in range(n):
                if picked[i]:
                    continue
                # Major change for duplicates, allow path for the first time, when the left most is picked. Block there after.
                if i > 0 and nums[i] == nums[i-1] and not picked[i-1]:
                    continue
                perm.append(nums[i])
                picked[i] = True
                traverse(perm, picked)
                picked[i] = False
                perm.pop()
        traverse([],[False]*n)
        return res