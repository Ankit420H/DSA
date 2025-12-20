class Solution:
    def subarraySum(self, a: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        r = 0
        for x in a:
            s += x
            r += d.get(s - k, 0)
            d[s] = d.get(s, 0) + 1
        return r
