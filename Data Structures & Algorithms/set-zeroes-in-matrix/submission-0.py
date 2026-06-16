class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zero_rows = [False]*n
        zero_cols = [False]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_rows[i], zero_cols[j] = True, True
        for i in range(n):
            for j in range(m):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0
        return None
        