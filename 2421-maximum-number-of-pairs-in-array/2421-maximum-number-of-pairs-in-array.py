class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        p = 0
        for v in d.values():
            p += v // 2

        return [p, len(nums) - 2 * p]