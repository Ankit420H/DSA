class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1=alphabet_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        d2=alphabet_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1
        a1=list(d1.values())
        a2=list(d2.values())
        for i in range(26):
            if (abs(a1[i]-a2[i])>3):
                return False
        return True