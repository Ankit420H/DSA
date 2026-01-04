import math

class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans = 0

        for x in nums:
            d = 0
            for i in range(2, math.isqrt(x) + 1):
                if x % i == 0:
                    if d:
                        d = 0
                        break
                    d = i
            if d and d * d != x:
                ans += 1 + x + d + x // d

        return ans
