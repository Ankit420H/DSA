class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        sp = sorted(p)
        for i in range(len(s) - len(p) + 1):
            if sp == sorted(s[i:i + len(p)]):
                ans.append(i)
        return ans



