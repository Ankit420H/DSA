class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        m = max(d.values())
        c = 0
        for v in d.values():
            if v == m:
                c += 1
        return c * m
