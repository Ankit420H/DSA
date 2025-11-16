class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        k=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                c=0
            k=max(k,c)
        return k