class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for x,y in d.items():
            if y==len(nums)//2:
                return x
        return -1