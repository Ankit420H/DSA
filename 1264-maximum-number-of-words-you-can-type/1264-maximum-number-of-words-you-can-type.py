class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t=list(map(str,text.split(" ")))
        print(t)
        count=0
        for i in t:
            c=False
            for j in i:
                if j in brokenLetters:
                    c=True
            if c==False:
                count+=1
        return count
            

