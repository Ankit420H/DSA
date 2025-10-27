class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        prev = 0
        for r in bank:
            cur = r.count('1')
            if cur:
                ans += prev * cur
                prev = cur
        return ans
