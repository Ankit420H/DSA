class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        s = {"electronics", "grocery", "pharmacy", "restaurant"}
        r = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in s and code[i] and all(x.isalnum() or x == "_" for x in code[i]):
                r.append(i)
        r.sort(key=lambda i: (businessLine[i], code[i]))
        return [code[i] for i in r]
