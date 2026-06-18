class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]*(rowIndex+1)
        # Only compute i = 1..rowIndex-1 because row[0] and row[rowIndex] are always 1 in Pascal's triangle
        for i in range(1, rowIndex):
            row[i] = (row[i-1]*(rowIndex-i+1))//i
        return row