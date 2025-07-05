class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s={}
        r=-1
        for i in arr:
            s[i] = s.get(i, 0) + 1
        for x,y in s.items():
            if x==y and x>r:
                r=x
        return r