#diagonal sum in leetcode
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pd=0
        sd=0
        l=len(mat)
        for i in range(l):
            for j in range(l):
                if i==j:
                    pd=pd+mat[i][j]
                elif i+j==l-1:
                    sd=sd+mat[i][j]
        return pd+sd      