class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set()
        r=set()
        for i in nums:
            if i in s:
                r.add(i)
            else:
                s.add(i)
        return list(r)