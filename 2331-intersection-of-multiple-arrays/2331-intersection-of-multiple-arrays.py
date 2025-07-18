class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        d = {}
        for row in nums:
            for x in set(row):
                 d[x] = d.get(x, 0) + 1
        res = []
        for k in d:
            if d[k] == len(nums):
                res.append(k)
        return sorted(res)