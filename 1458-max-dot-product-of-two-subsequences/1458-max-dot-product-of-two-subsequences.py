class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1
        b = nums2
        m = len(a)
        n = len(b)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(
                    dp[i][j + 1],
                    dp[i + 1][j],
                    max(0, dp[i][j]) + a[i] * b[j]
                )
        return dp[m][n]