class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        maxR = max(startPos, fruits[-1][0])
        amt = [0] * (maxR + 1)
        for pos, val in fruits:
            amt[pos] = val
        pre = list(itertools.accumulate(amt, initial=0))

        def get(l: int, r: int) -> int:
            a = max(0, startPos - l)
            b = min(maxR, startPos + r)
            return pre[b + 1] - pre[a]

        ans = 0
        for r in range(min(maxR - startPos, k) + 1):
            l = max(0, k - 2 * r)
            ans = max(ans, get(l, r))

        for l in range(min(startPos, k) + 1):
            r = max(0, k - 2 * l)
            ans = max(ans, get(l, r))

        return ans
