class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])
        dp=[1]*k
        for i in range(1,k):
            for j in range(i):
                if all(s[j]<=s[i] for s in strs):
                    dp[i]=max(dp[i],dp[j]+1)
        return k-max(dp)