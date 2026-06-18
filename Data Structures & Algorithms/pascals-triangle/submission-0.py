class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            cur = 1
            row = [1]*(i+1)
            # Only compute j = 1..i-1 because row[0] and row[i] are always 1 in Pascal's triangle
            # cur tracks C(i, j) from the previous value using C(i,j)=C(i,j-1)*(i-j+1)//j, so update this formula carefully if the loop bounds or row indexing change.
            for j in range(1, i):
                cur = (cur*(i-j+1))//j
                row[j] = cur
            res.append(row)
        return res