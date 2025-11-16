class Solution:
    def findErrorNums(self, a: List[int]) -> List[int]:
        n=len(a)
        s=set()
        d=0
        for x in a:
            if x in s:
                d=x
            s.add(x)
        for i in range(1,n+1):
            if i not in s:
                return [d,i]
