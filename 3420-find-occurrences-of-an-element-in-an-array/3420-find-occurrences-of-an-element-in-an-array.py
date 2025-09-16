class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        p = []
        for i in range(len(nums)):
            if nums[i] == x:
                p.append(i)
        ans = []
        for q in queries:
            if q <= len(p):
                ans.append(p[q - 1])
            else:
                ans.append(-1)
        return ans