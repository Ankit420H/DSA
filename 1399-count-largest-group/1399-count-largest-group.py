class Solution:
    def countLargestGroup(self, n: int) -> int:
        c = [0] * 37
        for i in range(1, n + 1):
            x = i
            s = 0
            while x:
                s += x % 10
                x //= 10
            c[s] += 1
        m = 0
        r = 0
        for v in c:
            if v > m:
                m = v
                r = 1
            elif v == m:
                r += 1
        return r