class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for x,y in d.items():
            if y>1:
                ans.append(x)
        return ans