class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        s = []
        l = 0

        for a in arr:
            r = len(s)
            s.append(a)
            for i in range(l, r):
                x = s[i] | a
                if x != s[-1]:
                    s.append(x)
            l = r

        return len(set(s))
