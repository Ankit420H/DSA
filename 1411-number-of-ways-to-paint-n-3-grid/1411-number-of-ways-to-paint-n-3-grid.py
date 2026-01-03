class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007
        c2 = 6
        c3 = 6

        for _ in range(1, n):
            nc2 = c2 * 3 + c3 * 2
            nc3 = c2 * 2 + c3 * 2
            c2 = nc2 % mod
            c3 = nc3 % mod

        return (c2 + c3) % mod
