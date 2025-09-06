class Solution:
    def makeTheIntegerZero(self, a: int, b: int) -> int:
        for k in range(61):
            t = a - k * b
            if t.bit_count() <= k <= t:
                return k
        return -1