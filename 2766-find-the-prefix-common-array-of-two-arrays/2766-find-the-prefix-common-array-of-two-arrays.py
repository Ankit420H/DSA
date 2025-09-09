class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0] * len(A)
        s1 = set()
        s2 = set()
        for i in range(len(A)):
            s1.add(A[i])
            s2.add(B[i])
            C[i] = len(s1 & s2)
        return C
