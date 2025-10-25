class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        d = n % 7

        a = 7 * w * (w + 7) // 2
        b = d * (2 * (w + 1) + (d - 1)) // 2

        return a + b
