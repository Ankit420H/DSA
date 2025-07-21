class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        s = set(range(1, n + 1))
        
        for i in range(n):
            row = set()
            col = set()
            for j in range(n):
                row.add(matrix[i][j])
                col.add(matrix[j][i])
            if row != s or col != s:
                return False
        return True
