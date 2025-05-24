class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        z=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    z.append([i,j])
        for r, c in z:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
            for i in range(len(matrix)):
                matrix[i][c] = 0