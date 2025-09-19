class Solution:
    def reverseDegree(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            a+=(i+1)*((ord("z")-ord(s[i]))+1)
        return a