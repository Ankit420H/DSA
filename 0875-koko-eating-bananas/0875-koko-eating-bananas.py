class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            th = 0
            for p in piles:
                th += (p + m - 1) // m
            if th <= h:
                r = m
            else:
                l = m + 1
        return l