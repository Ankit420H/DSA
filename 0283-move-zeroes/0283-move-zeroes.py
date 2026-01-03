class Solution(object):
    def moveZeroes(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[c]=nums[c],nums[i]
                c+=1
        return nums