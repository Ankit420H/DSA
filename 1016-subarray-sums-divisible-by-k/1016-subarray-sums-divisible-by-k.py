class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = {0: 1}
        s = 0
        ans = 0
        for x in nums:
            s += x
            r = s % k
            if r in m:
                ans += m[r]
            m[r] = m.get(r, 0) + 1
        return ans
