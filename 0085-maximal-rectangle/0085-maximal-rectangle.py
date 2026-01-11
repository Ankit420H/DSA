class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        h = [0] * n
        res = 0

        def solve(a):
            st = []
            ans = 0
            for i in range(len(a) + 1):
                while st and (i == len(a) or a[st[-1]] > a[i]):
                    x = a[st.pop()]
                    w = i if not st else i - st[-1] - 1
                    ans = max(ans, x * w)
                st.append(i)
            return ans

        for r in matrix:
            for i in range(n):
                h[i] = 0 if r[i] == '0' else h[i] + 1
            res = max(res, solve(h))

        return res
