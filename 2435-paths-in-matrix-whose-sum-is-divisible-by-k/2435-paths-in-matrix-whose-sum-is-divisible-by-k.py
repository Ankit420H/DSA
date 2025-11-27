class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M = 1000000007
        r = len(grid)
        c = len(grid[0])
        dp = [[0] * k for _ in range(c)]
        for j in range(c):
            x = grid[0][j] % k
            if j == 0:
                dp[j][x] = 1
            else:
                for s in range(k):
                    if dp[j-1][s]:
                        dp[j][(s + x) % k] = (dp[j][(s + x) % k] + dp[j-1][s]) % M
        for i in range(1, r):
            ndp = [[0] * k for _ in range(c)]
            for j in range(c):
                x = grid[i][j] % k
                for s in range(k):
                    if dp[j][s]:
                        ndp[j][(s + x) % k] = (ndp[j][(s + x) % k] + dp[j][s]) % M
                    if j > 0 and ndp[j-1][s]:
                        ndp[j][(s + x) % k] = (ndp[j][(s + x) % k] + ndp[j-1][s]) % M
            dp = ndp
        return dp[c-1][0]
