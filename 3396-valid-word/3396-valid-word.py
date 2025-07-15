class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        v = c = False
        ok = True
        for i in word:
            if not i.isalnum():
                ok = False
            if i in "aeiouAEIOU":
                v = True
            elif i.isalpha():
                c = True
        return v and c and ok
