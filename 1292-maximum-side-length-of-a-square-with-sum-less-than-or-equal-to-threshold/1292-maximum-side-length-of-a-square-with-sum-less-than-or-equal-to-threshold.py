class Solution:
    def maxSideLength(self, a: list[list[int]], t: int) -> int:
        m = len(a)
        n = len(a[0])
        r = 0

        p = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                p[i + 1][j + 1] = a[i][j] + p[i][j + 1] + p[i + 1][j] - p[i][j]

        def s(x1, y1, x2, y2):
            return p[x2 + 1][y2 + 1] - p[x1][y2 + 1] - p[x2 + 1][y1] + p[x1][y1]

        for i in range(m):
            for j in range(n):
                k = r
                while i + k < m and j + k < n:
                    if s(i, j, i + k, j + k) > t:
                        break
                    r = k + 1
                    k += 1
        return r
