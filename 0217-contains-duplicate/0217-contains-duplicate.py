class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m={}
        for i,x in enumerate(nums):
            if x in m:
                return True
            m[x]=i
        return False 