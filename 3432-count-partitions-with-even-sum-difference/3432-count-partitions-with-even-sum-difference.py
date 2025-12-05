class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        even=0
        for i in range(len(nums)-1):
            if abs(sum(nums[0:i+1])-sum(nums[i+1:len(nums)]))%2==0:
                even+=1
        return even