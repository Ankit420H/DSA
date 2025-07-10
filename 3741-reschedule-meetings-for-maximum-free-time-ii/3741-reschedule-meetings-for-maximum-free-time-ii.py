class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        g = [startTime[0]] + [startTime[i] - endTime[i - 1] for i in range(1, n)] + [eventTime - endTime[-1]]
        ml = [g[0]] + [0] * n
        mr = [0] * n + [g[n]]

        for i in range(1, n + 1):
            ml[i] = max(g[i], ml[i - 1])

        for i in range(n - 1, -1, -1):
            mr[i] = max(g[i], mr[i + 1])

        ans = 0
        for i in range(n):
            d = endTime[i] - startTime[i]
            a = g[i] + g[i + 1]
            c = d <= max(ml[i - 1] if i > 0 else 0, mr[i + 2] if i + 2 < n + 1 else 0)
            ans = max(ans, a + (d if c else 0))
        return ans
