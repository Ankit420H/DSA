class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maxVal = max(nums)
        ans = streak = 0

        for x in nums:
            if x == maxVal:
                streak += 1
                ans = max(ans, streak)
            else:
                streak = 0

        return ans
