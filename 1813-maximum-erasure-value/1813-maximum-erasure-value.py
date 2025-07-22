class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        s = set()
        l = 0
        total = 0
        res = 0
        for r in range(len(nums)):
            while nums[r] in s:
                s.remove(nums[l])
                total -= nums[l]
                l += 1
            s.add(nums[r])
            total += nums[r]
            res = max(res, total)
        return res