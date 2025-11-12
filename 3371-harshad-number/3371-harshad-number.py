class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        i=x
        s=0
        while i:
            s+=i%10
            i=i//10
        return s if x%s==0 else -1