class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: list[int], v: list[int]) -> int:
        h = sorted(h + [1, m])
        v = sorted(v + [1, n])

        hg = set()
        vg = set()

        for i in range(len(h)):
            for j in range(i):
                hg.add(h[i] - h[j])

        for i in range(len(v)):
            for j in range(i):
                vg.add(v[i] - v[j])

        for x in sorted(hg, reverse=True):
            if x in vg:
                return x * x % (10**9 + 7)
        return -1
