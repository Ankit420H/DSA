class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        inc = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        for i in range(k - 1, n - k):
            if inc[i] >= k - 1 and inc[i + k] >= k - 1:
                return True

        return False