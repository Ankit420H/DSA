class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        g = grid

        t = "43816729" * 2
        tr = t[::-1]

        def ok(i, j):
            s = ""
            for k in (0, 1, 2, 5, 8, 7, 6, 3):
                s += str(g[i + k // 3][j + k % 3])
            return s in t or s in tr

        r = len(g)
        c = len(g[0])
        ans = 0

        for i in range(r - 2):
            for j in range(c - 2):
                if g[i + 1][j + 1] == 5 and g[i][j] % 2 == 0:
                    ans += ok(i, j)

        return ans
