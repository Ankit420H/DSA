class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = 0
        for i in range(len(strs[0])):
            a = ""
            for j in range(len(strs)):
                a += strs[j][i]
            if a != "".join(sorted(a)):
                c += 1
        return c
