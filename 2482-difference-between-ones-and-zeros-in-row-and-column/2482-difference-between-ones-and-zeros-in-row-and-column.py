class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        r1 = [0] * m
        c1 = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r1[i] += 1
                    c1[j] += 1

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                diff[i][j] = r1[i] + c1[j] - (n - r1[i]) - (m - c1[j])

        return diff
