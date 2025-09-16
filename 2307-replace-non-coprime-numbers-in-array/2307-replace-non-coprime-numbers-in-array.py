class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            while ans and math.gcd(ans[-1], n) > 1:
                n = math.lcm(ans.pop(), n)
            ans.append(n)
        return ans
