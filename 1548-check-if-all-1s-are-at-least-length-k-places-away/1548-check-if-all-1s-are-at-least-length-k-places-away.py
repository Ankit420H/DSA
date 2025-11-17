class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=-1
        q=[]
        for i in nums:
            if i==1:
                if c>0:
                    q.append(c-1)
                c=1
            else:
                if c!=-1:
                    c+=1
        for i in q:
            if i<k:
                return False
        return True