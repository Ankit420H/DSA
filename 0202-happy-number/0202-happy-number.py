class Solution:
    def hap(self, n):
        s = 0
        while n > 0:
            a = n % 10
            s += a * a
            n //= 10
        return s

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.hap(n)
        return n == 1
