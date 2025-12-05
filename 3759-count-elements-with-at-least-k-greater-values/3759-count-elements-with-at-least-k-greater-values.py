class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0: return len(nums)
        nums.sort()
        n=len(nums)
        q=nums[n-k]
        s=0
        for i in range(n):
            if nums[i]<q:
                s+=1
        return s