class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = [[1] * k for _ in range(n)]
        ans = 1

        for i in range(n):
            for j in range(i):
                r = (nums[j] + nums[i]) % k
                l[i][r] = max(l[i][r], l[j][r] + 1)
                ans = max(ans, l[i][r])

        return ans