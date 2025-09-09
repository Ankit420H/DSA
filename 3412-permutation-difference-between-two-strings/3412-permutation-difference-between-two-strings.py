class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        p = {}
        for i in range(len(t)):
            p[t[i]] = i
        k = 0
        for i in range(len(s)):
            k += abs(i - p[s[i]])
        return k