class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=0
        for i in range(1,n+1):
            if n>=((i * (i + 1)) // 2):
                c+=1
            else:
                return c
        return c