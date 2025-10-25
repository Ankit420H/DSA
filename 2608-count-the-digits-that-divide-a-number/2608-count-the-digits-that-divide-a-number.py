class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        for d in str(num):
            if int(d) != 0 and num % int(d) == 0:
                c += 1
        return c
