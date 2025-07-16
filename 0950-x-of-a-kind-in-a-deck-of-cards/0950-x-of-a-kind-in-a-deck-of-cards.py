class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from math import gcd
        if len(deck) < 2:
            return False
        d = {}
        for i in deck:
            d[i] = d.get(i, 0) + 1
        v = list(d.values())
        g = v[0]
        for i in v[1:]:
            g = gcd(g, i)
        return g >= 2
