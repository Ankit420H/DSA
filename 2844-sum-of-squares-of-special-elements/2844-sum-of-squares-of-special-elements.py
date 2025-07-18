class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        s = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                s += nums[i] * nums[i]
        return s