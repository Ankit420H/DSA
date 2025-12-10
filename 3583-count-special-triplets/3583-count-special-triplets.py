class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        m = 10**9 + 7
        l = Counter()
        r = Counter(nums)
        res = 0
        for x in nums:
            r[x] -= 1
            d = x * 2
            res = (res + l[d] * r[d]) % m
            l[x] += 1
        return res
