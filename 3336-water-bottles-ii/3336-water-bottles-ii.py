class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        s = n
        while n >= e:
            n = n - e + 1
            e += 1
            s += 1
        return s
