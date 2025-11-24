class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        a=""
        for i in range(len(nums)):
            a=a+str(nums[i])
            if int(a,2)%5==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans