class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        ok=[0]*(n-1)
        c=0
        for i in range(m):
            f=0
            for j in range(n-1):
                if not ok[j] and strs[j][i]>strs[j+1][i]:
                    f=1
                    break
            if f:
                c+=1
            else:
                for j in range(n-1):
                    if strs[j][i]<strs[j+1][i]:
                        ok[j]=1
        return c
