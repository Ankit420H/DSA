class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r = nums[0]
        s = 0
        for x in nums:
            if s < 0:
                s = x
            else:
                s += x
            if s > r:
                r = s
        return r