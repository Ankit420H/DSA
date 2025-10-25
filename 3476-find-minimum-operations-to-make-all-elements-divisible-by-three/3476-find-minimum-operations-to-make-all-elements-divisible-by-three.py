class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        c = 0
        for n in nums:
            if n % 3 != 0:
                c += 1
        return c
    