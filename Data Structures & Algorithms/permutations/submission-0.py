class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(perm, picked):
            if len(perm) == n:
                res.append(perm[:])
                return
            for i in range(n):
                if not picked[i]:
                    perm.append(nums[i])
                    picked[i] = True
                    dfs(perm, picked)
                    perm.pop()
                    picked[i] = False
        dfs([], [False]*n)
        return res