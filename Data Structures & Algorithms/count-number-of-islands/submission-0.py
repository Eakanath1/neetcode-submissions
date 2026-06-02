class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == '1' and (i, j) not in visited:
                visited.add((i, j))
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(i, j)
        return res