class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # b=""
        # for i in s:
        #     if i in b:
        #         break
        #     b+=i
        # a=reversed(s)
        # k=""
        # for i in a:
        #     if i in k:
        #         break
        #     k+=i
        
        
        # return max(len(k),len(b))

        # s=list(s)
        # ans = 0 
        # for i in s:
        #     if i not in s:
        #         ans=max(ans,len(s))
        #     s.pop(index(i))
        #     print(s)
        # return ans
        s = list(s)
        ans = 0

        while s:
            seen = set()
            temp = []
            for ch in s:
                if ch in seen:
                    break
                seen.add(ch)
                temp.append(ch)
            ans = max(ans, len(temp))
            s.pop(0)  
        return ans