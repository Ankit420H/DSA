class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        ans=[]
        idx=0
        for i in range(1,n+1):
            if len(res)==len(target):
                return ans
            res.append(i)
            ans.append("Push")

            if res[-1]!= target[idx]:
                res.pop()
                ans.append("Pop")
            else:
                idx+=1

        return ans