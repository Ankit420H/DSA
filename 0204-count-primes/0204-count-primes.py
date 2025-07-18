class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        p = [1] * n
        p[0] = p[1] = 0

        i = 2
        while i * i < n:
            if p[i]:
                j = i * i
                while j < n:
                    p[j] = 0
                    j += i
            i += 1

        return sum(p)
