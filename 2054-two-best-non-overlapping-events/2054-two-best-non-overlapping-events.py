class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        a=0
        m=0
        x=[]
        for s,t,v in events:
            x.append((s,1,v))
            x.append((t+1,0,v))
        x.sort()
        for _,f,v in x:
            if f:
                a=max(a,m+v)
            else:
                m=max(m,v)
        return a