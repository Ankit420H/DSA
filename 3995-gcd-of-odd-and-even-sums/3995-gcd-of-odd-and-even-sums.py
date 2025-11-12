class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        se=so=0
        for i in range(n*2):
            if i%2==0:
                se+=i
            else:
                so+=i
        return math.gcd(se,so)