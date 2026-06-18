class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1]*(i+1)
            # Only compute j = 1..i-1 because row[0] and row[i] are always 1 in Pascal's triangle
            for j in range(1, i):
                # Use Pascal's recurrence from the previous row to avoid integer division and make the update simpler and less error-prone.
                row[j] = res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res