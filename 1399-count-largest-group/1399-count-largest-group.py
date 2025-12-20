class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            x = i
            s = 0
            while x:
                s += x % 10
                x //= 10
            d[s] = d.get(s, 0) + 1

        m = 0
        r = 0
        for v in d.values():
            if v > m:
                m = v
                r = 1
            elif v == m:
                r += 1
        return r