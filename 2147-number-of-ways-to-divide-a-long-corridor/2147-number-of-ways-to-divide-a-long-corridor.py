class Solution:
    def numberOfWays(self, corridor: str) -> int:
        m = 1000000007
        a = 1
        p = -1
        s = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                s += 1
                if s > 2 and s % 2 == 1:
                    a = a * (i - p) % m
                p = i
        return a if s > 1 and s % 2 == 0 else 0