class Solution:
    def maxDifference(self, s: str) -> int:
        f ={}
        for i in s:
            f[i]=f.get(i,0)+1
        v=list(f.values())
        mi=float('inf')
        ma=float('-inf')
        for x,y in f.items():
            if y%2==0 and y<mi:
                mi=y
            if y%2!=0 and y>ma:
                ma=y
        print(f)
        print(mi,ma)
        return -1 if ma - mi == 0 else ma - mi
