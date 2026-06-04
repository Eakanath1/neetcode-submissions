class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        def dfs(start, rem, path):
            if rem == 0:
                res.append(path[:])
                return
            for i in range(start, n):
                # skip duplicate values at the same tree level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur = candidates[i]
                if cur > rem:
                    return
                path.append(cur)
                dfs(i+1, rem-cur, path)
                path.pop()
        dfs(0, target, [])
        return res