class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        M = 1000000007
        mp = {}
        for x,y in points:
            mp[y] = mp.get(y,0)+1
        a = []
        for k in mp.values():
            if k > 1:
                a.append(k*(k-1)//2 % M)
        if len(a) < 2:
            return 0
        s = 0
        sq = 0
        for v in a:
            s = (s+v)%M
            sq = (sq+v*v)%M
        t = (s*s - sq) % M
        t = t * pow(2, M-2, M) % M
        return t % M
