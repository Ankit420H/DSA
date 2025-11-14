class Solution:
    def rangeAddQueries(self, n: int, q: List[List[int]]) -> List[List[int]]:
        d = [[0]*(n+1) for _ in range(n)]

        for v in q:
            r1, c1, r2, c2 = v
            for r in range(r1, r2+1):
                d[r][c1] += 1
                d[r][c2+1] -= 1

        ans = [[0]*n for _ in range(n)]
        for r in range(n):
            s = 0
            for c in range(n):
                s += d[r][c]
                ans[r][c] = s

        return ans
