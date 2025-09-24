class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        if num == 0:
            return "0"
        s = ""
        if (num < 0) ^ (den < 0):
            s += "-"
        num = abs(num)
        den = abs(den)
        s += str(num // den)
        if num % den == 0:
            return s
        s += "."
        m = {}
        r = num % den
        while r:
            if r in m:
                s = s[:m[r]] + "(" + s[m[r]:] + ")"
                break
            m[r] = len(s)
            r *= 10
            s += str(r // den)
            r %= den
        return s
