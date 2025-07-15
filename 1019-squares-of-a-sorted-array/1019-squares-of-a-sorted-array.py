class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        v=[0]*len(nums)
        l=0
        i=r=len(nums)-1
        while l<=r:
            if nums[l]>nums[r]:
                v[i]=nums[l]
                l+=1
            else:
                v[i]=nums[r]
                r-=1
            i-=1
        return v